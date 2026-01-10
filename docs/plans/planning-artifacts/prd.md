---
stepsCompleted: [1, 2, 3, 4, 6]
inputDocuments:
  - "docs/plans/moments-mind-studio-product-brief.md"
  - "docs/plans/planning-artifacts/research/market-global-pkm-market-user-pain-points-research-2026-01-08.md"
  - "docs/plans/planning-artifacts/research/technical-emotional-search-engine-research-2026-01-08.md"
  - "docs/plans/planning-artifacts/research/technical-permanent-archive-engine-research-2026-01-08.md"
  - "docs/plans/planning-artifacts/research/technical-semantic-graph-engine-research-2026-01-08.md"
workflowType: 'prd'
lastStep: 6
briefCount: 1
researchCount: 4
brainstormingCount: 0
projectDocsCount: 0
userJourneyCount: 11
---

# Product Requirements Document - new_learn

**Author:** 마스터
**Date:** 2026-01-10

## Executive Summary

### 제품 비전

Moments: Mind Studio는 정보 과잉 시대에 '나'를 잃어가는 현대인들을 위한 **지식 사진관**입니다. 단순한 웹 클리핑 도구를 넘어, 사용자가 저장한 정보들을 통해 자신의 관심사, 감정, 삶의 궤적을 되돌아볼 수 있는 **자아 회복 솔루션**입니다.

### 해결하는 문제

**기능적 문제:**
- 저장만 하고 다시 보지 않는 클리핑 (잊혀지는 지식)
- 여러 툴에 흩어진 파편화된 지식
- 링크 깨짐, 원본 소멸로 인한 접근 불가
- "왜" 저장했는지 의도의 망각
- 폴더 정리와 태깅의 숙제화

**본질적 문제:**
수많은 정보 속에서 '나'라는 존재를 잃어가는 현대인의 자아 상실

### 타겟 사용자

지식을 사랑하지만 정리에 지친 현대인:
- 정보 수집을 즐기지만 정리할 시간과 에너지가 부족함
- 과거 저장 자료를 찾지 못해 좌절한 경험이 있음
- 바쁜 일상 속에서 '나'를 잃어가고 있다는 막연한 불안감을 느낌

### 이 제품을 특별하게 만드는 것

#### Phase 1 MVP 핵심 차별화 요소 (우선순위순)

##### 1. 영구 박제 (Immutable Archive) - MVP 필수
링크가 깨지고 웹사이트가 사라져도, 내 사진관 안의 지식은 영원히 보존됩니다. WACZ 기술 기반으로 웹페이지 전체를 완벽하게 박제하여 시간이 지나도 저장 당시 그대로의 모습을 간직합니다.

**성공 지표:**
- 캡처 성공률 > 95%
- 링크 깨짐으로 인한 접근 실패 0%
- 원본 페이지 소멸 후에도 100% 접근 가능

##### 2. 자동 연결 (Automatic Linking) - MVP 필수
사용자가 수동으로 태그하거나 폴더에 넣지 않아도, AI가 맥락을 분석해 지식들을 자동으로 연결합니다. 시맨틱 그래프가 사용자 대신 지식의 다리를 놓아줍니다.

**정리의 정의:**
- 시스템이 자동으로 시맨틱 그래프에 노드 생성 및 연결 완료
- 사용자의 수동 작업 불필요 (제로 프릭션)

**성공 지표:**
- 자동 연결 정확도 > 80% (사용자 피드백 기반)
- 사용자의 수동 태깅 행위 < 10% (대부분 자동화)

##### 3. 자아 회복 루틴 (Daily Reflection) - MVP 필수
단순 저장이 아닌, 매일 밤 일기를 통해 '나'를 되찾는 성찰 시간. 오늘 모은 지식 조각들을 돌아보며 '나'라는 존재를 기록하고 재발견합니다.

**성공 지표:**
- 일기 작성 습관 형성률 > 40% (주 3회 이상 작성)
- 일기 작성 시 평균 과거 캡처 재방문 횟수 > 3개
- 30일 리텐션 > 60%

##### 4. 자연스러운 망각 (Natural Forgetting) - Phase 1.5 (검증 후 도입)
**[검증이 필요한 가정: 사용자가 완벽한 기억보다 자연스러운 망각을 선호할 것이다]**

기존 PKM 도구들이 "더 많이, 더 완벽하게 저장하라"고 강요할 때, Moments는 "잊어도 괜찮아. 그게 인간이야"라고 말합니다.

**재설계된 메커니즘 (Hard Delete → Fade Out):**
- 캡처 후 3일 동안 시맨틱 그래프에 연결되지 않으면 **점진적 희미화** 시작
- 완전 삭제가 아닌 "아카이브 레이어"로 이동 (검색 결과에서 우선순위 하락)
- 사용자가 언제든 재방문/일기 언급 시 즉시 복원되어 메인 그래프로 복귀
- 이는 **인간 뇌의 장기 기억 메커니즘**을 모방 (망각 곡선 + 재활성화)

**정리의 정의 (명확화):**
- 시맨틱 그래프에서 최소 2개 이상의 다른 노드와 연결됨
- 또는 일기에서 1회 이상 언급됨
- 또는 사용자가 1회 이상 재방문함

**성공 지표:**
- 희미화된 캡처의 복원율 < 5% (대부분 정말 불필요했던 것)
- "3일 타이머 스트레스" 관련 부정 피드백 < 10%
- 전체 캡처 중 희미화되는 비율 20-30% (적절한 필터링)

#### Phase 2 이후 차별화 요소

##### 5. 감성 검색 (Resonant Search) - Phase 2
"비 오던 날의 우울했던 기억"과 닮은 지식을 찾아주는 독보적인 검색 경험. 키워드가 아닌 감정과 맥락으로 과거를 탐색합니다. VAD 모델과 Plutchik의 감정 이론을 기반으로 사용자의 정서적 상태와 공명하는 기억을 찾아냅니다.

**성공 지표:**
- 감성 검색 사용률 > 20% (전체 검색 중)
- 감성 검색 만족도 > 4.0/5.0

