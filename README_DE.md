<div align="center">

<img src="assets/logo.jpg" width="200" alt="JobPilot Logo" style="border-radius: 20px;" />

# JobPilot ✈️

![JobPilot Banner](https://img.shields.io/badge/JobPilot-AI_Career_Co--Pilot-blue?style=for-the-badge&logo=openai)

[![Next.js](https://img.shields.io/badge/Next.js-14-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MCP](https://img.shields.io/badge/MCP-Ready-green?style=flat-square)](https://github.com/model-context-protocol)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**Ihr intelligenter KI-Agent für Karriereerfolg**
*Automatisierte Jobsuche, Lebenslauf-Optimierung und Bewerbungsmanagement*

[Funktionen](#-funktionen) • [Architektur](#-architektur) • [Erste Schritte](#-erste-schritte) • [Roadmap](#-roadmap)

[English](README.md) | [中文](README_CN.md) | [日本語](README_JP.md) | [한국어](README_KR.md) | [Français](README_FR.md) | [Deutsch](README_DE.md)

</div>

---

## 📖 Einführung

**JobPilot** ist ein Karriereassistent der nächsten Generation, angetrieben von **KI-Agenten** und dem **Model Context Protocol (MCP)**. Er agiert als Ihr persönlicher Recruiter, der unermüdlich auf Plattformen wie LinkedIn nach Jobs sucht, Ihren Lebenslauf für spezifische Stellenbeschreibungen (JD) optimiert und sogar den Bewerbungsprozess automatisiert.

JobPilot wurde für das KI-Zeitalter entwickelt und stellt einen vollständigen MCP-Server bereit, mit dem Sie ihn mit Ihren bevorzugten KI-Assistenten (wie Claude Desktop, OpenClaw oder benutzerdefinierten Agenten) verbinden können, um Ihre Jobsuche autonom zu steuern.

> **Warum JobPilot?**
> Anstatt Ihren Lebenslauf für jede Bewerbung manuell anzupassen, lassen Sie die Agenten von JobPilot die Stellenbeschreibung analysieren, Ihren Lebenslauf umschreiben, um relevante Fähigkeiten hervorzuheben, und die Bewerbung für Sie einreichen – während Sie schlafen.

<a href="https://glama.ai/mcp/servers/arthurpanhku/job-pilot">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/arthurpanhku/job-pilot/badge" alt="job-pilot MCP server" />
</a>

![JobPilot Dashboard](assets/dashboard-preview.jpg)

<video src="assets/grok-video-demo.mp4" controls="controls" style="max-width: 100%;">
</video>

## ✨ Funktionen

### 🤖 MCP-Native Architektur
- **Agent-First Design**: Von Grund auf als Model Context Protocol (MCP) Server entwickelt.
- **Universelle Kompatibilität**: Verbindet sich nahtlos mit jedem MCP-konformen Client (Claude, IDEs, Agenten-Frameworks).

### 📄 Intelligente Lebenslauf-Engine
- **Kontextbezogene Optimierung**: Analysiert Ihr Master-Profil gegen Ziel-JDs, um hyperpersonalisierte Lebensläufe zu generieren.
- **ATS-Freundlich**: Stellt sicher, dass generierte Lebensläufe für Bewerber-Tracking-Systeme optimiert sind.

### 🕵️ Automatisierter Job-Jäger
- **Intelligente Suche**: Scrapt und filtert Jobangebote von LinkedIn und Indeed basierend auf Ihrem semantischen Profil.
- **Auto-Bewerbung**: Automatisches Ausfüllen von Formularen mit integriertem Stealth-Modus und Anti-Erkennungs-Mechanismen (menschliche Verzögerungen, zufällige User-Agents).
- **Risikominimierung**: "Sicherer Modus" mit Probelauf-Funktion und manuellen Bestätigungsschritten, um Kontosperrungen zu vermeiden.

### 📊 Bewerbungs-Tracking
- **Dashboard**: Moderne Benutzeroberfläche mit Shadcn-Komponenten zur Visualisierung Ihres Bewerbungsstatus, Interview-Pipeline und Erfolgsquoten.
- **Verlauf**: Behalten Sie eine Aufzeichnung jeder angepassten Lebenslaufversion, die an Recruiter gesendet wurde.

## 🛠️ Tech Stack

- **Frontend**: 
  - [Next.js 14](https://nextjs.org/) (App Router)
  - TypeScript
  - Tailwind CSS & Lucide Icons
- **Backend**: 
  - [FastAPI](https://fastapi.tiangolo.com/) (Python)
  - Pydantic
  - MCP SDK (Python)
- **Automatisierung & KI**:
  - Playwright (Browser-Automatisierung)
  - OpenAI / Anthropic APIs (LLM)
  - Supabase (Datenbank & Auth)

## 🚀 Erste Schritte

### Voraussetzungen
- Node.js 18+
- Python 3.11+
- Git

### Installation

1. **Repository klonen**
   ```bash
   git clone https://github.com/yourusername/job-pilot.git
   cd job-pilot
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Unter Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
   # API & MCP Server starten
   python app/main.py
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   
   # UI starten
   npm run dev
   ```

4. **App zugreifen**
   - Frontend: `http://localhost:3000`
   - API Docs: `http://localhost:8000/docs`

## 🗺️ Roadmap

- [x] Projektinitialisierung & Architekturdesign
- [ ] **Phase 1**: MCP-Server-Implementierung & Basis-Profilmanagement
- [ ] **Phase 2**: LinkedIn Scraper Integration & Job-Matching
- [ ] **Phase 3**: Lebenslauf-Optimierungs-Pipeline (LLM)
- [ ] **Phase 4**: Automatisierte Bewerbung via OpenClaw/Playwright

## 🤝 Mitwirken

Beiträge sind willkommen! Fühlen Sie sich frei, einen Pull Request einzureichen.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=arthurpanhku/job-pilot&type=Date)](https://star-history.com/#arthurpanhku/job-pilot&Date)

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.
