# UX Design Specification - Moments: Mind Studio

**Project:** Moments: Mind Studio
**Date:** 2026-01-12 (복구)
**Version:** 1.1

---

## Executive Summary

### Project Vision

Moments: Mind Studio는 **"Digital Darkroom (디지털 암실)"** 컨셉의 지식 사진관입니다. 사용자가 저장한 정보들이 마치 필름처럼 서서히 현상되어 의미 있는 지식으로 연결되고, 자신의 관심사와 삶의 궤적을 되돌아볼 수 있는 **자아 회복 솔루션**입니다.

### Design Philosophy

> **"Developing Thoughts" (생각을 현상하다)**

- 미정리 상태 = "가능성의 상태", "현상 대기 중인 필름"으로 긍정적 재정의
- AI는 조용한 조수: 설명 없는 자동화 금지, 반드시 근거(키워드) 노출 및 사용자 수정 가능
- 정보 시각화: 텍스트 링크 대신 비주얼 카드 군집으로 연관성 표현

### Target Users

**Primary Persona:**
- 지식을 사랑하지만 정리에 지친 현대인
- 정보 수집을 즐기지만 정리할 시간과 에너지가 부족
- 바쁜 일상 속에서 '나'를 잃어가고 있다는 막연한 불안감

**Key Personas from PRD:**
- 이지훈 (32세 PM): 정보 과부하, 일과 삶 균형 재발견
- 마커스 첸 (35세 Architect): 회의론자, Anti-productivity 전환
- Dr. Yuki Tanaka (42세 Psychiatrist): 프라이버시 극도로 민감

### Design Challenges

1. **2초 캡처 UX**: 복잡한 백엔드 처리(WACZ, 임베딩)를 사용자에게 투명하게
2. **제로 프릭션 정리**: 폴더/태그 없이 자동 연결의 신뢰감 구축
3. **Deep Space 테마**: 어두운 배경에서의 가독성과 접근성
4. **Mobile-Desktop 동등 비중**: 캡처는 모바일, 성찰은 데스크톱 모두 중요

---

## Core User Experience

### Primary Actions

**"Capture & Connect"** - 두 가지 핵심 행동:

1. **Capture (캡처)**: 2초 안에 완료, 방해 없이 흐름 유지
2. **Connect (연결)**: AI가 자동으로 맥락 연결, 사용자는 발견의 기쁨만

### Platform Strategy

| Platform | Primary Use Cases | Priority |
|----------|-------------------|----------|
| **Mobile (iOS/Android)** | 캡처, 일기 작성, 빠른 검색 | ⭐⭐⭐⭐⭐ |
| **Desktop (Web)** | 그래프 탐색, 깊은 성찰, 장문 일기 | ⭐⭐⭐⭐⭐ |
| **Browser Extension** | 데스크톱 캡처 | ⭐⭐⭐⭐ |

**동등 비중 원칙**: Mobile-First이지만 Desktop 경험도 동등하게 중요

### Signature Interaction: "The Spark of Insight"

**시그니처 인터랙션** - 자동 연결이 발견될 때의 시각적 피드백:

1. **Magnetic Pull**: 관련 카드들이 자석처럼 서로 끌려옴
2. **Glow Effect**: 연결된 카드들이 부드럽게 빛남
3. **Spark Animation**: 연결선이 형성될 때 작은 불꽃 효과
4. **Soft Sound**: 선택적 효과음 (설정에서 끄기 가능)

```
[Card A] ~~~spark~~~ [Card B]
    \                  /
     \    ✨glow✨    /
      \              /
       [Connection]
```

---

## Design System Foundation

### Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Framework** | Next.js 15+ (App Router) | Web Application |
| **UI Components** | Shadcn UI | Accessible, Customizable Components |
| **Styling** | Tailwind CSS | Utility-first CSS |
| **Animation** | Framer Motion | Smooth Transitions, Morphing |
| **Icons** | Lucide React | Consistent Icon Set |
| **Cross-platform** | Tamagui | React Native + Web 공유 컴포넌트 |

