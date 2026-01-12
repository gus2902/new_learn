# User Stories - Moments: Mind Studio

본 문서는 보완된 11개의 유저 저니와 PRD를 바탕으로 도출된 상세 유저 스토리입니다. 각 스토리는 에픽(Epic)별로 분류되었으며, 구현 가능한 수준의 수락 기준과 기술적/페르소나 맥락을 포함합니다.

**Version:** 1.1 (2026-01-12 Updated)
**Changes:** EP-PROTOTYPE, EP-ONBOARDING, EP-GROWTH Epic 추가, MVP 스토리 보강, AC 보완

---

## Epic Overview

| Epic ID | Epic Name | Phase | Stories |
|---------|-----------|-------|---------|
| EP-PROTOTYPE | Phase 0 기술 검증 | Phase 0 | US-PROTO-01, US-PROTO-02 |
| EP-CAPTURE | 2초 캡처 및 영구 보존 (WACZ) | MVP | US-CAP-01 ~ US-CAP-04 |
| EP-GRAPH | 시맨틱 그래프 및 자동 연결 | MVP | US-GRAPH-01 ~ US-GRAPH-02 |
| EP-JOURNAL | 성찰 루틴 및 일기 작성 | MVP | US-JOURNAL-01 ~ US-JOURNAL-02 |
| EP-SEARCH | 검색 및 탐색 | MVP/Phase 2 | US-SEARCH-01 ~ US-SEARCH-04 |
| EP-ONBOARDING | 온보딩 및 초기 설정 | MVP | US-ONBOARD-01 ~ US-ONBOARD-02 |
| EP-GROWTH | 성장 및 리텐션 | MVP/Phase 1.5 | US-GROWTH-01 ~ US-GROWTH-03 |
| EP-ANALYTICS | 무의식적 패턴 분석 및 시각화 | Phase 2+ | US-ANAL-01 ~ US-ANAL-02 |

---

## EP-PROTOTYPE: Phase 0 기술 검증 ⚡

> **목표**: 2초 캡처 기술 실현 가능성 증명 (Go/No-Go Decision)

### US-PROTO-01: 2초 캡처 기술 PoC
- **User Story**: "AS A [개발자], I WANT Share Extension → WACZ 아카이빙 파이프라인이 2초 이내에 완료됨을 검증하고 싶다, SO THAT MVP 개발 전에 핵심 기술 리스크를 제거할 수 있다."
- **Acceptance Criteria**:
    - Share Extension에서 URL 전송 후 "저장됨 ✓" 표시까지 평균 2초 이내 완료.
    - 10개 주요 사이트(뉴스, 블로그, SNS, 커뮤니티 등)에서 테스트 시 캡처 성공률 > 95%.
    - 캡처 실패 시 Graceful Degradation: URL + 텍스트 스냅샷으로 fallback 저장.
    - 성능 벤치마크 보고서 작성 및 Go/No-Go 결정.
- **Technical Context**:
    - **Tech**: iOS Share Extension + SingleFile CLI + Cloudflare R2 저장.
    - **Metric**: 캡처 시간 p95 < 3초, 성공률 > 95%.
- **Exit Criteria**: 2초 달성 못하면 아키텍처 재설계 또는 프로젝트 재검토.

### US-PROTO-02: 백그라운드 WACZ 아카이빙 PoC
- **User Story**: "AS A [개발자], I WANT WACZ 완전 아카이빙이 백그라운드에서 비동기로 처리되는지 검증하고 싶다, SO THAT 사용자 체감 시간과 아카이빙 완료 시간을 분리할 수 있다."
- **Acceptance Criteria**:
    - 사용자에게 즉시 "저장됨 ✓" 표시 후, 백그라운드에서 WACZ 생성 진행.
    - WACZ 생성 완료 시 상태가 "영구 보관됨 ✓✓"로 업데이트.
    - WACZ 생성 실패 시 자동 재시도 (최대 3회), 최종 실패 시 HTML 스냅샷 보존.
    - Railway FastAPI 워커에서 Playwright 기반 WACZ 생성 성능 측정.
