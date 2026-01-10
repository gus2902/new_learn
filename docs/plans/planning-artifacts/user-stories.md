# User Stories - Moments: Mind Studio

본 문서는 보완된 11개의 유저 저니와 PRD를 바탕으로 도출된 상세 유저 스토리입니다. 각 스토리는 에픽(Epic)별로 분류되었으며, 구현 가능한 수준의 수락 기준과 기술적/페르소나 맥락을 포함합니다.

---

## EP-CAPTURE: 2초 캡처 및 영구 보존 (WACZ)

### US-CAP-01: 원터치 웹 클리핑 (2초 캡처)
- **User Story**: "AS A [이지훈/마커스 첸], I WANT 브라우저나 앱에서 단 한 번의 클릭이나 공유 버튼 클릭으로 보고 있는 내용을 즉시 저장하고 싶다, SO THAT 정보 수집 과정에서 흐름이 끊기지 않고 죄책감 없이 나중에 성찰할 수 있다."
- **Acceptance Criteria**:
    - 공유 버튼 클릭 후 'Moments' 선택 시, 별도의 추가 입력(태그, 폴더 등) 없이 즉시 저장이 완료되어야 함.
    - 저장이 완료되면 사용자에게 성공 알림이 최소한의 방해로 표시되어야 함 (2초 이내 처리).
    - 저장된 내용은 원본 URL뿐만 아니라 본문 텍스트와 이미지가 보존되어야 함.
- **Technical/Persona Context**:
    - **Tech**: WACZ 표준을 사용하여 정적 아카이브 생성. 오프라인 읽기 지원.
    - **Persona**: 정보 과부하를 겪는 이지훈과 정리에 지친 마커스 첸에게 '정리하지 않는 자유'를 주는 핵심 기능.

### US-CAP-02: 오프라인 우선(Local-only) 저장
- **User Story**: "AS A [Dr. Yuki Tanaka], I WANT 나의 모든 캡처 데이터가 클라우드가 아닌 내 기기에만 암호화되어 저장되기를 원한다, SO THAT 민감한 환자 상담 노트나 개인적인 생각을 안심하고 기록할 수 있다."
- **Acceptance Criteria**:
    - 온보딩 과정에서 'Local-only Mode'를 명시적으로 선택할 수 있어야 함.
    - Local-only 모드 활성화 시, 네트워크 상에 어떤 데이터도 전송되지 않음을 사용자가 확인할 수 있는 상태 표시가 있어야 함.
    - 기기 내 저장된 데이터는 업계 표준 암호화(AES-256 등)가 적용되어야 함.
- **Technical/Persona Context**:
    - **Tech**: WASM 기반 오프라인 DB 사용. 서버 통신 차단 아키텍처.
    - **Persona**: 프라이버시에 극도로 민감한 유키 다나카의 신뢰를 얻기 위한 필수 요구사항.

---

## EP-GRAPH: 시맨틱 그래프 및 자동 연결 (Neo4j)

### US-GRAPH-01: 자동 맥락 연결 (Magic Link)
- **User Story**: "AS A [마커스 첸], I WANT 내가 저장한 새로운 클립이 기존에 저장된 관련 클립들과 자동으로 연결되기를 원한다, SO THAT 내가 수동으로 링크를 만들지 않아도 지식의 맥락이 형성되는 것을 보고 싶다."
- **Acceptance Criteria**:
    - 새 클립 저장 시, 백그라운드에서 NLP 분석을 통해 기존 데이터와의 시맨틱 유사도를 계산해야 함.
    - 유사도가 임계치 이상인 클립들 사이에 '자동 연결(Automatic Link)'이 생성되어야 함.
    - 클립 상세 페이지 하단에 '자동으로 연결된 클립' 리스트가 노출되어야 함.
- **Technical/Persona Context**:
    - **Tech**: Embedding 모델(Sentence-BERT 등)을 통한 벡터 유사도 분석 + Neo4j 그래프 DB 연결.
    - **Persona**: 회의론자 마커스 첸이 '정말 아무것도 안 해도 된다'는 사실에 전율을 느끼게 하는 핵심 '마법의 순간'.

### US-GRAPH-02: 관심사 교집합 발견 (Intersection Discovery)
- **User Story**: "AS A [Aiden Rodriguez], I WANT 나의 캡처 데이터들 사이에서 내가 인지하지 못했던 새로운 관심사 교집합이 시각화되기를 원한다, SO THAT 나의 잠재적 재능이나 진로 방향을 발견하고 싶다."
- **Acceptance Criteria**:
    - 두 개 이상의 서로 다른 도메인(예: Tech, Music) 데이터가 공통된 키워드나 맥락(예: Creative Coding)으로 연결될 때 이를 상위 노드로 추출해야 함.
    - '당신의 패턴' 탭에서 이러한 교집합 지점을 시각적으로 강조하여 표시해야 함.
