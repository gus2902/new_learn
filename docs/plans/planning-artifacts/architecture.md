---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7]
inputDocuments:
  - "docs/plans/moments-mind-studio-product-brief.md"
  - "docs/plans/planning-artifacts/prd.md"
  - "docs/plans/planning-artifacts/research/market-global-pkm-market-user-pain-points-research-2026-01-08.md"
  - "docs/plans/planning-artifacts/research/technical-emotional-search-engine-research-2026-01-08.md"
  - "docs/plans/planning-artifacts/research/technical-permanent-archive-engine-research-2026-01-08.md"
  - "docs/plans/planning-artifacts/research/technical-semantic-graph-engine-research-2026-01-08.md"
  - "docs/plans/planning-artifacts/user-stories.md"
workflowType: 'architecture'
project_name: 'Moments: Mind Studio'
user_name: '마스터'
date: '2026-01-10T16:07:07+09:00'
partyModeContributors: ['Winston (Architect)', 'John (PM)', 'Amelia (Developer)', 'Murat (Test Architect)', 'Sally (UX Designer)']
---

# Architecture Decision Document

_This document builds collaboratively through step-by-step discovery. Sections are appended as we work through each architectural decision together._

---

## Architecture Initialization

아키텍처 설계 워크플로우가 성공적으로 시작되었습니다. 프로젝트의 비전과 요구사항을 바탕으로 최적의 시스템 구조를 설계하기 위한 준비를 마쳤습니다.

---

## Project Context Analysis

### Requirements Overview

**Functional Requirements:**
MVP는 7개의 핵심 기능 블록으로 구성됩니다: (1) 2초 캡처, (2) WACZ 영구 박제, (3) 시맨틱 그래프 자동 연결, (4) 일기 루틴, (5) 기본 검색, (6) 입소문 기능, (7) 측정 인프라. 특히 캡처-아카이브-그래프 파이프라인은 실시간 UX와 비동기 백엔드 처리의 분리를 요구합니다.

**Non-Functional Requirements:**
아키텍처를 형성하는 핵심 NFR: (1) 캡처 응답 시간 <2초, (2) API p95 <1초, (3) 가용성 >99.5%, (4) Local-only 모드 지원, (5) E2E 암호화 옵션, (6) 동시 접속 500명(MVP), (7) LazyGraphRAG 비용 최적화.

**Scale & Complexity:**
- Primary domain: Mobile App + Full-Stack (Backend AI)
- Complexity level: Medium-High
- Estimated architectural components: 10-12개

### Architectural Decisions from Party Mode Analysis

#### AD-01: Decoupled Capture Architecture
- **Decision**: 클라이언트는 URL+메타데이터만 전송, 서버에서 비동기 WACZ 처리.
- **Rationale**: 2초 캡처 SLA 달성을 위한 필수 분리.
- **Trade-off**: 캡처 성공과 아카이브 완료 사이의 시간차 발생 → 투명한 UX 상태 표시로 해결.
- **Contributors**: Winston (Architect), John (PM), Sally (UX Designer)

#### AD-02: Dual-mode Data Architecture
- **Decision**: Cloud Sync 모드와 Local-only 모드의 별도 데이터 플로우 설계.
- **Rationale**: 프라이버시 민감 사용자(의료/법률 전문가) 세그먼트 확보.
- **Trade-off**: 개발 복잡도 증가 → 두 모드의 명확한 경계와 별도 테스트 경로로 관리.
- **Contributors**: John (PM), Amelia (Developer)

#### AD-03: Phased Data Store Strategy
- **Decision**: Phase 0-1은 Postgres(JSON+pgvector), Phase 1.5+에서 Neo4j 마이그레이션.
- **Rationale**: MVP 빠른 출시 + 검증된 기술 우선, 실제 필요 시 마이그레이션.
- **Trade-off**: 마이그레이션 비용 발생 → 데이터 모델을 그래프 친화적으로 사전 설계.
- **Contributors**: Winston (Architect), Amelia (Developer)

#### AD-04: LazyGraphRAG Pattern
- **Decision**: 모든 캡처에 즉시 임베딩 생성하지 않고, 첫 재방문/일기 작성 시에만 임베딩.
- **Rationale**: LLM 비용 70-90% 절감.
- **Trade-off**: 첫 재방문 시 약간의 지연 발생 → 백그라운드 사전 임베딩 옵션 제공.
- **Contributors**: Winston (Architect)

### Technical Constraints & Dependencies

| 레이어 | 기술 스택 |
|--------|----------|
| **Mobile** | iOS (Swift), Android (Kotlin) with Share Extension |
| **Web** | React/Next.js + Chrome Extension (Manifest V3) |
| **Backend** | Node.js or Python (FastAPI) + LlamaIndex |
| **Data (Phase 0-1)** | Postgres (JSON + pgvector) |
| **Data (Phase 1.5+)** | Neo4j (Graph DB) |
| **Archive Storage** | WACZ (Object Storage - S3/R2) |
| **AI/ML** | Sentence-BERT (Embedding), VAD Model (Emotion), LLM (Lazy Evaluation) |

### Cross-Cutting Concerns Identified

| 관심사 | 설명 |
|--------|------|
| **인증/인가** | 모바일 OAuth2 + JWT, Local-only 모드 시 인증 불필요 |
| **암호화** | 선택적 E2E 암호화 (클라이언트 측 키 관리) |
| **이벤트 로깅** | Amplitude/Mixpanel 연동 (MVP 필수) |
| **성능 모니터링** | Sentry 연동 |
| **Feature Flag** | LaunchDarkly 또는 자체 구현 |
| **오프라인 지원** | 캡처 큐잉 + 백그라운드 싱크 |
| **Graceful Degradation** | 아카이브 실패 시 URL+텍스트 스냅샷 보존 |

### Test Strategy Alignment

| 테스트 영역 | 전략 |
|------------|------|
| **Phase 0 Go/No-Go** | 10개 사이트 E2E 성능 벤치마크 (2초 캡처 검증) |
| **Dual-path Testing** | Cloud Sync / Local-only 별도 테스트 경로 |
| **Risk-based Priority** | 캡처 성공률 > 아카이브 완전성 > 자동 연결 정확도 |
| **Graceful Degradation** | 아카이브 실패 시나리오 테스트 |

### UX State Transparency (Sally's Insight)

캡처 후 사용자에게 투명한 상태 표시:
1. **즉시**: "저장됨 ✓" (URL + 메타데이터 저장 완료)
2. **진행 중**: 작은 진행 표시기 (백그라운드 WACZ 아카이빙)
3. **완료**: "영구 보관됨 ✓✓" (WACZ 아카이브 완료)
4. **실패 시**: "원본 저장됨 (재시도 중)" + 조용한 백그라운드 재시도

---

## Technology Stack Evaluation

PRD 분석을 기반으로 각 기술 카테고리별 상세 비교 분석을 수행했습니다.

### Technology Version Specification (2026-01 기준)

모든 기술 스택의 구체적인 버전을 명시합니다. Phase 0 시작 시 최신 안정 버전으로 업데이트할 수 있습니다.

#### Core Runtime & Frameworks

| 기술 | 권장 버전 | 비고 |
|------|----------|------|
| **Node.js** | 22.x LTS | Turborepo, Next.js 실행 환경 |
| **Python** | 3.12.x | FastAPI, LlamaIndex 실행 환경 |
| **pnpm** | 9.x | Monorepo 패키지 매니저 |

#### Frontend (Mobile & Web)

| 기술 | 권장 버전 | 비고 |
|------|----------|------|
| **Expo SDK** | 54 | React Native 0.81, React 19.1 포함 |
| **React** | 19.1 | Expo SDK 54에 포함 |
| **React Native** | 0.81 | New Architecture 기본 활성화 |
| **Next.js** | 15.x 또는 16.x | App Router, Turbopack 안정화 |
| **TypeScript** | 5.7.x | 모든 JS/TS 프로젝트 공통 |
| **Tamagui** | 1.x (최신) | React Native + Web 공유 컴포넌트 |
| **TanStack Query** | 5.x | 서버 상태 관리 |
| **Zustand** | 5.x | 전역 상태 관리 |