##### 6. 디지털 뇌 복제 (Digital Brain Twin) - 궁극적 비전 (Phase 3+)
인간 뇌의 작동 방식을 디지털로 구현합니다:
- **관심도 기반 기억 강도**: 자주 확인하는 지식은 강화되고, 보지 않는 지식은 점차 희미해집니다
- **재회상을 통한 기억 복원**: 일기를 다시 읽거나 예전 기억을 찾는 행위를 하면 지식 그래프에서 연결이 다시 강화됩니다
- 진짜 Second Brain - 단순히 정보를 저장하는 것이 아니라, 사용자의 인지 패턴과 관심사를 학습하고 복제하는 디지털 뇌

### 경쟁 환경 분석

**기존 솔루션들이 해결하지 못한 이유:**

| 경쟁자 | 접근 방식 | 실패 지점 | Moments의 차별점 |
|--------|----------|----------|----------------|
| **Notion, Obsidian** | 강력한 정리 기능 제공 | 정리가 숙제가 됨. 수동 태깅/연결 부담 | 자동 연결 - 제로 프릭션 |
| **Readwise Reader, Matter** | 하이라이트 + 메모 중심 | 링크 깨짐 문제 미해결. 원본 소멸 시 접근 불가 | 영구 박제 - WACZ 완전 보존 |
| **Mem, Reflect** | AI 자동 연결 시도 | 감성적 가치 부재. 도구로만 느껴짐 | 자아 회복 - 일기 통한 성찰 |
| **Evernote** | 만능 노트 앱 | 지나치게 복잡. "나"를 찾는 경험 부재 | 지식 사진관 은유 - 명확한 정체성 |
| **모든 PKM 도구** | "더 많이 저장" 철학 | 완벽주의 강요. 정리 부담 증가 | 자연스러운 망각 - 인간화 |

**핵심 인사이트:**
기존 도구들은 "지식 관리"에만 집중했고, "나를 되찾는 경험"을 제공하지 못했습니다. Moments는 도구가 아닌 **자아 회복 솔루션**입니다.

### 검증이 필요한 핵심 가정 (MVP에서 테스트)

1. **가정 1: 영구 보존의 가치**
   - 사용자가 실제로 과거 캡처를 재방문할까? (현재 PKM 도구에서는 재방문율이 매우 낮음)
   - 검증 방법: 캡처 후 7일/30일/90일 재방문율 추적

2. **가정 2: 일기 습관 형성**
   - 매일 밤 일기를 쓰는 루틴이 정착될까? (대부분의 일기 앱들은 리텐션이 낮음)
   - 검증 방법: 7일/30일 일기 작성 지속률, 주간 작성 빈도

3. **가정 3: 제로 정리의 매력**
   - 자동 연결만으로 충분할까? 사용자가 수동 정리 욕구를 느끼지 않을까?
   - 검증 방법: 수동 태깅/폴더 생성 비율, "수동 정리 기능 추가" 요청 빈도

4. **가정 4: 망각의 수용**
   - 사용자가 "3일 후 희미화"를 자유로 느낄까, 불안으로 느낄까?
   - 검증 방법: 희미화 알림에 대한 감정 반응, 복원 시도율, 정성 인터뷰

5. **가정 5: 기술 복잡도 vs UX 심플함**
   - Neo4j, GraphRAG, WACZ 같은 복잡한 스택으로도 "2초 캡처"가 가능할까?
   - 검증 방법: 캡처 완료까지 평균 소요 시간, 실패율

## 프로젝트 분류

**기술 타입:** Mobile App (Primary) + Web App (Secondary)
**도메인:** General (Personal Knowledge Management)
**복잡도:** Medium-High
**프로젝트 컨텍스트:** Greenfield - 새로운 프로젝트

### 분류 근거

**Mobile App을 Primary로 선정한 이유:**
- Phase 1의 핵심은 iOS/Android 네이티브 앱과 Share Extension
- "2초 안에 완료"되는 캡처 경험이 제품의 핵심 가치
- 모바일 우선 UX: The Capture (캡처), The Atelier (정리)

**Web App을 Secondary로 포함한 이유:**
- Browser Extension을 통한 데스크톱 캡처 지원
- 웹 버전을 통한 크로스 플랫폼 접근성

**복잡도 평가 (Medium-High):**
- **High 수준의 기술 스택:**
  - Permanent Archive Engine (WACZ, SingleFile, Playwright)
  - Semantic Graph Engine (LlamaIndex, Neo4j, GraphRAG)
  - Emotional Search Engine (감성 분석, VAD 모델, Plutchik)
  - 멀티모달 AI 처리 (텍스트, 이미지, 맥락)

- **Medium 수준의 도메인 복잡도:**
  - PKM 도메인은 healthcare나 fintech처럼 고도로 규제된 분야가 아님
  - 표준 보안 및 UX 요구사항 적용

**기술 스택과 UX 심플함의 균형:**
- 백엔드: 복잡한 AI/그래프 처리는 비동기로 진행
- 프론트엔드: 사용자는 "캡처 버튼 누르기"만 경험 (2초 목표)
- 아키텍처: Event-driven 설계로 UX와 처리 레이어 분리

**입력 문서:**
- Product Brief: 1개
- Market Research: 1개 (PKM 시장 분석 및 사용자 페인 포인트)
- Technical Research: 3개 (감성 검색, 영구 박제, 시맨틱 그래프)

## Success Criteria

### User Success

**North Star: "매일 밤 일기를 쓰면서 나에 대해 알아가는 순간"**

Moments의 성공은 사용자가 단순히 정보를 저장하는 것이 아니라, **자신을 재발견하는 경험**에서 측정됩니다.

**핵심 사용자 성공 지표:**

1. **습관 형성 성공**
   - 일기 작성 습관 정착률: 주 3회 이상 작성하는 사용자 > 40%
   - Journal Completion Rate: 밤 9시 루틴 완성률 > 60%
   - 30일 리텐션: > 60%
   - **Activation (활성화)**: 첫 7일 내 일기 1회 작성 > 50%

2. **재발견의 기쁨**
   - Reconnection Rate: 과거 캡처 재방문율 > 40%
   - 일기 작성 시 평균 과거 캡처 참조 횟수 > 3개
   - **"나 재발견" 측정**: 일기 작성 후 "성찰에 도움됨" 버튼 클릭율 > 30%

