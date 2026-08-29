---
stepsCompleted: [1, 2, 3, 4]
inputDocuments:
  - "docs/plans/planning-artifacts/prd.md"
  - "docs/plans/planning-artifacts/architecture.md"
  - "docs/plans/planning-artifacts/ux-design-specification.md"
workflowType: 'epics-and-stories'
project_name: 'Moments: Mind Studio'
user_name: '마스터'
date: '2026-01-17T13:30:00+09:00'
---

# Moments: Mind Studio - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for Moments: Mind Studio, decomposing the requirements from the PRD, UX Design, and Architecture into implementable stories.

## Requirements Inventory

### Functional Requirements

**캡처 기능 (Capture)**
- FR1: 2초 이내 캡처 완료 - Share Extension(iOS/Android) 및 브라우저 공유하기로 URL 캡처
- FR2: Ghost Memo - 캡처 시 선택적 한 줄 메모 추가
- FR3: 무드 컬러 각인 - 5가지 감정 컬러 선택

**영구 박제 (Permanent Archive)**
- FR4: WACZ 기반 웹페이지 완전 박제 - 링크 깨짐 없이 영구 보존
- FR5: 아카이브 상태 투명 표시 - "저장됨 → 아카이빙 중 → 영구 보관됨" 상태 전환
- FR6: Graceful Degradation - WACZ 실패 시 URL + 텍스트 스냅샷 보존

**자동 연결 (Automatic Linking)**
- FR7: 시맨틱 그래프 자동 생성 - AI가 지식 간 연결 자동 생성
- FR8: LazyGraphRAG - 첫 재방문/일기 작성 시에만 임베딩 생성 (비용 최적화)
- FR9: 자동 연결 피드백 - "도움됨/도움안됨" 버튼으로 정확도 측정

**일기 루틴 (Daily Reflection)**
- FR10: 밤 9시 푸시 알림 - "오늘의 조각들이 도착했습니다"
- FR11: Daily Journal View - 오늘 수집한 카드 리스트 확인 및 검토
- FR12: 일기 작성 - 오늘의 감정/한줄평 남기기
- FR13: 일기 피드백 - "성찰에 도움됨" 버튼

**검색 기능 (Search)**
- FR14: 키워드 검색 - 텍스트 기반 검색
- FR15: 타임라인 뷰 - 시간순 정렬
- FR16: 무드별 필터 - 감정 컬러 기반 필터링

**입소문 기능 (Viral)**
- FR17: Referral 링크 생성 - "이 앱 추천하기" 기능
- FR18: 가입 시 설문 - "어떻게 알게 되셨나요?"

**인증 (Authentication)**
- FR19: OAuth 2.0 로그인 - Google, Apple
- FR20: Local-only 모드 - 생체인증(FaceID/TouchID) + SQLCipher 암호화
- FR21: E2E 암호화 옵션 - 클라이언트 측 키 관리

### Non-Functional Requirements

**성능**
- NFR1: 캡처 응답 시간 < 2초 (사용자 체감)
- NFR2: API 응답 시간 p95 < 1초
- NFR3: 그래프 쿼리 응답 < 500ms

**안정성**
- NFR4: 서비스 가용성 > 99.5%
- NFR5: 캡처 성공률 > 95%
- NFR6: 모바일 앱 크래시율 < 0.5%

**확장성**
- NFR7: 동시 접속자 500명 (MVP)
- NFR8: 사용자당 저장 용량 500MB 지원

**보안**
- NFR9: E2E 암호화 옵션 제공
- NFR10: GDPR/개인정보보호법 준수
- NFR11: 보안 취약점 0건 (critical/high)

**비용**
- NFR12: LazyGraphRAG로 LLM 비용 70-90% 절감

### Additional Requirements

**Architecture 기반**
- AR1: Supabase + Railway 하이브리드 배포 (AD-01~04 결정사항)
- AR2: Dual-mode Data Architecture - Cloud Sync / Local-only 별도 플로우
- AR3: Decoupled Capture - 클라이언트 URL+메타데이터만 전송, 서버 비동기 WACZ 처리
- AR4: Monorepo 구조 (Turborepo) - apps/mobile, apps/web, apps/api, packages/shared
- AR5: Tamagui 컴포넌트 시스템 - React Native + Web 공유
- AR6: TanStack Query + Zustand 상태 관리
- AR7: PostgreSQL + pgvector (Phase 0-1), Neo4j 마이그레이션 (Phase 1.5+)

