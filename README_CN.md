<div align="center">

<img src="assets/logo.jpg" width="200" alt="JobPilot Logo" style="border-radius: 20px;" />

# JobPilot ✈️

![JobPilot Banner](https://img.shields.io/badge/JobPilot-AI_Career_Co--Pilot-blue?style=for-the-badge&logo=openai)

[![Next.js](https://img.shields.io/badge/Next.js-14-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MCP](https://img.shields.io/badge/MCP-Ready-green?style=flat-square)](https://github.com/model-context-protocol)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**您的 AI 职业成功智能代理**
*自动化职位搜索、简历优化和申请管理*

[功能](#-功能) • [架构](#-架构) • [快速开始](#-快速开始) • [路线图](#-路线图)

[English](README.md) | [中文](README_CN.md) | [日本語](README_JP.md) | [한국어](README_KR.md) | [Français](README_FR.md) | [Deutsch](README_DE.md)

</div>

---

## 📖 简介

**JobPilot** 是下一代职业助手，由 **AI Agents** 和 **Model Context Protocol (MCP)** 驱动。它就像您的私人招聘专员，孜孜不倦地在 LinkedIn 等平台上搜索工作，针对特定的职位描述 (JD) 优化您的简历，甚至自动完成申请流程。

JobPilot 专为 AI 时代设计，公开了一个完整的 MCP 服务器，允许您将其与您最喜欢的 AI 助手（如 Claude Desktop、OpenClaw 或自定义代理）连接，以自主处理您的求职工作。

> **为什么选择 JobPilot？**
> 无需为每个申请手动调整简历，让 JobPilot 的代理分析 JD，重写您的简历以突出相关技能，并在您睡觉时为您提交申请。

<a href="https://glama.ai/mcp/servers/arthurpanhku/job-pilot">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/arthurpanhku/job-pilot/badge" alt="job-pilot MCP server" />
</a>

![JobPilot Dashboard](assets/dashboard-preview.jpg)

<video src="assets/grok-video-demo.mp4" controls="controls" style="max-width: 100%;">
</video>

## ✨ 功能

### 🤖 MCP 原生架构
- **代理优先设计**：从底层构建为 Model Context Protocol (MCP) 服务器。
- **通用兼容性**：与任何符合 MCP 标准的客户端（Claude、IDE、代理框架）无缝连接。

### 📄 智能简历引擎
- **上下文感知优化**：根据目标 JD 分析您的主简历，生成高度个性化的简历。
- **ATS 友好**：确保生成的简历针对申请人跟踪系统进行了优化。

### 🕵️ 自动化职位猎人
- **智能搜索**：根据您的语义资料，抓取并筛选 LinkedIn 和 Indeed 上的职位列表。
- **自动申请**：内置隐身模式和反检测机制（拟人化延迟、随机用户代理）的自动填表功能。
- **风险降低**：“安全模式”具有试运行功能和手动确认步骤，以避免账户被标记。

### 📊 申请跟踪
- **仪表盘**：使用 Shadcn 组件构建的现代化 UI，可视化您的申请状态、面试流程和成功率。
- **历史记录**：保留发送给招聘人员的每个定制简历版本的记录。

## 🛠️ 技术栈

- **前端**: 
  - [Next.js 14](https://nextjs.org/) (App Router)
  - TypeScript
  - Tailwind CSS & Lucide Icons
- **后端**: 
  - [FastAPI](https://fastapi.tiangolo.com/) (Python)
  - Pydantic
  - MCP SDK (Python)
- **自动化 & AI**:
  - Playwright (浏览器自动化)
  - OpenAI / Anthropic APIs (LLM)
  - Supabase (数据库 & 认证)

## 🚀 快速开始

### 前提条件
- Node.js 18+
- Python 3.11+
- Git

### 安装

1. **克隆仓库**
   ```bash
   git clone https://github.com/yourusername/job-pilot.git
   cd job-pilot
   ```

2. **后端设置**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
   # 启动 API & MCP 服务器
   python app/main.py
   ```

3. **前端设置**
   ```bash
   cd frontend
   npm install
   
   # 启动 UI
   npm run dev
   ```

4. **访问应用**
   - 前端: `http://localhost:3000`
   - API 文档: `http://localhost:8000/docs`

## 🗺️ 路线图

- [x] 项目初始化与架构设计
- [ ] **阶段 1**: MCP 服务器实现与基础资料管理
- [ ] **阶段 2**: LinkedIn 爬虫集成与职位匹配
- [ ] **阶段 3**: 简历优化管道 (LLM)
- [ ] **阶段 4**: 通过 OpenClaw/Playwright 自动申请

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=arthurpanhku/job-pilot&type=Date)](https://star-history.com/#arthurpanhku/job-pilot&Date)

## 📄 许可证

本项目基于 MIT 许可证开源 - 详情请参阅 [LICENSE](LICENSE) 文件。