3. **감정적 만족**
   - Emotional Satisfaction: 회고 후 만족도 > 4.2/5.0
   - NPS (Net Promoter Score): > 50
   - "이 앱이 내 삶을 바꿨다" 피드백 수집 (정성)

4. **핵심 기능 성공 지표**
   - **캡처 성공**: 캡처 성공률 > 95%, 2초 내 완료율 > 90%
   - **영구 보존**: 링크 깨짐 접근 실패 0%, 원본 소멸 후 접근 가능 100%
   - **자동 연결 신뢰도**: 시스템 추천 연결에 대한 "helpful" 피드백 > 80%
     - 목표 80%, 최소 허용 50%
     - 측정: 연결 카드에 "도움됨/도움안됨" 피드백 버튼
     - 중요: 신규 연결 추가 OK, 추천 연결 해제는 실패 신호
   - **망각의 품질**: 망각의 공간 이동 후 30일 내 복원율 < 10%
     - 낮을수록 좋음 = 정말 불필요한 것만 희미화됨

5. **일일 참여 지표**
   - Capture Rate: 일일 평균 클리핑 > 5회
   - 캡처 후 Ghost Memo (한 줄 생각) 작성율: > 30%

**사용자 성공의 순간 (Aha Moments):**
- "3개월 전 일기를 읽으며 그때의 내가 떠오르는 순간"
- "자동 연결된 지식들을 보며 '내 생각의 패턴'을 발견하는 순간"
- "망각의 공간에서 정말 불필요했던 캡처가 사라지며 느끼는 해방감"

### Business Success

**비즈니스 우선순위: 참여도 → 성장 (입소문) → 수익**

*참여도가 성장의 전제조건입니다. 참여 없이는 입소문도 없습니다.*

**첫 달 목표 (초기 견인력 확보):**

1. **첫 100명 확보**
   - Product Hunt 런칭
   - Reddit (r/PKMS, r/productivity) 참여
   - Twitter/X PKM 커뮤니티 소개
   - Hacker News "Show HN" 포스트

2. **초기 참여도 검증**
   - 첫 7일 일기 작성율 (Activation): > 30%
   - 일일 평균 캡처: > 3회
   - 초기 피드백 수집 (정성)

**3개월 목표 (가설 검증 + 참여도 확립):**

1. **참여도 우선 (최우선)**
   - DAU/MAU 비율: > 0.4 (주 3회 이상 사용)
   - Capture per User per Day: > 5회
   - Journal Completion per Week: > 3회
   - Activation: 첫 7일 내 일기 1회 작성 > 50%

2. **핵심 지표**
   - MAU (Monthly Active Users): **500명** (현실적 목표)
   - 일기 작성 습관 정착 사용자: 200명 (40% of MAU)
   - 철학: "가설이 틀려도 사용자가 가치를 찾았다면 성공"

3. **검증 가정 추적 (우선순위 지정)**
   - **우선 검증 (3개월):**
     - 가정 1 (영구 보존 가치): 캡처 후 7일/30일/90일 재방문율 측정
     - 가정 2 (일기 습관): 7일/30일 일기 작성 지속률 측정
     - 가정 5 (기술 vs UX): 캡처 평균 소요 시간 < 2초, 실패율 < 5%
   - **후속 검증 (6개월):**
     - 가정 3 (제로 정리): 수동 태깅 비율 < 10%
     - 가정 4 (망각 수용): 희미화 알림 부정 피드백 < 10%

**6개월 목표 (참여도 안정화 + 입소문 시작):**

1. **참여도 심화**
   - 30일 리텐션: > 60%
   - 일기 습관 정착: > 40% (주 3회 이상)
   - "성찰 도움됨" 클릭율: > 30%

2. **입소문 시작**
   - MAU: 800명
   - Viral K-factor: > 0.3 (건강한 성장)
   - NPS: > 40
   - 자발적 SNS/블로그 리뷰: 월 5+ 건

3. **완전한 가정 검증**
   - 5개 가정 모두 측정 완료
   - Phase 1.5 (망각의 인간화) 도입 여부 결정

**12개월 목표 (입소문 성장 + 지속가능성):**

1. **성장 지표**
   - MAU: **2,000명** (유기적 성장, 현실적 목표)
   - Viral K-factor: > **0.5** (1명이 0.5명 초대, 건강한 입소문)
   - NPS: > 50
   - 앱스토어 리뷰 평점: > 4.5/5.0
   - **"입소문" 출처 신규 가입: > 40%**
     - 측정 방법: Referral link UTM 추적 + 가입 설문 "어떻게 알게 되셨나요?"

2. **참여도 유지**
   - 30일 리텐션: > 60%
   - 90일 리텐션: > 40%
   - 주 활성 사용자 비율 (WAU/MAU): > 0.7

3. **수익 지표**
   - 구독 모델: 프리미엄 기능 전환율 > 5%
   - AI 비용 관리: 개인 API 키 사용자 옵션 제공
   - MRR (Monthly Recurring Revenue): 트래킹 (목표는 성장 후 설정)

4. **커뮤니티 & 브랜드**
   - "정말 좋은 솔루션" 평가 확보
   - SNS/블로그 자발적 리뷰: 월 10+ 건
   - PKM 커뮤니티 내 인지도 확보

**운영 지표 (1인 개발자 + 직장인 지속가능성):**
- 주간 유지보수 시간: < 10시간
- 치명적 버그 발생률: < 1% (MAU 대비)
- 서버 비용: 사용자당 < $2/월
- AI 비용: 개인 API 키로 전가 또는 최적화로 < $0.5/사용자/월

**입소문 트리거 (사용자가 친구에게 추천하는 순간):**
- "3개월 전 일기를 보며 옛날 내가 떠올랐을 때"
- "깨진 링크 걱정 없이 과거 자료를 다시 찾았을 때"
- "태그 안 달았는데 AI가 알아서 연결해줬을 때"
- "일기를 쓰며 내가 무얼 좋아하는지 깨달았을 때"

### Technical Success

**핵심 기술 목표:**

**Phase 0: Tech Prototype (Week 1-4) - Critical Path 검증**