**UX Design 기반**
- UX1: Warm Archive 테마 - #8C5E45 Primary, #F7F5F0 Background
- UX2: Hybrid Modern Stack 레이아웃 - Home(피드), Library(그리드), Journal(타임라인)
- UX3: FragmentCard 커스텀 컴포넌트 - 썸네일, 제목, 요약, 감정 컬러
- UX4: MoodPicker 커스텀 컴포넌트 - 5가지 무드 컬러 원형 버튼
- UX5: "현상 중" 로딩 애니메이션 - 흐릿→선명 전환
- UX6: 반응형 디자인 - Mobile Bottom Nav ↔ Desktop Sidebar
- UX7: 다크 모드 - "밤의 서재" 컨셉

**테스트 전략**
- TEST1: Phase 0 Go/No-Go - 10개 사이트 E2E 성능 벤치마크
- TEST2: Dual-path Testing - Cloud Sync / Local-only 별도 테스트 경로

### FR Coverage Map

| FR | Epic | 설명 |
|----|------|------|
| FR1 | Epic 2 | 2초 캡처 |
| FR2 | Epic 2 | Ghost Memo |
| FR3 | Epic 2 | 무드 컬러 |
| FR4 | Epic 2 | WACZ 영구 박제 |
| FR5 | Epic 2 | 아카이브 상태 표시 |
| FR6 | Epic 2 | Graceful Degradation |
| FR7 | Epic 3 | 시맨틱 그래프 자동 생성 |
| FR8 | Epic 3 | LazyGraphRAG |
| FR9 | Epic 3 | 자동 연결 피드백 |
| FR10 | Epic 4 | 밤 9시 푸시 알림 |
| FR11 | Epic 4 | Daily Journal View |
| FR12 | Epic 4 | 일기 작성 |
| FR13 | Epic 4 | 일기 피드백 |
| FR14 | Epic 5 | 키워드 검색 |
| FR15 | Epic 5 | 타임라인 뷰 |
| FR16 | Epic 5 | 무드별 필터 |
| FR17 | Epic 6 | Referral 링크 |
| FR18 | Epic 6 | 가입 설문 |
| FR19 | Epic 1 | OAuth 로그인 |
| FR20 | Epic 1 | Local-only 모드 + 로컬 암호화 |
| FR21 | Epic 1 | E2E 암호화 |

## Epic List

### Epic 1: 안전한 시작과 프라이버시 모드
사용자가 로그인 또는 Local-only 모드를 선택하고 신뢰할 수 있는 출발점을 확보

**User Outcome**: Google/Apple 로그인 또는 Local-only 모드로 프라이버시를 보장받으며 사용 시작
**FRs covered**: FR19, FR20, FR21
**Implementation Notes**: Expo/Next.js/FastAPI 스타터 기반 초기화 (Architecture starter template)

---

### Epic 2: 2초 캡처와 영구 보존
사용자가 어디서든 2초 내에 URL을 캡처하고, 감정/메모를 더해 영구 보존

**User Outcome**: 빠르게 저장하고 링크가 깨져도 원본 그대로 열람 가능
**FRs covered**: FR1, FR2, FR3, FR4, FR5, FR6

---

### Epic 3: 지식 자동 연결과 품질 피드백
AI가 지식 간 연결을 자동 생성하고 사용자 피드백으로 품질 개선

**User Outcome**: 태그나 폴더 없이도 관련 지식이 자동 연결됨
**FRs covered**: FR7, FR8, FR9

---

### Epic 4: 밤 9시 회고 루틴
하루 지식을 회고하고 감정/생각을 기록하는 루틴 제공

**User Outcome**: 매일 밤 "오늘의 조각들"을 확인하고 일기로 정리
**FRs covered**: FR10, FR11, FR12, FR13

---

### Epic 5: 검색과 재발견
키워드/타임라인/무드로 과거 지식을 쉽게 찾아 재발견

**User Outcome**: 잊고 있던 지식을 쉽게 찾고 연결된 맥락을 확인
**FRs covered**: FR14, FR15, FR16

---

