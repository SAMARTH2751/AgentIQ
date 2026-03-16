# 📦 AgentIQ — Complete Setup & Deployment Guide
## How to Run on Laptop · Upload to GitHub · Deploy on LinkedIn, CV, Portfolio

---

# PART 1: RUN ON YOUR LAPTOP
## ════════════════════════════════════════════

### Step 1 — Install Python
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or 3.12 (latest stable)
3. During install: ✅ CHECK "Add Python to PATH"
4. Verify: Open CMD/Terminal and run:
   ```
   python --version
   ```
   You should see: `Python 3.11.x`

---

### Step 2 — Get Your Anthropic API Key
1. Go to: https://console.anthropic.com/
2. Sign up for a free account
3. Click "API Keys" in sidebar
4. Click "Create Key" → Copy it (starts with `sk-ant-api03-...`)
5. ⚠️ NEVER share this key or put it on GitHub

---

### Step 3 — Download the Project
**Option A: Download ZIP (easiest)**
1. Go to your GitHub repo (after uploading - see Part 2)
2. Click green "Code" button → "Download ZIP"
3. Extract to a folder like: `C:\Projects\AgentIQ\`

**Option B: Clone with Git**
```bash
git clone https://github.com/YOUR_USERNAME/AgentIQ.git
cd AgentIQ
```

---

### Step 4 — Set Up Virtual Environment
Open CMD (Windows) or Terminal (Mac/Linux) in the project folder:

**Windows:**
```cmd
cd C:\Projects\AgentIQ
python -m venv venv
venv\Scripts\activate
```
You'll see `(venv)` appear in your terminal — that means it's active.

**Mac/Linux:**
```bash
cd ~/Projects/AgentIQ
python3 -m venv venv
source venv/bin/activate
```

---

### Step 5 — Install Dependencies
```bash
pip install -r requirements.txt
```
This installs: streamlit, anthropic, python-dotenv

---

### Step 6 — Add Your API Key
1. In the project folder, find `.env.example`
2. Copy it and rename to `.env`
3. Open `.env` in Notepad/VS Code
4. Replace the placeholder with your key:
   ```
   ANTHROPIC_API_KEY=sk-ant-api03-YOUR-REAL-KEY-HERE
   ```
5. Save the file

---

### Step 7 — Run the App 🚀
```bash
streamlit run app.py
```
Your browser will open automatically at: **http://localhost:8501**

If it doesn't open, manually go to: http://localhost:8501

---

### How to Use AgentIQ
1. Enter your Anthropic API key in the sidebar (or it reads from .env)
2. Type a research topic (e.g., "Agentic AI in Healthcare")
3. Choose research depth: Quick / Standard / Deep Dive
4. Select focus areas (optional)
5. Click "🚀 Launch Agent Pipeline"
6. Watch 4 agents work in real-time!
7. Go to "View Report" tab to see the full report
8. Download as Markdown or Text



---
---

# PART 2: UPLOAD TO GITHUB
## ════════════════════════════════════════════

### Step 1 — Install Git
Download from: https://git-scm.com/downloads
Run the installer with default settings.

Verify: `git --version`

---

### Step 2 — Create GitHub Account
Go to: https://github.com
Sign up with your email.

---

### Step 3 — Create a New Repository
1. Click the "+" icon (top right) → "New repository"
2. Settings:
   - **Repository name:** `AgentIQ`
   - **Description:** `🤖 Multi-Agent AI Research Assistant built with Python, Streamlit & Claude API | CSE435 Seminar Project`
   - **Visibility:** Public ✅ (so it appears on your profile)
   - **Initialize:** UNCHECK everything (we'll push our own files)
3. Click "Create repository"
4. Copy the repository URL (looks like: `https://github.com/yourusername/AgentIQ.git`)

---

### Step 4 — Configure Git (first time only)
```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@gmail.com"
```

---

### Step 5 — Push Your Project to GitHub
Navigate to your project folder in terminal:

```bash
cd C:\Projects\AgentIQ        # (Windows) adjust path as needed
# OR
cd ~/Projects/AgentIQ         # (Mac/Linux)

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "🚀 Initial commit: AgentIQ Multi-Agent AI Research Assistant"

# Connect to GitHub
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/AgentIQ.git

# Push!
git push -u origin main
```

Enter your GitHub username and password when prompted.
(For password, use a Personal Access Token — see below)

---

### Step 5b — Create Personal Access Token (GitHub requires this)
1. GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. "Generate new token"
3. Give it a name, select "repo" scope
4. Copy the token
5. Use this token as your "password" when pushing

---

### Step 6 — Make Your Repository Look Professional
On GitHub.com, in your repository:

1. **Add Topics/Tags:** Click "About" gear → Add topics:
   `python`, `streamlit`, `ai`, `multi-agent`, `anthropic`, `llm`, `agentic-ai`, `research-tool`, `cse435`

2. **Add Description:** 
   `🤖 Multi-Agent AI Research Assistant | 4 AI agents collaborate to research, analyze & write reports | Python + Streamlit + Claude API`

3. **Pin it to your profile:**
   Go to your GitHub profile → "Customize your profile" → "Pin repositories" → Select AgentIQ

---

### Step 7 — Deploy Live on Streamlit Cloud (FREE)
Make your app accessible online with a shareable URL!