### Why This Stack

1. **Shadcn UI**: Radix primitives 기반, 완전한 커스터마이징 가능, 접근성 내장
2. **Framer Motion**: `layoutId`로 MorphingCard 구현, GPU 가속
3. **Tailwind**: 1인 개발자에게 최적, Design Token 관리 용이
4. **Lucide**: Shadcn과 완벽 호환, 일관된 아이콘 스타일

---

## Visual Design Foundation

### Color System: Deep Space Theme

**Core Philosophy**: 우주 공간에서 지식이 별처럼 빛나는 경험

#### Background Colors (배경)

| Token | Hex | Usage |
|-------|-----|-------|
| `bg-void` | `#0a0a0f` | 최심층 배경 (그래프 캔버스) |
| `bg-space` | `#0f172a` | 기본 배경 (Slate-900) |
| `bg-nebula` | `#1e293b` | 카드 배경 (Slate-800) |
| `bg-surface` | `#334155` | 상승된 표면 (Slate-700) |

#### Semantic Accent Colors (의미 있는 강조색)

| Token | Hex | Meaning | Usage |
|-------|-----|---------|-------|
| `accent-fact` | `#3b82f6` | 사실/정보 (Blue-500) | 팩트 기반 캡처 |
| `accent-insight` | `#ec4899` | 통찰/감정 (Pink-500) | 개인적 깨달음 |
| `accent-ai` | `#8b5cf6 → #ec4899` | AI 처리 중 (Purple Gradient) | AI 작업 표시 |
| `accent-connection` | `#06b6d4` | 연결 (Cyan-500) | Synapse 연결선 |
| `accent-growth` | `#10b981` | 성장/성공 (Emerald-500) | 긍정 피드백 |
| `accent-warning` | `#f59e0b` | 주의 (Amber-500) | 경고 상태 |

#### Mood Colors (5가지 무드)

| Mood | Hex | Emoji Hint |
|------|-----|------------|
| `mood-curious` | `#3b82f6` | 🔵 호기심 |
| `mood-inspired` | `#f59e0b` | 🟡 영감 |
| `mood-peaceful` | `#10b981` | 🟢 평화 |
| `mood-passionate` | `#ef4444` | 🔴 열정 |
| `mood-reflective` | `#8b5cf6` | 🟣 성찰 |

#### Text Colors (텍스트)

| Token | Hex | Usage |
|-------|-----|-------|
| `text-primary` | `#f8fafc` | 주요 텍스트 (Slate-50) |
| `text-secondary` | `#cbd5e1` | 보조 텍스트 (Slate-300) |
| `text-muted` | `#64748b` | 비활성 텍스트 (Slate-500) |

### Typography

**Font Family**: Geist Sans (Primary), Inter (Fallback)

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| `h1` | 2.25rem (36px) | 700 | 1.2 |
| `h2` | 1.875rem (30px) | 600 | 1.3 |
| `h3` | 1.5rem (24px) | 600 | 1.4 |
| `body` | 1rem (16px) | 400 | 1.6 |
| `caption` | 0.875rem (14px) | 400 | 1.5 |
| `small` | 0.75rem (12px) | 400 | 1.4 |

**Font Constraint**: ❌ Serif(명조체) 사용 금지 → Sans-serif(고딕)로 통일

### Spacing System

Tailwind 기본 4px 기반:
- `space-1`: 4px
- `space-2`: 8px
- `space-3`: 12px
- `space-4`: 16px
- `space-6`: 24px
- `space-8`: 32px

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `rounded-sm` | 4px | 작은 버튼, 태그 |
| `rounded-md` | 8px | 입력 필드 |
| `rounded-lg` | 12px | 카드 |
| `rounded-xl` | 16px | 모달, 큰 카드 |
| `rounded-full` | 9999px | 아바타, 원형 버튼 |

### Shadow System