🚨 **2초 캡처 실패 = 전체 제품 실패**

- **목표**: "2초 캡처 + 영구 보존" 기술 실현가능성 증명
- **Success Criteria**:
  - Share Extension → WACZ 저장 평균 소요 시간 < 2초 (사용자 체감)
  - 캡처 성공률 > 95%
  - 10개 주요 사이트 테스트 (뉴스, 블로그, SNS 등)
- **Deliverable**: 기술 PoC, 성능 벤치마크 보고서
- **Go/No-Go Decision**: 2초 달성 못하면 아키텍처 재설계

**Phase 1: MVP (Month 1-3)**

1. **Permanent Archive Engine**
   - 캡처 성공률: > 95%
   - WACZ 완전 보존율: 100%
   - 평균 캡처 시간: < 2초 (사용자 체감)
   - 백그라운드 처리: SingleFile CLI 기반

2. **Semantic Graph Engine**
   - 자동 연결 "helpful" 피드백: 목표 > 80%, 최소 허용 > 50%
   - LazyGraphRAG 비용 절감: 70-90% (기존 대비)
   - 그래프 쿼리 응답 시간: < 500ms

3. **시스템 안정성**
   - 서비스 가용성: > 99.5%
   - API 응답 시간 (p95): < 1초
   - 모바일 앱 크래시율: < 0.5%
   - 데이터 손실: 0건

4. **측정 인프라 (MVP 필수)**
   - 기본 이벤트 로깅 시스템 (Amplitude/Mixpanel)
   - Feature Flag 시스템 (LaunchDarkly/자체)
   - A/B 테스트 프레임워크
   - 성능 모니터링 (Sentry)

5. **확장성**
   - 동시 접속자 처리: 500명
   - 사용자당 저장 용량: 평균 500MB 지원

6. **보안 & 프라이버시**
   - E2E 암호화 옵션 제공
   - 로컬 우선 저장 옵션 (민감 데이터)
   - GDPR/개인정보보호법 준수
   - 보안 취약점: 0건 (critical/high)

**Phase 2: Scale (Month 6-12)**

- 동시 접속자: 2,000명
- Playwright 기반 고급 캡처 엔진
- K8s 오토스케일링

### Measurable Outcomes

**Phase 0: Tech Prototype (Week 1-4):**

| 지표 | 목표 | 측정 방법 |
|------|------|----------|
| **2초 캡처** | 평균 < 2초 | 성능 테스트 (10개 사이트) |
| **캡처 성공률** | > 95% | E2E 테스트 자동화 |
| **Go/No-Go** | 성공 시 MVP 진행 | 기술 검토 회의 |

**첫 달 (초기 견인력):**

| 지표 | 목표 | 측정 방법 |
|------|------|----------|
| **첫 100명** | 100 MAU | 가입자 수 집계 |
| **초기 Activation** | > 30% | 첫 7일 일기 작성율 |
| **기술 안정성** | 크래시율 < 1% | Sentry 모니터링 |

**Phase 1 MVP 완료 기준 (3개월):**

| 지표 | 목표 | 측정 방법 |
|------|------|----------|
| **참여도** | DAU/MAU > 0.4 | 이벤트 로깅 |
| **습관 정착** | 일기 습관 200명 | 주 3회+ 작성자 수 |
| **기술 성공** | 2초 캡처 90% | 평균 캡처 완료 시간 |
| **MAU** | 500명 | 월별 활성 사용자 |
| **우선 가설 검증** | 3개 가정 측정 | A/B 테스트, 인터뷰 |

**Phase 1.5 검증 완료 기준 (6개월):**

| 지표 | 목표 | 측정 방법 |
|------|------|----------|
| **망각 수용** | 부정 피드백 < 10% | 희미화 알림 반응 추적 |
| **망각 품질** | 30일 복원율 < 10% | 망각 공간 복원율 |
| **리텐션** | 30일 > 60% | 코호트 분석 |
| **MAU** | 800명 | 월별 활성 사용자 |
| **입소문 시작** | K-factor > 0.3 | Referral 추적 |

**Phase 2 성장 확인 기준 (12개월):**

| 지표 | 목표 | 측정 방법 |
|------|------|----------|
| **입소문 성장** | K-factor > 0.5 | Referral 추적 |
| **MAU** | 2,000명 | 월별 활성 사용자 |
| **NPS** | > 50 | 분기별 설문 |
| **수익** | Premium 전환 > 5% | 구독 전환율 |
| **리텐션** | 90일 > 40% | 코호트 분석 |

**AARRR (Pirate Metrics) 프레임워크:**

| 단계 | 지표 | 3개월 목표 | 12개월 목표 | 측정 방법 |
|------|------|-----------|------------|----------|
| **Acquisition** | 신규 가입 | 500명 | 2,000명 | 가입자 수 |
| **Activation** | 첫 7일 일기 작성 | > 50% | > 60% | 이벤트 로깅 |
| **Retention** | 30일 리텐션 | > 60% | > 60% | 코호트 분석 |
| **Referral** | K-factor | 0.2-0.3 | > 0.5 | UTM + 설문 |
| **Revenue** | Premium 전환 | N/A | > 5% | 결제 데이터 |

## Product Scope

### MVP - Minimum Viable Product (Phase 1: 0-3개월)

**입소문의 핵심 - 반드시 포함:**

1. **영구 박제 (Immutable Archive)**
   - "링크 안 깨지네!" WOW 모멘트
   - WACZ 기반 완전 보존
   - Share Extension (iOS/Android)
   - Browser Extension (Chrome)

2. **자동 연결 (Automatic Linking)**
   - "태그 안 해도 되네!" 마찰 제거
   - 시맨틱 그래프 자동 생성
   - LlamaIndex + Neo4j 기반
   - 연결 카드에 "도움됨/도움안됨" 피드백 버튼

3. **일기 루틴 (Daily Reflection)**
   - "나를 알아가는 경험" North Star
   - 밤 9시 루틴 (AI 초안 + 수동 조정)
   - The Self-Query (나를 묻는 질문)
   - 일기 작성 후 "성찰에 도움됨" 피드백 버튼