- **Technical Context**:
    - **Tech**: FastAPI + Playwright + Supabase Queues.
    - **Metric**: WACZ 생성 평균 시간 < 30초, 성공률 > 90%.

---

## EP-CAPTURE: 2초 캡처 및 영구 보존 (WACZ) 📸

> **목표**: 정보 수집 흐름을 끊지 않는 즉각적인 캡처 + 영구 보존

### US-CAP-01: 원터치 웹 클리핑 (2초 캡처)
- **User Story**: "AS A [이지훈/마커스 첸], I WANT 브라우저나 앱에서 단 한 번의 클릭이나 공유 버튼 클릭으로 보고 있는 내용을 즉시 저장하고 싶다, SO THAT 정보 수집 과정에서 흐름이 끊기지 않고 죄책감 없이 나중에 성찰할 수 있다."
- **Acceptance Criteria**:
    - 공유 버튼 클릭 후 'Moments' 선택 시, 별도의 추가 입력(태그, 폴더 등) 없이 즉시 저장이 완료되어야 함.
    - 저장이 완료되면 사용자에게 성공 알림이 최소한의 방해로 표시되어야 함 (2초 이내 처리).
    - 저장된 내용은 원본 URL뿐만 아니라 본문 텍스트와 이미지가 보존되어야 함.
    - **[추가] 캡처 상태가 투명하게 표시되어야 함:**
        - 즉시: "저장됨 ✓" (URL + 메타데이터)
        - 진행 중: 작은 진행 표시기 (WACZ 아카이빙)
        - 완료: "영구 보관됨 ✓✓"
        - 실패 시: "원본 저장됨 (재시도 중)"
- **Technical/Persona Context**:
    - **Tech**: WACZ 표준을 사용하여 정적 아카이브 생성. 오프라인 읽기 지원.
    - **Persona**: 정보 과부하를 겪는 이지훈과 정리에 지친 마커스 첸에게 '정리하지 않는 자유'를 주는 핵심 기능.

### US-CAP-02: 오프라인 우선(Local-only) 저장
- **User Story**: "AS A [Dr. Yuki Tanaka], I WANT 나의 모든 캡처 데이터가 클라우드가 아닌 내 기기에만 암호화되어 저장되기를 원한다, SO THAT 민감한 환자 상담 노트나 개인적인 생각을 안심하고 기록할 수 있다."
- **Acceptance Criteria**:
    - 온보딩 과정에서 'Local-only Mode'를 명시적으로 선택할 수 있어야 함.
    - Local-only 모드 활성화 시, 네트워크 상에 어떤 데이터도 전송되지 않음을 사용자가 확인할 수 있는 상태 표시가 있어야 함.
    - 기기 내 저장된 데이터는 업계 표준 암호화(AES-256 등)가 적용되어야 함.
    - **[추가]** "서버 전송: 0 bytes" 명시적 표시로 신뢰 구축.
- **Technical/Persona Context**:
    - **Tech**: WASM 기반 오프라인 DB 사용. 서버 통신 차단 아키텍처.
    - **Persona**: 프라이버시에 극도로 민감한 유키 다나카의 신뢰를 얻기 위한 필수 요구사항.

### US-CAP-03: 무드 컬러 각인
- **User Story**: "AS A [이지훈], I WANT 캡처할 때 그 순간의 감정을 5가지 색상 중 하나로 표시하고 싶다, SO THAT 나중에 그때의 감정을 함께 떠올릴 수 있다."
- **Acceptance Criteria**:
    - 캡처 시 5가지 무드 컬러(🔵호기심, 🟡영감, 🟢평화, 🔴열정, 🟣성찰) 중 선택 가능.
    - 무드 선택은 선택 사항이며, 미선택 시 기본값(🔵호기심) 자동 적용.
    - 무드 선택 UI는 1탭으로 완료 가능해야 함 (캡처 흐름 방해 금지).
    - 저장된 캡처 카드에 무드 컬러가 시각적으로 표시되어야 함 (테두리 또는 배지).
