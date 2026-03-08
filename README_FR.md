<div align="center">

<img src="assets/logo.jpg" width="200" alt="JobPilot Logo" style="border-radius: 20px;" />

# JobPilot ✈️

![JobPilot Banner](https://img.shields.io/badge/JobPilot-AI_Career_Co--Pilot-blue?style=for-the-badge&logo=openai)

[![Next.js](https://img.shields.io/badge/Next.js-14-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MCP](https://img.shields.io/badge/MCP-Ready-green?style=flat-square)](https://github.com/model-context-protocol)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**Votre Agent IA Intelligent pour la Réussite Professionnelle**
*Recherche d'emploi automatisée, Optimisation de CV et Gestion des candidatures*

[Fonctionnalités](#-fonctionnalités) • [Architecture](#-architecture) • [Démarrage](#-démarrage) • [Feuille de route](#-feuille-de-route)

[English](README.md) | [中文](README_CN.md) | [日本語](README_JP.md) | [한국어](README_KR.md) | [Français](README_FR.md) | [Deutsch](README_DE.md)

</div>

---

## 📖 Introduction

**JobPilot** est un assistant de carrière de nouvelle génération propulsé par des **Agents IA** et le **Model Context Protocol (MCP)**. Il agit comme votre recruteur personnel, cherchant inlassablement des emplois sur des plateformes comme LinkedIn, optimisant votre CV pour des descriptions de poste spécifiques (JD), et automatisant même le processus de candidature.

Conçu pour l'ère de l'IA, JobPilot expose un serveur MCP complet, vous permettant de le connecter avec vos assistants IA préférés (comme Claude Desktop, OpenClaw ou des agents personnalisés) pour gérer votre recherche d'emploi de manière autonome.

> **Pourquoi JobPilot ?**
> Au lieu d'ajuster manuellement votre CV pour chaque candidature, laissez les agents de JobPilot analyser la description de poste, réécrire votre CV pour mettre en évidence les compétences pertinentes, et soumettre la candidature pour vous—pendant que vous dormez.

<a href="https://glama.ai/mcp/servers/arthurpanhku/job-pilot">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/arthurpanhku/job-pilot/badge" alt="job-pilot MCP server" />
</a>

![JobPilot Dashboard](assets/dashboard-preview.jpg)

<video src="assets/grok-video-demo.mp4" controls="controls" style="max-width: 100%;">
</video>

## ✨ Fonctionnalités

### 🤖 Architecture Native MCP
- **Conception Agent-First** : Construit à partir de zéro comme un serveur Model Context Protocol (MCP).
- **Compatibilité Universelle** : Se connecte de manière transparente avec tout client compatible MCP (Claude, IDE, frameworks d'agents).

### 📄 Moteur de CV Intelligent
- **Optimisation Contextuelle** : Analyse votre profil maître par rapport aux JD cibles pour générer des CV hyper-personnalisés.
- **Compatible ATS** : Assure que les CV générés sont optimisés pour les systèmes de suivi des candidats.

### 🕵️ Chasseur d'Emploi Automatisé
- **Recherche Intelligente** : Scrape et filtre les offres d'emploi de LinkedIn et Indeed en fonction de votre profil sémantique.
- **Candidature Auto** : Remplissage automatique de formulaires avec mode furtif intégré et mécanismes anti-détection (délais humains, agents utilisateurs aléatoires).
- **Réduction des Risques** : "Mode sans échec" avec capacité de test à blanc et étapes de confirmation manuelle pour éviter les blocages de compte.

### 📊 Suivi des Candidatures
- **Tableau de Bord** : UI moderne construite avec des composants Shadcn pour visualiser le statut de vos candidatures, le pipeline d'entretiens et les taux de réussite.
- **Historique** : Conservez une trace de chaque version de CV adaptée envoyée aux recruteurs.

## 🛠️ Stack Technique

- **Frontend** : 
  - [Next.js 14](https://nextjs.org/) (App Router)
  - TypeScript
  - Tailwind CSS & Lucide Icons
- **Backend** : 
  - [FastAPI](https://fastapi.tiangolo.com/) (Python)
  - Pydantic
  - SDK MCP (Python)
- **Automatisation & IA** :
  - Playwright (Automatisation de navigateur)
  - API OpenAI / Anthropic (LLM)
  - Supabase (Base de données & Auth)

## 🚀 Démarrage

### Prérequis
- Node.js 18+
- Python 3.11+
- Git

### Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/yourusername/job-pilot.git
   cd job-pilot
   ```

2. **Configuration Backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   pip install -r requirements.txt
   
   # Démarrer l'API & le Serveur MCP
   python app/main.py
   ```

3. **Configuration Frontend**
   ```bash
   cd frontend
   npm install
   
   # Démarrer l'UI
   npm run dev
   ```

4. **Accéder à l'Application**
   - Frontend : `http://localhost:3000`
   - Docs API : `http://localhost:8000/docs`

## 🗺️ Feuille de route

- [x] Initialisation du projet & Conception de l'architecture
- [ ] **Phase 1** : Implémentation du serveur MCP & Gestion de base du profil
- [ ] **Phase 2** : Intégration du Scraper LinkedIn & Matching d'emploi
- [ ] **Phase 3** : Pipeline d'optimisation de CV (LLM)
- [ ] **Phase 4** : Candidature automatisée via OpenClaw/Playwright

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une Pull Request.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=arthurpanhku/job-pilot&type=Date)](https://star-history.com/#arthurpanhku/job-pilot&Date)

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
