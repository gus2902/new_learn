# PHASE 4 - Step 2: SAM (Serviceable Available Market) 추정

## 📋 Step 2 개요

**작업일:** 2026-01-10
**상태:** ✅ 완료 (글로벌 페르소나 반영 업데이트)
**분석 대상 시장:** 웹페이지 클리핑 후 자동 정리 (AI-Powered PKM)
**목표:** 우리가 실제로 도달 가능한 시장 규모를 숫자로 증명하기

**참고 자료:**
- PHASE 4 Step 1: TAM 추정 결과 (Global $3.0B / 한국 $125M)
- PHASE 3: 업데이트된 4개 글로벌 페르소나 (Sarah, 이지훈, Elena, Marcus)
- PHASE 3 Step 4: Pain Point 우선순위 매트릭스

---

## 🎯 SAM 추정 방법론

### SAM 정의
**SAM (Serviceable Available Market):** 우리 제품/서비스가 실제로 도달 가능한 시장 규모 (타겟 세그먼트 및 초기 공략 지역 기준)

### 계산 방식
```
SAM = Σ (타겟 페르소나별 잠재 사용자 수 × 가중 ARPU)
```

---

## 📊 SAM 추정: 방법 1 - 타겟 세그먼트별 시장 규모

### 타겟 세그먼트 정의 (Global-First)

PHASE 3의 페르소나 설계 결과를 바탕으로 시장을 4가지 핵심 세그먼트로 세분화했습니다.

| **페르소나** | **세그먼트 성격** | **비중 (KR 기준)** | **공략 지역** |
| --- | --- | --- | --- |
| **Sarah Mitchell** | Global AI Savvy (Expert) | 20% | Global (Day 1) |
| **이지훈 (PM)** | Hyper-Local Champion | 30% | Korea (Day 1) |
| **Elena Rossi** | Multilingual Researcher | 35% | Global (Phase 2) |
| **Marcus Chen** | Enterprise Strategist | 15% | Global B2B (Phase 3) |

### 한국 시장 기반 SAM 계산 (Bottom-Up 보완)

**기준:** TAM (한국) = $125M

#### 세그먼트별 시장 규모 (비중 적용)

| **세그먼트** | **비중** | **시장 규모** | **계산** |
| --- | --- | --- | --- |
| **Elena (Research)** | 35% | $43.75M | $125M × 35% |
| **이지훈 (Local Expert)** | 30% | $37.50M | $125M × 30% |
| **Sarah (Global Savvy)** | 20% | $25.00M | $125M × 20% |
| **Marcus (Business)** | 15% | $18.75M | $125M × 15% |
| **합계** | **100%** | **$125.0M** | - |

---

## 📊 SAM 추정: 방법 2 - 페르소나별 ARPU × 잠재 사용자 수

### 페르소나별 ARPU 및 전환율 추정

| **페르소나** | **프리미엄 ARPU (연)** | **전환율(가정)** | **실제 연 ARPU** | **특징** |
| --- | --- | --- | --- | --- |
| **Sarah** | $120 (Global Standard) | 25% | $30.0 | X/Substack 통합 가치 높음 |
| **이지훈** | $96 (KR Premium) | 20% | $19.2 | 한국형 하이퍼 파서 유료 지불 용의 |
| **Elena** | $60 (Researcher Discount) | 15% | $9.0 | 다국어 인사이트 연결 및 방대한 데이터 |
| **Marcus** | $180 (B2B/Security) | 30% | $54.0 | Local LLM/Privacy-First 프리미엄 |

### SAM 계산 (한국 시장 잠재 고객 2.85M 명 기준)

| **페르소나** | **잠재 사용자 수** | **실제 연 ARPU** | **SAM** | **비고** |
| --- | --- | --- | --- | --- |
| **Elena Rossi** | 1.00M 명 | $9.0 | $9.00M | 학계 및 전문 연구군 |
| **이지훈 (PM)** | 0.85M 명 | $19.2 | $16.32M | 국내 IT 서비스 종사자 |
| **Sarah Mitchell** | 0.57M 명 | $30.0 | $17.10M | 글로벌 트렌드 세터 |
| **Marcus Chen** | 0.43M 명 | $54.0 | $23.22M | 보안 민감 기업 부문 |
| **합계** | **2.85M 명** | - | **$65.64M** | - |

**→ 최종 산출 SAM (한국 중심): $65.64M (약 853억원)**

---

## 🎯 페르소나별 접근 가능성 (Strategy)

### 1. Sarah Mitchell (Global AI Savvy) - � Day 1 우선순위
- **이유:** 글로벌 마켓의 '초기 수용자(Early Adopter)'로, 제품의 영구 박제(WACZ) 기술에 가장 민감하고 강력한 바이럴을 일으킬 수 있는 집단.
- **전략:** Product Hunt 런칭, X(Twitter) 테크 인플루언서 협업.

### 2. 이지훈 (Hyper-Local Champion) - 🔴 Day 1 우선순위
- **이유:** 글로벌 도구가 해결하지 못하는 '네이버/브런치'의 무결성 박제 및 한-영 교차 검색 니즈가 독보적임.
- **전략:** 국내 개발자 커뮤니티(EO, 커리어리 등) 중심의 '글로벌 도구 보완재' 브랜딩.

### 3. Elena Rossi (Multilingual Researcher) - 🟡 Phase 2 확장
- **이유:** 다국어 소스 간의 '감성적/시맨틱 연결' 기능을 통해 단순 저장을 넘어선 통찰 도구로 진화 시 공략.
- **전략:** 학술 리서치 큐레이션 기능 및 '성좌형 지식 그래프' 고도화.

### 4. Marcus Chen (Enterprise Strategist) - 🔵 Phase 3 확장
- **이유:** B2B 보안 가이드 준수 및 Local LLM 인프라 요구. 높은 ARPU 보장되나 초기 구축 비용 발생.
- **전략:** 기업용 온프레미스/개인 로컬 서버 모드 출시 후 Enterprise 세일즈 시작.

---

## � 최종 요약 및 인사이트

### 1. SAM 비중 변화
기존에는 학생/연구원(김지은) 비중이 높았으나, 업데이트된 글로벌 전략에서는 **수익성이 높은 Sarah(Global AI Savvy)와 Marcus(Enterprise)**의 시장 기여도가 $40.32M으로 전체 SAM의 **61%**를 차지함.

### 2. 하이퍼 로컬의 전략적 가치
**이지훈(Local Expert)** 세그먼트는 한국 시장에서만 $16.32M의 기회를 창출하며, 이는 글로벌 경쟁자(Readwise 등)가 진입하기 힘든 'Moments'만의 강력한 성벽(Moat)이 됨.

### 3. 결론
우리의 SAM은 단순한 저장 도구 사용자가 아닌, **'지식의 가치를 극대화하고 보안을 중시하는 헤비 유저'**를 중심으로 재편되었으며, 이는 높은 ARPU와 충성도를 확보할 수 있는 논리적 근거가 됨.

---

*문서 생성일: 2026-01-10*
*마지막 업데이트: 2026-01-10*