- **Technical/Persona Context**:
    - **Tech**: 무드 컬러는 캡처 메타데이터로 저장, 검색 필터링에 활용.
    - **Persona**: 감정적 맥락을 중시하는 사용자에게 의미 있는 분류 제공.

### US-CAP-04: Browser Extension 캡처 (데스크톱)
- **User Story**: "AS A [마커스 첸], I WANT 데스크톱 브라우저에서도 한 번의 클릭으로 웹페이지를 캡처하고 싶다, SO THAT 업무 중 발견한 자료도 모바일과 동일하게 저장할 수 있다."
- **Acceptance Criteria**:
    - Chrome Extension 설치 후, 툴바 아이콘 클릭 시 현재 페이지 즉시 캡처.
    - 키보드 단축키(Ctrl/Cmd + Shift + S) 지원.
    - 캡처 완료 시 브라우저 내 Toast 알림 표시.
    - 모바일 Share Extension과 동일한 백엔드 파이프라인 사용.
- **Technical/Persona Context**:
    - **Tech**: Chrome Extension Manifest V3, Supabase Auth 연동.
    - **Persona**: 데스크톱 작업이 많은 마커스 첸의 워크플로우 지원.

### US-CAP-05: 데이터 내보내기 (Export/Backup)
- **User Story**: "AS A [Dr. Yuki Tanaka], I WANT 내 모든 데이터를 언제든 내보내고 백업할 수 있기를 원한다, SO THAT 서비스 종료나 기기 변경 시에도 내 지식을 잃지 않을 수 있다."
- **Acceptance Criteria**:
    - 설정에서 "전체 데이터 내보내기" 기능 제공.
    - 내보내기 형식: JSON (메타데이터) + WACZ 파일 (아카이브) ZIP 묶음.
    - 내보내기 시 AES-256 암호화 옵션 제공.
    - 내보내기 진행 상황 표시 및 완료 알림.
- **Technical/Persona Context**:
    - **Tech**: 백그라운드 작업으로 처리, 대용량 파일 청크 처리.
    - **Persona**: 데이터 소유권을 중시하는 유키 다나카의 요구사항.

---

## EP-GRAPH: 시맨틱 그래프 및 자동 연결 (Neo4j) 🕸️

> **목표**: 수동 정리 없이 AI가 지식의 맥락을 자동으로 형성

### US-GRAPH-01: 자동 맥락 연결 (Magic Link)
- **User Story**: "AS A [마커스 첸], I WANT 내가 저장한 새로운 클립이 기존에 저장된 관련 클립들과 자동으로 연결되기를 원한다, SO THAT 내가 수동으로 링크를 만들지 않아도 지식의 맥락이 형성되는 것을 보고 싶다."
- **Acceptance Criteria**:
    - 새 클립 저장 시, 백그라운드에서 NLP 분석을 통해 기존 데이터와의 시맨틱 유사도를 계산해야 함.
    - 유사도가 임계치 이상인 클립들 사이에 '자동 연결(Automatic Link)'이 생성되어야 함.
    - 클립 상세 페이지 하단에 '자동으로 연결된 클립' 리스트가 노출되어야 함.
    - **[추가] 각 자동 연결에 "도움됨 👍 / 도움 안됨 👎" 피드백 버튼이 있어야 함.**
    - **[추가] 연결 근거(공통 키워드)가 노출되어야 하며, 사용자가 연결을 수정/삭제할 수 있어야 함.**
- **Technical/Persona Context**:
    - **Tech**: Embedding 모델(Sentence-BERT 등)을 통한 벡터 유사도 분석 + Neo4j 그래프 DB 연결.
    - **Persona**: 회의론자 마커스 첸이 '정말 아무것도 안 해도 된다'는 사실에 전율을 느끼게 하는 핵심 '마법의 순간'.