- **Technical/Persona Context**:
    - **Tech**: Neo4j의 Community Detection 알고리즘 또는 GraphRAG를 통한 추상적 주제 추출.
    - **Persona**: 진로 고민이 있는 에이든과 서연이에게 '자기 발견'의 가치를 제공.

---

## EP-JOURNAL: 성찰 루틴 및 일기 작성

### US-JOURNAL-01: 클립 연동 지능형 일기 가이드
- **User Story**: "AS A [이지훈], I WANT 하루를 마무리하며 일기를 쓸 때 오늘 내가 저장한 클립들이 가이드로 제시되기를 원한다, SO THAT 오늘 하루 나의 관심사와 감정을 더 쉽게 회복하고 기록할 수 있다."
- **Acceptance Criteria**:
    - 일기 작성 화면 진입 시, 해당 날짜에 저장된 클립들을 타임라인 형태로 노출해야 함.
    - 클립을 클릭하여 일기 본문에 인용하거나, 해당 클립에 대한 생각을 즉시 적을 수 있는 'Ghost Memo' 인터페이스를 제공해야 함.
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

---

## EP-SEARCH: 감성 및 맥락 기반 검색

### US-SEARCH-01: 감정 유사도 검색 (Emotional Search)
- **User Story**: "AS A [Priya Sharma], I WANT 구체적인 키워드가 생각나지 않을 때 '따뜻하고 우아한 느낌'과 같은 감정 표현으로 결과가 검색되기를 원한다, SO THAT 디자인 영감과 같이 언어로 정의하기 어려운 정보를 쉽게 찾고 싶다."
- **Acceptance Criteria**:
    - 검색창에 텍스트나 음성으로 감정 쿼리 입력 가능.
    - VAD(Valence-Arousal-Dominance) 모델을 기반으로 쿼리의 감정 벡터와 데이터의 감정 벡터 간 유사도 계산.
    - 검색 결과 옆에 '감정 유사도'가 %로 표시되어야 함.
- **Technical/Persona Context**:
    - **Tech**: Multi-modal Embedding (CLIP 등) 또는 텍스트 Sentiment 분석 기반 벡터 검색.
    - **Persona**: 키워드 검색의 한계를 느끼는 크리에이티브 전문가 프리야에게 '말이 통하는 도구'라는 인식을 심어줌.

---

## EP-ANALYTICS: 무의식적 패턴 분석 및 시각화

### US-ANAL-01: 나이테 분석 리포트 (Growth Timeline)
- **User Story**: "AS A [이지훈 2년 후], I WANT 장기적으로 쌓인 나의 지식 데이터가 어떻게 변화하고 성장해왔는지 시각화된 보고서를 보고 싶다, SO THAT 나의 전문성이 어떻게 확장되었는지 '나이테'처럼 확인하고 싶다."
- **Acceptance Criteria**:
    - 분기별/연도별 핵심 주제 키워드의 변화를 동심원 또는 타임라인 차트로 시각화해야 함.
    - 과거 대비 현재의 주요 관심사 이동 경로를 추적하여 '신규 발견 주제'와 '심화 주제'를 구분해 보여줘야 함.
- **Technical/Persona Context**:
    - **Tech**: 다목적 시계열 그래프 분석. LLM을 통한 주제 추상화(Summarization).
    - **Persona**: 2년 이상 사용한 파워 유저 이지훈에게 장기 사용의 임계치 너머 보상을 제공.

### US-ANAL-02: 부모용 진로 가이드 (Family Mode)
- **User Story**: "AS A [박미영], I WANT 내 딸 서연이의 구체적인 기록 내용은 보지 않더라도, 딸이 어떤 분야에 관심을 가지고 있는지 통계적인 리포트만 공유받고 싶다, SO THAT 딸의 프라이버시를 존중하면서도 현명하게 진로를 응원할 수 있다."
- **Acceptance Criteria**:
    - 자녀의 '패턴 비율'(예: 동물 30%, 과학 20%) 차트만 부모에게 전송할 수 있는 공유 프로토콜 구현.
    - 상세 메모 및 일기 내용은 절대 노출되지 않음을 보장하는 보안 장치.
- **Technical/Persona Context**:
    - **Tech**: Zero-knowledge Proof 스타일의 데이터 요약 공유 또는 사용자 승인 기반 메타데이터 추출.
    - **Persona**: 자녀와 소통하고 싶은 부모 박미영과 프라이버시가 중요한 서연이 사이의 신뢰 가교 역할.