1. Go to: https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select: Repository = AgentIQ, Branch = main, Main file = app.py
5. Under "Advanced settings" → "Secrets":
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-api03-your-key-here"
   ```
6. Click "Deploy!"

You'll get a URL like: **https://agentiq-yourname.streamlit.app**
Share this everywhere — LinkedIn, CV, portfolio!



---
---

# PART 3: ADD TO LINKEDIN
## ════════════════════════════════════════════

### Add to "Projects" Section
1. Go to your LinkedIn profile
2. Scroll down → Click "Add section" → "Projects"
3. Fill in:
   - **Project Name:** AgentIQ — Multi-Agent AI Research Assistant
   - **Description:**
     ```
     Built a production-grade multi-agent AI system where 4 specialized AI agents 
     (Planner, Researcher, Analyzer, Writer) autonomously collaborate to produce 
     comprehensive research reports on any topic.
     
     Tech Stack: Python · Streamlit · Anthropic Claude API · Multi-Agent Architecture
     
     🏆 CSE435 Comprehensive Seminar Project (2025–26)
     • Implemented agent-to-agent communication patterns (ReAct-inspired)
     • 3 configurable research depths with 6 focus area options
     • Real-time pipeline visualization with report export (Markdown/Text)
     • Deployed live on Streamlit Community Cloud
     
     GitHub: github.com/yourusername/AgentIQ
     Live Demo: your-app.streamlit.app
     ```
   - **Skills:** Python, Artificial Intelligence, Machine Learning, Streamlit, API Development
   - **Associated with:** [Your College Name]
   - **Project URL:** Your Streamlit Cloud URL
4. Click "Save"

---

### Make a LinkedIn Post (Gets attention!)
Copy and customize this post:

```
🚀 Excited to share my CSE435 Seminar Project: AgentIQ!

I built a Multi-Agent AI Research Assistant where 4 specialized AI agents 
collaborate autonomously to research any topic:

🗺️ Planner Agent → Breaks goal into sub-tasks
🔍 Researcher Agent → Gathers comprehensive data  
🧠 Analyzer Agent → Synthesizes insights & trends
✍️ Writer Agent → Produces polished reports

This isn't just theory — it's a working application built with:
→ Python + Streamlit for the web interface
→ Anthropic Claude API as the AI backbone
→ Custom agent architecture inspired by ReAct (NeurIPS 2023)

Agentic AI is Gartner's #1 tech trend for 2025–26, and I've implemented 
it from scratch!

🔗 Live Demo: [your-streamlit-url]
🐙 GitHub: [your-github-url]

#AgenticAI #Python #MachineLearning #Streamlit #AnthropicClaude #OpenSource
#CSE #ArtificialIntelligence #StudentProject #AI2026
```

---
---

# PART 4: ADD TO CV & RESUME
## ════════════════════════════════════════════

### Projects Section (CV/Resume Format)

```
PROJECTS
─────────────────────────────────────────────────────────────

AgentIQ — Multi-Agent AI Research Assistant              2025–26
GitHub: github.com/yourusername/AgentIQ
Demo: your-app.streamlit.app

• Designed and implemented a 4-agent AI pipeline (Planner, Researcher, 
  Analyzer, Writer) using Anthropic Claude Sonnet 4 API
• Built full-stack web application with Python + Streamlit featuring 
  real-time agent status visualization and session management
• Implemented configurable research depths and focus areas with 
  Markdown/text report export functionality
• Deployed on Streamlit Community Cloud with API key security best 
  practices (dotenv, gitignore, no hardcoded secrets)
• Tech Stack: Python 3.11, Streamlit 1.35, Anthropic API, Git

Academic Context: CSE435 Comprehensive Seminar, [College Name]
```

### Skills to Add to Resume
Under "Technical Skills":
- **AI/ML:** Agentic AI, Large Language Models (LLMs), Multi-Agent Systems, Prompt Engineering
- **Frameworks:** Streamlit, Anthropic SDK, LangChain (conceptual)
- **Tools:** Git, GitHub, VS Code, Python Virtual Environments

---
---

# PART 5: ADD TO PORTFOLIO WEBSITE
## ════════════════════════════════════════════

### If you have a GitHub Pages portfolio:

Create a project card in your portfolio HTML:
```html
<div class="project-card featured">
  <div class="project-badge">🏆 Featured Project</div>
  <h3>🤖 AgentIQ</h3>
  <p class="subtitle">Multi-Agent AI Research Assistant</p>
  <p>4 specialized AI agents collaborate to research, analyze, and write 
  comprehensive reports on any topic. Built with Python, Streamlit & Claude API.</p>
  <div class="tech-tags">
    <span>Python</span><span>Streamlit</span>
    <span>Anthropic API</span><span>Multi-Agent AI</span>
  </div>
  <div class="project-links">
    <a href="https://agentiq-you.streamlit.app" class="btn-demo">🚀 Live Demo</a>
    <a href="https://github.com/you/AgentIQ" class="btn-github">🐙 GitHub</a>
  </div>
</div>
```

---
---

# QUICK REFERENCE CHEATSHEET
## ════════════════════════════════════════════

| Platform | What to Do | Link to Share |
|----------|-----------|---------------|
| 💻 Laptop | `streamlit run app.py` | http://localhost:8501 |
| 🐙 GitHub | Push code, add README | github.com/you/AgentIQ |
| 🌐 Live Demo | Deploy Streamlit Cloud | you.streamlit.app |
| 💼 LinkedIn | Add to Projects section | linkedin.com/in/you |
| 📄 Resume/CV | Add under Projects | — |
| 🌍 Portfolio | Add project card | your-portfolio.com |

## Most Important Links to Get:
1. ✅ GitHub URL: `github.com/YOUR_USERNAME/AgentIQ`
2. ✅ Live Demo URL: `agentiq-yourname.streamlit.app`
3. ✅ API Key: `console.anthropic.com`

---
*AgentIQ — CSE435 Comprehensive Seminar Project 2025–26*