| Token | Value | Usage |
|-------|-------|-------|
| `shadow-glow-sm` | `0 0 10px rgba(59, 130, 246, 0.3)` | 작은 발광 |
| `shadow-glow-md` | `0 0 20px rgba(59, 130, 246, 0.4)` | 중간 발광 |
| `shadow-glow-lg` | `0 0 40px rgba(59, 130, 246, 0.5)` | 큰 발광 (연결 강조) |
| `shadow-card` | `0 4px 6px -1px rgba(0, 0, 0, 0.3)` | 카드 그림자 |

---

## Design Direction

### Selected Direction: "C. Balanced Hybrid (Library First)"

**컨셉**: 메이슨리 그리드(라이브러리)를 기본 뷰로, 그래프 뷰로 자연스럽게 전환

#### Layout Strategy

```
┌─────────────────────────────────────────────────────────┐
│  [🔍 Search]          [Grid/Graph Toggle]    [⚙️]      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   ┌──────┐  ┌──────────┐  ┌──────┐                     │
│   │ Card │  │   Card   │  │ Card │   ← Masonry Grid    │
│   │  A   │  │    B     │  │  C   │     (Default)       │
│   └──────┘  │          │  └──────┘                     │
│             └──────────┘                               │
│   ┌──────────┐  ┌──────┐                               │
│   │   Card   │  │ Card │                               │
│   │    D     │  │  E   │                               │
│   └──────────┘  └──────┘                               │
│                                                         │
│                    ↕️ Toggle                            │
│                                                         │
│        (A)────────(B)                                  │
│         │  \       │                                   │
│         │   \      │        ← Graph View               │
│        (C)   (D)──(E)          (연결 탐색)             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

#### View Transition

- **Trigger**: 상단 Toggle 버튼 또는 카드 더블클릭
- **Animation**: Framer Motion `layoutId`로 Morphing 전환
- **Duration**: 400ms ease-in-out
- **State Persistence**: 마지막 뷰 상태 저장

---

## Component Strategy

### Core Components

#### 1. MorphingCard

**Purpose**: Grid View ↔ Graph View 간 자연스러운 변환

**States**:
- `grid`: 직사각형, 상세 정보 표시
- `graph`: 원형/정사각형, 연결선 표시
- `expanded`: 전체 화면, 상세 보기

**Implementation**:
```tsx
<motion.div
  layoutId={`card-${id}`}
  className={cn(
    "bg-nebula rounded-lg",
    state === "grid" && "w-full aspect-video",
    state === "graph" && "w-16 h-16 rounded-full"
  )}
  transition={{ duration: 0.4, ease: "easeInOut" }}
>
  {/* Content adapts to state */}
</motion.div>
```

**Visual Specs**:
| State | Size | Border Radius | Content |
|-------|------|---------------|---------|
| Grid | 100% width, auto height | 12px | Title, Preview, Mood, Date |
| Graph | 64px × 64px | 50% (circle) | Thumbnail only |
| Expanded | Full viewport | 16px | Full content, Actions |

#### 2. SynapseCanvas

**Purpose**: 카드 간 연결선을 SVG Bezier 곡선으로 렌더링

**Features**:
- 동적 곡률: 거리에 따라 곡선 강도 조절
- 연결 강도 시각화: 선 두께와 불투명도로 표현
- 애니메이션: 새 연결 생성 시 그리기 효과

**Implementation**:
```tsx
<svg className="absolute inset-0 pointer-events-none">
  <motion.path
    d={`M ${x1} ${y1} Q ${cx} ${cy} ${x2} ${y2}`}
    stroke="var(--accent-connection)"
    strokeWidth={Math.max(1, strength * 3)}
    strokeOpacity={0.3 + strength * 0.5}
    fill="none"
    initial={{ pathLength: 0 }}
    animate={{ pathLength: 1 }}
    transition={{ duration: 0.6 }}
  />