#### Backend (Python)

| 기술 | 권장 버전 | 비고 |
|------|----------|------|
| **FastAPI** | 0.128.x | 최신 안정 버전 |
| **Pydantic** | 2.x | 데이터 검증 (v2 필수) |
| **LlamaIndex** | 0.12.x (최신) | GraphRAG, 임베딩 |
| **Sentence-Transformers** | 3.x (최신) | Sentence-BERT 임베딩 |
| **Playwright** | 1.50.x (최신) | WACZ 아카이빙 |
| **asyncpg** | 0.30.x | Postgres 비동기 드라이버 |

#### BaaS & Infrastructure

| 기술 | 권장 버전 | 비고 |
|------|----------|------|
| **Supabase CLI** | 2.71.x | Config-as-Code 지원 |
| **@supabase/supabase-js** | 2.90.x | 클라이언트 SDK |
| **PostgREST** | 14.x | Supabase 관리형 (자동 업데이트) |
| **pgvector** | 0.8.x | Supabase 확장 (대시보드 활성화) |

#### Build & CI Tools

| 기술 | 권장 버전 | 비고 |
|------|----------|------|
| **Turborepo** | 2.x | Monorepo 빌드 시스템 |
| **ESLint** | 9.x | Flat Config 지원 |
| **Prettier** | 3.x | 코드 포맷터 |
| **Playwright (E2E)** | 1.50.x | E2E 테스트 프레임워크 |
| **Vitest** | 2.x | 단위 테스트 (Jest 호환) |

#### Chrome Extension

| 기술 | 권장 버전 | 비고 |
|------|----------|------|
| **Manifest** | V3 | Chrome Extension 표준 |
| **Vite** | 6.x | 빌드 도구 |
| **CRXJS Vite Plugin** | 2.x | Extension 개발 도구 |

#### Version Update Policy

1. **Phase 0 시작 시**: 모든 패키지의 최신 안정 버전 확인 후 `package.json` / `requirements.txt` 고정
2. **Minor 업데이트**: 패치/마이너 버전은 자유롭게 업데이트 (CI 테스트 통과 시)
3. **Major 업데이트**: 별도 브랜치에서 테스트 후 마이그레이션 계획 수립

### 1. 모바일 개발 플랫폼 비교

| 평가 항목 | React Native/Expo | Flutter | Native (Swift + Kotlin) |
|----------|------------------|---------|------------------------|
| **개발 속도** | ⭐⭐⭐⭐⭐ 매우 빠름 | ⭐⭐⭐⭐ 빠름 | ⭐⭐ 느림 (2배 작업) |
| **Share Extension 지원** | ⭐⭐⭐ 가능 (네이티브 브릿지) | ⭐⭐ 제한적 | ⭐⭐⭐⭐⭐ 완벽 지원 |
| **성능 (2초 캡처)** | ⭐⭐⭐⭐ 충분 | ⭐⭐⭐⭐⭐ 우수 | ⭐⭐⭐⭐⭐ 최고 |
| **Local-only 모드** | ⭐⭐⭐⭐ SQLite/WatermelonDB | ⭐⭐⭐⭐ Hive/SQLite | ⭐⭐⭐⭐⭐ Core Data/Room |
| **1인 개발자 적합성** | ⭐⭐⭐⭐⭐ 최적 | ⭐⭐⭐⭐ 적합 | ⭐⭐ 부적합 |
| **웹과 코드 공유** | ⭐⭐⭐⭐⭐ React 공유 가능 | ⭐⭐⭐ Flutter Web | ⭐ 불가능 |
| **MVP 출시 속도** | ⭐⭐⭐⭐⭐ 최고 | ⭐⭐⭐⭐ 빠름 | ⭐⭐ 느림 |

**🏆 추천: React Native + Expo**
- 1인 개발자 + 직장인 제약 (주간 유지보수 <10시간)
- iOS/Android 동시 개발로 시간 절약
- Next.js 웹앱과 React 컴포넌트/로직 공유 (60-70%)

### 2. 백엔드 플랫폼 비교

| 평가 항목 | Node.js (NestJS/Fastify) | Python (FastAPI) | Go (Fiber/Echo) |
|----------|-------------------------|------------------|-----------------|
| **개발 속도** | ⭐⭐⭐⭐⭐ 매우 빠름 | ⭐⭐⭐⭐⭐ 매우 빠름 | ⭐⭐⭐ 중간 |
| **AI/ML 생태계** | ⭐⭐⭐ LangChain.js (제한적) | ⭐⭐⭐⭐⭐ LlamaIndex 네이티브 | ⭐⭐ 제한적 |
| **LlamaIndex 지원** | ⭐⭐ JS 버전 (기능 제한) | ⭐⭐⭐⭐⭐ 공식 Python 버전 | ⭐ 미지원 |
| **Sentence-BERT/임베딩** | ⭐⭐⭐ ONNX 런타임 | ⭐⭐⭐⭐⭐ 네이티브 | ⭐⭐ 외부 서비스 |
| **pgvector 지원** | ⭐⭐⭐⭐ pgvector-node | ⭐⭐⭐⭐⭐ pgvector-python | ⭐⭐⭐⭐ pgvector-go |
| **WACZ 처리** | ⭐⭐⭐ SingleFile CLI | ⭐⭐⭐⭐ Playwright Python | ⭐⭐ 외부 프로세스 |
| **프론트엔드 언어 통일** | ⭐⭐⭐⭐⭐ TypeScript | ⭐⭐ Python | ⭐ Go |
| **1인 개발자 적합성** | ⭐⭐⭐⭐⭐ 최적 | ⭐⭐⭐⭐ 적합 | ⭐⭐⭐ 학습 곡선 |

**🏆 추천: Python (FastAPI)**
- LlamaIndex, Sentence-BERT, VAD 모델 모두 Python 네이티브
- GraphRAG 패턴 Python에서만 완벽 지원
- 임베딩 비용 최적화: sentence-transformers 로컬 실행

### 3. 웹 프론트엔드 비교

| 평가 항목 | Next.js 14+ | Vite + React | SvelteKit |
|----------|-------------|--------------|-----------|
| **개발 속도** | ⭐⭐⭐⭐ 빠름 | ⭐⭐⭐⭐⭐ 매우 빠름 | ⭐⭐⭐⭐ 빠름 |
| **SSR/SEO** | ⭐⭐⭐⭐⭐ 네이티브 | ⭐⭐ 별도 설정 | ⭐⭐⭐⭐⭐ 네이티브 |
| **React Native 코드 공유** | ⭐⭐⭐⭐⭐ 완벽 | ⭐⭐⭐⭐⭐ 완벽 | ⭐ 불가능 |
| **Chrome Extension** | ⭐⭐⭐⭐ 가능 | ⭐⭐⭐⭐⭐ 최적 (CRXJS) | ⭐⭐⭐ 가능 |
| **배포 용이성** | ⭐⭐⭐⭐⭐ Vercel 최적화 | ⭐⭐⭐⭐ 어디서나 | ⭐⭐⭐⭐ Vercel 지원 |
| **API Routes** | ⭐⭐⭐⭐⭐ 내장 | ⭐⭐ 별도 서버 | ⭐⭐⭐⭐⭐ 내장 |

**🏆 추천: Next.js 14+**
- React Native와 컴포넌트/훅 최대 공유
- Vercel 배포: 무료 티어, 자동 스케일링
- API Routes로 BFF 레이어 구현 가능

### 4. 배포 플랫폼 비교 (Supabase 포함)