### US-GRAPH-02: 관심사 교집합 발견 (Intersection Discovery)
- **User Story**: "AS A [Aiden Rodriguez], I WANT 나의 캡처 데이터들 사이에서 내가 인지하지 못했던 새로운 관심사 교집합이 시각화되기를 원한다, SO THAT 나의 잠재적 재능이나 진로 방향을 발견하고 싶다."
- **Acceptance Criteria**:
    - 두 개 이상의 서로 다른 도메인(예: Tech, Music) 데이터가 공통된 키워드나 맥락(예: Creative Coding)으로 연결될 때 이를 상위 노드로 추출해야 함.
    - '당신의 패턴' 탭에서 이러한 교집합 지점을 시각적으로 강조하여 표시해야 함.
    - **[추가] Graph View에서 교집합 노드는 다른 노드보다 크게 표시되고 Glow 효과 적용.**
- **Technical/Persona Context**:
    - **Tech**: Neo4j의 Community Detection 알고리즘 또는 GraphRAG를 통한 추상적 주제 추출.
    - **Persona**: 진로 고민이 있는 에이든과 서연이에게 '자기 발견'의 가치를 제공.

---

## EP-JOURNAL: 성찰 루틴 및 일기 작성 📓

> **목표**: 매일 밤 '나'를 되찾는 성찰 시간 제공

### US-JOURNAL-01: 클립 연동 지능형 일기 가이드
- **User Story**: "AS A [이지훈], I WANT 하루를 마무리하며 일기를 쓸 때 오늘 내가 저장한 클립들이 가이드로 제시되기를 원한다, SO THAT 오늘 하루 나의 관심사와 감정을 더 쉽게 회복하고 기록할 수 있다."
- **Acceptance Criteria**:
    - 일기 작성 화면 진입 시, 해당 날짜에 저장된 클립들을 타임라인 형태로 노출해야 함.
    - 클립을 클릭하여 일기 본문에 인용하거나, 해당 클립에 대한 생각을 즉시 적을 수 있는 'Ghost Memo' 인터페이스를 제공해야 함.
    - **[추가] AI가 오늘 저장한 클립 기반으로 일기 초안을 자동 생성 (선택 사항).**
    - **[추가] AI가 "The Self-Query" 질문 제안 (예: "오늘 왜 이 글이 마음에 와닿았나요?").**
    - **[추가] 일기 작성 완료 후 "성찰에 도움됨 👍" 피드백 버튼 표시.**
- **Technical/Persona Context**:
    - **Tech**: 로컬 타임라인 인덱싱. 일기 텍스트와 클립 간의 n:m 관계 매핑.
    - **Persona**: 바쁜 일상에서 성찰의 기회를 놓치기 쉬운 이지훈에게 성찰의 문턱을 낮춰줌.

### US-JOURNAL-02: 타임 캡슐 알림 (Re-engagement)
- **User Story**: "AS A [Elena Rodriguez], I WANT 과거의 특정 시점에 내가 썼던 일기나 중요하게 생각했던 클립이 오늘 다시 나타나기를 원한다, SO THAT 나의 성장 궤적을 확인하고 잊고 있던 초심을 회복하고 싶다."
- **Acceptance Criteria**:
    - 앱 복귀 시 또는 특정 주기마다 '6개월 전 오늘', '1년 전 오늘' 등의 주요 기록을 카드 형태로 노출해야 함.
    - 과거의 나와 현재의 나를 이어주는 감성적인 메시지(예: "당신은 이때 이런 꿈을 꾸고 있었네요")가 포함되어야 함.
- **Technical/Persona Context**:
    - **Tech**: 과거 특정 날짜의 High-weight 노드(일기 등) 우선 추출 트리거.
    - **Persona**: 이직 후 앱 사용이 뜸해졌던 엘레나를 다시 서비스로 불러들이는 핵심 리텐션 장치.
- **Phase**: Phase 1.5

---

## EP-SEARCH: 검색 및 탐색 🔍

> **목표**: 키워드, 시간, 감정 등 다양한 방식으로 과거 지식 탐색