4. **2초 캡처**
   - 이게 안 되면 습관 형성 실패
   - 무드 컬러 각인 (5가지)
   - Ghost Memo (선택적 한 줄 생각)

5. **기본 검색**
   - 키워드 검색
   - 타임라인 뷰
   - 무드별 필터

6. **입소문 최소 기능 (추가)**
   - "이 앱 추천하기" Referral 링크 생성
   - UTM 파라미터 자동 추가
   - 가입 시 "어떻게 알게 되셨나요?" 설문

7. **측정 인프라**
   - 이벤트 로깅 시스템
   - 성능 모니터링
   - 피드백 수집 UI

**MVP 제외 (Phase 1.5 이후):**
- 망각의 인간화 (3일 룰) - 가설 검증 필요
- 감성 검색 - Phase 2
- 공동 사진관 - Phase 3
- 아침 루틴 (The Studio) - Phase 2

### Growth Features (Post-MVP)

**Phase 1.5: 검증 후 도입 (3-6개월)**

1. **자연스러운 망각 (Natural Forgetting)**
   - 3일 룰 + Fade Out 메커니즘
   - 망각의 공간 (아카이브 레이어)
   - 복원 기능
   - **조건: 가정 4 검증 완료 (부정 피드백 < 10%)**

**Phase 2: 지능화 (6-12개월)**

1. **감성 검색 (Resonant Search)**
   - VAD 모델 + Plutchik 감정 추출
   - The Memory Dial UI
   - 맥락 기반 재발견

2. **아침 루틴 (The Studio)**
   - Today's Arsenal (오늘의 무기)
   - Quick Menu (이동시간 전용)
   - 일정 연동 큐레이션

3. **고급 자동화**
   - Smart Deduplication (지능형 중복 감지)
   - Voice Journal (음성 일기)
   - 나이테 리포트 (월간)

4. **입소문 강화**
   - 지식 선물하기 (간소화 버전)
   - 공유 가능한 일기 하이라이트

**Phase 3: 연결 (12-18개월)**

1. **공동 사진관 (Shared Studio)**
   - 테마형 공동 앨범
   - Knowledge Gifting 완전판
   - Silent Resonance (조용한 공명)

2. **회고 확장**
   - 분기/연간 나이테 리포트
   - Constellation View (D3.js 시각화)
   - 성장 타임라인

### Vision (Future: Phase 4+)

**디지털 뇌 복제 (Digital Brain Twin) - 궁극적 비전**

인간 뇌의 작동 방식을 디지털로 구현:
- 관심도 기반 기억 강도 (자주 보는 지식 강화)
- 재회상을 통한 기억 복원 (일기/검색으로 연결 재강화)
- 사용자 인지 패턴 학습 및 복제

**확장 비전:**
- Desktop/Web 버전
- API 개방 (3rd party 연동)
- Calendar, Todo 앱 연동
- 커뮤니티 지식 공유 플랫폼

## User Journeys

Moments의 성공은 다양한 사용자 세그먼트가 각자의 방식으로 가치를 발견하는 데 달려 있습니다. 11개의 사용자 여정은 AARRR 프레임워크 전체를 커버하며, MVP부터 Phase 3까지의 기능 요구사항을 도출합니다.

### Journey Overview

| # | 이름 | 역할 | AARRR 단계 | 핵심 가치 | 문서 링크 |
|---|------|------|-----------|----------|---------|
| 1 | 이지훈 | 32세 PM, 한국 | Activation → Retention | 일과 삶 균형 재발견 | [상세 여정](./user-journeys/journey-01-lee-jihoon.md) |
| 2 | Sarah Mitchell | 28세 Engineer, 미국 | Activation | 첫 사용자 빈 캔버스 경험 | [상세 여정](./user-journeys/journey-02-sarah-mitchell.md) |
| 3 | 박서연 | 16세 고등학생, 한국 | Activation → Revenue | 청소년 진로 발견 | [상세 여정](./user-journeys/journey-03-park-seoyeon.md) |
| 4 | Aiden Rodriguez | 21세 대학생, 브라질 | Activation | 관심사 교집합 발견 | [상세 여정](./user-journeys/journey-04-aiden-rodriguez.md) |
| 5 | Priya Sharma | 29세 프리랜서, 인도 | Phase 2 Validation | Emotional Search 활용 | [상세 여정](./user-journeys/journey-05-priya-sharma.md) |
| 6 | Marcus Chen | 35세 Architect, 싱가포르 | Acquisition → Activation | 회의론자 전환 (Anti-productivity) | [상세 여정](./user-journeys/journey-06-marcus-chen.md) |
| 7 | Elena Rodriguez | 27세 Marketing Manager, 멕시코 | Reactivation | Churn 극복 (Time Capsule) | [상세 여정](./user-journeys/journey-07-elena-rodriguez.md) |
| 8 | 이지훈 2년 후 | 34세 Director, 한국 | Deep Retention | Power User (Phase 2-3 기능) | [상세 여정](./user-journeys/journey-08-lee-jihoon-2yr.md) |
| 9 | Dr. Yuki Tanaka | 42세 Psychiatrist, 일본 | Activation | 프라이버시 장벽 극복 | [상세 여정](./user-journeys/journey-09-dr-yuki-tanaka.md) |
| 10 | 박미영 | 48세 교사, 한국 | Referral | 부모→자녀 입소문 메커니즘 | [상세 여정](./user-journeys/journey-10-park-miyoung.md) |
| 11 | Jamie Park | 29세 UX Writer, 미국 | Acquisition | 디지털 미니멀리스트 설득 | [상세 여정](./user-journeys/journey-11-jamie-park.md) |

### Journey Requirements Summary

11개 여정에서 도출된 기능 요구사항을 Phase별로 정리:

**MVP Features (Phase 1: 필수):**
- 2초 캡처 (폴더/태그 없이)
- 자동 연결 (시맨틱 그래프)
- 일기 루틴 with 자동 클립 연결
- Zero-friction onboarding (빈 캔버스)
- Local-only mode + End-to-end encryption
- 부모용 온보딩 플로우
- Minimal UI (no gamification, notifications off by default)
- "도움됨/도움안됨" 피드백 버튼 (자동 연결, 일기)