| 평가 항목 | Supabase | Railway + Vercel | AWS (ECS/Lambda) |
|----------|----------|------------------|------------------|
| **설정 용이성** | ⭐⭐⭐⭐⭐ 가장 쉬움 | ⭐⭐⭐⭐⭐ 매우 쉬움 | ⭐⭐ 복잡 |
| **Postgres + pgvector** | ⭐⭐⭐⭐⭐ 네이티브 내장 | ⭐⭐⭐⭐⭐ Railway 네이티브 | ⭐⭐⭐⭐ RDS pgvector |
| **인증 시스템** | ⭐⭐⭐⭐⭐ Supabase Auth 내장 | ⭐⭐⭐ 별도 구현 필요 | ⭐⭐⭐ Cognito |
| **실시간 기능** | ⭐⭐⭐⭐⭐ Realtime 2.0 (<50ms) | ⭐⭐⭐ WebSocket 직접 구현 | ⭐⭐⭐ AppSync/WebSocket |
| **Edge Functions** | ⭐⭐⭐⭐ Deno 기반 (TypeScript) | ⭐⭐⭐⭐⭐ Vercel Edge | ⭐⭐⭐⭐ Lambda@Edge |
| **Python 백엔드 지원** | ⭐⭐ Edge Functions만 (TS/JS) | ⭐⭐⭐⭐⭐ Railway 컨테이너 | ⭐⭐⭐⭐⭐ 완벽 |
| **Object Storage** | ⭐⭐⭐⭐ Supabase Storage 내장 | ⭐⭐⭐ 외부 연동 (R2) | ⭐⭐⭐⭐⭐ S3 네이티브 |
| **AI/ML 워크로드** | ⭐⭐ Edge에서 제한적 | ⭐⭐⭐⭐⭐ 컨테이너 완벽 | ⭐⭐⭐⭐⭐ 완벽 |
| **백그라운드 작업** | ⭐⭐⭐⭐ Queues, Cron Jobs (신규) | ⭐⭐⭐⭐⭐ 완벽 | ⭐⭐⭐⭐⭐ 완벽 |
| **비용 (MVP)** | ⭐⭐⭐⭐ 무료~$25/월 | ⭐⭐⭐⭐⭐ ~$10-30/월 | ⭐⭐ $50+/월 |
| **1인 개발자 적합성** | ⭐⭐⭐⭐⭐ 최적 | ⭐⭐⭐⭐⭐ 최적 | ⭐⭐ DevOps 부담 |

### 5. Supabase 심층 분석

#### Supabase 장점 (Moments 프로젝트 관점)

| 장점 | 설명 | PRD 요구사항 매핑 |
|------|------|-----------------|
| **올인원 BaaS** | DB + Auth + Storage + Realtime 통합 | 개발 속도 ↑, 1인 개발자 부담 ↓ |
| **pgvector 네이티브** | 벡터 검색 내장, 대시보드에서 활성화 | AD-03: Postgres+pgvector 전략 |
| **Supabase Auth** | OAuth2, JWT, Magic Link 내장 | 인증 구현 시간 절약 |
| **Realtime 2.0** | <50ms 지연, 다중 테이블 실시간 업데이트 | 일기 루틴 실시간 동기화 |
| **Edge Functions** | Deno 2.1, Node.js 호환, AI 추론 지원 | 가벼운 API 로직 |
| **Queues & Cron** | 백그라운드 작업 지원 (2024 신규) | WACZ 아카이빙 큐 |
| **무료 티어** | 50K MAU, 500MB DB, 1GB Storage | MVP 검증 충분 |

#### Supabase 한계 (Moments 프로젝트 관점)

| 한계 | 설명 | 영향도 | 대안 |
|------|------|-------|------|
| **Python 미지원** | Edge Functions = TypeScript/Deno만 | ⚠️ 높음 | 별도 Python 서버 필요 |
| **LlamaIndex 불가** | Python 네이티브 라이브러리 사용 불가 | ⚠️ 높음 | Railway에 Python 배포 |
| **WACZ 처리 제한** | Playwright 등 무거운 작업 불가 | ⚠️ 높음 | 외부 워커 필요 |
| **Sentence-BERT** | 로컬 임베딩 모델 실행 불가 | ⚠️ 높음 | 외부 API 또는 워커 |
| **Storage 용량** | Pro 플랜 100GB, WACZ 대용량 시 비용 증가 | 중간 | Cloudflare R2 병행 |
| **Local-only 모드** | Supabase는 클라우드 기반, 오프라인 설계 복잡 | 중간 | 클라이언트 SQLite 병행 |

#### Supabase 하이브리드 아키텍처 제안