### US-SEARCH-02: 키워드 검색 (MVP)
- **User Story**: "AS A [이지훈], I WANT 기억나는 단어나 문구로 과거 캡처를 검색하고 싶다, SO THAT 필요한 정보를 빠르게 찾을 수 있다."
- **Acceptance Criteria**:
    - 검색창에 키워드 입력 시 제목, 본문, Ghost Memo에서 일치하는 캡처 검색.
    - 검색 결과는 관련도순으로 정렬되며, 최신순/오래된순 정렬 옵션 제공.
    - 검색어가 하이라이트되어 표시.
    - 검색 결과가 없을 때 친절한 Empty State 메시지 표시.
- **Technical/Persona Context**:
    - **Tech**: Postgres Full-text Search 또는 pgvector 시맨틱 검색.
    - **Persona**: 빠른 정보 접근을 원하는 모든 사용자의 기본 기능.
- **Phase**: MVP

### US-SEARCH-03: 타임라인 뷰 (MVP)
- **User Story**: "AS A [이지훈], I WANT 특정 날짜나 기간의 캡처를 타임라인으로 보고 싶다, SO THAT 시간 순서대로 과거를 되돌아볼 수 있다."
- **Acceptance Criteria**:
    - 캘린더 UI에서 날짜 선택 시 해당 날짜의 캡처 목록 표시.
    - 날짜 범위 선택 기능 제공 (이번 주, 이번 달, 사용자 지정).
    - 타임라인은 시간순(오전→오후) 또는 역순 정렬 가능.
    - 캡처가 없는 날짜는 시각적으로 구분.
- **Technical/Persona Context**:
    - **Tech**: 날짜 인덱싱, 캘린더 컴포넌트.
    - **Persona**: 시간 기반 회상을 선호하는 사용자.
- **Phase**: MVP

### US-SEARCH-04: 무드별 필터 (MVP)
- **User Story**: "AS A [Priya Sharma], I WANT 특정 감정으로 저장한 캡처만 필터링하고 싶다, SO THAT 그때의 감정과 비슷한 영감을 다시 찾을 수 있다."
- **Acceptance Criteria**:
    - 검색 결과 또는 라이브러리에서 5가지 무드 컬러로 필터링 가능.
    - 다중 무드 선택 지원 (예: 호기심 + 영감).
    - 필터 적용 시 즉시 결과 업데이트 (debounce 300ms).
    - 현재 적용된 필터가 UI에 명확히 표시.
- **Technical/Persona Context**:
    - **Tech**: 무드 컬러 메타데이터 필터링.
    - **Persona**: 감정 기반 탐색을 원하는 크리에이티브 전문가.
- **Phase**: MVP

### US-SEARCH-01: 감정 유사도 검색 (Emotional Search)
- **User Story**: "AS A [Priya Sharma], I WANT 구체적인 키워드가 생각나지 않을 때 '따뜻하고 우아한 느낌'과 같은 감정 표현으로 결과가 검색되기를 원한다, SO THAT 디자인 영감과 같이 언어로 정의하기 어려운 정보를 쉽게 찾고 싶다."
- **Acceptance Criteria**:
    - 검색창에 텍스트나 음성으로 감정 쿼리 입력 가능.
    - VAD(Valence-Arousal-Dominance) 모델을 기반으로 쿼리의 감정 벡터와 데이터의 감정 벡터 간 유사도 계산.
    - 검색 결과 옆에 '감정 유사도'가 %로 표시되어야 함.
- **Technical/Persona Context**:
    - **Tech**: Multi-modal Embedding (CLIP 등) 또는 텍스트 Sentiment 분석 기반 벡터 검색.
    - **Persona**: 키워드 검색의 한계를 느끼는 크리에이티브 전문가 프리야에게 '말이 통하는 도구'라는 인식을 심어줌.
- **Phase**: Phase 2

---

## EP-ONBOARDING: 온보딩 및 초기 설정 🚀

> **목표**: Zero-friction 온보딩으로 첫 사용 장벽 제거