### Epic 6: 입소문 루프
추천과 가입 경로 추적으로 성장 루프를 만든다

**User Outcome**: Referral로 친구 초대, 가입 경로 분석을 통한 성장 최적화
**FRs covered**: FR17, FR18

---

## Epic Dependencies

```
Epic 1 (안전한 시작) ────────────────┐
    │                               │
    ▼                               │
Epic 2 (캡처/보존)                  │
    │                               │
    ├──────────────┬───────────────┐
    ▼              ▼               ▼
Epic 3 (자동 연결) Epic 4 (회고)  Epic 5 (검색)
                                        │
                                        ▼
                              Epic 6 (입소문)
```

## Implementation Priority

| 우선순위 | Epic | 이유 |
|----------|------|------|
| Critical | Epic 1 | 사용자 진입점 및 신뢰 기반 |
| Critical | Epic 2 | 핵심 가치 (2초 캡처 + 영구 보존) |
| High | Epic 4 | North Star (회고 루틴) |
| High | Epic 3 | 차별화 요소 (자동 연결) |
| Medium | Epic 5 | 재발견 경험 |
| Medium | Epic 6 | 성장 루프 |

---

## Stories

### Epic 1: 안전한 시작과 프라이버시 모드

#### Story 1.1: 스타터 템플릿 기반 프로젝트 세팅
As a 개발자,
I want 모바일/웹/백엔드를 스타터 템플릿으로 초기화하기를,
So that 표준 구조와 의존성이 빠르게 준비된다.

**Acceptance Criteria:**
**Given** 신규 프로젝트를 시작할 때
**When** Expo, Next.js, FastAPI 스타터를 적용하면
**Then** apps/mobile, apps/web, apps/api 구조가 생성된다
**And** 기본 빌드/실행이 성공한다
**And** 공통 환경 변수 템플릿이 준비된다

#### Story 1.2: OAuth 로그인 (Google/Apple)
As a 사용자,
I want Google/Apple 계정으로 로그인하기를,
So that 별도 회원가입 없이 빠르게 서비스를 시작할 수 있다.

**Acceptance Criteria:**
**Given** 로그인 화면이 표시되었을 때
**When** 사용자가 "Google로 계속하기" 또는 "Apple로 계속하기"를 선택하면
**Then** 해당 OAuth 플로우가 시작된다
**And** 인증 성공 시 홈 화면으로 이동하고 사용자 프로필(이름, 이메일, 아바타)이 저장된다

### Story 1.3: Local-only 모드 선택
As a 프라이버시 중시 사용자,
I want 클라우드 동기화 없이 로컬에서만 사용하기를,
So that 내 데이터가 내 기기에만 저장되도록 보장할 수 있다.

**Acceptance Criteria:**
**Given** 온보딩 중 모드 선택 화면이 표시되었을 때
**When** 사용자가 "Local-only (오프라인)" 옵션을 선택하면
**Then** 클라우드 기능이 비활성화된다
**And** 데이터는 로컬 저장소에만 저장된다
**And** 앱 상단에 "로컬 모드" 인디케이터가 표시된다

### Story 1.4: 로컬 데이터 암호화 (SQLCipher)
As a Local-only 사용자,
I want 로컬 데이터베이스가 암호화되기를,
So that 기기 분실 시에도 데이터가 안전하다.

**Acceptance Criteria:**
**Given** Local-only 모드가 활성화되었을 때
**When** 로컬에 데이터가 저장되면
**Then** SQLCipher로 암호화되어 저장된다
**And** 앱 외부에서 DB 파일을 열 수 없다
**And** 암호화 키는 Keychain/Keystore에 안전하게 저장된다

### Story 1.5: E2E 암호화 옵션
As a 보안 중시 사용자,
I want 클라우드에 저장되는 데이터도 암호화되기를,
So that 서버가 해킹되어도 내 데이터가 안전하다.

**Acceptance Criteria:**
**Given** Cloud 모드에서 E2E 암호화가 활성화되었을 때
**When** 데이터가 서버로 전송되면
**Then** 클라이언트에서 암호화된 상태로 전송된다
**And** 서버는 암호화된 데이터만 저장한다
**And** 복호화 키는 사용자만 보유한다

### Epic 2: 2초 캡처와 영구 보존