```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend Layer                            │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │  React Native   │  │    Next.js      │  │ Chrome Extension │  │
│  │     (Expo)      │  │   (Vercel)      │  │                  │  │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘  │
└───────────┼────────────────────┼────────────────────┼───────────┘
            │                    │                    │
            ▼                    ▼                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Supabase Layer (BaaS)                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  Supabase   │  │  Supabase   │  │  Supabase   │              │
│  │    Auth     │  │   Realtime  │  │   Storage   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│  ┌─────────────────────────────────────────────────┐            │
│  │         Postgres + pgvector (Supabase)          │            │
│  │  - 사용자 데이터, 캡처 메타데이터, 임베딩 벡터  │            │
│  └─────────────────────────────────────────────────┘            │
│  ┌─────────────────┐  ┌─────────────────┐                       │
│  │ Edge Functions  │  │  Queues/Cron    │                       │
│  │ (가벼운 API)    │  │ (작업 트리거)   │                       │
│  └────────┬────────┘  └────────┬────────┘                       │
└───────────┼────────────────────┼────────────────────────────────┘
            │                    │
            ▼                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                   AI/ML Worker Layer (Railway)                   │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                  Python + FastAPI                            ││
│  │  - LlamaIndex (GraphRAG)                                     ││
│  │  - Sentence-BERT (임베딩)                                    ││
│  │  - VAD 모델 (감정 분석)                                      ││
│  │  - WACZ 아카이빙 (Playwright)                                ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Object Storage (Cloudflare R2)                │
│  - WACZ 아카이브 파일 저장                                       │
│  - S3 호환 API                                                   │
│  - 무료 이그레스                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 배포 플랫폼 최종 비교

| 시나리오 | Supabase 단독 | Supabase + Railway | Railway + Vercel |
|----------|--------------|-------------------|------------------|
| **AI/ML 지원** | ❌ 불가 | ✅ Railway에서 | ✅ Railway에서 |
| **개발 복잡도** | ⭐⭐⭐⭐⭐ 최소 | ⭐⭐⭐⭐ 약간 증가 | ⭐⭐⭐⭐ 약간 증가 |
| **인증 구현** | ⭐⭐⭐⭐⭐ 내장 | ⭐⭐⭐⭐⭐ 내장 | ⭐⭐⭐ 직접 구현 |
| **비용 (MVP)** | ~$25/월 | ~$30-40/월 | ~$15-30/월 |
| **PRD 요구사항 충족** | ⚠️ 50% (AI 제외) | ✅ 100% | ✅ 100% |

**🏆 최종 추천: Supabase + Railway 하이브리드**

**추천 이유:**
1. **Supabase 활용**: Auth, Realtime, Postgres+pgvector, Storage (경량 파일)
2. **Railway 활용**: Python FastAPI + LlamaIndex + 임베딩 + WACZ 처리
3. **Cloudflare R2**: WACZ 대용량 아카이브 저장 (무료 이그레스)
4. **Vercel**: Next.js 프론트엔드 배포

이 조합은 Supabase의 개발 생산성과 Railway의 AI/ML 유연성을 모두 확보합니다.

### 스타터 템플릿 후보

| 카테고리 | 스타터 | 명령어 |
|----------|--------|--------|
| **모바일** | Expo + Supabase | `npx create-expo-app@latest moments-mobile --template tabs` |
| **웹** | Next.js + Supabase | `npx create-next-app@latest moments-web --typescript --tailwind --eslint --app` |
| **백엔드 AI** | FastAPI | `pip install fastapi uvicorn sqlalchemy asyncpg` |

---

## Core Architectural Decisions

Step 4에서 결정된 세부 아키텍처 항목입니다. Party Mode 토론을 통해 개발, 테스트, 보안 관점의 피드백을 반영하여 강화되었습니다.

### Decision Priority Analysis

**Critical Decisions (Block Implementation):**
- 데이터 모델링 접근법 (Hybrid)
- 인증 방식 (Supabase Auth + Local 생체인증)
- API 설계 패턴 (PostgREST + FastAPI)
- 상태 관리 (Zustand + TanStack Query)

**Important Decisions (Shape Architecture):**
- 마이그레이션 전략 (Supabase Migrations)
- CI/CD 파이프라인 (GitHub Actions)
- 모니터링 (Sentry + Amplitude)

**Deferred Decisions (Post-MVP):**
- 캐싱 전략 (Redis) - 사용량 증가 시 도입
- CDN 구성 - 글로벌 확장 시 검토
- 멀티 리전 배포 - 규모 확장 시 검토

### Data Architecture

#### DA-01: 데이터 모델링 접근법
- **Decision**: Hybrid (관계형 + JSONB)
- **Rationale**: 핵심 엔티티(사용자, 캡처, 일기)는 관계형으로 데이터 무결성 보장. 메타데이터, 태그, 커스텀 필드는 JSONB로 유연성 확보.
- **Implementation**:
  ```sql
  -- 핵심 테이블은 관계형
  CREATE TABLE captures (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id),
    url TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    -- 메타데이터는 JSONB
    metadata JSONB DEFAULT '{}'::jsonb,
    -- 임베딩은 pgvector
    embedding vector(384)
  );
  
  -- JSONB 필드에 GIN 인덱스 필수 (Murat 제안)
  CREATE INDEX idx_captures_metadata ON captures USING GIN (metadata);
  ```
- **Contributors**: Winston (Architect), Murat (Test Architect)

#### DA-02: 데이터 검증 전략 (Party Mode에서 수정됨)
- **Decision**: Dual Validation (Frontend + Backend)
- **Rationale**: Amelia의 지적 수용 - UX를 위한 즉각적 피드백 + 보안/무결성을 위한 서버 검증
- **Implementation**:
  - **Frontend**: React Hook Form + 기본 RegEx 검증 (이메일, 필수값 등)
  - **Backend**: Pydantic 모델로 최종 검증
  - **타입 공유**: OpenAPI → openapi-typescript로 자동 생성
- **Contributors**: Winston (Architect), Amelia (Developer)

#### DA-03: 마이그레이션 전략 (Party Mode에서 보강됨)
- **Decision**: Supabase Migrations
- **Rationale**: Supabase CLI 통합, SQL 기반 Postgres 기능 완전 활용
- **Workflow** (Murat 제안 반영):
  1. 로컬 개발: `supabase start` → Docker에서 로컬 Supabase 실행
  2. 마이그레이션 생성: `supabase migration new <name>`
  3. CI 테스트: GitHub Actions에서 마이그레이션 적용 검증
  4. 운영 배포: `supabase db push`
- **Contributors**: Winston (Architect), Murat (Test Architect)

### Authentication & Security

#### SEC-01: 인증 방식
- **Decision**: Supabase Auth (Cloud Mode) + 기기 생체인증 (Local-only Mode)
- **Cloud Mode**:
  - OAuth 2.0: Google, Apple (MVP)
  - Magic Link: 이메일 기반 비밀번호 없는 로그인
  - JWT + Refresh Token: Supabase SDK 자동 관리
- **Local-only Mode**:
  - iOS: FaceID/TouchID → Keychain에서 SQLCipher 키 추출
  - Android: BiometricPrompt → Keystore에서 SQLCipher 키 추출
  - Fallback: 6자리 PIN (키 파생)
- **Contributors**: Winston (Architect), Anti-Gravity (Security)

#### SEC-02: API 보안 (Party Mode에서 강화됨)
- **Decision**: Supabase RLS + 의무 보안 테스트
- **RLS 정책**: 모든 테이블에 Row Level Security 적용
- **보안 테스트 필수** (Anti-Gravity 제안):
  ```sql
  -- RLS 정책 예시
  CREATE POLICY "Users can only view own captures"
  ON captures FOR SELECT
  USING (auth.uid() = user_id);
  
  -- 부정 테스트 케이스 필수
  -- "다른 사용자의 캡처는 절대 조회 불가"를 테스트로 증명
  ```
- **Contributors**: Winston (Architect), Anti-Gravity (Security)

#### SEC-03: Local-only 데이터 암호화 (Party Mode에서 강화됨)
- **Decision**: SQLCipher + OS Keychain 키 관리
- **Implementation**:
  - SQLCipher로 로컬 SQLite 전체 암호화
  - 암호화 키는 OS Keychain/Keystore에 저장 (앱 언인스톨 시 자동 삭제)
  - 생체인증 통과 시에만 키 접근 가능
  - 메모리 키 상주 시간 최소화
- **Contributors**: Anti-Gravity (Security)

### API & Communication Patterns

#### API-01: API 설계 패턴
- **Decision**: Dual API Layer
- **Supabase PostgREST**: 클라이언트 → Supabase 직접 연결 (CRUD 자동화)
- **FastAPI REST**: AI/ML 워크로드 전용 (LlamaIndex, 임베딩, WACZ)
- **Rationale**: 각 도구의 장점 활용, 복잡도 분리

#### API-02: 실시간 통신
- **Decision**: Supabase Realtime
- **Use Cases**:
  - 캡처 상태 업데이트 (저장됨 → 아카이빙 중 → 완료)
  - 일기 동기화 (멀티 디바이스)
  - 자동 연결 알림 (새로운 연결 발견)

#### API-03: 에러 처리 표준
- **Decision**: RFC 7807 Problem Details
- **Format**:
  ```json
  {
    "type": "https://moments.app/errors/capture-failed",
    "title": "Capture Failed",
    "status": 500,
    "detail": "WACZ archiving timed out after 30 seconds",
    "instance": "/api/captures/abc123"
  }
  ```
- **Logging**: Sentry 통합 (자동 에러 추적)

### Frontend Architecture

#### FE-01: 상태 관리
- **Decision**: Zustand (전역) + TanStack Query (서버 상태)
- **Zustand**: 테마, 사용자 설정, 로컬 UI 상태
- **TanStack Query**: API 캐싱, 낙관적 업데이트, 오프라인 큐
- **Supabase Hooks**: Realtime 구독 관리

#### FE-02: 컴포넌트 아키텍처
- **Decision**: Tamagui (React Native + Web 공유)
- **Rationale**: 단일 컴포넌트 코드로 iOS, Android, Web 모두 지원
- **Design Tokens**: Tamagui 테마 시스템으로 다크 모드 지원
- **Icons**: Lucide React / Lucide React Native (통일)

#### FE-03: 코드 공유 전략
- **Monorepo 구조**: Turborepo 또는 Nx
- **공유 패키지**:
  - `@moments/shared`: 타입, 유틸리티, 상수
  - `@moments/ui`: Tamagui 컴포넌트
  - `@moments/hooks`: 공유 React 훅

### Infrastructure & Deployment

#### INFRA-01: CI/CD 파이프라인
- **Decision**: GitHub Actions
- **Pipelines**:
  | Trigger | Action |
  |---------|--------|
  | PR to main | Lint, Test, Type Check |
  | Push to main | Deploy to Staging |
  | Release tag | Deploy to Production |
  | Scheduled | E2E Tests (Playwright) |

#### INFRA-02: 환경 설정
- **Decision**: 플랫폼 네이티브 환경 변수
- **Configuration**:
  - Vercel: Project Settings → Environment Variables
  - Railway: Project Settings → Variables
  - Mobile: `app.config.ts` + EAS Secrets

#### INFRA-03: 모니터링 & 로깅
- **Decision**: Sentry + Amplitude + 플랫폼 내장 메트릭
- **Implementation**:
  | 도구 | 용도 |
  |------|------|
  | Sentry | 에러 추적, 성능 모니터링 |
  | Amplitude | 사용자 이벤트, 퍼널 분석 |
  | Vercel Analytics | 웹 Core Web Vitals |
  | Railway Metrics | 백엔드 CPU/메모리 |

### Decision Impact Analysis

**Implementation Sequence:**
1. Supabase 프로젝트 생성 + Auth 설정
2. 데이터베이스 스키마 + RLS 정책 배포
3. FastAPI 백엔드 배포 (Railway)
4. Next.js 웹 배포 (Vercel)
5. React Native 앱 개발 (Expo EAS)
6. 모니터링 연동 (Sentry, Amplitude)

**Cross-Component Dependencies:**
- Supabase Auth → 모든 클라이언트 인증의 단일 소스
- TanStack Query → Supabase PostgREST + FastAPI 모두 호출
- Tamagui → Mobile + Web 컴포넌트 공유의 핵심

---

## Implementation Patterns & Consistency Rules

Step 5에서 정의된 구현 패턴입니다. Party Mode 토론을 통해 실용성, 자동 검증, 참조 가이드라인이 보강되었습니다.

### Pattern Categories Defined

**Critical Conflict Points Identified:** 5개 카테고리, 20+ 잠재적 충돌 영역

### Naming Patterns

#### NP-01: 데이터베이스 네이밍 규칙

| 항목 | 패턴 | 예시 |
|------|------|------|
| **테이블명** | `snake_case`, 복수형 | `captures`, `diary_entries`, `user_connections` |
| **컬럼명** | `snake_case` | `user_id`, `created_at`, `mood_color` |
| **외래키** | `{테이블_단수}_id` | `user_id`, `capture_id` |
| **인덱스** | `idx_{테이블}_{컬럼}` | `idx_captures_user_id` |
| **RLS 정책** | `{동작}_{테이블}_{조건}` | `select_captures_own` |

#### NP-02: API 네이밍 규칙

| 항목 | 패턴 | 예시 |
|------|------|------|
| **Supabase REST** | `/rest/v1/{테이블}` | `/rest/v1/captures` |
| **FastAPI 엔드포인트** | `/v1/{리소스}` | `/v1/embeddings`, `/v1/archive` |
| **라우트 파라미터** | `:id` | `/api/captures/:id` |
| **쿼리 파라미터** | `snake_case` | `?user_id=123` |

#### NP-03: 코드 네이밍 규칙

| 항목 | 패턴 | 예시 |
|------|------|------|
| **React 컴포넌트** | `PascalCase` | `CaptureCard`, `DiaryEditor` |
| **파일명 (컴포넌트)** | `PascalCase.tsx` | `CaptureCard.tsx` |
| **파일명 (유틸리티)** | `camelCase.ts` | `dateUtils.ts` |
| **함수명 (JS/TS)** | `camelCase` | `getUserCaptures()` |
| **함수명 (Python)** | `snake_case` | `get_user_captures()` |
| **상수** | `SCREAMING_SNAKE_CASE` | `MAX_CAPTURE_SIZE` |
| **환경변수** | `SCREAMING_SNAKE_CASE` | `SUPABASE_URL` |

### Structure Patterns

#### SP-01: 프로젝트 조직

```
moments/
├── apps/
│   ├── mobile/              # Expo React Native
│   │   └── src/
│   │       ├── features/    # 기능별 폴더
│   │       ├── components/  # 공유 컴포넌트
│   │       ├── hooks/       # 커스텀 훅
│   │       └── services/    # API 서비스
│   ├── web/                 # Next.js
│   │   └── src/
│   │       ├── app/         # App Router
│   │       ├── features/
│   │       └── components/
│   └── api/                 # FastAPI
│       └── app/
│           ├── routers/
│           ├── services/
│           └── models/
├── packages/
│   ├── shared/              # 타입, 유틸리티
│   ├── ui/                  # Tamagui 컴포넌트
│   └── hooks/               # 공유 React 훅
├── supabase/                # Supabase 설정
│   ├── migrations/
│   └── functions/
└── turbo.json
```

#### SP-02: 테스트 위치 (Co-located)

```
features/
└── capture/
    ├── CaptureCard.tsx
    ├── CaptureCard.test.tsx    # 컴포넌트와 같은 폴더
    ├── useCaptureQuery.ts
    └── useCaptureQuery.test.ts
