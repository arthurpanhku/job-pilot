<div align="center">

<img src="assets/logo.jpg" width="200" alt="JobPilot Logo" style="border-radius: 20px;" />

# JobPilot ✈️

![JobPilot Banner](https://img.shields.io/badge/JobPilot-AI_Career_Co--Pilot-blue?style=for-the-badge&logo=openai)

[![Next.js](https://img.shields.io/badge/Next.js-14-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MCP](https://img.shields.io/badge/MCP-Ready-green?style=flat-square)](https://github.com/model-context-protocol)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**성공적인 커리어를 위한 지능형 AI 에이전트**
*자동화된 구직, 이력서 최적화 및 지원 관리*

[기능](#-기능) • [아키텍처](#-아키텍처) • [시작하기](#-시작하기) • [로드맵](#-로드맵)

[English](README.md) | [中文](README_CN.md) | [日本語](README_JP.md) | [한국어](README_KR.md) | [Français](README_FR.md) | [Deutsch](README_DE.md)

</div>

---

## 📖 소개

**JobPilot**은 **AI 에이전트**와 **Model Context Protocol (MCP)**로 구동되는 차세대 커리어 어시스턴트입니다. 개인 채용 담당자처럼 LinkedIn과 같은 플랫폼에서 끊임없이 일자리를 검색하고, 특정 직무 기술서(JD)에 맞춰 이력서를 최적화하며, 지원 프로세스까지 자동화합니다.

AI 시대를 위해 설계된 JobPilot은 전체 MCP 서버를 노출하여 Claude Desktop, OpenClaw 또는 맞춤형 에이전트와 같은 즐겨 사용하는 AI 어시스턴트와 연결하여 구직 활동을 자율적으로 처리할 수 있습니다.

> **왜 JobPilot인가요?**
> 모든 지원서마다 수동으로 이력서를 수정하는 대신, JobPilot의 에이전트가 JD를 분석하고, 관련 기술을 강조하도록 이력서를 다시 작성하고, 잠자는 동안 대신 지원서를 제출하도록 하세요.

<a href="https://glama.ai/mcp/servers/arthurpanhku/job-pilot">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/arthurpanhku/job-pilot/badge" alt="job-pilot MCP server" />
</a>

![JobPilot Dashboard](assets/dashboard-preview.jpg)

<video src="assets/grok-video-demo.mp4" controls="controls" style="max-width: 100%;">
</video>

## ✨ 기능

### 🤖 MCP-네이티브 아키텍처
- **에이전트 우선 설계**: 처음부터 Model Context Protocol (MCP) 서버로 구축되었습니다.
- **범용 호환성**: 모든 MCP 호환 클라이언트(Claude, IDE, 에이전트 프레임워크)와 원활하게 연결됩니다.

### 📄 지능형 이력서 엔진
- **컨텍스트 인식 최적화**: 마스터 프로필을 목표 JD와 비교 분석하여 초개인화된 이력서를 생성합니다.
- **ATS 친화적**: 생성된 이력서가 지원자 추적 시스템(ATS)에 최적화되도록 보장합니다.

### 🕵️ 자동화된 잡 헌터
- **스마트 검색**: 사용자의 의미론적 프로필을 기반으로 LinkedIn 및 Indeed의 구인 목록을 스크래핑하고 필터링합니다.
- **자동 지원**: 스텔스 모드 및 감지 방지 메커니즘(사람과 유사한 지연, 무작위 사용자 에이전트)이 내장된 자동 양식 작성.
- **위험 감소**: 계정 플래그를 방지하기 위한 드라이 런 기능 및 수동 확인 단계가 있는 "안전 모드".

### 📊 지원 추적
- **대시보드**: Shadcn 컴포넌트로 구축된 최신 UI로 지원 상태, 인터뷰 파이프라인 및 성공률을 시각화합니다.
- **기록**: 채용 담당자에게 보낸 모든 맞춤형 이력서 버전의 기록을 유지합니다.

## 🛠️ 기술 스택

- **프론트엔드**: 
  - [Next.js 14](https://nextjs.org/) (App Router)
  - TypeScript
  - Tailwind CSS & Lucide Icons
- **백엔드**: 
  - [FastAPI](https://fastapi.tiangolo.com/) (Python)
  - Pydantic
  - MCP SDK (Python)
- **자동화 & AI**:
  - Playwright (브라우저 자동화)
  - OpenAI / Anthropic APIs (LLM)
  - Supabase (데이터베이스 & 인증)

## 🚀 시작하기

### 필수 조건
- Node.js 18+
- Python 3.11+
- Git

### 설치

1. **저장소 복제**
   ```bash
   git clone https://github.com/yourusername/job-pilot.git
   cd job-pilot
   ```

2. **백엔드 설정**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows의 경우: venv\Scripts\activate
   pip install -r requirements.txt
   
   # API & MCP 서버 시작
   python app/main.py
   ```

3. **프론트엔드 설정**
   ```bash
   cd frontend
   npm install
   
   # UI 시작
   npm run dev
   ```

4. **앱 접속**
   - 프론트엔드: `http://localhost:3000`
   - API 문서: `http://localhost:8000/docs`

## 🗺️ 로드맵

- [x] 프로젝트 초기화 & 아키텍처 설계
- [ ] **1단계**: MCP 서버 구현 & 기본 프로필 관리
- [ ] **2단계**: LinkedIn 스크래퍼 통합 & 구인 매칭
- [ ] **3단계**: 이력서 최적화 파이프라인 (LLM)
- [ ] **4단계**: OpenClaw/Playwright를 통한 자동 지원

## 🤝 기여하기

기여는 언제나 환영합니다! 자유롭게 Pull Request를 제출해주세요.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=arthurpanhku/job-pilot&type=Date)](https://star-history.com/#arthurpanhku/job-pilot&Date)

## 📄 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다 - 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.