**Phase 1.5 (Validation: 3-6개월):**
- Time Capsule ("X개월 전 오늘" 알림)
- Dormant user reactivation email 시리즈
- Referral mechanism (친구/가족 초대)
- Full Export/Backup (AES-256, multiple formats)
- "Your memories are waiting" positioning

**Phase 2 (Intelligence: 6-12개월):**
- Emotional Search (감정 유사도 검색 - Priya, 이지훈 2년차)
- 나이테 리포트 (성장 궤적 시각화 - 이지훈 2년차)
- Smart Filtering (결과 너무 많을 때 Top N - 이지훈 2년차)
- Noise Reduction (강한 연결만 표시 - 이지훈 2년차)
- Year in Review 자동 생성 (Elena)

**Phase 3 (Vision: 12-18개월):**
- GraphRAG (미발견 연결고리 제안 - 이지훈 2년차)
- AI 큐레이터
- 대화형 디지털 뇌

### Critical Journey Insights

**Marcus (회의론자)의 교훈:**
- **Anti-productivity-porn positioning**: "정리 안 해도 된다"가 핵심 차별화
- **Zero friction의 중요성**: 폴더, 태그, 수동 링크 모두 제거
- **첫 일기의 힘**: Day 18에 첫 일기 작성이 전환점 (Activation 지표)

**Elena (재방문자)의 교훈:**
- **Time Capsule의 감정적 힘**: "6개월 전 오늘" 알림이 reactivation 결정타
- **Sunk cost 활용**: "당신의 203개 추억" - 버리기 아까운 감정
- **Friend referral 효과**: Email보다 친구 추천이 훨씬 강력

**이지훈 2년 후 (Power User)의 교훈:**
- **Scale 문제 예측**: 검색 결과 너무 많음, 자동 링크 노이즈 증가
- **Phase 2 features 정당화**: Emotional Search, 나이테 리포트, GraphRAG 필요성 입증
- **Magic Moment**: "내 디지털 뇌가 나보다 나를 더 잘 안다"

**Dr. Yuki (프라이버시)의 교훈:**
- **Trust building 필수**: Local-only mode, 암호화 투명성, Export 소유권
- **Target segment**: 의료/법률/저널리즘 전문가 세그먼트 확보
- **Network transparency**: "서버 전송: 0 bytes" 명시적 표시

**박미영 (부모)의 교훈:**
- **Generational appeal**: 부모도 자기 발견 (자기 돌봄 패턴 발견)
- **"먼저 써보세요" 전략**: 이해한 후 추천해야 수용률 높음
- **Viral loop**: 부모 → 자녀 → 부모의 친구들 → 반복

**Jamie (미니멀리스트)의 교훈:**
- **역설적 positioning**: "앱을 추가했는데 전체 앱이 줄었다" (17개 → 15개)
- **App consolidation**: Bear/Things/Day One 대체 가능
- **Thought leader endorsement**: Cal Newport 같은 인플루언서 중요

### AARRR Mapping

| AARRR 단계 | 커버하는 여정 | 핵심 인사이트 |
|-----------|------------|-------------|
| **Acquisition** | Marcus (회의론자), Jamie (미니멀리스트) | 저항 극복: "또 다른 앱" → "이건 다르다" 전환 |
| **Activation** | 이지훈, Sarah, 박서연, Aiden, Marcus, Dr. Yuki | 첫 일기 작성이 결정적 전환점 (Day 3-18) |
| **Retention** | 이지훈, 박서연 | 일기 습관 정착 (주 3회+)이 30일 리텐션 예측 |
| **Referral** | 박미영 (부모), Elena (친구 추천) | 부모→자녀, 친구→친구 입소문 메커니즘 |
| **Revenue** | 이지훈 2년 후, Priya | Phase 2 features (Emotional Search, 나이테)가 Premium 전환 동기 |
| **Reactivation** | Elena | Time Capsule + "추억이 기다립니다" 포지셔닝 |

### Journey-Driven Product Decisions

11개 여정 분석을 통해 확정된 제품 결정:

1. **MVP에 "도움됨" 피드백 버튼 필수 포함** (Marcus, 이지훈)
   - 자동 연결 신뢰도 측정
   - 일기 작성 후 성찰 도움 측정

2. **Local-only mode는 MVP 필수** (Dr. Yuki)
   - 의료/법률 전문가 세그먼트 확보
   - Privacy-first positioning 차별화

3. **부모용 온보딩 플로우 Phase 1에 포함** (박미영)
   - Referral 메커니즘의 핵심
   - "먼저 써보세요" 전략

4. **Time Capsule은 Phase 1.5에 추가** (Elena)
   - Reactivation의 결정타
   - 6개월 dormant user 복귀 메커니즘

5. **Phase 2 features 우선순위: Emotional Search > 나이테 리포트 > GraphRAG** (이지훈 2년 후, Priya)
   - Power User retention 핵심
   - Premium 전환 동기

6. **Anti-productivity positioning 강화** (Marcus, Jamie)
   - "정리 안 해도 된다"
   - "앱을 줄이는 앱"
   - Cal Newport endorsement 활용

## Innovation & Novel Patterns

### Detected Innovation Areas

Moments: Mind Studio introduces **paradigm shifts** across three dimensions of Personal Knowledge Management:

#### 1. 영구 박제 (Permanent Archiving) - Technical Innovation

**What's Novel:**
전통적 웹 클리핑 도구들은 URL만 저장하거나 텍스트만 추출합니다. Moments는 **WACZ (Web Archive Collection Zipped)** 기술을 활용해 웹페이지를 **완전한 상태로 박제**합니다.

**Challenged Assumption:**
"링크가 깨지면 어쩔 수 없다" → "모든 지식은 영구적으로 보존 가능하다"

**Technical Novelty:**
- SingleFile + Playwright를 활용한 완전한 DOM/CSS/JavaScript 캡처
- 타임캡슐 방식: 저장 시점의 상태를 100% 복원 가능
- 링크 깨짐률 0% 달성 (기존 도구는 30-50% 링크 깨짐)

#### 2. 자연스러운 망각 (Natural Forgetting) - UX/Cognitive Innovation