#### Story 2.1: 2초 URL 캡처
As a 사용자,
I want 공유하기나 붙여넣기로 URL을 즉시 캡처하기를,
So that 흐름을 끊지 않고 빠르게 저장할 수 있다.

**Acceptance Criteria:**
**Given** 외부 앱/브라우저에서 공유하기를 실행했을 때
**When** Moments를 선택하거나 URL을 붙여넣으면
**Then** 2초 이내에 캡처가 완료된다
**And** URL과 페이지 제목이 자동으로 저장된다

#### Story 2.2: Ghost Memo와 무드 컬러
As a 사용자,
I want 캡처 시 한 줄 메모와 무드 컬러를 남기기를,
So that 나중에 저장 의도와 감정을 기억할 수 있다.

**Acceptance Criteria:**
**Given** 캡처 화면이 열렸을 때
**When** 사용자가 메모를 입력하고 무드 컬러를 선택하면
**Then** 메모는 최대 100자까지 저장된다
**And** 5가지 무드 컬러 중 하나를 선택할 수 있다
**And** 메모와 무드가 캡처 카드에 표시된다

#### Story 2.3: WACZ 영구 보존과 상태 표시
As a 사용자,
I want 캡처한 페이지가 WACZ로 영구 보존되고 상태가 표시되기를,
So that 링크가 깨져도 원본을 신뢰할 수 있다.

**Acceptance Criteria:**
**Given** URL이 캡처되었을 때
**When** 아카이빙이 진행되면
**Then** WACZ로 영구 보존된다
**And** 상태가 "저장됨 → 아카이빙 중 → 영구 보관됨"으로 표시된다
**And** 아카이브 완료 후 원본 페이지를 열람할 수 있다

#### Story 2.4: Graceful Degradation 폴백
As a 사용자,
I want WACZ 아카이빙 실패 시에도 기본 정보가 보존되기를,
So that 어떤 상황에서도 지식이 손실되지 않는다.

**Acceptance Criteria:**
**Given** WACZ 아카이빙이 실패했을 때
**When** 실패가 감지되면
**Then** URL, 제목, 메타데이터가 보존된다
**And** 가능한 경우 텍스트 스냅샷이 저장된다
**And** "기본 저장됨" 상태가 표시된다

#### Story 2.5: 캡처 상태 실시간 표시
As a 사용자,
I want 아카이브 상태 변화를 실시간으로 확인하기를,
So that 내 지식이 안전하게 보존되고 있음을 알 수 있다.

**Acceptance Criteria:**
**Given** 캡처 카드가 표시되었을 때
**When** 아카이빙 진행 상태가 변경되면
**Then** "저장됨 → 아카이빙 중 → 영구 보관됨" 상태가 즉시 갱신된다
**And** 완료 상태는 시각적으로 확인 가능하다

### Epic 3: 지식 자동 연결과 품질 피드백

#### Story 3.1: 시맨틱 자동 연결 생성
As a 사용자,
I want 캡처된 지식이 자동으로 연결되기를,
So that 태그 없이도 관련 지식을 발견할 수 있다.

**Acceptance Criteria:**
**Given** 여러 Fragment가 저장되어 있을 때
**When** 연결 계산이 실행되면
**Then** 유사도 기준으로 관련 Fragment가 연결된다
**And** 연결 결과가 상세 화면에 표시된다

#### Story 3.2: LazyGraphRAG 임베딩 지연
As a 시스템,
I want 첫 재방문 시에만 임베딩을 생성하기를,
So that LLM 비용을 크게 절감할 수 있다.

**Acceptance Criteria:**
**Given** 새로운 Fragment가 캡처되었을 때
**When** 사용자가 해당 Fragment를 처음 재방문하면
**Then** 임베딩이 생성되고 저장된다
**And** 재방문 전에는 임베딩을 생성하지 않는다

#### Story 3.3: 자동 연결 피드백
As a 사용자,
I want 자동 연결 결과에 피드백을 남기기를,
So that 추천 정확도가 개선된다.

**Acceptance Criteria:**
**Given** 연결된 지식이 표시되었을 때
**When** 사용자가 "도움됨" 또는 "도움안됨"을 선택하면
**Then** 피드백이 기록된다
**And** 연결 품질이 다음 추천에 반영된다

