---
stepsCompleted: [1, 2, 3, 4, 5]
inputDocuments: ["docs/plans/moments-mind-studio-product-brief.md"]
workflowType: 'research'
lastStep: 1
research_type: 'technical'
research_topic: 'permanent-archive-engine'
research_goals: 'Verify technical feasibility of perfect web page preservation (HTML/CSS/JS/Image) and identify optimal tools and architecture.'
user_name: '마스터'
date: '2026-01-08'
web_research_enabled: true
source_verification: true
---

# Research Report: Technical Research

**Date:** 2026-01-08
**Author:** 마스터
**Research Type:** technical

---

## Research Overview

[Research overview and methodology will be appended here]

## Technology Stack Analysis

### Programming Languages

고성능 웹 아카이빙 및 브라우저 제어를 위해 2025년 기준 다음 언어들이 주로 사용됩니다.

- **Node.js / TypeScript**: Playwright 및 Puppeteer와의 네이티브 통합이 가장 강력하며, DOM 조작 및 브라우저 자동화에 최적화된 생태계를 보유하고 있습니다.
- **Python**: 데이터 처리 및 오케스트레이션(예: ArchiveBox)에 널리 사용되지만, 고도로 병렬화된 크롤링 시 GIL(Global Interpreter Lock)이 병목이 될 수 있습니다.
- **Go**: Browsertrix-crawler와 같이 높은 동시성이 요구되는 네트워킹 레이어 및 시스템 구축에 선호됩니다.
- **Java**: Internet Archive의 Heritrix와 같이 대규모 엔터프라이즈급 크롤러의 핵심 언어로 여전히 사용됩니다.

_Popular Languages: Node.js (Browser control), Python (Orchestration)_
_Emerging Languages: Go (High-concurrency crawler components)_
_Language Evolution: 정적 HTML 파싱 중심에서 헤드리스 브라우저 제어(JS 실행) 중심으로 이동_
_Performance Characteristics: Node.js는 메모리 점유율이 높으나 DOM 조작 속도가 빠름, Go는 실행 효율성 및 병렬 처리에 탁월_
_Source: https://commoncrawl.org/blog/web-archiving-file-formats-explained_

### Development Frameworks and Libraries

현대적인 웹 페이지의 '동적 콘텐츠'를 완벽하게 보존하기 위한 핵심 라이브러리입니다.