**What's Novel:**
기존 PKM 도구: "더 많이, 더 완벽하게 저장하라"
Moments: "잊어도 괜찮아. 그게 인간이야"

**Challenged Assumption:**
"모든 저장은 영구적이어야 한다" → "인간 뇌처럼 자연스럽게 망각해야 한다"

**Cognitive Science Foundation:**
- **망각 곡선 (Ebbinghaus)** + **간격 반복 (Spaced Repetition)** 원리 적용
- 캡처 후 3일간 시맨틱 그래프에 연결 안 되면 → 점진적 희미화
- Hard Delete ❌ → Fade-out to Archive Layer ✓
- 재방문/일기 언급 시 즉시 복원 (인간 기억의 재활성화 모방)

**Innovation Impact:**
- "정리해야 한다"는 강박 제거
- 90% 사용자가 경험하는 "저장 후 죄책감" 해결
- 자동 품질 필터: 정말 중요한 지식만 살아남음

#### 3. 감성 검색 (Emotional Search) - AI Innovation (Phase 2)

**What's Novel:**
기존 검색: 키워드, 태그, 날짜
Moments: **감정 상태**와 **맥락**으로 검색

**Challenged Assumption:**
"검색은 키워드 기반이어야 한다" → "인간은 감정으로 기억을 떠올린다"

**Technical Foundation:**
- **VAD 모델 (Valence-Arousal-Dominance)**: 감정을 3차원 벡터로 수치화
- **Plutchik의 감정 이론**: 8가지 기본 감정 휠
- **감정 유사도 검색**: "실망했을 때" → 과거 비슷한 감정 상태의 캡처 검색

**Example Use Case:**
```
사용자 쿼리: "실망했을 때"
시스템 응답: 
- 2023년 12월 일기: "디자인 제안 거절됨" (감정 유사도 95%)
- 2024년 4월 일기: "팀원 퇴사, 위기" (감정 유사도 92%)

과거의 나: "거절당했지만... 일주일 후 더 나은 아이디어가 나왔어. 
거절은 끝이 아니라 새 시작."
```

**Innovation Impact:**
- 키워드 없이도 과거 기억 접근
- 감정 치유: 과거의 나로부터 위로받기
- 장기 사용자 (2년+) 핵심 가치

#### 4. 디지털 뇌 복제 (Digital Brain Twin) - Vision (Phase 3)

**What's Novel:**
기존 PKM: 지식 데이터베이스
Moments: **인지 패턴 복제**

**Challenged Assumption:**
"PKM은 저장 도구다" → "PKM은 제2의 뇌다"

**Cognitive Replication:**
- **관심도 기반 기억 강도**: 자주 확인하는 지식 = 시냅스 강화
- **재회상 통한 복원**: 일기 다시 읽기 = 기억 재활성화
- **GraphRAG**: 미발견 연결고리 제안 (뇌의 무의식적 연상 작용)

**나이테 리포트 (Growth Rings Report):**
```
동심원 시각화:
- 2026년 (내부 원): "AI 기초 학습"
- 2027년 Q1-Q2: "AI 윤리 깊이 탐구"
- 2027년 Q3-Q4: "실무 적용"
- 2028년 (외부 원): "사상적 리더십"

터닝 포인트: 2027년 6월 - "첫 컨퍼런스 발표"
```

**Innovation Impact:**
- 사용자가 인지하지 못한 성장 궤적 시각화
- "나는 정말 성장했구나" 자기 인식
- 장기 리텐션 (2년+) 핵심 동기

#### 5. Anti-Productivity 철학 - Philosophical Innovation

**What's Novel:**
기존 생산성 도구: "더 많이 하라"
Moments: "더 깊이 이해하라"

**Challenged Assumption:**
"생산성 = 더 많은 output" → "생산성 = 더 깊은 자기 이해"

**Positioning:**
- "The Anti-Productivity App"
- "One App to Replace Many" (Bear + Things + Day One 대체)
- Digital Minimalist 타겟 (Cal Newport 독자)

**Innovation Impact:**
- 역설: 앱을 추가했는데 전체 앱 수 감소 (17개 → 15개)
- Screen time 감소: Bear ↓66%, Things ↓42%
- "생산성 포르노" 피로 세그먼트 확보

### Market Context & Competitive Landscape

**Innovation Validation:**

| 경쟁자 | 접근 방식 | 실패 지점 | Moments 혁신 |
|--------|----------|----------|-------------|
| **Notion, Obsidian** | 강력한 정리 기능 | 정리가 숙제됨 | 자동 연결 + 자연스러운 망각 |
| **Readwise, Matter** | 하이라이트 중심 | 링크 깨짐 미해결 | WACZ 영구 박제 (0% 링크 깨짐) |
| **Mem, Reflect** | AI 자동 연결 시도 | 감성적 가치 부재 | 감성 검색 + 자아 회복 루틴 |
| **Evernote** | 만능 노트 앱 | 지나치게 복잡 | 지식 사진관 은유 - 명확한 정체성 |

**Key Insight:**
기존 도구들은 "지식 관리"에만 집중했고, **"나를 되찾는 경험"**을 제공하지 못했습니다. Moments는 도구가 아닌 **자아 회복 솔루션**입니다.

**Market Gap:**
- PKM 시장: $2B+ (2026)
- 하지만 30일 리텐션 < 25% (대부분 도구)
- "앱 피로" 증가: 평균 사용자 앱 17개 (Digital Minimalist 증가)
- **미충족 니즈**: 정리 없는 지식 관리 + 감성적 연결

### Validation Approach

**5가지 핵심 가정의 검증 전략:**

#### 1. 영구 보존의 가치
**가정:** 사용자가 실제로 과거 캡처를 재방문할까?
**검증 방법:**
- 캡처 후 7일/30일/90일 재방문율 추적
- 목표: 7일 > 30%, 30일 > 40%
- **실패 신호:** 30일 < 20% → 영구 보존이 과잉 기능

#### 2. 일기 습관 형성
**가정:** 매일 밤 일기를 쓰는 루틴이 정착될까?
**검증 방법:**
- 7일/30일 일기 작성 지속률
- 목표: 주 3회 이상 작성 > 40%
- **실패 신호:** 30일 < 20% → 일기 루틴 재설계 필요