### US-ONBOARD-01: Zero-friction 온보딩
- **User Story**: "AS A [Sarah Mitchell], I WANT 앱을 처음 열었을 때 복잡한 설정 없이 바로 시작할 수 있기를 원한다, SO THAT 호기심이 식기 전에 가치를 경험할 수 있다."
- **Acceptance Criteria**:
    - 앱 설치 후 3단계 이내로 첫 캡처까지 도달 가능.
    - 필수 입력: 없음 (이메일/소셜 로그인만으로 시작).
    - 선택 입력: 이름, 알림 설정, Local-only 모드 선택.
    - 온보딩 건너뛰기 옵션 제공.
    - 빈 캔버스 상태에서도 가치가 느껴지는 Empty State 디자인 (Singularity 점 컨셉).
- **Technical/Persona Context**:
    - **Tech**: Supabase Auth (OAuth2: Google, Apple), Progressive Disclosure.
    - **Persona**: 새로운 앱에 회의적인 Sarah에게 즉각적인 가치 제공.
- **Phase**: MVP

### US-ONBOARD-02: 부모용 온보딩 플로우
- **User Story**: "AS A [박미영], I WANT 자녀에게 추천하기 전에 먼저 이 앱이 무엇인지 충분히 이해하고 싶다, SO THAT 신뢰할 수 있는 앱인지 확인 후 자녀에게 추천할 수 있다."
- **Acceptance Criteria**:
    - "자녀를 위한 앱 찾기" 전용 온보딩 경로 제공.
    - 앱의 핵심 가치를 부모 관점에서 설명 (프라이버시, 진로 발견 등).
    - 부모가 먼저 1주일 사용 후 자녀 초대 권장 메시지.
    - 자녀 초대 시 Referral 링크 자동 생성.
- **Technical/Persona Context**:
    - **Tech**: 온보딩 분기 처리, Referral 시스템 연동.
    - **Persona**: 자녀 교육에 관심 있는 부모 박미영의 신뢰 구축.
- **Phase**: MVP

---

## EP-GROWTH: 성장 및 리텐션 📈

> **목표**: 입소문 메커니즘 + 장기 사용 유도

### US-GROWTH-01: Referral 링크 생성
- **User Story**: "AS A [이지훈], I WANT 친구에게 이 앱을 추천할 때 전용 링크를 공유하고 싶다, SO THAT 내 추천으로 가입한 친구와 함께 성장할 수 있다."
- **Acceptance Criteria**:
    - 설정 > "친구 초대" 메뉴에서 개인 Referral 링크 생성 가능.
    - 링크에 UTM 파라미터 자동 추가 (추적용).
    - 링크 공유 시 앱 미리보기 카드(OG Image) 표시.
    - 내 추천으로 가입한 친구 수 표시 (인센티브 기반 확장 가능).
- **Technical/Persona Context**:
    - **Tech**: Referral 코드 생성, UTM 추적, OG Image 동적 생성.
    - **Persona**: 열정적인 사용자가 자발적으로 앱을 홍보.
- **Phase**: MVP

### US-GROWTH-02: 가입 설문 (Attribution)
- **User Story**: "AS A [Product Manager], I WANT 신규 사용자가 어떻게 앱을 알게 되었는지 파악하고 싶다, SO THAT 효과적인 채널에 집중할 수 있다."
- **Acceptance Criteria**:
    - 가입 완료 직후 "어떻게 Moments를 알게 되셨나요?" 설문 표시.
    - 선택지: 친구 추천, SNS, 앱스토어 검색, 블로그/리뷰, 기타(직접 입력).
    - 설문은 선택 사항이며 건너뛰기 가능.
    - 응답 데이터는 Amplitude로 전송하여 분석.
- **Technical/Persona Context**:
    - **Tech**: 온보딩 플로우 연동, Amplitude 이벤트 로깅.
    - **Persona**: 제품 성장 분석을 위한 데이터 수집.
- **Phase**: MVP

