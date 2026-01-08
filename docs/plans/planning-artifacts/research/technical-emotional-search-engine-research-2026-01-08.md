---
stepsCompleted: [1, 2, 3, 4, 5]
inputDocuments: ["docs/plans/moments-mind-studio-product-brief.md"]
workflowType: 'research'
lastStep: 5
research_type: 'technical'
research_topic: 'emotional-search-engine'
research_goals: 'Researching ways to transform information into emotional content through diary analysis, emotional modeling, and hybrid vector-metadata indexing, with future multimodal extensibility.'
user_name: '마스터'
date: '2026-01-08'
web_research_enabled: true
source_verification: true
---

# Research Report: Technical Research (Emotional Search Engine)

**Date:** 2026-01-08
**Author:** 마스터
**Research Type:** technical

---

## Research Overview

이 연구는 Moments: Mind Studio의 핵심 비전인 '정보의 감성적 전환'을 실현하기 위한 기술적 토대를 마련합니다. 사용자의 일기와 스크랩된 콘텐츠에서 감성 데이터를 추출하고, 이를 지식 그래프 및 벡터 검색과 결합하여 사용자에게 정서적 애착을 줄 수 있는 지식 관리 시스템을 구축하는 방안을 탐구합니다.

---

## Technical Research Scope Confirmation

**Research Topic:** emotional-search-engine
**Research Goals:** Researching ways to transform information into emotional content through diary analysis, emotional modeling, and hybrid vector-metadata indexing, with future multimodal extensibility.

**Technical Research Scope:**

- **Sentiment & Emotion Analysis Models** - LLM based extraction, multi-dimensional emotion models (Plutchik, VAD).
- **Metadata Schema Design** - Structuring emotional metadata for knowledge fragments.
- **Hybrid Retrieval Architecture** - Combining vector similarity with emotional filtering and ranking.
- **Multimodal Extensibility** - Future-proofing for image and voice emotion analysis.
- **Emotional UX Integration** - Technical methods to reflect emotions back to users (Visual/Textual).

**Research Methodology:**

- Current web data with rigorous source verification
- Multi-source validation for critical technical claims
- Confidence level framework for uncertain information
- Comprehensive technical coverage with architecture-specific insights

**Scope Confirmed:** 2026-01-08

---

## Technology Stack Analysis

### Programming Languages

감성 분석 및 검색 엔진 구축을 위해 2024-2025년 기준 다음 언어들이 핵심적인 역할을 합니다.

- **Python**: NLP 및 머신러닝 생태계의 절대적인 표준입니다. **Hugging Face**, **PyTorch**, **LangChain** 등 최신 감성 분석 도구들이 Python을 기본으로 지원하며, 특히 일기 텍스트 데이터의 전처리와 LLM 통합에 가장 효율적입니다.
- **JavaScript (Node.js)**: **NLP.JS**와 같은 프레임워크를 통해 실시간 웹 애플리케이션에서 경량 감성 분석을 수행할 때 사용됩니다. 클라이언트 사이드에서의 즉각적인 반응성을 위해 점점 채택이 늘고 있습니다.

_Popular Languages: Python (Back-end, AI/ML), JavaScript (Front-end, Real-time Analysis)_
_Emerging Languages: Mojo (AI 성능 최적화), Rust (고성능 데이터 전처리 파이프라인)_
_Language Evolution: 단순 스크립트 기반 언어에서 분산 처리 및 LLM 오케스트레이션 기능을 내장한 언어 환경으로 진화 중_
_Performance Characteristics: Python은 라이브러리 풍부성에서 압도적이나, 고성능 처리가 필요한 경우 Rust와의 결합이 증가함_
_Source: https://www.wedowebapps.com/python-sentiment-analysis-libraries/, https://mentorsol.com/source-sentiment-analysis-tools/_

### Development Frameworks and Libraries

감성 분석의 깊이를 더해주는 2025년 기준 핵심 프레임워크들입니다.

- **Hugging Face Transformers**: **RoBERTa**, **BERT** 기반의 최신 감정 분류 모델(`j-hartmann/emotion-english-distilroberta-base` 등)을 활용하여 7가지 기본 감정을 정밀하게 추출하는 데 필수적입니다.
- **LlamaIndex (PropertyGraphIndex)**: 비정형 텍스트에서 지식 트리플을 추출할 뿐만 아니라, 엔티티에 감성 메타데이터를 속성(Property)으로 부착하여 그래프 구조로 저장하는 기능을 제공합니다.
- **VADER & TextBlob**: 소셜 미디어나 일기와 같은 비정형 텍스트의 긍/부정 극성(Polarity)과 주관성(Subjectivity)을 빠르게 파악하기 위한 경량 라이브러리로 여전히 널리 사용됩니다.