```

### Format Patterns

#### FP-01: API 응답 포맷

**성공 응답:** 직접 데이터 반환 (래퍼 없음)
```json
{
  "id": "abc123",
  "url": "https://example.com",
  "createdAt": "2026-01-10T16:37:00+09:00",
  "moodColor": "blue"
}
```

**에러 응답:** RFC 7807 Problem Details
```json
{
  "type": "https://moments.app/errors/not-found",
  "status": 404,
  "title": "Capture Not Found",
  "detail": "The requested capture does not exist."
}
```

#### FP-02: 데이터 변환 규칙 (Party Mode에서 명시됨)

| 레이어 | 포맷 | 변환 방법 |
|--------|------|----------|
| **Database** | `snake_case` | - |
| **FastAPI** | `snake_case` | - |
| **API Response** | `camelCase` | Pydantic `alias` 사용 |
| **Frontend** | `camelCase` | 변환 불필요 (API 그대로 사용) |

**FastAPI 변환 규칙:**
```python
from pydantic import BaseModel, Field

class CaptureResponse(BaseModel):
    id: str
    user_id: str = Field(..., alias='userId')
    mood_color: str = Field(..., alias='moodColor')
    created_at: str = Field(..., alias='createdAt')
    
    class Config:
        populate_by_name = True  # Pydantic v2
```

### Communication Patterns

#### CP-01: 상태 관리

| 항목 | 패턴 | 예시 |
|------|------|------|
| **Zustand Store** | `use{기능}Store` | `useCaptureStore`, `useDiaryStore` |
| **TanStack Query Key** | `[리소스, ...조건]` | `['captures', userId]` |
| **상태 업데이트** | Immutable | Zustand immer 미들웨어 |

#### CP-02: 이벤트 네이밍

| 항목 | 패턴 | 예시 |
|------|------|------|
| **Supabase Realtime** | 테이블 변경 자동 감지 | `captures` 테이블 구독 |
| **커스텀 이벤트** | `camelCase` | `captureCreated`, `diaryUpdated` |

### Process Patterns

#### PP-01: 에러 처리

| 상황 | 패턴 |
|------|------|
| **네트워크 에러** | Toast 알림 + 자동 재시도 (3회) |
| **인증 에러 (401)** | 로그인 화면 리다이렉트 |
| **유효성 검증 실패** | 인라인 에러 메시지 |
| **서버 에러 (500)** | Toast + Sentry 자동 보고 |

#### PP-02: 로딩 상태

| 항목 | 패턴 |
|------|------|
| **로딩 변수명** | `isLoading`, `isPending` |
| **데이터 영역** | 스켈레톤 표시 |
| **버튼** | 스피너 + disabled |

### Import 정렬 규칙 (Party Mode에서 추가됨)

**순서 (eslint-plugin-simple-import-sort):**
1. React / React Native
2. 외부 라이브러리 (alphabetical)
3. 내부 패키지 (`@moments/...`)
4. 상대 경로 (`./`, `../`)

**예시:**
```typescript
// 1. React
import React, { useState, useEffect } from 'react';

// 2. 외부 라이브러리
import { useQuery } from '@tanstack/react-query';
import { supabase } from '@supabase/supabase-js';

// 3. 내부 패키지
import { Button } from '@moments/ui';
import { formatDate } from '@moments/shared';

// 4. 상대 경로
import { CaptureCard } from './CaptureCard';
import styles from './styles.module.css';
```

### Pattern Enforcement (Party Mode에서 추가됨)

#### 자동 검증 도구

| 패턴 | 검증 도구 | CI 단계 |
|------|----------|--------|
| 코드 네이밍 | ESLint `naming-convention` | PR Check |
| Import 순서 | `eslint-plugin-simple-import-sort` | PR Check |
| 코드 포맷 | Prettier | PR Check (자동 수정) |
| API 스키마 | OpenAPI 검증 | PR Check |
| 테스트 위치 | 커스텀 CI 스크립트 | PR Check |
| DB 네이밍 | Supabase Migration 리뷰 | PR Review |

#### ESLint 설정 예시

```javascript
// .eslintrc.js
module.exports = {
  plugins: ['simple-import-sort'],
  rules: {
    'simple-import-sort/imports': 'error',
    'simple-import-sort/exports': 'error',
    '@typescript-eslint/naming-convention': [
      'error',
      { selector: 'variable', format: ['camelCase', 'UPPER_CASE'] },
      { selector: 'function', format: ['camelCase', 'PascalCase'] },
      { selector: 'typeLike', format: ['PascalCase'] },
    ],
  },
};
```

#### PR 체크리스트 템플릿 (Party Mode에서 추가됨)

```markdown
## 패턴 준수 체크리스트

