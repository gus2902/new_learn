# Codex + BMAD 통합 가이드

이 문서는 OpenAI Codex CLI에서 BMAD-METHOD를 사용하는 방법을 단계별로 설명합니다.

---

## 목차

1. [개요](#개요)
2. [문제 진단](#문제-진단)
3. [Codex Custom Prompts 이해](#codex-custom-prompts-이해)
4. [해결 방법](#해결-방법)
5. [설치 방법](#설치-방법)
6. [사용 방법](#사용-방법)
7. [설정 옵션](#설정-옵션)
8. [트러블슈팅](#트러블슈팅)

---

## 개요

### BMAD-METHOD란?

**BMAD-METHOD** (Build More, Architect Dreams)는 AI 주도 애자일 개발 프레임워크로:

- 21개 전문 에이전트 (PM, Architect, Developer, UX Designer 등)
- 50+ 가이드 워크플로우 (PRD 생성, 아키텍처 설계, 스프린트 계획 등)
- 스케일 적응형 인텔리전스 (버그 수정 ~ 엔터프라이즈 시스템)

### Codex CLI란?

**OpenAI Codex CLI**는 터미널 기반 AI 코딩 어시스턴트로:

- 대화형 TUI (터미널 UI) 인터페이스
- 코드베이스 분석 및 편집
- Custom Prompts (재사용 가능한 프롬프트 템플릿)
- Skills (전문 작업용 명령어 번들)

---

## 문제 진단

### 문제 현상

```
✗ BMAD 프롬프트 설치 완료
✗ Codex 재시작 완료
✗ 하지만 /prompts 명령어가 표시되지 않음
```

### 원인 분석

Codex는 **전역 `~/.codex/` 디렉토리만 스캔**하고, **프로젝트 `.codex/`는 자동으로 읽지 않습니다.**

```bash
# 현재 설치 상태
.codex/prompts/           # 프로젝트 내 (Codex가 읽지 않음)
~/.codex/prompts/         # 전역 (비어 있음)

# Codex가 기대하는 디렉토리
~/.codex/prompts/         # 전역만 스캔
```

### 환경변수 확인

```bash
# CODEX_HOME 확인
echo $CODEX_HOME
# 결과: 비어 있음 → Codex가 전역 디렉토리만 사용
```

---

## Codex Custom Prompts 이해

### 작동 방식

```
1. CODEX_HOME 환경변수 확인
   ↓
2. CODEX_HOME 설정되어 있음
   → $CODEX_HOME/.codex/prompts/ 사용
   ↓
3. CODEX_HOME 설정되어 있지 않음
   → ~/.codex/prompts/ (전역) 사용
   ↓
4. *.md 파일 스캔
   ↓
5. 슬래시 명령어 메뉴에 등록
   → / 입력 후 "prompts:"로 검색 가능
```

### 프롬프트 파일 형식

```markdown
---
name: 'my-prompt'
description: 'My custom prompt'
---

# 프롬프트 내용
이 프롬프트가 Codex에 로드됩니다.
```

### 호출 방식

```bash
# Codex 슬래시 메뉴에서
/prompts:my-prompt

# 또는 직접 입력 (메뉴에서 선택)
/prompts:my-prompt ARG1="value" ARG2="value"
```

---

## 해결 방법

### 해결 1: 전역 설치 (간단)

프롬프트를 `~/.codex/prompts/`에 복사:

```bash
# 전역 디렉토리 생성
mkdir -p ~/.codex/prompts

# 프로젝트에서 전역으로 복사
cp -r .codex/prompts/* ~/.codex/prompts/

# Codex 재시작
codex
```

**장점**: 모든 프로젝트에서 사용 가능
**단점**: 프로젝트별 프롬프트 분리 불가

---

### 해결 2: CODEX_HOME 설정 (추천 - 프로젝트별)

프로젝트별로 `CODEX_HOME`을 설정:

#### Windows (`.cmd` 파일)

```batch
@echo off
set CODEX_HOME=%~dp0.codex
codex %*
```

**설명**:
- `%~dp0`: 현재 배치 파일이 있는 드라이브 경로
- `set CODEX_HOME=%~dp0.codex`: Codex 홈을 프로젝트 `.codex/`로 설정
- `%*`: 모든 인자를 Codex에 전달

#### Unix/macOS (`.sh` 파일 또는 alias)

**스크립트 파일**:
```bash
#!/bin/bash
export CODEX_HOME="$(pwd)/.codex"
codex "$@"
```

**Shell alias** (`.bashrc` 또는 `.zshrc`):
```bash
alias codex-local='CODEX_HOME="$PWD/.codex" codex'
```

**장점**: 각 프로젝트에서 독립적인 프롬프트
**단점**: 각 프로젝트에서 설정 필요

---

## 설치 방법

### 1단계: BMAD 설치

```bash
# 프로젝트 루트에서
npx bmad-method@alpha install
```

설치 중 다음을 선택:
- **IDE**: Codex
- **설치 모드**: Global 또는 Project

### 2단계: 설정 방법 선택

#### 옵션 A: 전역 설치

```bash
# 복사 명령어 실행
cp -r .codex/prompts/* ~/.codex/prompts/

# 확인
ls ~/.codex/prompts/ | wc -l
# 결과: 50+ 개 파일
```

#### 옵션 B: 프로젝트별 설치 (Windows)

```batch
# codex.cmd 파일 생성 (프로젝트 루트)
@echo off
set CODEX_HOME=%~dp0.codex
codex %*
```

파일 경로: `C:\Users\USERNAME\Documents\ProjectName\codex.cmd`

### 3단계: Codex 재시작

```bash
# 옵션 A (전역)
codex

# 옵션 B (프로젝트별)
.\codex.cmd
```

---

## 사용 방법

### 프로젝트별 사용 (추천)

```bash
# 현재 디렉토리에서
.\codex.cmd
```

#### 작동 과정

1. `CODEX_HOME=C:\Users\USERNAME\Documents\ProjectName\.codex`로 설정
2. Codex 시작
3. `CODEX_HOME/.codex/prompts/` 디렉토리 스캔
4. BMAD 프롬프트 로드
5. 슬래시 명령어 메뉴에서 사용 가능

#### 프롬프트 실행

```
# Codex 시작 후
/  → 슬래시 메뉴 열기
prompts:  → 프롬프트 검색
bmad  → BMAD 프롬프트 필터

# 예시
/prompts:bmad-bmm-agents-pm
/prompts:bmad-bmm-workflows-create-prd
/prompts:bmad-bmm-agents-architect
```

---

### 전역 사용

```bash
# 어느 프로젝트에서나
codex
```

#### 장점

- 한 번만 설치하면 모든 프로젝트에서 사용
- 별도의 설정 파일 불필요

#### 단점

- 모든 프로젝트에서 같은 프롬프트 사용
- 프로젝트별 커스터마이즈 불가

---

## 설정 옵션

### 두 방법 비교

| 특징 | 프로젝트별 | 전역 |
|---|---|---|
| **설치 위치** | `.codex/prompts/` (프로젝트 내) | `~/.codex/prompts/` (사용자 홈) |
| **사용 범위** | 현재 프로젝트만 | 모든 프로젝트 |
| **설정 방법** | `codex.cmd` 또는 `CODEX_HOME` 설정 | 복사만 하면 됨 |
| **장점** | 각 프로젝트에서 독립적인 프롬프트 | 어느 프로젝트에서나 사용 |
| **단점** | 각 프로젝트에서 설정 필요 | 프로젝트별 분리 불가 |
| **추천 상황** | 개인 프로젝트 | 공통 프롬프트 |

---

### 프로젝트 구조 (프로젝트별 설정)

```
my-project/
├── .codex/
│   ├── prompts/
│   │   ├── bmad-bmm-agents-pm.md
│   │   ├── bmad-bmm-agents-architect.md
│   │   └── bmad-bmm-workflows-*.md
│   └── config.toml (선택적)
├── codex.cmd           (Windows)
├── codex.sh            (Unix/macOS)
└── src/
```

---

## 트러블슈팅

### 문제 1: `/prompts` 명령어가 없음

**원인**: 프롬프트 파일이 올바른 디렉토리에 없음

**해결**:

```bash
# 파일 위치 확인
ls ~/.codex/prompts/  # 전역
ls .codex/prompts/      # 프로젝트

# CODEX_HOME 확인
echo $CODEX_HOME

# Codex 재시작
codex
```

---

### 문제 2: 프롬프트 파일이 로드되지 않음

**원인**: 파일 형식이 올바르지 않거나 Codex가 재시작되지 않음

**해결**:

```bash
# 파일 형식 확인
head -n 5 ~/.codex/prompts/bmad-bmm-agents-pm.md

# YAML frontmatter가 있어야 함
---
name: 'pm'
description: 'pm agent'
---

# Codex 재시작
codex
```

---

### 문제 3: 프로젝트별 설정이 작동하지 않음 (Windows)

**원인**: `codex.cmd` 파일이 올바른 위치에 없거나 형식이 틀림

**해결**:

```batch
# 파일 위치 확인 (프로젝트 루트)
type codex.cmd

# 올바른 형식
@echo off
set CODEX_HOME=%~dp0.codex
codex %*

# 이렇게 실행
.\codex.cmd
```

---

### 문제 4: CODEX_HOME이 설정되지 않음

**원인**: 환경변수 설정이 올바르지 않음

**해결**:

#### Windows

```batch
# codex.cmd 확인
type codex.cmd

# 다음 줄이 있어야 함
set CODEX_HOME=%~dp0.codex
```

#### Unix/macOS

```bash
# alias 확인
grep "codex" ~/.bashrc
grep "codex" ~/.zshrc

# 다음 줄이 있어야 함
alias codex-local='CODEX_HOME="$PWD/.codex" codex'

# 재로드
source ~/.bashrc  # 또는 source ~/.zshrc
```

---

### 문제 5: BMAD 프롬프트가 메뉴에 나타나지 않음

**원인**: Codex가 프롬프트를 스캔하지 못함

**해결**:

```bash
# 1. 파일이 실제로 존재하는지 확인
ls ~/.codex/prompts/bmad-*.md
# 또는
ls .codex/prompts/bmad-*.md

# 2. 파일 형식 확인
head -n 3 ~/.codex/prompts/bmad-bmm-agents-pm.md

# 3. Codex 재시작
codex

# 4. Codex 로그 확인
/status
```

---

## BMAD 프롬프트 예시

### 에이전트

```bash
# PM 에이전트
/prompts:bmad-bmm-agents-pm

# 아키텍트
/prompts:bmad-bmm-agents-architect

# 개발자
/prompts:bmad-bmm-agents-dev
```

### 워크플로우

```bash
# PRD 생성
/prompts:bmad-bmm-workflows-create-prd

# 아키텍처 생성
/prompts:bmad-bmm-workflows-create-architecture

# 에픽/스토리 생성
/prompts:bmad-bmm-workflows-create-epics-and-stories

# 스프린트 계획
/prompts:bmad-bmm-workflows-sprint-planning
```

---

## 요약

### 빠른 시작

```bash
# 1. BMAD 설치
npx bmad-method@alpha install

# 2. 설정 (프로젝트별 - Windows)
# codex.cmd 파일 생성:
@echo off
set CODEX_HOME=%~dp0.codex
codex %*

# 3. 실행
.\codex.cmd

# 4. 프롬프트 사용
/
→ prompts:
→ bmad
→ 원하는 프롬프트 선택
```

---

## 추가 리소스

- [Codex CLI 공식 문서](https://developers.openai.com/codex/cli/)
- [Custom Prompts 가이드](https://developers.openai.com/codex/custom-prompts/)
- [Slash Commands 가이드](https://developers.openai.com/codex/cli/slash-commands/)
- [BMAD-METHOD 저장소](https://github.com/bmad-code-org/BMAD-METHOD)
- [BMAD-METHOD 문서](https://docs.bmad-method.org)

---

## 마지막 업데이트

- **날짜**: 2026-01-10
- **Codex 버전**: 0.80.0
- **BMAD 버전**: latest

---

## 피드백

이 문서에 오류가 있거나 개선 제안이 있다면 BMAD-METHOD 저장소에 이슈를 제출해주세요.