</svg>
```

#### 3. AITagPulse

**Purpose**: AI가 생성한 태그/연결에 "왜?"를 표시

**Behavior**:
1. 태그 옆에 작은 `?` 아이콘
2. 호버/탭 시 AI 근거 툴팁 표시
3. 사용자가 수정/삭제 가능

**Visual**:
```
[#machine-learning] [?]
                     ↓
  ┌─────────────────────────────────┐
  │ AI 근거: "neural network",       │
  │ "deep learning" 키워드 감지      │
  │                    [수정] [삭제] │
  └─────────────────────────────────┘
```

#### 4. CaptureStatusIndicator

**Purpose**: 캡처 후 백그라운드 처리 상태를 투명하게 표시

**States**:
1. ✓ "저장됨" - URL + 메타데이터 저장 완료 (즉시)
2. ◐ "아카이빙 중" - WACZ 처리 진행 (진행 표시기)
3. ✓✓ "영구 보관됨" - WACZ 완료
4. ⟳ "재시도 중" - 실패 시 백그라운드 재시도

#### 5. SplitReferenceView (일기 작성용)

**Purpose**: 일기 작성 시 과거 캡처를 참조하며 작성

**Layout**:
```
┌──────────────────────┬──────────────────────┐
│                      │                      │
│   Today's Captures   │    Diary Editor      │
│   (Timeline)         │                      │
│                      │                      │
│   [Card] ← drag →    │    "오늘 저장한      │
│   [Card]             │     이 글을 보며..." │
│   [Card]             │                      │
│                      │                      │
│   AI Summary ↓       │                      │
│   "오늘 3개 저장,    │                      │
│    주제: AI, Design" │                      │
│                      │                      │
└──────────────────────┴──────────────────────┘
```

---

## User Journey Flows

### Journey 1: Rapid Capture (2초 캡처)

**Context**: 모바일에서 웹페이지를 보다가 저장하고 싶을 때

**Flow**:
```
1. Share Button 클릭
   ↓
2. Moments 선택
   ↓
3. [Optional] 무드 컬러 선택 (기본값 자동 선택)
   ↓
4. [Optional] Ghost Memo 입력 (한 줄 생각)
   ↓
5. 저장 완료 (Non-blocking Pulse UI)
   - 즉시 "저장됨 ✓" 표시
   - 백그라운드에서 WACZ 아카이빙
   - 사용자는 원래 앱으로 복귀
```

**Critical UX**: 
- 전체 플로우 **2초 이내** 완료
- 추가 입력 없이 즉시 저장 가능
- 성공 알림은 최소한의 방해로 (Toast, 2초 후 자동 소멸)

### Journey 2: Spark of Insight (연결 발견)

**Context**: 그래프 뷰에서 탐색하다가 새로운 연결 발견

**Flow**:
```
1. Graph View 진입
   ↓
2. 카드 위 호버/탭
   ↓
3. 관련 카드들이 자석처럼 끌려옴 (Magnetic Pull)
   ↓
4. 연결선이 빛나며 표시 (Glow + Spark)
   ↓
5. "왜 연결됐지?" 궁금하면 연결선 탭
   ↓
6. AI 근거 팝오버: "공통 키워드: UX, 사용자 경험"
   ↓
7. [도움됨] / [도움 안됨] 피드백
```

**Critical UX**:
- 발견의 기쁨을 시각적으로 강조
- AI 연결 근거 항상 노출 가능
- 피드백 버튼으로 AI 학습

### Journey 3: Reflection & Synthesis (성찰 일기)

**Context**: 밤 9시, 하루를 마무리하며 일기 작성

**Flow**:
```
1. 앱 진입 (밤 9시 푸시 알림 또는 자발적)
   ↓
2. "오늘의 순간들" 타임라인 표시
   - 오늘 캡처한 모든 카드
   - AI 요약: "오늘 5개 저장, 주제: AI 윤리, 디자인 시스템"
   ↓
3. Split View 일기 에디터 열기
   - 왼쪽: 오늘의 캡처들 (드래그 가능)
   - 오른쪽: 일기 작성 영역
   ↓
4. 캡처 카드를 일기에 드래그 앤 드롭으로 인용
   ↓
5. AI가 "The Self-Query" 질문 제안
   - "오늘 왜 이 글이 마음에 와닿았나요?"
   ↓
6. 일기 작성 완료
   ↓
7. "성찰에 도움됨" 피드백 버튼
```

**Critical UX**:
- 부담 없는 시작 (AI 초안 제공)
- 과거 캡처와 자연스러운 연결
- Ghost Memo 내용 자동 반영

---

## UX Consistency Patterns

### Button Hierarchy

| Type | Appearance | Usage |
|------|------------|-------|
| **Primary** | Solid Blue (`accent-fact`) | 주요 액션 (저장, 확인) |
| **Secondary** | Outline Blue | 보조 액션 (취소, 건너뛰기) |
| **Ghost** | Text only + Hover 배경 | 3차 액션 |
| **Destructive** | Solid Red | 삭제 (확인 필요) |

### Feedback Patterns

| Pattern | Animation | Duration | Usage |
|---------|-----------|----------|-------|
| **Pulse** | Scale 1.0 → 1.05 → 1.0 | 300ms | 저장 성공 |
| **Shake** | X -5px → 5px → 0 | 200ms | 입력 오류 |
| **Breathing** | Opacity 0.5 → 1 → 0.5 | 2s loop | 로딩/처리 중 |
| **Spark** | Particle burst | 400ms | 연결 발견 |

### Navigation Patterns

#### Mobile Navigation (Bottom Tab)

```
┌─────────────────────────────────────┐
│                                     │
│           [Content Area]            │
│                                     │
├─────────────────────────────────────┤
│  [Home]  [Search]  [+]  [Diary] [Me]│
│    ○       ○      ●      ○      ○   │
│                 Glow                │
└─────────────────────────────────────┘
```

**규칙**:
- ❌ Floating Button 금지: 모든 탭 **동일 크기**
- ✅ Capture 버튼만 **Filled + Glow**로 강조
- 탭 아이콘: Lucide React (Outline style, Active = Filled)

#### Desktop Navigation (Sidebar)

```
┌──────┬──────────────────────────────┐
│      │                              │
│ Logo │        [Content Area]        │
│      │                              │
│──────│                              │
│ Home │                              │
│Search│                              │
│Diary │                              │
│──────│                              │
│ [+]  │                              │
│Capture                              │
│      │                              │
└──────┴──────────────────────────────┘
```

**규칙**:
- Collapsible: 접혀도 아이콘만 표시
- Capture 버튼: 사이드바 하단 고정, 강조

#### Tablet Navigation

**규칙**: Tablet = **Extended Mobile**
- 하단 탭 **유지** (데스크톱 사이드바 아님)
- Grid 컬럼 확장 (3-4열)
- Split View 활용 가능

### Empty States

**철학**: 빈 상태 = "가능성의 시작"

```
┌─────────────────────────────────────┐
│                                     │
│              ✦                      │
│         (Singularity)               │
│                                     │
│    "모든 우주는 하나의 점에서       │
│     시작됩니다.                     │
│                                     │
│     첫 번째 순간을 캡처해보세요."   │
│                                     │
│         [+ 캡처하기]                │
│                                     │
└─────────────────────────────────────┘
```

**규칙**:
- 우주/별 메타포 사용
- 긍정적 프레이밍 ("비어있다" 대신 "시작점")
- 명확한 CTA 버튼

### Deletion UX

**규칙**: ❌ 즉시 삭제 후 Undo 방식 **금지**

```
┌─────────────────────────────────────┐
│                                     │
│   🗑️ 정말 삭제하시겠습니까?         │
│                                     │
│   "2023년 12월의 이 순간을          │
│    영원히 보낼 준비가 되셨나요?"    │
│                                     │
│   [취소]          [삭제하기]        │
│                                     │
└─────────────────────────────────────┘
```

**규칙**:
- 반드시 **확인 팝업** 표시
- 감성적 문구로 소중함 상기
- 휴지통 30일 보관 (완전 삭제 전)

---

## Responsive Design & Accessibility

### Responsive Strategy

-   **Breakpoints:** Tailwind Default (`sm`: 640px, `md`: 768px, `lg`: 1024px, `xl`: 1280px).
-   **Device Adaptation:**
    -   **Mobile (< 768px):** Bottom Tab Navigation. Single Column Layout. Full-screen Modal for details.
    -   **Tablet (768px - 1024px):** **Extended Mobile**. Bottom Tab 유지하되 Grid 컬럼 확장(3-4열) 및 Split View(목록+상세) 활용.
    -   **Desktop (> 1024px):** Collapsible Sidebar Navigation. Multi-column Masonry. Floating Windows & Panels.

### Accessibility Strategy

-   **Color Contrast:** Deep Navy 배경 위 텍스트는 `Slate-100` 이상을 사용하여 **Contrast Ratio 7:1 (AAA)** 목표 준수.
-   **Keyboard Navigation:** 마우스 없이도 모든 기능을 사용할 수 있도록 Focus Ring(Bright Blue)을 명확히 표시하고 논리적 탭 순서(Tab Order) 구현.
-   **Screen Reader:** `MorphingCard`, `SynapseCanvas` 등 비표준 UI 요소에 `aria-label` 및 `role` 속성을 철저히 적용하여 맥락 정보 제공.
-   **Reduced Motion:** 화려한 애니메이션(Spark, Morphing)은 `prefers-reduced-motion` 미디어 쿼리 감지 시 단순 Fade 효과로 대체.

### Localization (i18n) Strategy

-   **Day 1 Support:** 초기 아키텍처부터 `next-intl` 등을 도입하여 **한국어/영어** 동시 지원.
-   **Resource Management:** 모든 UI 텍스트를 JSON 리소스 파일로 분리하여 관리, 향후 글로벌 확장 시 번역 비용 최소화.

### Implementation Guidelines

1.  **Mobile First:** 모든 스타일링은 모바일(`base`)을 기준으로 작성하고, `md:`, `lg:` 접두사를 사용하여 큰 화면 대응.
2.  **Semantic HTML:** `div` 남발 대신 `main`, `nav`, `article`, `section` 등 시맨틱 태그 사용하여 구조적 접근성 확보.
3.  **Touch Targets:** 모바일/태블릿 환경에서 모든 인터랙티브 요소는 최소 44x44px 영역 확보.

---

## MUST NOT Do (Critical Constraints)

다음 항목들은 **절대 위반 금지**입니다:

| # | 금지 항목 | 올바른 대안 |
|---|----------|-------------|
| 1 | ❌ Serif(명조체) 폰트 사용 | ✅ Sans-serif(고딕, Geist Sans/Inter)로 통일 |
| 2 | ❌ 즉시 삭제 후 Undo 방식 | ✅ 반드시 확인 팝업 (소중한 추억 존중) |
| 3 | ❌ 모바일 Floating Button (크기 다르게) | ✅ 동일 크기, Capture만 Filled+Glow로 강조 |
| 4 | ❌ 태블릿에 데스크톱 UX 적용 | ✅ 태블릿은 Extended Mobile (하단 탭 유지) |
| 5 | ❌ 설명 없는 AI 자동화 | ✅ 반드시 근거(키워드) 노출 및 사용자 수정 가능 |
| 6 | ❌ 텍스트 링크로만 연관성 표현 | ✅ 비주얼 카드 군집으로 표현 |
| 7 | ❌ 미정리 상태를 "지저분함"으로 표현 | ✅ "가능성의 상태", "현상 대기 중인 필름"으로 긍정적 재정의 |
| 8 | ❌ 피드백 버튼 없는 AI 기능 | ✅ "도움됨/도움안됨" 버튼 필수 |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-10 | Initial creation via UX Design workflow |
| 1.1 | 2026-01-12 | Restored after file corruption |

---

**Document Status:** ✅ Complete (Restored)
**Last Updated:** 2026-01-12