- [ ] 컴포넌트명은 PascalCase로 작성
- [ ] DB 테이블/컬럼명은 snake_case로 작성
- [ ] API 응답은 camelCase로 변환 (Pydantic alias)
- [ ] 테스트 파일은 컴포넌트와 같은 폴더에 위치
- [ ] Import 순서 규칙 준수 (ESLint 통과)
- [ ] 에러 응답은 RFC 7807 형식 준수
```

### AI Agent Mandatory Rules

**모든 AI 에이전트는 반드시 다음을 준수:**

1. ✅ 테이블/컬럼명: `snake_case` 복수형
2. ✅ React 컴포넌트: `PascalCase.tsx`
3. ✅ Python 함수: `snake_case`
4. ✅ API 응답 날짜: ISO 8601
5. ✅ 에러 응답: RFC 7807
6. ✅ 테스트 파일: 컴포넌트와 같은 폴더에 `.test.tsx`
7. ✅ DB → API 변환: Pydantic `alias` 사용
8. ✅ Import 순서: React → 외부 → 내부 → 상대
9. ✅ TanStack Query 키: `[리소스, ...조건]` 배열

### Pattern Examples

**Good Example (올바른 패턴):**
```typescript
// CaptureCard.tsx - PascalCase 파일명
import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { Card } from '@moments/ui';
import { formatDate } from '@moments/shared';
import { CaptureImage } from './CaptureImage';

export function CaptureCard({ captureId }: { captureId: string }) {
  const { data, isPending } = useQuery({
    queryKey: ['captures', captureId],  // 배열 형식
    queryFn: () => fetchCapture(captureId),
  });
  // ...
}
```

**Anti-Pattern (피해야 할 패턴):**
```typescript
// ❌ capture-card.tsx - 잘못된 파일명 (kebab-case)
// ❌ 잘못된 import 순서
import { CaptureImage } from './CaptureImage';
import React from 'react';
import { Card } from '@moments/ui';

// ❌ CAPTURES - 잘못된 query key (문자열)
const { data } = useQuery({ queryKey: 'CAPTURES' });
```

---

## Project Structure & Boundaries

Step 6에서 정의된 프로젝트 구조입니다. Party Mode 토론을 통해 Chrome Extension, 테스트 구조, 환경 변수 공유 전략이 보강되었습니다.

### Complete Project Directory Structure

```
moments/
├── README.md
├── package.json                    # Turborepo workspace 루트
├── turbo.json                      # Turborepo 설정
├── pnpm-workspace.yaml             # pnpm workspace 설정
├── playwright.config.ts            # E2E 테스트 설정 (Murat 추가)
├── .gitignore
├── .env.common                     # 공통 환경변수 (Amelia 추가)
├── .env.example
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                  # PR 린트, 테스트
│   │   ├── deploy-web.yml          # Vercel 배포
│   │   ├── deploy-api.yml          # Railway 배포
│   │   └── e2e.yml                 # E2E 테스트 (스케줄)
│   ├── PULL_REQUEST_TEMPLATE.md    # PR 체크리스트 포함
│   └── CODEOWNERS
│
├── apps/
│   ├── mobile/                     # 📱 Expo React Native
│   ├── web/                        # 🌐 Next.js 14+
│   ├── api/                        # 🐍 FastAPI (Python)
│   └── extension/                  # 🔌 Chrome Extension (Amelia 추가)
│
├── packages/
│   ├── shared/                     # 📦 공유 타입, 유틸리티
│   ├── ui/                         # 🎨 Tamagui 컴포넌트
│   ├── hooks/                      # 🪝 공유 React 훅
│   └── test-utils/                 # 🧪 공유 테스트 유틸 (Murat 추가)
│
├── supabase/                       # 🗄️ Supabase 설정
│   ├── config.toml
│   ├── migrations/
│   ├── functions/                  # Edge Functions
│   └── seed.sql
│
├── tests/                          # 📋 통합 E2E 테스트 (Murat 추가)
│   └── e2e/
│       ├── capture-flow.spec.ts
│       └── diary-flow.spec.ts
│
└── docs/
    ├── architecture.md
    ├── api-reference.md
    └── deployment.md
```

### apps/mobile/ (Expo React Native)

```
apps/mobile/
├── package.json
├── app.json
├── app.config.ts
├── eas.json
├── babel.config.js
├── tsconfig.json
├── metro.config.js
├── .env.local
│
├── app/                            # Expo Router
│   ├── _layout.tsx
│   ├── index.tsx
│   ├── (tabs)/
│   │   ├── _layout.tsx
│   │   ├── capture.tsx
│   │   ├── diary.tsx
│   │   ├── search.tsx
│   │   └── settings.tsx
│   ├── (auth)/
│   │   ├── login.tsx
│   │   └── onboarding.tsx
│   └── capture/[id].tsx
│
├── src/
│   ├── features/
│   │   ├── capture/
│   │   │   ├── CaptureCard.tsx
│   │   │   ├── CaptureCard.test.tsx
│   │   │   ├── CaptureForm.tsx
│   │   │   ├── ShareExtensionHandler.tsx
│   │   │   ├── useCaptureQuery.ts
│   │   │   └── captureService.ts
│   │   ├── diary/
│   │   │   ├── DiaryEditor.tsx
│   │   │   ├── DiaryEditor.test.tsx
│   │   │   ├── DiaryEntryCard.tsx
│   │   │   ├── useDiaryQuery.ts
│   │   │   └── diaryService.ts
│   │   ├── search/
│   │   │   ├── SearchBar.tsx
│   │   │   ├── SearchResults.tsx
│   │   │   └── useSearchQuery.ts
│   │   └── auth/
│   │       ├── AuthProvider.tsx
│   │       ├── useAuth.ts
│   │       └── authService.ts
│   ├── components/
│   │   ├── MoodSelector.tsx
│   │   ├── TimelineView.tsx
│   │   └── LoadingSpinner.tsx
│   ├── hooks/
│   │   ├── useLocalStorage.ts
│   │   └── useOfflineQueue.ts
│   ├── services/
│   │   ├── supabaseClient.ts
│   │   ├── apiClient.ts
│   │   └── offlineManager.ts
│   ├── stores/
│   │   ├── useCaptureStore.ts
│   │   ├── useDiaryStore.ts
│   │   └── useSettingsStore.ts
│   ├── utils/
│   │   └── dateUtils.ts
│   └── types/
│       └── index.ts
│
├── ios/
│   └── ShareExtension/
│       ├── ShareViewController.swift
│       └── Info.plist
│
└── android/
    └── app/src/main/java/.../ShareActivity.java
```

### apps/web/ (Next.js 14+)

```
apps/web/
├── package.json
├── next.config.js
├── tailwind.config.js
├── tsconfig.json
├── .env.local
│
├── src/
│   ├── app/
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── (auth)/
│   │   │   ├── login/page.tsx
│   │   │   └── callback/page.tsx
│   │   ├── (dashboard)/
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx
│   │   │   ├── diary/page.tsx
│   │   │   ├── search/page.tsx
│   │   │   └── settings/page.tsx
│   │   └── capture/[id]/page.tsx
│   ├── features/
│   │   ├── capture/
│   │   ├── diary/
│   │   └── auth/
│   ├── components/
│   │   ├── Header.tsx
│   │   ├── Sidebar.tsx
│   │   └── Footer.tsx
│   ├── lib/
│   │   ├── supabaseClient.ts
│   │   └── apiClient.ts
│   └── stores/
│       └── useCaptureStore.ts
│
├── public/
│   ├── favicon.ico
│   └── assets/
│
└── tests/
    └── components/