_Major Frameworks: Hugging Face, LlamaIndex, LangChain_
_Micro-frameworks: VADER, TextBlob, spaCy_
_Evolution Trends: 단순 긍/부정 분석에서 다차원(VAD 모델, Plutchik) 감정 추론 및 맥락 파악으로 진화_
_Ecosystem Maturity: LLM 기반의 감성 추출 및 인덱싱 도구들이 매우 성숙한 단계에 진입함_
_Source: https://medium.com/@junjunzaragosa2309/sentiment-analyzer-natural-language-processing-web-application-fa0ea89f5825, https://developers.llamaindex.ai/python/examples/property_graph/property_graph_basic/_

### Database and Storage Technologies

감성 데이터와 벡터 임베딩을 결합하여 저장하기 위한 데이터 기술입니다.

- **Vector Databases (Weaviate, Qdrant, Pinecone)**: 임베딩 벡터와 함께 감성 메타데이터(예: joy: 0.8, sadness: 0.1)를 저장하고, 이를 필터링 조건으로 사용하여 "행복한 기억과 관련된 정보"만 검색하는 하이브리드 검색을 지원합니다.
- **Neo4j (Graph DB)**: 지식 사이의 연결뿐만 아니라, "감정" 자체를 노드로 설정하여 특정 감정이 어떤 정보들과 주로 연결되는지 시각화하고 분석하는 데 유용합니다.

_Relational Databases: PostgreSQL (pgvector를 통한 벡터 및 메타데이터 통합 저장)_
_NoSQL Databases: MongoDB (Atlas Vector Search를 활용한 유연한 스키마 지원)_
_In-Memory Databases: Redis (실시간 감성 피드백 처리를 위한 캐시 및 벡터 인덱스)_
_Data Warehousing: Snowflake/BigQuery (대규모 감성 트렌드 분석용)_
_Source: https://therightsw.com/vector-database/, https://lakefs.io/blog/best-vector-databases/_

### Development Tools and Platforms

- **Streamlit**: AI 모델의 감성 분석 결과를 빠르게 대시보드로 시각화하여 MVP를 구축하는 데 최적화된 플랫폼입니다.
- **SenticNet API**: 상징적 AI와 딥러닝을 결합하여 텍스트의 정서적 개념과 극성을 추출하는 고급 API 서비스를 제공합니다.

_Source: https://sentic.net/api/, https://medium.com/@junjunzaragosa2309/sentiment-analyzer-natural-language-processing-web-application-fa0ea89f5825_

### Cloud Infrastructure and Deployment

- **AWS Comprehend / Google Cloud NLP**: 관리형 서비스로 제공되는 감성 분석 API로, 인프라 관리 없이 대규모 텍스트 처리가 가능합니다.
- **Docker & Kubernetes**: 감성 분석 모델과 벡터 DB를 컨테이너화하여 일관된 환경에서 배포하고 확장하는 데 사용됩니다.
- **Ollama**: 개인화된 일기 분석 시 데이터 프라이버시를 위해 로컬 환경에서 감성 추출용 LLM을 실행하는 데 필수적인 도구입니다.

_Source: https://www.wedowebapps.com/python-sentiment-analysis-libraries/, https://github.com/shahedsabab/hybrid-graphrag_

### Technology Adoption Trends

- **Multimodal Sentiment (MLLM)**: 텍스트뿐만 아니라 이미지, 음성의 감정을 통합 분석하는 MLLM(Multimodal LLM)의 채택이 가속화되고 있습니다 (예: EMOVA).
- **Hybrid Reasoning**: 벡터 검색의 유사성과 그래프의 구조적 연결, 그리고 감성 메타데이터의 필터링을 결합한 '하이브리드 추론'이 표준으로 자리 잡고 있습니다.
- **Local Privacy**: 민감한 감성 데이터를 보호하기 위해 로컬 LLM을 통한 온디바이스(On-device) 분석이 중요한 트렌드로 부상하고 있습니다.