### Epic 4: 밤 9시 회고 루틴

#### Story 4.1: 밤 9시 푸시 알림
As a 사용자,
I want 밤 9시에 회고 알림을 받기를,
So that 하루 지식을 정리할 타이밍을 놓치지 않는다.

**Acceptance Criteria:**
**Given** 오늘 1개 이상의 Fragment를 캡처했을 때
**When** 밤 9시가 되면
**Then** "오늘의 조각들이 도착했습니다" 알림이 발송된다
**And** 알림을 탭하면 Journal 화면이 열린다

#### Story 4.2: 오늘의 카드 리스트
As a 사용자,
I want 오늘 수집한 카드들을 한눈에 보기를,
So that 하루 동안 무엇을 배웠는지 확인할 수 있다.

**Acceptance Criteria:**
**Given** Journal 화면이 열렸을 때
**When** 오늘 날짜가 선택되면
**Then** 오늘 캡처된 Fragment들이 시간순으로 표시된다
**And** 빈 날에는 안내 메시지가 표시된다

#### Story 4.3: 일기 작성
As a 사용자,
I want 오늘의 감정과 생각을 기록하기를,
So that 나만의 의미를 남길 수 있다.

**Acceptance Criteria:**
**Given** 오늘의 카드 리스트가 표시될 때
**When** 사용자가 일기 작성 화면을 열어 저장하면
**Then** 텍스트와 무드가 오늘 날짜에 연결된다
**And** 이후 다시 조회할 수 있다

#### Story 4.4: 일기 피드백
As a 사용자,
I want 일기 작성 후 짧은 피드백을 남기기를,
So that 회고 루틴의 가치를 측정할 수 있다.

**Acceptance Criteria:**
**Given** 일기 저장이 완료되었을 때
**When** 사용자가 "성찰에 도움됨" 여부를 선택하면
**Then** 응답이 기록된다
**And** 분석 이벤트로 집계된다

### Epic 5: 검색과 재발견

#### Story 5.1: 키워드 검색
As a 사용자,
I want 키워드로 지식을 검색하기를,
So that 기억나는 단어로 빠르게 찾을 수 있다.

**Acceptance Criteria:**
**Given** 검색 화면이 열렸을 때
**When** 검색어를 입력하면
**Then** 제목, 메모, 본문에서 매칭되는 결과가 표시된다
**And** 결과가 관련도순으로 정렬된다

#### Story 5.2: 타임라인 뷰
As a 사용자,
I want 시간순으로 지식을 탐색하기를,
So that 언제 무엇을 수집했는지 기억을 더듬을 수 있다.

**Acceptance Criteria:**
**Given** Library 탭에서 타임라인 뷰를 선택했을 때
**When** 스크롤하면
**Then** Fragment들이 날짜별로 그룹화되어 표시된다
**And** 과거 데이터가 추가로 로드된다

#### Story 5.3: 무드별 필터
As a 사용자,
I want 감정별로 지식을 필터링하기를,
So that 특정 기분일 때 수집한 것들을 모아볼 수 있다.

**Acceptance Criteria:**
**Given** 무드 필터가 표시될 때
**When** 특정 무드를 선택하면
**Then** 해당 무드가 태그된 Fragment만 표시된다
**And** 필터 해제 시 전체가 다시 표시된다

### Epic 6: 입소문 루프

#### Story 6.1: Referral 링크 생성
As a 사용자,
I want 친구에게 공유할 수 있는 초대 링크를 생성하기를,
So that 내가 좋아하는 앱을 쉽게 추천할 수 있다.

**Acceptance Criteria:**
**Given** "친구 초대" 메뉴가 있을 때
**When** "초대 링크 만들기"를 선택하면
**Then** 고유한 Referral 링크가 생성된다
**And** 공유 시트로 바로 공유할 수 있다

#### Story 6.2: 유입 경로 설문
As a PM,
I want 신규 사용자의 유입 경로를 수집하기를,
So that 효과적인 마케팅 채널을 식별할 수 있다.

**Acceptance Criteria:**
**Given** 신규 사용자가 가입을 완료했을 때
**When** 온보딩 중 설문이 표시되면
**Then** "어떻게 알게 되셨나요?" 질문이 제공된다
**And** 선택지가 기록되어 분석 이벤트로 저장된다