```

### apps/extension/ (Chrome Extension - Party Mode에서 추가)

```
apps/extension/
├── package.json
├── manifest.json                   # Manifest V3
├── vite.config.ts
├── tsconfig.json
│
├── src/
│   ├── popup/
│   │   ├── Popup.tsx
│   │   ├── index.html
│   │   └── main.tsx
│   ├── background/
│   │   └── service-worker.ts
│   ├── content/
│   │   └── content-script.ts
│   ├── lib/
│   │   └── supabaseClient.ts
│   └── storage/
│       └── localCaptures.ts
│
└── public/
    └── icons/
```

### apps/api/ (FastAPI - Python)

```
apps/api/
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── .env
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── embeddings.py           # /v1/embeddings
│   │   ├── archive.py              # /v1/archive (WACZ)
│   │   ├── connections.py          # /v1/connections (GraphRAG)
│   │   └── health.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── embedding_service.py
│   │   ├── archive_service.py
│   │   ├── graph_service.py
│   │   └── emotion_service.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── capture.py
│   │   ├── diary.py
│   │   └── connection.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── repositories/
│   ├── utils/
│   │   ├── __init__.py
│   │   └── auth.py
│   └── workers/                    # MVP: FastAPI 내부, 스케일링 시 분리
│       ├── __init__.py
│       └── archive_worker.py
│
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_embeddings.py
    ├── test_archive.py
    └── test_connections.py
```

### packages/ (공유 패키지)

```
packages/
├── shared/
│   ├── package.json
│   ├── tsconfig.json
│   └── src/
│       ├── index.ts
│       ├── types/
│       │   ├── capture.ts
│       │   ├── diary.ts
│       │   └── user.ts
│       ├── utils/
│       │   ├── dateUtils.ts
│       │   └── formatters.ts
│       └── constants/
│           ├── moodColors.ts
│           └── apiEndpoints.ts
│
├── ui/
│   ├── package.json
│   ├── tsconfig.json
│   ├── tamagui.config.ts
│   └── src/
│       ├── index.ts
│       ├── Button.tsx
│       ├── Card.tsx
│       ├── Input.tsx
│       └── themes/
│           ├── light.ts
│           └── dark.ts
│
├── hooks/
│   ├── package.json
│   ├── tsconfig.json
│   └── src/
│       ├── index.ts
│       ├── useDebounce.ts
│       ├── useLocalStorage.ts
│       └── useSupabaseRealtime.ts
│
└── test-utils/                     # Party Mode에서 추가
    ├── package.json
    ├── tsconfig.json
    └── src/
        ├── fixtures/
        │   ├── captureFixtures.ts
        │   └── userFixtures.ts
        ├── mocks/
        │   ├── supabaseMock.ts
        │   └── apiMock.ts
        └── factories/
            └── captureFactory.ts
```

### supabase/ (Supabase 설정)

```
supabase/
├── config.toml
├── seed.sql
├── migrations/
│   ├── 20260110_001_init_users.sql
│   ├── 20260110_002_init_captures.sql
│   ├── 20260110_003_init_diary_entries.sql
│   ├── 20260110_004_init_connections.sql
│   └── 20260110_005_init_rls_policies.sql
│
└── functions/                      # Edge Functions (TypeScript)
    ├── daily-digest/
    │   └── index.ts                # Cron: 일일 다이제스트 알림
    └── webhook-handler/
        └── index.ts                # 웹훅 처리
```

### Architectural Boundaries

#### API Boundaries

| 경계 | 소스 → 타겟 | 통신 방식 | 인증 |
|------|------------|----------|------|
| 클라이언트 → Supabase | Mobile/Web/Extension | PostgREST + Realtime | Supabase Auth JWT |
| 클라이언트 → FastAPI | Mobile/Web/Extension | REST | Supabase JWT 검증 |
| FastAPI → Supabase | Railway | Service Role Key | Service Role |
| FastAPI → R2 | Railway | S3 API | API Key |

#### Edge Function vs FastAPI 기준 (Party Mode에서 추가)

| 용도 | 선택 | 이유 |
|------|------|------|
| 웹훅 처리 | Edge Function | 빠른 응답, 가벼움 |
| Cron Job (일일 집계) | Edge Function | Supabase 네이티브 |
| 임베딩 생성 | FastAPI | Sentence-BERT 필요 |
| WACZ 아카이빙 | FastAPI | Playwright, 무거운 처리 |
| GraphRAG 쿼리 | FastAPI | LlamaIndex 필요 |

#### Data Boundaries

| 데이터 | 저장소 | 접근 패턴 |
|--------|--------|----------|
| 사용자 데이터 | Supabase Postgres | RLS 보호 |
| 캡처 메타데이터 | Supabase Postgres | RLS 보호 |
| 임베딩 벡터 | Supabase Postgres (pgvector) | FastAPI 작성, 클라이언트 읽기 |
| WACZ 파일 | Cloudflare R2 | FastAPI 작성, 클라이언트 읽기 |
| 로컬 캡처 (Local-only) | SQLite (SQLCipher) | 클라이언트 전용 |

### Requirements to Structure Mapping

#### Epic → Directory Mapping

| Epic | Primary Directory | Key Files |
|------|-------------------|-----------|
| **EP-CAPTURE** | `apps/mobile/src/features/capture/` | `CaptureCard.tsx`, `ShareExtensionHandler.tsx` |
| **EP-CAPTURE** | `apps/extension/src/popup/` | `Popup.tsx` |
| **EP-CAPTURE** | `apps/api/app/routers/archive.py` | WACZ 아카이빙 API |
| **EP-GRAPH** | `apps/api/app/services/graph_service.py` | LlamaIndex GraphRAG |
| **EP-JOURNAL** | `apps/mobile/src/features/diary/` | `DiaryEditor.tsx` |
| **EP-SEARCH** | `apps/mobile/src/features/search/` | `SearchBar.tsx` |
| **EP-ANALYTICS** | `supabase/functions/daily-digest/` | 일일 다이제스트 |

#### Cross-Cutting Concerns

| Concern | Location |
|---------|----------|
| 인증 | `apps/*/src/features/auth/`, `apps/api/app/utils/auth.py` |
| 에러 처리 | `packages/shared/src/utils/errors.ts`, `apps/api/app/middleware/` |
| 로깅 | Sentry 통합 (각 앱) |
| 상태 관리 | `apps/*/src/stores/` |

### Environment Variables Strategy (Party Mode에서 추가)

#### 공통 환경변수 (.env.common)

```bash
# .env.common - 모든 앱에서 공유
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=eyJhbGc...
SENTRY_DSN=https://xxx@sentry.io/xxx
AMPLITUDE_API_KEY=xxx
```

#### 앱별 환경변수

```bash
# apps/mobile/.env.local
EXPO_PUBLIC_API_URL=https://api.moments.app

# apps/web/.env.local
NEXT_PUBLIC_API_URL=https://api.moments.app

# apps/api/.env
SUPABASE_SERVICE_ROLE_KEY=eyJhbGc...
R2_ACCESS_KEY_ID=xxx
R2_SECRET_ACCESS_KEY=xxx
```

### Future Scaling Considerations (Party Mode에서 추가)

#### Worker 분리 시나리오

**현재 (MVP):**
```
apps/api/
└── app/workers/archive_worker.py  # FastAPI 내부
```

**스케일링 시:**
```
apps/
├── api/                           # API 서버
└── workers/                       # 별도 서비스
    ├── archive/
    │   └── Dockerfile
    └── embedding/
        └── Dockerfile