_Source: https://arxiv.org/abs/2409.18042, https://medium.com/@delta-c/affective-computing-and-emotion-ai-90ab076b5dcf_

---

## Integration Patterns Analysis

### API Design Patterns

감성 검색 엔진과 AI 에이전트 간의 상호 운용성을 확보하기 위한 최신 API 설계 패턴입니다.

- **Microsoft AI Chat Protocol**: 생성형 AI 출력(감성 데이터 포함)을 실시간으로 스트리밍하기 위한 표준 API 계약입니다. 다양한 모델과 오케스트레이션 도구 간의 일관된 데이터 소비를 보장합니다.
- **Model Context Protocol (MCP)**: 2025년 기준 LLM 애플리케이션과 외부 데이터 소스(감성 저장소 등)를 연결하기 위한 표준 프로토콜로, **JSON-RPC 2.0**을 기반으로 리소스, 도구, 프롬프트를 통합합니다.
- **RESTful & Streaming API**: `/predict`, `/batch_predict`와 같은 엔드포인트를 통해 실시간 감성 예측을 수행하며, Redis와 같은 인메모리 캐시를 결합하여 성능을 최적화하는 패턴이 널리 사용됩니다.

_RESTful APIs: High-performance endpoints with Redis caching (zakn.dev 2025)_
_GraphQL APIs: Flexible data retrieval for complex emotional graphs_
_RPC and gRPC: Low-latency binary communication for real-time multimodal analysis_
_Webhook Patterns: Notification of emotional state changes in real-time streams_
_Source: https://github.com/microsoft/ai-chat-protocol, https://modelcontextprotocol.io/specification/latest, https://zakn.dev/posts/sentiment_

### Communication Protocols

- **JSON-RPC 2.0**: MCP에서 채택한 경량 원격 프로시저 호출 프로토콜로, 감성 분석 서버와 클라이언트 간의 상태 저장 통신에 최적화되어 있습니다.
- **WebSocket Protocols**: "차가운 정보"에서 추출된 "따뜻한 감성" 피드백을 사용자에게 즉각적으로 전달하기 위해 지속적인 연결을 유지하는 패턴입니다.
- **Message Queue Protocols (AMQP, MQTT)**: IoT 장치(음성 인식기 등)나 백엔드 마이크로서비스 간의 비동기 감성 데이터 전달에 사용됩니다.

_Source: https://modelcontextprotocol.io/specification/latest, https://zakn.dev/posts/sentiment_

### Data Formats and Standards

감성 데이터를 구조화하고 교환하기 위한 핵심 형식입니다.

- **JSON-LD (Linked Data)**: MixedEmotions 프로젝트와 Open Annotation (OA) 온톨로지에서 권장하는 형식으로, 감성 메타데이터와 지식 엔티티 간의 의미적 연결을 표현하는 데 최적입니다.
- **Emotion Markup Language (EmotionML)**: W3C에서 정의한 감정 주석 및 표현을 위한 표준 언어로, 웹 서비스 간의 정서적 일관성을 유지하는 데 도움을 줍니다.
- **Activity Streams 2.0**: 사용자의 감성적 활동(일기 작성, 감성적 스크랩 등)을 추적하고 연동하기 위한 메타데이터 관리 형식입니다.

_Source: https://github.com/MixedEmotions/JSON-LD_schema, https://en.wikipedia.org/wiki/Emotion_Markup_Language_

## Architectural Patterns and Design

### System Architecture Patterns

감성 검색 엔진은 실시간성, 개인 정보 보호, 그리고 복잡한 감정 추론을 동시에 달성하기 위해 **계층적 하이브리드 아키텍처(Hierarchical Hybrid Architecture)**를 채택합니다.

- **Edge-First Emotion Sensing**: 클라이언트 SDK(Browser/App)에서 스크롤 속도, 마우스 지터, 체류 시간 등 미세 상호작용 신호를 캡처하고, 엣지(Edge) 또는 로컬에서 1차적인 감성 스코어링을 수행하여 지연 시간을 150ms 미만으로 유지합니다.
- **Agentic Multi-Agent Architecture**: LangChain/LangGraph를 활용하여 감정 인식, 맥락 분석, 결과 생성 등 각 기능을 독립적인 에이전트로 분리하는 모듈형 아키텍처가 부상하고 있습니다. 이는 기능 확장이 용이하고 특정 단계의 모델만 업그레이드하기에 적합합니다.
- **Hybrid Decision Engine**: 규칙 기반 시스템(Expert Rules)과 딥러닝 모델(LLM)을 결합하여, 명확한 감정은 빠르게 처리하고 모호한 맥락은 LLM의 추론을 거치는 하이브리드 의사결정 구조를 사용합니다.

