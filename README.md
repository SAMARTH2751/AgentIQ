# 🤖 AgentIQ — Multi-Agent AI Research Assistant

<div align="center">

![AgentIQ Banner](https://img.shields.io/badge/AgentIQ-Multi--Agent%20AI-00BFFF?style=for-the-badge&logo=robot&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Anthropic](https://img.shields.io/badge/Claude-Sonnet%204-CC785C?style=for-the-badge&logo=anthropic&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A production-grade demonstration of Agentic AI — 4 specialized AI agents that collaboratively research, analyze, and write comprehensive reports on any topic.**

[Live Demo](#-live-demo) · [Quick Start](#-quick-start) · [Architecture](#-architecture) · [Features](#-features)

</div>

---

## 📸 Demo

> **4 AI agents working in sequence** — Planner → Researcher → Analyzer → Writer

```
User Input: "Agentic AI in Healthcare"
     ↓
🗺️  Planner Agent    → Creates structured research plan (3-8 key questions)
     ↓
🔍  Researcher Agent → Gathers comprehensive information & data
     ↓
🧠  Analyzer Agent   → Synthesizes insights, identifies gaps & trends
     ↓
✍️  Writer Agent     → Produces polished, publication-quality report
     ↓
📄  Final Report     → Downloadable Markdown/Text report
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **4 Specialized Agents** | Planner, Researcher, Analyzer, Writer — each with unique system prompts |
| 🎚️ **3 Research Depths** | Quick Overview, Standard, Deep Dive |
| 🎯 **Focus Areas** | Technical, Applications, Ethics, Trends, Comparisons |
| 📥 **Export Reports** | Download as Markdown or plain text |
| 📚 **Session History** | Access previous research sessions |
| 🎨 **Beautiful UI** | Dark navy theme with real-time agent status updates |
| 💡 **Topic Suggestions** | 8 trending CSE/AI topics pre-loaded |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- An Anthropic API key ([get one free](https://console.anthropic.com/))

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/AgentIQ.git
cd AgentIQ
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your Anthropic API key
# ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
```

### 5. Run the App
```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501** 🎉

---

## 🏗️ Architecture

### Agent Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                        AgentIQ Pipeline                         │
├─────────────┬─────────────┬─────────────┬───────────────────────┤
│  🗺️ Planner  │ 🔍 Researcher│ 🧠 Analyzer  │    ✍️ Writer          │
│             │             │             │                       │
│ Goal → Plan │ Plan → Data │ Data → Insights│ All → Final Report  │
│             │             │             │                       │
│ Bloom L1–L2 │ Bloom L2–L3 │ Bloom L4–L5 │  Bloom L5–L6          │
└─────────────┴─────────────┴─────────────┴───────────────────────┘
```

### Project Structure

```
AgentIQ/
├── 📄 app.py                  # Main Streamlit application
├── 📋 requirements.txt        # Python dependencies
├── 🔒 .env.example            # Environment template
├── 🚫 .gitignore              # Git ignore rules
│
├── 🤖 agents/
│   ├── __init__.py
│   ├── planner.py             # PlannerAgent — goal decomposition
│   ├── researcher.py          # ResearcherAgent — information gathering
│   ├── analyzer.py            # AnalyzerAgent — critical synthesis
│   └── writer.py              # WriterAgent — report generation
│
├── 🛠️ utils/
│   ├── __init__.py
│   └── helpers.py             # Formatting, file utilities
│
└── ⚙️ .streamlit/
    └── config.toml            # Streamlit theme config
```

### Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Streamlit 1.35+ | Web UI, real-time updates |
| **AI Core** | Anthropic Claude Sonnet 4 | Language model for all agents |
| **Agent Pattern** | Custom Python classes | Specialized system prompts per agent |
| **State Management** | Streamlit Session State | Session history & report storage |
| **Export** | Python built-ins | Markdown/text report download |

---

## 🎓 Academic Context

This project was developed for **CSE435 Comprehensive Seminar (2025–26)** at [Your College Name].

**Topic:** *Agentic AI: Autonomous Multi-Agent Systems for Real-World Applications*

### Course Outcome Mapping

| CO | Description | How This Project Covers It |
|----|-------------|---------------------------|
| CO1 | Relate industry/research trends | Project itself IS a 2026 trending tech |
| CO2 | Synthesize scholarly literature | Researcher agent cites real papers (ReAct, AutoGen, etc.) |
| CO3 | Apply technical/computational methods | 4-agent pipeline, API integration, state management |
| CO4 | Technical communication & visual aids | Streamlit UI, real-time pipeline visualization |
| CO5 | Scientific writing & ethical practices | Report generation, .env for key security, MIT license |
| CO6 | Limitations & future directions | Ethics section, rate limits, future enhancements listed |

---

## 🔮 Future Enhancements

- [ ] **Web Search Integration** — Real-time data via Tavily/Serper API
- [ ] **PDF Export** — Download reports as formatted PDFs
- [ ] **Multi-model Support** — Switch between Claude, GPT-4, Gemini
- [ ] **Citation Generator** — Auto-generate IEEE/APA citations
- [ ] **Agent Memory** — Cross-session learning with vector DB (Pinecone/FAISS)
- [ ] **Collaborative Mode** — Multi-user research sessions
- [ ] **REST API** — Expose pipeline as a REST endpoint

---

## ⚠️ Limitations

- **Rate Limits**: Subject to Anthropic API rate limits (free tier: ~5 req/min)
- **Knowledge Cutoff**: Claude's training data cutoff applies to research depth
- **No Real-time Web Search**: Currently uses model knowledge (see Future Enhancements)
- **Cost**: Each research session uses ~2,000–5,000 tokens across 4 API calls

---

## 🔐 Security

- **Never commit** your `.env` file or API key to Git
- API key is entered via UI or `.env` file — never hardcoded
- `.gitignore` excludes all sensitive files by default
- Use [Streamlit Secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) for cloud deployments

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**[Your Name]**
- 🎓 B.Tech CSE — [Your College], Batch [Year]
- 📧 [your.email@example.com]
- 🔗 [LinkedIn](https://linkedin.com/in/yourprofile)
- 🐙 [GitHub](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- [Anthropic](https://anthropic.com) for the Claude API
- [Streamlit](https://streamlit.io) for the amazing web framework
- Research inspired by: [ReAct (Yao et al., 2023)](https://arxiv.org/abs/2210.03629), [AutoGen (Wu et al., 2023)](https://arxiv.org/abs/2308.08155)
- Guided by: **[Prof. Name]** — CSE435 Course Instructor

---

<div align="center">
⭐ If this project helped you, please consider giving it a star!

*Made with ❤️ for CSE435 Comprehensive Seminar*
</div>
