# US-PROTO-01: 2초 캡처 기술 PoC

**Epic:** EP-PROTOTYPE (Phase 0 기술 검증)
**Status:** in-progress
**Priority:** Critical (Go/No-Go Decision)
**Created:** 2026-01-13
**Sprint:** Phase 0

---

## User Story

> AS A [개발자],
> I WANT Share Extension → WACZ 아카이빙 파이프라인이 2초 이내에 완료됨을 검증하고 싶다,
> SO THAT MVP 개발 전에 핵심 기술 리스크를 제거할 수 있다.

---

## Acceptance Criteria

| ID | Criteria | Metric |
|----|----------|--------|
| AC-1 | Share Extension에서 URL 전송 후 "저장됨 ✓" 표시까지 평균 2초 이내 완료 | p50 < 2s, p95 < 3s |
| AC-2 | 10개 주요 사이트에서 테스트 시 캡처 성공률 > 95% | Success Rate > 95% |
| AC-3 | 캡처 실패 시 Graceful Degradation: URL + 텍스트 스냅샷으로 fallback 저장 | Fallback 100% |
| AC-4 | 성능 벤치마크 보고서 작성 및 Go/No-Go 결정 | Report Complete |

---

## Exit Criteria (Go/No-Go Gate)

| Outcome | Condition | Action |
|---------|-----------|--------|
| **GO** | p50 < 2s AND 성공률 > 95% | MVP 개발 시작 |
| **CONDITIONAL GO** | p50 2-3s AND 성공률 > 90% | 아키텍처 최적화 후 재검증 |
| **NO-GO** | p50 > 3s OR 성공률 < 90% | 아키텍처 재설계 또는 프로젝트 재검토 |

---

## Technical Context

### Architecture Decision (AD-01)
- 클라이언트는 URL+메타데이터만 전송
- 서버에서 비동기 WACZ 처리
- 캡처 성공과 아카이브 완료 사이의 시간차는 UX 상태 표시로 해결

### Tech Stack (Phase 0)
| Component | Technology | Version |
|-----------|------------|---------|
| Mobile | React Native + Expo | SDK 54 |
| Share Extension | iOS Native Module | Swift |
| Backend | Python FastAPI | 0.128.x |
| Archive | Playwright + SingleFile | 1.50.x |
| Storage | Supabase (Postgres) | - |
| Object Storage | Cloudflare R2 | - |

### Test Sites (10개)
| Category | Sites |
|----------|-------|
| 뉴스 | naver.com/news, bbc.com |
| 블로그 | medium.com, brunch.co.kr |
| SNS | twitter.com, instagram.com |
| 커뮤니티 | reddit.com, clien.net |
| 기술 | github.com, stackoverflow.com |

---

## Task Breakdown

### Phase 0-A: 환경 설정 (Day 1-2)

| Task ID | Task | Est. Hours | Status |
|---------|------|------------|--------|
| T-01 | Monorepo 초기화 (Turborepo + pnpm) | 2h | ✅ done |
| T-02 | Expo 프로젝트 생성 (SDK 54, TypeScript) | 2h | ✅ done |
| T-03 | FastAPI 백엔드 스캐폴딩 | 2h | ✅ done |
| T-04 | Supabase 프로젝트 설정 (DB + Auth) | 2h | ✅ done |
| T-05 | Cloudflare R2 버킷 생성 및 연동 | 1h | ✅ done |

### Phase 0-B: Share Extension PoC (Day 3-5)

| Task ID | Task | Est. Hours | Status |
|---------|------|------------|--------|
| T-06 | iOS Share Extension 네이티브 모듈 생성 | 4h | pending |
| T-07 | URL 추출 및 메타데이터 파싱 로직 | 3h | pending |
| T-08 | Supabase API 호출 (captures 테이블 저장) | 2h | pending |
| T-09 | "저장됨 ✓" 토스트 알림 UI | 2h | pending |
| T-10 | 오프라인 캡처 큐잉 (AsyncStorage) | 3h | pending |

### Phase 0-C: 백엔드 캡처 파이프라인 (Day 6-8)

| Task ID | Task | Est. Hours | Status |
|---------|------|------------|--------|
| T-11 | FastAPI /capture 엔드포인트 구현 | 2h | pending |
| T-12 | Playwright 기반 페이지 로딩 + 스크린샷 | 4h | pending |
| T-13 | SingleFile CLI 통합 (HTML 아카이빙) | 4h | pending |
| T-14 | Cloudflare R2 업로드 로직 | 2h | pending |
| T-15 | Graceful Degradation (fallback 저장) | 3h | pending |

### Phase 0-D: 벤치마크 및 검증 (Day 9-10)

| Task ID | Task | Est. Hours | Status |
|---------|------|------------|--------|
| T-16 | 10개 사이트 E2E 캡처 테스트 스크립트 | 3h | pending |
| T-17 | 성능 측정 로깅 (캡처 시간, 성공률) | 2h | pending |
| T-18 | 벤치마크 보고서 작성 | 2h | pending |
| T-19 | Go/No-Go 결정 문서화 | 1h | pending |

---

## Total Estimation

| Phase | Tasks | Hours | Days |
|-------|-------|-------|------|
| 0-A: 환경 설정 | 5 | 9h | 1-2 |
| 0-B: Share Extension | 5 | 14h | 3-5 |
| 0-C: 백엔드 파이프라인 | 5 | 15h | 6-8 |
| 0-D: 벤치마크 | 4 | 8h | 9-10 |
| **Total** | **19** | **46h** | **10 days** |

---

## Dependencies

| Dependency | Type | Risk Level |
|------------|------|------------|
| Expo SDK 54 Share Extension 지원 | Technical | Medium |
| SingleFile CLI 서버 실행 | Technical | Low |
| Cloudflare R2 API | Infrastructure | Low |
| Supabase Realtime (상태 업데이트) | Infrastructure | Low |

---

## Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Share Extension 네이티브 브릿지 복잡도 | Medium | High | Expo Config Plugin 활용, 커뮤니티 예제 참조 |
| 일부 사이트 JS 렌더링 지연 | High | Medium | Timeout 설정 + Fallback to URL only |
| Playwright cold start 지연 | Medium | Medium | 서버 warm-up 전략, 연결 풀링 |
| R2 업로드 latency | Low | Low | 비동기 처리로 UX 분리 |

---

## Definition of Done

- [ ] 10개 테스트 사이트 모두에서 캡처 테스트 완료
- [ ] 성능 벤치마크 보고서 작성 완료
- [ ] p50 < 2초, p95 < 3초 달성 여부 확인
- [ ] 캡처 성공률 > 95% 달성 여부 확인
- [ ] Graceful Degradation 동작 확인
- [ ] Go/No-Go 결정 문서화

---

## Notes

### 시작하기 전 확인사항
1. Apple Developer Account 활성화 (Share Extension 테스트)
2. Cloudflare 계정 + R2 활성화
3. Supabase 프로젝트 생성 권한

### PoC 범위 제한
- 이 스토리는 iOS Share Extension만 검증 (Android는 MVP에서)
- WACZ 완전 아카이빙은 US-PROTO-02에서 검증
- 현재 단계에서는 HTML 스냅샷 + 메타데이터 저장으로 충분

---

## Related Documents

- [PRD](../../planning-artifacts/prd.md)
- [Architecture](../../planning-artifacts/architecture.md)
- [UX Design Specification](../../planning-artifacts/ux-design-specification.md)
- [User Stories](../../planning-artifacts/user-stories.md)