_Source: https://medium.com/@ruler547/how-to-build-a-real-time-emotion-engine-architecture-guide-3a348f054956, https://iscap.us/proceedings/2025/pdf/6457.pdf_

### Design Principles and Best Practices

"차가운 정보를 따뜻한 감정으로 전환"하기 위한 핵심 설계 원칙입니다.

- **Engagement & Trust over Efficiency**: 단순한 검색 효율성보다 사용자와의 정서적 교감 및 신뢰 구축을 우선순위에 둡니다. 시스템의 오류(잘못된 감정 판단 등)가 발생했을 때 이를 투명하게 알리고 사용자가 직접 수정할 수 있는 피드백 루프를 제공합니다.
- **Human-in-the-Loop**: 감성 분석 결과를 바탕으로 한 자동화된 조치보다, 사용자에게 정서적 통찰을 제공하고 최종 선택권을 부여하는 '인간 중심 설계'를 준수합니다.
- **Affective UX Parameters**: 콘텐츠의 의미(Purposive), 전달 매체(Media), 그리고 시스템의 '페르소나'(Teacher/Partner)라는 세 가지 파라미터를 조정하여 지루함, 호기심, 좌절감 등의 학습/탐색 상태를 관리합니다.

_Source: https://vismod.media.mit.edu/pub/tech-reports/TR-541.pdf, https://link.springer.com/article/10.1007/s10758-025-09867-1_

### Scalability and Performance Patterns

- **Modular Ingestion & Labeling**: 데이터 수집, 감성 레이블링, 요약 레이블링을 독립적인 서비스로 계층화하여 실시간 분석의 부하를 분산합니다.
- **Static Summarization Snapping**: 실시간 DB 쿼리를 피하기 위해 분석된 감성 요약을 JSON 스냅샷 형태로 미리 생성하여 대시보드 및 검색 결과의 응답 속도를 극대화합니다.
- **Test-time Scaling (HEART)**: 복잡한 감정적 맥락이 필요한 경우에만 LLM의 연산량을 늘리는(Scaling at test-time) 적응형 연산 패턴을 적용하여 비용과 성능의 균형을 맞춥니다.

_Source: https://arxiv.org/html/2509.11444v1, https://arxiv.org/abs/2509.22876_

### Integration and Communication Patterns

- **Streaming Sentiment Feeds**: WebSockets 또는 HTTP/2를 통해 감성 분석 파이프라인의 중간 결과를 클라이언트에 실시간으로 전송하여 UI가 즉각적으로 '정서적으로 반응'하도록 설계합니다.
- **Standardized AI Chat Protocols**: Microsoft의 AI Chat Protocol과 같은 표준 규격을 사용하여 감성 추출 모델과 다양한 프론트엔드 인터페이스 간의 상호 교환성을 보장합니다.

_Source: https://github.com/microsoft/ai-chat-protocol, https://zakn.dev/posts/sentiment_

### Security Architecture Patterns

- **Privacy-by-Design Repository**: Elasticsearch 또는 벡터 DB 기반의 클라우드 저장소 구축 시, 설계 단계부터 생체 및 감성 데이터의 기밀성, 무결성, 가용성을 보장하는 보안 아키텍처를 적용합니다.
- **Local-first / Opt-in Model**: 민감한 일기 데이터의 감성 추출은 가능한 한 로컬 환경(On-device)에서 수행하고, 클라우드 저장은 사용자의 명시적 동의와 익명화 처리를 거친 후 진행합니다.

_Source: https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1567702/abstract, https://www.researchgate.net/publication/395806525_Affective_Computing_and_Emotional_Data_Challenges_and_Implications_in_Privacy_Regulations_The_AI_Act_and_Ethics_in_Large_Language_Models_

### Data Architecture Patterns

- **Multi-dimensional Emotion Schemas**: Plutchik의 8개 기본 감정과 VAD(Valence-Arousal-Dominance) 차원을 결합한 복합 스키마를 사용하여 감정의 강도와 맥락을 정밀하게 기록합니다.
- **Emotional Resonance Engine**: 음악 이론이나 색상 코드 등 다른 도메인의 개념을 감정 데이터와 매핑하여, 정보를 시각적/청각적으로 전환하기 위한 메타데이터 구조를 유지합니다.