```

**분리 조건:**
- WACZ 아카이빙 큐가 5분 이상 지연될 때
- 임베딩 처리가 API 응답 시간에 영향을 줄 때
- 월 비용이 $100 초과 시 (비용 최적화)

---

## Architecture Validation Results

Step 7에서 수행된 아키텍처 검증 결과입니다.

### Coherence Validation ✅

#### Decision Compatibility
모든 기술 스택이 상호 호환됩니다:
- React Native (Expo SDK 54) + Tamagui + Supabase JS SDK: ✅ 호환
- Next.js 15/16 + TanStack Query + Vercel: ✅ 호환
- FastAPI + LlamaIndex + Sentence-Transformers: ✅ Python 네이티브 호환
- Supabase (pgvector, Realtime, Auth) + Railway: ✅ 호환
- Turborepo Monorepo + pnpm workspace: ✅ 호환

#### Pattern Consistency
모든 구현 패턴이 기술 스택과 정합합니다:
- 네이밍 규칙 (snake_case → camelCase 변환): ✅ Pydantic alias로 구현
- 프로젝트 구조 (Feature-based, Co-located 테스트): ✅ 모든 앱에 적용
- 상태 관리 (Zustand + TanStack Query): ✅ 모바일/웹 동일 패턴
- 에러 처리 (RFC 7807): ✅ FastAPI + 클라이언트 동일 포맷

#### Structure Alignment
프로젝트 구조가 모든 아키텍처 결정을 지원합니다:
- apps/ 폴더: Mobile, Web, API, Extension 분리 ✅
- packages/ 폴더: shared, ui, hooks, test-utils 공유 ✅
- supabase/ 폴더: migrations, functions 관리 ✅
- tests/ 폴더: 통합 E2E 테스트 ✅

### Requirements Coverage Validation ✅

#### Epic/Feature Coverage

| Epic | 아키텍처 지원 | 검증 결과 |
|------|-------------|----------|
| **EP-CAPTURE** | Mobile Share Extension, Chrome Extension, FastAPI Archive | ✅ 완전 지원 |
| **EP-GRAPH** | FastAPI GraphRAG, Supabase pgvector | ✅ 완전 지원 |
| **EP-JOURNAL** | Mobile DiaryEditor, Supabase Realtime | ✅ 완전 지원 |
| **EP-SEARCH** | Supabase Full-text + pgvector | ✅ 완전 지원 |
| **EP-ANALYTICS** | Supabase Edge Functions, Amplitude | ✅ 완전 지원 |

#### Non-Functional Requirements Coverage

| NFR | 아키텍처 해결책 | 검증 결과 |
|-----|--------------|----------|
| **2초 캡처** | AD-01: Decoupled Architecture | ✅ 클라이언트 즉시 응답, 서버 비동기 처리 |
| **Local-only 모드** | SEC-03: SQLCipher + 생체인증 | ✅ 완전 오프라인 지원 |
| **E2E 암호화** | SEC-03: 클라이언트 측 키 관리 | ✅ 선택적 암호화 가능 |
| **99.5% 가용성** | Supabase + Railway SLA | ✅ 플랫폼 SLA 보장 |
| **LazyGraphRAG 비용 절감** | AD-04: 첫 재방문 시 임베딩 | ✅ 70-90% 비용 절감 |

### Implementation Readiness Validation ✅

#### Decision Completeness

| 항목 | 상태 | 비고 |
|------|------|------|
| 기술 스택 선택 | ✅ 완료 | 모든 기술 스택 확정 |
| 버전 명시 | ✅ 완료 | 2026-01 기준 최신 버전 명시 |
| 패턴 문서화 | ✅ 완료 | 예시 코드 포함 |
| 프로젝트 구조 | ✅ 완료 | 파일/폴더 레벨까지 정의 |

#### Structure Completeness

| 항목 | 상태 | 비고 |
|------|------|------|
| 루트 구성 | ✅ 완료 | Turborepo, CI/CD, .env 전략 |
| 앱별 구조 | ✅ 완료 | Mobile, Web, API, Extension |
| 공유 패키지 | ✅ 완료 | shared, ui, hooks, test-utils |
| Supabase 구조 | ✅ 완료 | migrations, functions |

#### Pattern Completeness

| 항목 | 상태 | 비고 |
|------|------|------|
| 네이밍 패턴 | ✅ 완료 | DB, API, 코드 모두 정의 |
| 구조 패턴 | ✅ 완료 | Feature-based, Co-located |
| 포맷 패턴 | ✅ 완료 | 변환 규칙 + Pydantic 예시 |
| 검증 자동화 | ✅ 완료 | ESLint, Prettier, CI |

### Gap Analysis Results

**Critical Gaps**: 없음 ✅

**Important Gaps**: 없음 ✅

**Nice-to-Have (향후 개선 가능)**:
| 항목 | 설명 | 우선순위 |
|------|------|---------|
| API 버전 관리 | `/v1/` 이후 버전 전환 전략 | 🟢 낮음 (Phase 2+) |
| 캐싱 전략 | Redis 도입 시 패턴 정의 | 🟢 낮음 (스케일링 시) |
| 멀티 리전 | 글로벌 배포 전략 | 🟢 낮음 (Phase 3+) |

### Architecture Completeness Checklist

**✅ Requirements Analysis (Step 2)**
- [x] 프로젝트 문맥 분석 완료
- [x] 규모 및 복잡도 평가 (Medium-High)
- [x] 기술 제약 식별
- [x] 교차 관심사 매핑

**✅ Technology Stack (Step 3)**
- [x] 모바일: React Native + Expo SDK 54
- [x] 웹: Next.js 15/16
- [x] 백엔드: Python FastAPI 0.128.x
- [x] BaaS: Supabase + Railway
- [x] 스토리지: Cloudflare R2
- [x] 모든 버전 명시 완료

**✅ Core Decisions (Step 4)**
- [x] 데이터 아키텍처 (Hybrid, Pydantic, Supabase Migrations)
- [x] 인증 & 보안 (Supabase Auth, SQLCipher, RLS)
- [x] API & 통신 (PostgREST + FastAPI, Realtime)
- [x] 프론트엔드 (Zustand, TanStack Query, Tamagui)
- [x] 인프라 (GitHub Actions, Sentry, Amplitude)

**✅ Implementation Patterns (Step 5)**
- [x] 네이밍 규칙 확립
- [x] 구조 패턴 정의
- [x] 포맷 패턴 명시
- [x] 자동 검증 도구 설정

**✅ Project Structure (Step 6)**
- [x] 완전한 디렉토리 구조 정의
- [x] 컴포넌트 경계 확립
- [x] 통합 포인트 매핑
- [x] Epic → 구조 매핑 완료

### Architecture Readiness Assessment

| 항목 | 상태 |
|------|------|
| **전체 상태** | ✅ **구현 준비 완료 (READY FOR IMPLEMENTATION)** |
| **확신 수준** | 🟢 **높음 (High)** |

**핵심 강점:**
1. **Party Mode 강화**: 개발, 테스트, 보안 관점의 다각적 검토 완료
2. **AI 에이전트 친화적**: 명확한 패턴과 예시로 일관된 구현 가능
3. **확장성 고려**: 향후 Worker 분리, 스케일링 시나리오 문서화
4. **1인 개발자 최적화**: 관리 부담 최소화, BaaS 활용
5. **기술 버전 명시**: 모든 기술 스택의 구체적 버전 확정

**향후 개선 영역:**
- API 버전 관리 전략 (Phase 2+)
- Redis 캐싱 도입 (스케일링 시)
- 멀티 리전 배포 (Phase 3+)

### Implementation Handoff

**AI Agent Guidelines:**
1. 이 아키텍처 문서를 모든 구현의 기준으로 사용
2. 구현 패턴을 일관되게 적용 (네이밍, 구조, 포맷)
3. 프로젝트 구조와 경계를 준수
4. 의문 사항 발생 시 이 문서 참조

**First Implementation Priority:**
```bash
# 1. Monorepo 초기화
npx create-turbo@latest moments --package-manager pnpm

# 2. Supabase 프로젝트 생성
supabase init

# 3. 앱 스캐폴딩
cd apps && npx create-expo-app@latest mobile --template tabs
cd apps && npx create-next-app@latest web --typescript --tailwind --eslint --app
cd apps && mkdir api && cd api && pip install fastapi uvicorn

# 4. 공유 패키지 설정
cd packages && mkdir shared ui hooks test-utils
```

---

**아키텍처 문서 작성 완료**: 2026-01-10T16:50:00+09:00
**작성자**: Winston (Architect) with Party Mode Contributors