### US-GROWTH-03: 휴면 사용자 재참여 (Reactivation)
- **User Story**: "AS A [Elena Rodriguez], I WANT 한동안 앱을 사용하지 않았을 때 과거의 소중한 기록이 기다리고 있다는 알림을 받고 싶다, SO THAT 다시 앱으로 돌아올 동기를 얻을 수 있다."
- **Acceptance Criteria**:
    - 30일 이상 미접속 시 푸시 알림 또는 이메일 발송.
    - 메시지: "당신의 203개 추억이 기다리고 있어요" 스타일의 감성적 문구.
    - Time Capsule 컨텐츠 미리보기 포함 (예: "6개월 전 오늘...").
    - 알림 수신 후 7일 내 복귀율 추적.
- **Technical/Persona Context**:
    - **Tech**: Supabase Cron + Edge Function, 푸시 알림/이메일 서비스.
    - **Persona**: 이직 후 앱 사용이 뜸해진 엘레나의 재참여 유도.
- **Phase**: Phase 1.5

---

## EP-ANALYTICS: 무의식적 패턴 분석 및 시각화 📊

> **목표**: 장기 사용자에게 성장 궤적 시각화 및 자기 발견 제공

### US-ANAL-01: 나이테 분석 리포트 (Growth Timeline)
- **User Story**: "AS A [이지훈 2년 후], I WANT 장기적으로 쌓인 나의 지식 데이터가 어떻게 변화하고 성장해왔는지 시각화된 보고서를 보고 싶다, SO THAT 나의 전문성이 어떻게 확장되었는지 '나이테'처럼 확인하고 싶다."
- **Acceptance Criteria**:
    - 분기별/연도별 핵심 주제 키워드의 변화를 동심원 또는 타임라인 차트로 시각화해야 함.
    - 과거 대비 현재의 주요 관심사 이동 경로를 추적하여 '신규 발견 주제'와 '심화 주제'를 구분해 보여줘야 함.
- **Technical/Persona Context**:
    - **Tech**: 다목적 시계열 그래프 분석. LLM을 통한 주제 추상화(Summarization).
    - **Persona**: 2년 이상 사용한 파워 유저 이지훈에게 장기 사용의 임계치 너머 보상을 제공.
- **Phase**: Phase 2+

### US-ANAL-02: 부모용 진로 가이드 (Family Mode)
- **User Story**: "AS A [박미영], I WANT 내 딸 서연이의 구체적인 기록 내용은 보지 않더라도, 딸이 어떤 분야에 관심을 가지고 있는지 통계적인 리포트만 공유받고 싶다, SO THAT 딸의 프라이버시를 존중하면서도 현명하게 진로를 응원할 수 있다."
- **Acceptance Criteria**:
    - 자녀의 '패턴 비율'(예: 동물 30%, 과학 20%) 차트만 부모에게 전송할 수 있는 공유 프로토콜 구현.
    - 상세 메모 및 일기 내용은 절대 노출되지 않음을 보장하는 보안 장치.
    - **[추가] 자녀가 공유를 명시적으로 승인해야만 부모에게 전송됨.**
- **Technical/Persona Context**:
    - **Tech**: Zero-knowledge Proof 스타일의 데이터 요약 공유 또는 사용자 승인 기반 메타데이터 추출.
    - **Persona**: 자녀와 소통하고 싶은 부모 박미영과 프라이버시가 중요한 서연이 사이의 신뢰 가교 역할.
- **Phase**: Phase 2+

---

## Story Priority Matrix

| Priority | Phase | Stories | Count |
|----------|-------|---------|-------|
| 🔴 Critical | Phase 0 | US-PROTO-01, US-PROTO-02 | 2 |
| 🟠 High | MVP | US-CAP-01~05, US-GRAPH-01~02, US-JOURNAL-01, US-SEARCH-02~04, US-ONBOARD-01~02, US-GROWTH-01~02 | 15 |
| 🟡 Medium | Phase 1.5 | US-JOURNAL-02, US-GROWTH-03 | 2 |
| 🟢 Low | Phase 2+ | US-SEARCH-01, US-ANAL-01~02 | 3 |
| **Total** | | | **22** |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-10 | Initial creation (9 stories) |
| 1.1 | 2026-01-12 | Added EP-PROTOTYPE, EP-ONBOARDING, EP-GROWTH; MVP Search stories; AC enhancements (22 stories) |