_Source: https://osf.io/r35hj/, https://arxiv.org/html/2509.15986v1_

### Deployment and Operations Architecture

- **Federated Learning Approach**: 중앙 서버에 데이터를 모으지 않고 개별 사용자의 로컬에서 학습된 감성 모델의 가중치만 공유하여 전체 시스템의 정확도를 높이는 연합 학습 배포 전략을 고려합니다.
- **Serverless Event Pipelines**: Knative와 같은 서버리스 환경에서 감성 추출 작업을 이벤트 기반으로 실행하여 운영 비용을 최적화합니다.

_Source: https://www.sciencedirect.com/science/article/abs/pii/S1566253524005311_

## Implementation Approaches and Technology Adoption

### Technology Adoption Strategies

Moments: Mind Studio의 감성 검색 기능을 구현하기 위한 단계적 채택 전략입니다.

- **Phase 1: Hybrid Semantic-Emotional Intent Decoding**: 전통적인 키워드 중심 SEO에서 벗어나 사용자의 검색 쿼리 뒤에 숨겨진 '감성적 의도'(예: 불안, 호기심, 좌절)를 해독하는 기능을 우선 구현합니다. 긴 문장형 쿼리에서 감성 트리거 단어를 추출하여 콘텐츠와 매칭합니다.
- **Phase 2: Gradual Multi-dimensional Modeling**: 단순 긍/부정 분석에서 시작하여, 2024년 SemEval 등에서 우수성이 검증된 '감정-원인 쌍 추출(ECPEC)' 프레임워크를 도입하여 일기 내 감정의 원인까지 파악하는 단계로 확장합니다.
- **Phase 3: Emotional Resonance System Integration**: 정보를 '따뜻한 대상'으로 전환하기 위해 색상 코드나 음악적 톤(ERS 시스템)을 감성 메타데이터와 결합하여 사용자에게 공감적인 시각/청각적 피드백을 제공합니다.

_Source: https://getuplift.co/optimize-emotional-search-intent-to-drive-conversions/, https://aclanthology.org/2024.semeval-1.81.pdf, https://osf.io/r35hj/_

### Development Workflows and Tooling

- **Human-Centric Testing Framework (HEval)**: 자동화된 감성 분석의 한계를 보완하기 위해 2025년 기준 크라우드소싱 기반의 HEval 도구를 도입, 시스템의 '정서적 톤'과 대화의 질을 인간의 관점에서 지속적으로 교정합니다.
- **Dual-Pass Extraction Workflow**: LLM(GPT-4o)을 '교사 모델'로 사용하여 복잡한 감성 맥락을 추출하고, 이를 경량화된 '학생 모델'(DistilRoBERTa 등)에 증류(Distillation)하여 로컬 환경에서도 고성능 감성 분석이 가능하게 구축합니다.

_Source: https://openassistantgpt.io/blogs/best-open-source-tools-for-chatbot-testing, https://www.scitepress.org/Papers/2024/129512/129512.pdf_

### Testing and Quality Assurance

- **Emotional Gold-Set Calibration**: 감성 레이블링의 일관성을 위해 인간 전문가가 작성한 'Gold-set'을 유지하며, 모델과의 일치도를 나타내는 Cohen’s kappa 계수를 0.7 이상으로 관리합니다.
- **Sarcasm & Negation specialized checks**: 단순 모델이 놓치기 쉬운 반어법이나 부정 문구를 처리하기 위한 전용 '추론 프롬프트(Reasoning prompts)'와 테스트 케이스를 CI/CD 파이프라인에 통합합니다.

_Source: https://geneo.app/blog/best-practices-measuring-sentiment-ai-generated-answers-2025/_

### Deployment and Operations Practices

- **Privacy-Preserving Local-first Ingestion**: 사용자의 가장 사적인 '일기' 데이터는 로컬 SDK(Browser/App) 내에서 1차 감성 스코어링을 수행하고, 중앙 서버로는 익명화된 벡터 데이터만 전송하여 프라이버시 사고를 원천 차단합니다.
- **Real-time API Caching (Redis)**: 반복되는 텍스트나 유사한 감성 패턴에 대해 Redis 캐시 계층을 두어 비싼 ML 추론 비용을 절감하고 응답 시간을 150ms 이내로 단축합니다.