- **[SingleFile](https://github.com/gildas-lormeau/SingleFile)**: CSS, 이미지, 폰트를 하나의 HTML 파일로 임베딩하는 고정밀 스냅샷 도구의 표준입니다.
- **[Playwright](https://playwright.dev/)**: 2024-2025년 기준 Puppeteer보다 선호되는 도구로, 강력한 자동 대기(Auto-waiting) 및 모든 브라우저 엔진(Chromium, WebKit, Firefox) 지원이 강점입니다.
- **[Browsertrix Crawler](https://webrecorder.net/browsertrix)**: Kubernetes 네이티브 크롤러로, 복잡한 JS 기반 사이트를 아카이빙하는 데 최적화되어 있습니다.
- **[ArchiveBox](https://archivebox.io/)**: 여러 도구(SingleFile, Puppeteer 등)를 병렬 실행하여 다층적 보존을 수행하는 오픈소스 오케스트레이터입니다.

_Major Frameworks: Playwright, SingleFile, Browsertrix_
_Micro-frameworks: Wpull (Python-based downloader), Scoop (Witnessing-based capture)_
_Evolution Trends: 단순 다운로드에서 브라우저 렌더링 결과물 저장으로 진화_
_Ecosystem Maturity: Playwright를 중심으로 한 브라우저 제어 생태계가 매우 성숙함_
_Source: https://webrecorder.net/blog/2025-02-06-preserving-government-websites-with-browsertrix/_

### Database and Storage Technologies

영구 보존을 위해 데이터 무결성과 접근성을 보장하는 기술입니다.

- **WARC (Web ARChive, ISO 28500)**: HTTP 요청/응답 스트림을 저장하는 국제 표준 포맷입니다. 장기 보존 및 법적 증거력 확보에 필수적입니다.
- **[WACZ (Web Archive Collection Zipped)](https://specs.webrecorder.net/wacz/)**: WARC 파일을 인덱스 및 메타데이터와 함께 압축한 현대적 포맷으로, 별도 서버 없이 브라우저에서 랜덤 액세스 재생이 가능합니다.
- **Object Storage (S3-compatible)**: 불변성(Immutability)이 중요한 WARC 파일을 저장하기 위한 업계 표준입니다.
- **Apache Parquet**: Common Crawl 등에서 대규모 웹 아카이브 메타데이터를 효율적으로 쿼리하기 위해 사용되는 컬럼형 저장 포맷입니다.

_Relational Databases: PostgreSQL (Metadata management)_
_NoSQL Databases: Elasticsearch/OpenSearch (Full-text search across archives)_
_In-Memory Databases: Redis (Crawl queue management)_
_Data Warehousing: Apache Parquet on S3 (Large-scale analysis)_
_Source: https://commoncrawl.org/blog/web-archiving-file-formats-explained_

### Development Tools and Platforms

- **Docker/Kubernetes**: 헤드리스 브라우저 인스턴스를 격리하고 확장하기 위한 필수 플랫폼입니다.
- **[Browserkube](https://github.com/webrecorder/browserkube)**: K8s 상에서 브라우저 파드(Pod)를 관리하는 전용 도구입니다.
- **Browserless.io**: 자체 구축 대신 사용할 수 있는 클라우드 기반 헤드리스 브라우저 서비스입니다.

_Source: https://webrecorder.net/blog/2025-02-06-preserving-government-websites-with-browsertrix/_

### Cloud Infrastructure and Deployment

대규모 웹 캡처는 'Headless Browser Cluster' 패턴을 따릅니다.

- **K8s Browser Pods**: 부하에 따라 브라우저 인스턴스를 수평 확장(HPA)합니다.
- **Serverless (Lambda/Cloud Run)**: 단일 페이지 캡처와 같은 온디맨드 요청에 사용되나, 브라우저 로딩 시간 및 타임아웃 제한을 고려해야 합니다.
- **CDN/Edge Computing**: 캡처된 정적 결과물(SingleFile HTML)을 사용자에게 빠르게 서빙하기 위해 활용됩니다.

_Source: https://lil.law.harvard.edu/blog/2025/05/02/iipc-web-archiving-conference-2025-recap/_

### Technology Adoption Trends

- **RAG & AI Integration**: 2024-2025년 가장 큰 트렌드로, **[WARC-GPT](https://github.com/webrecorder/warc-gpt)**와 같이 저장된 웹 아카이브를 LLM과 연결하여 대화형으로 지식을 탐색하는 시도가 활발합니다.
- **Shift to WACZ**: 기존 WARC의 재생(Replay) 어려움을 해결하기 위해 클라이언트 사이드 재생이 용이한 WACZ 포맷 채택이 늘고 있습니다.

_Source: https://journal.code4lib.org/articles/18555_

---

## Integration Patterns Analysis

### API Design Patterns

고성능 웹 아카이빙 엔진의 관리와 확장을 위해 다음과 같은 API 설계 패턴이 사용됩니다.

- **RESTful APIs**: 아카이브 컬렉션 관리, 사용자 권한 설정, 메타데이터 조회 등 일반적인 행정 작업에 표준으로 사용됩니다. (예: ArchiveBox, pywb)
- **GraphQL**: 복잡한 데이터 관계(크롤링 히스토리, 캡처된 자산 간의 계층 구조 등)를 효율적으로 쿼리하기 위해 **Browsertrix Cloud** 등에서 채택하고 있습니다.
- **gRPC**: 관리 레이어와 분산된 크롤러 노드 간의 고성능, 저지연 통신에 사용되며, 수백 개의 동시 브라우저 세션을 제어하는 데 적합합니다.
- **Webhook Patterns**: 캡처 완료, 오류 발생 등 장시간 실행되는 크롤링 작업의 상태 변화를 외부 시스템(Moments 알림 엔진 등)에 전달하는 데 활용됩니다.

_Source: https://webrecorder.net/browsertrix_

### Communication Protocols

브라우저 오케스트레이션과 실시간 제어를 위한 핵심 프로토콜입니다.

- **CDP (Chrome DevTools Protocol)**: 크로뮴 기반 브라우저와 통신하며 네트워크 요청 가로채기, 스크립트 주입, DOM 스냅샷 촬영을 수행하는 핵심 로우레벨 프로토콜입니다.
- **WebSocket Protocols**: CDP의 전송 계층으로 사용될 뿐만 아니라, 사용자가 실시간으로 브라우징을 가이드하며 아카이빙하는 '대화형 모드(Interactive Mode)' 구현에 필수적입니다.
- **gRPC with Protocol Buffers**: 내부 마이크로서비스 간의 이진 통신 프로토콜로, 데이터 전송 효율을 극대화합니다.

_Source: https://playwright.dev/_

### Data Formats and Standards

시스템 간 상호 운용성을 보장하는 데이터 표준입니다.

- **WARC (ISO 28500)**: 로우 HTTP 데이터 보관의 표준입니다.
- **WACZ (Web Archive Collection Zipped)**: 2024-2025년 기준 가장 권장되는 패키징 포맷입니다. WARC, 인덱스, 메타데이터를 하나의 ZIP으로 묶어 HTTP Range 요청을 통한 부분 재생이 가능합니다.
- **Frictionless Data (datapackage.json)**: WACZ 내에서 데이터의 구조, 해시, 출처 메타데이터를 정의하는 데 사용되어 데이터 과학 도구들과의 호환성을 보장합니다.

_Source: https://specs.webrecorder.net/wacz/1.2.0/_

### System Interoperability Approaches

- **API Gateway Patterns**: **Kong**이나 **Apollo Router**를 사용하여 인증, 속도 제한, 라우팅을 중앙 집중식으로 관리합니다.
- **Service Mesh**: 마이크로서비스 간 통신의 가시성과 보안(mTLS)을 확보하기 위해 사용됩니다.

_Source: https://pasksoftware.com/api-integration-patterns/_

### Microservices Integration Patterns

- **Circuit Breaker Pattern**: 특정 사이트의 응답 지연이나 브라우저 인스턴스 오류가 시스템 전체로 확산되는 것을 방지합니다.
- **Service Discovery**: 동적으로 증설되는 크롤러 노드들을 관리 레이어가 자동으로 감지하고 작업을 할당합니다.

_Source: https://github.com/istresearch/scrapy-cluster_

### Event-Driven Integration

- **Redis Bloom Filters**: 수십억 개의 URL 중복 여부를 빠르게 확인하기 위한 크롤링 프론티어 설계 패턴입니다.
- **RabbitMQ / Kafka**: 크롤링 작업 큐 관리 및 캡처된 텍스트를 AI 인덱싱 파이프라인(Vector DB 등)으로 흘려보내는 이벤트 스트림으로 활용됩니다.

_Source: https://pasksoftware.com/api-integration-patterns/_

### Integration Security Patterns

- **OAuth 2.0 and JWT**: 관리 API 보안의 표준이며, 특정 컬렉션에 대한 접근 권한(Scope)을 제어합니다.
- **mTLS (mutual TLS)**: 'Zero Trust' 아키텍처를 위해 조정 레이어와 브라우저 노드 간의 인증된 통신에 사용됩니다.

_Source: https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Microservices_Security_Cheat_Sheet.md_

---

## Technical Research Scope Confirmation

**Research Topic:** permanent-archive-engine
**Research Goals:** Verify technical feasibility of perfect web page preservation (HTML/CSS/JS/Image) and identify optimal tools and architecture.

**Technical Research Scope:**

- Architecture Analysis - design patterns, frameworks, system architecture
- Implementation Approaches - development methodologies, coding patterns
- Technology Stack - languages, frameworks, tools, platforms
- Integration Patterns - APIs, protocols, interoperability
- Performance Considerations - scalability, optimization, patterns

**Research Methodology:**

- Current web data with rigorous source verification
- Multi-source validation for critical technical claims
- Confidence level framework for uncertain information
- Comprehensive technical coverage with architecture-specific insights

**Scope Confirmed:** 2026-01-08

---

## Architectural Patterns and Design

### System Architecture Patterns

고성능 웹 아카이빙 엔진의 시스템 아키텍처는 2024-2025년 기준 다음과 같은 패턴으로 진화하고 있습니다.

- **Microservices vs Monolith**: **ArchiveBox**는 셀프 호스팅에 효과적인 모듈형 모놀리식으로 운영되지만, **Browsertrix Cloud**와 같은 엔터프라이즈 시스템은 마이크로서비스 아키텍처를 사용합니다. 이는 *Crawl Manager*(스케줄링), *Browser Workers*(실행), *Storage/Indexing* 서비스를 분리합니다.
- **Event-Driven Crawl Pipelines**: 고처리량 시스템은 **Apache Kafka** 또는 **RabbitMQ**를 사용하여 크롤링 작업을 분산합니다. "Seed Producer"가 URL을 토픽에 주입하고, "Browser Workers"가 이를 소비하며, "Crawl Events"(리소스 캡처 완료, WARC 청크 완료 등)를 다시 시스템으로 보내 인덱싱 및 후처리를 수행합니다.

_Source: https://www.javacodegeeks.com/2025/12/event-driven-architecture-kafka-vs-rabbitmq-vs-pulsar-a-2025-decision-framework.html_

### Design Principles and Best Practices

주요 웹 아카이빙 시스템들의 설계 원칙을 비교 분석했습니다.

- **Browsertrix (Webrecorder)**: **클라이언트 사이드 재생**과 **브라우저 기반 캡처**에 집중합니다. JS 기반 사이트가 정확하게 렌더링되도록 "헤드리스 브라우저 우선" 접근 방식을 사용합니다.
- **ArchiveBox**: **포맷 다양성**과 **자체 문서화**를 강조합니다. WARC뿐만 아니라 PDF, 스크린샷, 정적 HTML도 캡처하여, 단일 포맷이 미래에 실패할 수 있다는 원칙을 따릅니다.
- **Internet Archive (Heritrix)**: **대규모 크롤링 효율성**에 초점을 맞춥니다. 브라우저 기반 도구와 달리 프로토콜 레벨(HTTP) 캡처에 집중하는 Java 기반 크롤러입니다.
- **Scoop (Harvard LIL)**: **권위 있는 캡처**를 위해 설계된 최신 엔진(2023)으로, 법적 인용을 위한 고정밀 "증명(witnessing)" 기능에 중점을 둡니다.

_Source: https://docs.archivebox.io, https://lil.law.harvard.edu/blog/2023/04/13/scoop-witnessing-the-web_

### Scalability and Performance Patterns

- **Headless Browser Clusters**: 고정밀 캡처 확장을 위해 대규모 Chromium/Brave 인스턴스 클러스터 관리가 필요합니다. **BrowserKube**(Kubernetes 네이티브 브라우저 오케스트레이션)가 표준 패턴으로, 큐 깊이에 따라 브라우저 파드를 수평 확장합니다.
- **WARC/WACZ Sharding**: 페타바이트 규모에서는 WARC를 **날짜** 또는 **URL 해시**로 샤딩합니다. **WARC-DL**(2022-2024)은 실시간 AI 메타데이터 추출을 위해 CPU 클러스터에서 GPU 클러스터로 WARC 데이터를 스트리밍하는 패턴을 도입했습니다.

_Source: https://github.com/webrecorder/browserkube, https://arxiv.org/abs/2209.12299_

### Data Architecture Patterns

- **WACZ (Web Archive Collection Zipped)**: 2024년 휴대용 웹 아카이브 표준입니다. WARC를 인덱스 및 메타데이터와 함께 패키징합니다. **HTTP Range Requests**를 지원하여 브라우저 측 플레이어가 전체 아카이브를 다운로드하지 않고도 특정 페이지에 필요한 바이트만 가져올 수 있습니다.
- **CDXJ Indexing**: JSON 기반 CDX(CDXJ)가 확장성으로 인해 선호됩니다. 인덱싱은 일반적으로 수십억 개의 레코드에서 밀리초 미만의 조회를 위해 **Elasticsearch** 또는 **OutbackCDX**와 같은 고성능 저장소로 오프로드됩니다.

_Source: https://specs.webrecorder.net/wacz/1.1.1/_

### Security Architecture Patterns

- **Browser Isolation**: 헤드리스 브라우저는 "Side-Channel Attacks" 및 "Local File Ingress"에 취약합니다. 최신 아키텍처는 브라우저 파드의 강화된 샌드박싱을 위해 **gVisor** 또는 **Kata Containers**를 사용합니다.
- **Rewriting-Free Playback**: `pywb`가 개척한 핵심 보안 패턴입니다. 아카이브된 HTML의 링크를 재작성하는 대신, **Service Worker**를 사용하여 요청을 가로채 아카이브 재생 중 브라우저가 실수로 라이브 인터넷에서 데이터를 가져오는 "Live Web Leakage"를 방지합니다.

_Source: https://blog.dshr.org/2017/06/wac2017-security-issues-for-web-archives.html_

### Deployment and Operations Architecture

- **Kubernetes-Native**: 2025년의 "Gold Standard"입니다. Helm 차트를 통한 배포로 브라우저 워커 자동 확장 및 WARC 스테이징을 위한 **Persistent Volume Claims(PVC)**를 활용합니다.
- **Docker Compose**: **셀프 호스팅** 인스턴스(예: ArchiveBox)의 지배적인 패턴으로, 올인원 컨테이너가 데이터베이스(PostgreSQL/Redis), 워커, 웹 UI를 관리합니다.
- **Cloud-Native Object Storage**: WARC 영속성을 위해 로컬 디스크에서 **S3 호환 스토리지**(예: MinIO, AWS S3)로 전환하는 것이 내구성과 리전 간 가용성을 위한 표준입니다.

_Source: https://github.com/webrecorder/browserkube_

---

## Implementation Approaches and Technology Adoption

### Technology Adoption Strategies

**Moments: Mind Studio**와 같은 스타트업을 위해 2024-2025년에 가장 효과적인 전략은 **하이브리드 통합(Hybrid Integration)**입니다.

- **Build vs Buy vs Integrate 분석**:
  - **Build**: 브라우저 엔진을 처음부터 구축하는 것은 비현실적입니다.
  - **Buy (SaaS)**: 대규모로 운영 시 비용이 과도해질 수 있습니다.
  - **Integrate (권장)**: 검증된 오픈소스 도구를 통합하는 것이 최적입니다.

- **SingleFile CLI 통합**: "Instant Snapshot" 기능에 최적입니다. 자산과 CSS가 포함된 단일 자체 완결형 HTML 파일을 생성하며, 전체 텍스트 검색 인덱싱에 용이합니다.
- **Browsertrix Crawler 통합**: 복잡한 멀티페이지 또는 고정밀 아카이브(예: 소셜 미디어 피드)에는 WARC/WACZ 파일 생성을 위한 업계 표준인 Browsertrix가 적합합니다.
- **Playwright 우선**: 2024-2025년 기준 Puppeteer보다 Playwright를 권장합니다. 최신 브라우저 기능 지원, 멀티 컨텍스트 시나리오에서의 성능, 캡처 정확도에 중요한 "Auto-wait" 메커니즘이 더 강력합니다.

_Source: https://github.com/gildas-lormeau/single-file-cli, https://crawler.docs.browsertrix.com/_

### Development Workflows and Tooling

- **브라우저 기반 CI/CD**: **GitHub Actions + Playwright**를 사용하여 자동화된 회귀 테스트를 수행합니다.
- **정확도(Fidelity) 테스트**: 원본 라이브 사이트와 아카이브된 스냅샷을 비교하는 시각적 회귀 테스트가 필요합니다.
  - **도구**: **Pixelmatch** 또는 **Loki**를 사용하여 CI 중 스냅샷의 시각적 차이를 자동화합니다.
- **Fidelity Scorecard 구현**:
  1. 자산 완전성 (누락된 404 이미지/JS)
  2. 시각적 유사성 (DOM 구조 비교)
  3. 상호작용성 (아카이브된 JS의 기능 여부, 예: 메뉴/토글)

_Source: https://circleci.com/blog/ci-cd-testing-strategies-for-web-apps/_

### Testing and Quality Assurance

- **Canary Suite**: 주요 사이트 100개를 매일 캡처하여 브라우저 업데이트로 인한 캡처 로직 손상을 사용자에게 영향을 미치기 전에 감지합니다.
- **Visual Regression Testing**: 캡처된 페이지의 스크린샷을 원본과 비교하여 렌더링 정확도를 검증합니다.

### Deployment and Operations Practices

- **헤드리스 브라우저 확장**: 메인 애플리케이션 서버에서 브라우저를 실행하지 않습니다. 관리형 서비스(**Browserless.io**) 또는 자체 호스팅 K8s(**Browserkube**)를 사용합니다.
- **컨테이너화된 캡처 작업**: 메모리 누수 및 "좀비" 브라우저 프로세스를 방지하기 위해 각 캡처 작업을 컨테이너화합니다.
- **저장소 수명 주기 관리**:
  - **Hot Tier (S3 Standard)**: 즉시 조회/인덱싱을 위한 새 캡처
  - **Cold Tier (S3 Glacier Instant Retrieval)**: 90일 이상 된 아카이브

_Source: https://browsercat.com/post/scalable-headless-browser-automation_

### Team Organization and Skills

**Moments** 프로젝트의 영구 박제 엔진을 유지하기 위해 필요한 팀 역량:

- **Node.js / Playwright**: Chrome DevTools Protocol(CDP) 및 브라우저 내부 구조에 대한 심층 전문 지식
- **DevOps / K8s**: 임시 컨테이너 관리 및 브라우저 클러스터의 "noisy neighbor" 문제 처리 지식
- **디지털 보존 표준**: WARC, WACZ 및 메타데이터 스키마(JSON-LD)에 대한 이해

### Cost Optimization and Resource Management

- **컴퓨팅 비용**:
  - 단일 고정밀 캡처: ~10-30초 동안 2 vCPU 및 2GB RAM 소요
  - 대규모 운영 시 스팟 인스턴스 또는 전문 제공업체 사용 시 캡처당 ~$0.01 ~ $0.05

- **저장 비용**:
  - 2024년 평균 페이지 용량: ~2.5MB
  - 100만 캡처 = 2.5TB
  - S3 Standard: ~$60/월, Glacier: ~$10/월로 절감 가능
  - **WARC/WACZ 중복 제거**: 콘텐츠 인식 청킹(IPFS 스타일)을 사용하여 공통 자산(Google Fonts, React JS 등)을 사용자 간에 중복 제거하면 저장 오버헤드를 최대 40%까지 줄일 수 있습니다.

_Source: https://almanac.httparchive.org/en/2024/page-weight, https://specs.webrecorder.net/wacz-ipfs/latest/_

### Risk Assessment and Mitigation

| 위험 요소 | 설명 | 완화 전략 |
|-----------|------|-----------|
| **브라우저 업데이트** | Chrome 업데이트가 캡처 로직을 자주 손상시킴 | 캡처 컨테이너에서 브라우저 버전 고정, 일일 Canary Suite로 손상 조기 감지 |
| **법적/저작권 문제** | Internet Archive 관련 소송 사례 (Hachette v. Internet Archive) | **개인 용도**로 명확히 포지셔닝, 가능한 경우 `robots.txt` 준수 |
| **저장소 손상** | WARC 파일 손상 위험 | 체크섬 검증, 다중 리전 복제, 정기적인 무결성 검사 |

_Source: https://www.wired.com/story/internet-archive-memory-wayback-machine-lawsuits/_

---

## Technical Research Recommendations

### Implementation Roadmap for Moments: Mind Studio

| Phase | 목표 | 기술 스택 | 예상 기간 |
|-------|------|-----------|-----------|
| **Phase 1: SingleFile MVP** | 블로그/아티클 99% 정확도 캡처 | SingleFile CLI + S3 | 4-6주 |
| **Phase 2: WACZ Integration** | 복잡한 사이트(YouTube, Twitter) 지원 | Browsertrix + WACZ | 6-8주 |
| **Phase 3: Client-Side Capture** | "2초 캡처" 약속 실현, 서버 비용 절감 | Browser Extension (이미 렌더링된 DOM 캡처) | 8-12주 |

### Technology Stack Recommendations

**Moments: Mind Studio**를 위한 권장 기술 스택:

- **캡처 엔진**: SingleFile CLI (MVP) → Playwright + Browsertrix (확장)
- **저장 포맷**: SingleFile HTML (MVP) → WACZ (확장)
- **인프라**: Docker Compose (MVP) → Kubernetes + Helm (확장)
- **저장소**: S3 Standard + Glacier 수명 주기 정책
- **인덱싱**: SQLite (MVP) → Elasticsearch/OpenSearch (확장)
- **재생**: 브라우저 직접 열기 (SingleFile) → ReplayWeb.page (WACZ)

### Skill Development Requirements

| 역할 | 필수 스킬 | 학습 리소스 |
|------|-----------|-------------|
| Backend Engineer | Node.js, Playwright, CDP | Playwright 공식 문서 |
| DevOps Engineer | K8s, Helm, Container Security | Browserkube GitHub |
| Data Engineer | WARC/WACZ 표준, Elasticsearch | Webrecorder 스펙 문서 |

### Success Metrics and KPIs

| 지표 | 설명 | 목표 |
|------|------|------|
| **Capture Fidelity Score** | 원본 대비 시각적/기능적 정확도 | 95%+ |
| **Capture Latency** | 캡처 요청부터 완료까지 시간 | <30초 |
| **Storage Efficiency** | 중복 제거 후 저장 공간 절감률 | 30%+ |
| **Replay Success Rate** | 아카이브된 페이지의 성공적 재생 비율 | 99%+ |

---

## Executive Summary

**영구 박제 엔진(Permanent Archive Engine)**에 대한 기술 연구 결과, 2024-2025년 기준 **Moments: Mind Studio** 프로젝트를 위한 최적의 구현 전략은 다음과 같습니다:

1. **기술적 실현 가능성: ✅ 확인됨**
   - SingleFile, Playwright, Browsertrix 등 성숙한 오픈소스 도구를 통해 고정밀 웹 페이지 보존이 충분히 가능합니다.

2. **권장 아키텍처**:
   - **MVP**: SingleFile CLI + S3 저장 (간단하고 빠른 시작)
   - **확장**: Playwright + WACZ + Kubernetes (엔터프라이즈급 확장성)

3. **핵심 기술 선택**:
   - **캡처**: Playwright (브라우저 제어) + SingleFile (단일 파일 생성)
   - **저장**: WACZ 포맷 (클라이언트 사이드 재생, Range Request 지원)
   - **인프라**: Kubernetes + S3 호환 스토리지

4. **차별화 기회**:
   - **WARC-GPT** 통합을 통한 "자신의 지식과 대화하기" 기능은 Product Brief의 '자아 회복 솔루션' 비전과 완벽히 부합합니다.

---

**연구 완료일**: 2026-01-08
**연구 유형**: Technical Research
**연구 주제**: Permanent Archive Engine
