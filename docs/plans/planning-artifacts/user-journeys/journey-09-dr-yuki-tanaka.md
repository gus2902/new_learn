# User Journey: Dr. Yuki Tanaka - 프라이버시의 벽을 넘어

**Persona:**
- **이름**: Dr. Yuki Tanaka (田中ゆき)
- **나이**: 42세
- **직업**: Psychiatrist (정신과 의사)
- **위치**: 도쿄, 일본
- **배경**: 환자 상담 케이스, 임상 노트, 개인 성찰 기록. 클라우드 서비스에 대한 깊은 불신.

**AARRR 단계**: Activation (프라이버시 장벽 극복 → Trust Building)

---

## Act 1: 클라우드에 대한 불신 (Day 0)

Dr. Yuki는 오래된 Moleskine 노트를 펼쳤다. 30년간 손글씨로 기록. 종이 노트 47권.

동료: "Yuki, 요즘 다들 앱 쓰는데."

**Dr. Yuki**: "앱? 클라우드에 올라가잖아. 환자 정보를 클라우드에? 절대 안 돼."

검색: "Offline note-taking app", "Local-only PKM", "Privacy-first"

결과는 실망스러웠다. Notion - 클라우드. Evernote - 클라우드. Obsidian - 모바일 동기화는 클라우드.

"다들 클라우드를 강요하네..."

---

## Act 2: 블로그 발견 (Day 1)

일요일 Hacker News:

**"Why We Built Moments on WACZ: True Offline-First Architecture"**

> "Moments는 다릅니다.
>
> - ✅ Local-only mode: 클라우드에 절대 업로드 안 됨
> - ✅ End-to-end encryption: 당신만 키 소유
> - ✅ Full export: 모든 데이터 standard format 추출
>
> **'당신의 지식은 당신의 것'**"

댓글:

**Moments Dev**: "Network monitor로 확인하세요. 단 1 byte도 서버로 안 갑니다."

"한번... 시험해 볼까?"

---

## Act 3: 첫 설치와 설정 (Day 1, 저녁)

온보딩:

---

**"프라이버시 설정을 선택하세요."**

**옵션 1: Cloud Sync (권장)**
- 모든 기기 접근
- 자동 백업

**옵션 2: Local-only Mode**
- 이 기기에만 저장
- 클라우드에 절대 업로드 안 됨
- ⚠️ 기기 분실 시 복구 불가

---

"와... 진짜 선택하라고 하네. 대부분 앱은 클라우드를 강요하는데."

**"Local-only Mode"** 선택.

확인 다이얼로그:

---

✅ 데이터는 이 iPhone에만 저장
✅ 서버로 전송 안 됨
✅ End-to-end encryption (키는 당신만 소유)
✅ 수동 백업 권장

---

"좋아. 진짜인지 확인해 보자."

---

## Act 4: 첫 민감한 노트 (Day 3)

환자 상담 후. 새 캡처:

> **환자 C (가명)**
> - Panic disorder, CBT session 3
> - 호흡 기법 효과. 다음 주 exposure therapy
> - 개인 성찰: 환자 두려움이 내 과거 떠올림. 슈퍼비전 필요.

저장.

화면 하단:

**🔒 로컬 암호화 저장됨 | 서버 전송: 없음**

설정 확인:

---

**현재 저장 상태:**
- 총 클립: 3개
- 저장 위치: iPhone 내부 (encrypted)
- 클라우드 업로드: 0 bytes
- 마지막 서버 통신: 없음

---

"진짜... 클라우드에 안 올라가네."

하지만 여전히 의심. *"정말 확실한가?"*

---

## Act 5: 기술적 검증 (Day 5)

개발자 친구 Kenji:

"이 앱 network monitoring 해줄래?"

Kenji가 Charles Proxy로 확인.

**Kenji**: "API 호출 없음. Analytics도 없음. 정말 아무것도 안 보내."

화면: 0 requests to Moments servers.

**Kenji** (감탄): "요즘 보기 드문데. 진짜 offline-first네."

**"믿을 수 있겠어."**

---

## Act 6: 일기의 시작 (Week 2)

**Day 10** - 저녁 일기:

> "오늘 환자 D와의 세션이 힘들었다. PTSD 치료가 더디다.
>
> 하지만... Moments에 이렇게 쓸 수 있다는 게 놀라워. 30년간 종이에만 썼는데, 디지털로 쓰면서도 **안전하다**는 느낌."

화면 하단:

**🔐 암호화되어 저장됨 | 당신만 읽을 수 있습니다**

미소 지었다.

---

## Act 7: 데이터 소유권 확인 (Month 1)

한 달. 47개 클립, 12개 일기.

설정 > Export:

---

**Format:**
- Moments Backup
- Standard JSON
- Plain Text (Markdown)

**암호화:**
- AES-256

**저장 위치:**
- Local Files

---

"Standard JSON + AES-256 + Local"선택.

Export → `moments-backup-2026-12-01.encrypted.json`

파일을 USB 드라이브에 복사 → 집 금고에 보관.

**"내 데이터는... 정말 내 거야. 회사가 아니라, 내가 소유해."**

---

## Act 8: 신뢰의 완성 (Month 2)

두 달째. 93개 클립, 28개 일기. 환자 노트 62개 (모두 device-only).

백업: 주 1회 (USB 드라이브).

동료: "Yuki, 요즘 노트북 많이 쓰네?"

**Dr. Yuki**: "응. Moments. Local-only mode."

**동료**: "정말? 클라우드 안 써? 나도 써볼까? 환자 정보 클라우드 올리기 불안했거든."

**Dr. Yuki**: "써봐. **진짜 개인 지식 관리**란 게 이런 거더라고."

---

## Act 9: Magic Moment - "내 데이터, 내 통제" (Month 3)

연말 회고:

> "30년간 종이 노트. 디지털은 의심스러웠다.
>
> 하지만 Moments는... 달랐다.
>
> 처음으로 디지털 도구를 쓰면서 **통제권**을 느꼈다.
>
> - Local-only mode: 선택권을 나에게
> - 암호화 표시: 투명했다
> - Export: 완전한 소유권
>
> **내 데이터, 내 통제. 이게 진짜 개인 지식.**
>
> 신뢰한다. 처음으로."

---

## Magic Moment

매일 일기 쓸 때 하단 표시:

**🔐 암호화되어 저장됨 | 당신만 읽을 수 있습니다 | 서버 전송: 0 bytes**

**"내가 통제한다. 내가 소유한다. 그게 전부다."**

---

## Requirements Revealed

**Privacy-First Features (MVP):**

1. **Local-only Mode**
   - 온보딩 시 Cloud vs Local 동등한 선택
   - Warning (기기 분실 복구 불가)

2. **투명한 암호화**
   - "🔒 로컬 암호화 저장됨" 표시
   - 실시간 상태 확인

3. **Network 투명성**
   - "서버 전송: 0 bytes"
   - Local-only는 analytics도 전송 안 함

4. **Full Export/Backup**
   - Multiple formats (Backup, JSON, Markdown)
   - AES-256 암호화
   - Local 저장

5. **데이터 소유권**
   - Standard format export
   - No vendor lock-in

**Target Segments:**
- 의료 전문가 (HIPAA)
- 변호사, 상담사
- 저널리스트
- 프라이버시 중시형

**Key Metrics:**
- Local-only mode 선택률
- Privacy-conscious user activation
- Backup 빈도
- "데이터 소유권" NPS

---

## Emotional Journey
- Day 0: 불신/회의 (클라우드의 공포)
- Day 1: 호기심 (오프라인 퍼스트 아키텍처 발견)
- Day 3: 안도 (서버 전송 없음 확인)
- Day 5: 확신 (기술적 검증 완료)
- Week 2: 평온 (데이터의 안전한 소유감)
- Month 3: 소속감/자부심 (진짜 개인 지식 관리의 가치 실현)

---

## 입소문 트리거
- "동료 의사들이 '환자 정보를 기록하는 데 불안하지 않냐'고 물었을 때, Moments의 'Local-only Mode'를 보여주며 '단 1바이트도 서버로 가지 않는다'고 단언할 때"
- "USB에 암호화된 백업본을 복제하여 가방에 넣는 순간, 내 지식에 대한 완전한 통제권을 느끼고 이를 다른 전문가들에게 추천할 때"