_Source: https://medium.com/@ruler547/how-to-build-a-real-time-emotion-engine-architecture-guide-3a348f054956, https://zakn.dev/posts/sentiment_

### Team Organization and Skills

- **Affective Computing & Ethics Specialist**: 기술적 구현뿐만 아니라 감성 데이터 처리의 윤리적 가이드라인을 수립할 수 있는 전문가가 필요합니다.
- **Hybrid AI Engineers**: 전통적인 NLP 개발 지식과 최신 LLM 프롬프트 엔지니어링 능력을 동시에 갖춘 엔지니어링 조직이 요구됩니다.

### Cost Optimization and Resource Management

- **Model Cascading/Routing Strategy**: 모든 텍스트를 고가의 LLM으로 분석하지 않고, 짧은 텍스트는 VADER/TextBlob과 같은 경량 규칙 기반 모델로, 복잡한 맥락의 일기는 LLM으로 라우팅하여 토큰 비용을 최대 50% 절감합니다.
- **Context Window Management**: 'Rolling Memory' 기법을 사용하여 과거의 감성 맥락을 요약된 형태로 유지함으로써 컨텍스트 윈도우 크기를 줄여 추론 비용을 최적화합니다.

_Source: https://futureagi.com/blogs/llm-cost-optimization-2025, https://arxiv.org/html/2508.06105v1_

### Risk Assessment and Mitigation

- **Transparency & Consent**: 감성 데이터 수집 및 분석 사실을 사용자에게 명확히 고지하고, 언제든 분석 기능을 끌 수 있는(Opt-out) 명시적 제어권을 제공합니다.
- **Bias Monitoring**: 특정 문화권이나 인구 통계적 집단에 대해 감성 분석이 편향되지 않도록 정기적인 편향성 테스트를 수행하고 이를 공개합니다.
- **Integrity of Personal Narrative**: 시스템의 감성 분석 결과가 사용자의 실제 감정과 다를 경우 사용자가 이를 수정할 수 있게 하여, 자신의 서사가 시스템에 의해 왜곡되지 않도록 보호합니다.

_Source: https://link.springer.com/article/10.1007/s43681-023-00307-3, https://thelightbulb.ai/blog/ethical-considerations-in-emotion-ai-balancing-innovation-and-privacy/_

## Technical Research Recommendations

### Implementation Roadmap

1.  **Phase 1 (MVP - 3개월)**: 일기 텍스트 기반 Plutchik 8대 감정 추출 및 기본 벡터-감성 하이브리드 검색 구현.
2.  **Phase 2 (Optimization - 6개월)**: 로컬 LLM(Ollama) 도입을 통한 프라이버시 강화 및 Redis 기반 추론 캐싱 최적화.
3.  **Phase 3 (Expansion - 12개월)**: 이미지/음성 멀티모달 감성 추출 엔진 통합 및 '따뜻한 대상'으로의 시각화(ERS) 완성.

### Technology Stack Recommendations

-   **Backend**: Python (FastAPI) + LlamaIndex (PropertyGraphIndex)
-   **Extraction**: Hugging Face (RoBERTa) + OpenAI/Llama3 (Cascading)
-   **Storage**: Neo4j (Graph) + Weaviate (Hybrid Vector Store)
-   **Security**: Local LLM (Ollama) + AES-256 Encryption

### Skill Development Requirements

-   **NLP/Affective Computing**: Plutchik, VAD 모델 및 최신 Transformer 모델 활용 능력.
-   **LLM Ops**: 프롬프트 엔지니어링, 모델 증류(Distillation), 추론 비용 최적화.
-   **Privacy & Ethics**: GDPR/AI Act 기반의 데이터 보호 및 윤리적 설계 역량.

### Success Metrics and KPIs

-   **감성 분석 정확도**: Gold-set 대비 F1 Score 0.75 이상 달성.
-   **정서적 도달률**: 검색 결과에 대해 사용자가 '공감' 또는 '애착' 피드백을 남긴 비율.
-   **응답 속도**: 감성 검색 결과 반환 지연 시간 500ms 이내 (캐싱 적용 시 150ms).
-   **데이터 보안**: 클라우드 전송 데이터 중 개인 식별 정보(PII) 포함 비율 0%.