#### 3. 제로 정리의 매력
**가정:** 자동 연결만으로 충분할까?
**검증 방법:**
- 수동 태깅/폴더 생성 비율 < 10%
- "수동 정리 기능 추가" 요청 빈도
- **실패 신호:** 수동 정리 요청 > 30% → 하이브리드 모드 고려

#### 4. 망각의 수용
**가정:** 사용자가 "3일 후 희미화"를 자유로 느낄까, 불안으로 느낄까?
**검증 방법:**
- 희미화 알림에 대한 감정 반응 (정성 인터뷰)
- 복원 시도율 < 10% (대부분 정말 불필요)
- **실패 신호:** "3일 타이머 스트레스" 부정 피드백 > 20% → 타이머 연장 또는 옵션화

#### 5. 기술 복잡도 vs UX 심플함
**가정:** Neo4j, GraphRAG, WACZ로도 "2초 캡처" 가능할까?
**검증 방법:**
- 캡처 완료 평균 시간 < 2초 (90%ile)
- 캡처 실패율 < 5%
- **실패 신호:** 평균 시간 > 5초 → 아키텍처 재설계

**Phase-별 검증 우선순위:**

| Phase | 검증 대상 | 핵심 메트릭 | Go/No-Go 기준 |
|-------|----------|-----------|--------------|
| **Phase 0 (Week 1-4)** | 2초 캡처 기술 검증 | 캡처 시간, 성공률 | < 3초, > 90% |
| **Phase 1 (Month 1-3)** | 일기 습관 + 자동 연결 | 30일 리텐션, 자동 연결 정확도 | > 50%, > 70% |
| **Phase 1.5 (Month 3-6)** | 자연스러운 망각 | 복원율, 부정 피드백 | < 15%, < 20% |
| **Phase 2 (Month 6-12)** | 감성 검색 | 감성 검색 사용률, 만족도 | > 15%, > 4.0/5 |
| **Phase 3 (Month 12+)** | 디지털 뇌 복제 | 장기 리텐션, NPS | > 70% (2년), > 60 |

### Risk Mitigation

**Innovation Risk #1: 자연스러운 망각 거부감**
- **Risk:** 사용자가 "자동 삭제"로 오해 → 신뢰 상실
- **Mitigation:**
  - Hard Delete ❌ → Fade-out ✓ (완전 삭제 없음)
  - "아카이브 레이어" 네이밍으로 안심감 제공
  - 언제든 복원 가능 명시
  - Phase 1.5로 연기 (검증 후 도입)
- **Fallback:** 옵션화 ("자연스러운 망각" On/Off)

**Innovation Risk #2: WACZ 기술 복잡도**
- **Risk:** 모바일에서 WACZ 처리 성능 저하 → 2초 캡처 실패
- **Mitigation:**
  - 서버 사이드 캡처 (모바일은 URL만 전송)
  - Progressive Loading: 텍스트 먼저, 미디어 나중에
  - 캡처 상태 투명하게 표시
- **Fallback:** HTML snapshot (WACZ 실패 시)

**Innovation Risk #3: 감성 검색 정확도**
- **Risk:** VAD 모델이 감정 오판 → 사용자 실망
- **Mitigation:**
  - Phase 2로 연기 (충분한 일기 데이터 확보 후)
  - 키워드 검색과 하이브리드 제공
  - 피드백 루프로 모델 개선
- **Fallback:** 감성 검색을 "실험적 기능"으로 라벨링

**Innovation Risk #4: GraphRAG 비용**
- **Risk:** 모든 클립에 LLM 임베딩 → 비용 폭발
- **Mitigation:**
  - Lazy Evaluation: 첫 재방문 시 임베딩
  - 캐싱: 동일 URL은 공유 임베딩
  - Free tier: 500 clips/month 제한
- **Fallback:** 기본 TF-IDF 검색 (Pro tier만 GraphRAG)

**Innovation Risk #5: Anti-Productivity 포지셔닝 오해**
- **Risk:** "게으른 앱"으로 오인 → 진지한 사용자 이탈
- **Mitigation:**
  - "Anti-Productivity Theater" 명확화
  - "더 깊이 이해하라" 메시지 강조
  - Cal Newport 등 Thought Leader 추천 확보
- **Fallback:** "Zero-Friction PKM"으로 포지셔닝 조정

### Implementation Considerations

**Technical Debt vs Innovation Speed:**
- **Phase 0-1:** "Ship fast" - 기술 부채 허용
  - WACZ 대신 HTML snapshot (임시)
  - Neo4j 대신 Postgres JSON (임시)
- **Phase 1.5:** "Refactor for scale"
  - WACZ 엔진 교체
  - Neo4j 마이그레이션
- **Phase 2+:** "Innovate with confidence"
  - 충분한 사용자 데이터 확보 후 AI 투자

**Innovation-Market Fit Sequence:**
1. **Month 1-3:** MVP - 영구 박제 + 자동 연결 검증
2. **Month 3-6:** Validation - 자연스러운 망각 검증
3. **Month 6-12:** Intelligence - 감성 검색 + 나이테 리포트
4. **Month 12+:** Vision - 디지털 뇌 복제

**Critical Success Factor:**
각 Phase의 혁신은 **이전 Phase의 검증 성공**을 전제로 합니다. Phase 1에서 일기 습관 형성 실패 시 → Phase 2 감성 검색은 무의미.

---

**혁신 요약:**

Moments: Mind Studio는 **5가지 차원의 혁신**을 통해 PKM 시장을 재정의합니다:

1. **기술 혁신**: WACZ 영구 박제 (링크 깨짐 0%)
2. **인지 과학 혁신**: 자연스러운 망각 (인간 뇌 모방)
3. **AI 혁신**: 감성 검색 (감정으로 기억 탐색)
4. **철학 혁신**: Anti-Productivity (더 깊이 이해하기)
5. **비전 혁신**: Digital Brain Twin (제2의 뇌 복제)

**핵심 인사이트:**
"기존 PKM 도구들은 지식을 저장했지만, Moments는 **나를 저장**합니다."
