import UIKit
import Social
import MobileCoreServices
import UniformTypeIdentifiers

class ShareViewController: SLComposeServiceViewController {
    
    private var sharedURL: URL?
    private var sharedTitle: String?
    
    override func isContentValid() -> Bool {
        return sharedURL != nil
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        navigationController?.navigationBar.tintColor = UIColor.white
        navigationController?.navigationBar.backgroundColor = UIColor(red: 0.04, green: 0.04, blue: 0.06, alpha: 1.0)
        
        extractSharedContent()
    }
    
    private func extractSharedContent() {
        guard let extensionItem = extensionContext?.inputItems.first as? NSExtensionItem,
              let attachments = extensionItem.attachments else {
            return
        }
        
        for attachment in attachments {
            if attachment.hasItemConformingToTypeIdentifier(UTType.url.identifier) {
                attachment.loadItem(forTypeIdentifier: UTType.url.identifier, options: nil) { [weak self] (item, error) in
                    if let url = item as? URL {
                        DispatchQueue.main.async {
                            self?.sharedURL = url
                            self?.textView.text = url.absoluteString
                            self?.validateContent()
                        }
                    }
                }
            } else if attachment.hasItemConformingToTypeIdentifier(UTType.plainText.identifier) {
                attachment.loadItem(forTypeIdentifier: UTType.plainText.identifier, options: nil) { [weak self] (item, error) in
                    if let text = item as? String, let url = URL(string: text), url.scheme != nil {
                        DispatchQueue.main.async {
                            self?.sharedURL = url
                            self?.textView.text = url.absoluteString
                            self?.validateContent()
                        }
                    }
                }
            }
        }
        
        if let title = extensionItem.attributedContentText?.string {
            sharedTitle = title
        }
    }
    
    override func didSelectPost() {
        guard let url = sharedURL else {
            extensionContext?.completeRequest(returningItems: [], completionHandler: nil)
            return
        }
        
        let captureData: [String: Any] = [
            "url": url.absoluteString,
            "title": sharedTitle ?? contentText ?? "Untitled",
            "capturedAt": ISO8601DateFormatter().string(from: Date()),
            "moodColor": "curiosity"
        ]
        
        saveCaptureToAppGroup(captureData)
        sendCaptureToAPI(captureData)
        
        extensionContext?.completeRequest(returningItems: [], completionHandler: nil)
    }
    
    private func saveCaptureToAppGroup(_ data: [String: Any]) {
        guard let userDefaults = UserDefaults(suiteName: "group.com.moments.mindstudio") else {
            return
        }
        
        var pendingCaptures = userDefaults.array(forKey: "pendingCaptures") as? [[String: Any]] ?? []
        pendingCaptures.append(data)
        userDefaults.set(pendingCaptures, forKey: "pendingCaptures")
        userDefaults.synchronize()
    }
    
    private func sendCaptureToAPI(_ data: [String: Any]) {
        guard let url = URL(string: "https://api.moments.app/api/v1/capture") else {
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.timeoutInterval = 2.0
        
        do {
            request.httpBody = try JSONSerialization.data(withJSONObject: data)
        } catch {
            return
        }
        
        let task = URLSession.shared.dataTask(with: request) { _, response, error in
            if let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 {
                self.markCaptureAsSynced(data)
            }
        }
        task.resume()
    }
    
    private func markCaptureAsSynced(_ data: [String: Any]) {
        guard let userDefaults = UserDefaults(suiteName: "group.com.moments.mindstudio"),
              let urlString = data["url"] as? String else {
            return
        }
        
        var pendingCaptures = userDefaults.array(forKey: "pendingCaptures") as? [[String: Any]] ?? []
        pendingCaptures.removeAll { ($0["url"] as? String) == urlString }
        userDefaults.set(pendingCaptures, forKey: "pendingCaptures")
    }
    
    override func configurationItems() -> [Any]! {
        return []
    }
}
