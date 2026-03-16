"""
AgentIQ — Multi-Agent AI Research Assistant
CSE435 Comprehensive Seminar Project
"""

import streamlit as st
import time
from agents.planner import PlannerAgent
from agents.researcher import ResearcherAgent
from agents.analyzer import AnalyzerAgent
from agents.writer import WriterAgent
from utils.helpers import format_report, get_topic_suggestions

# ── Page Config ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AgentIQ — Multi-Agent Research Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ─────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

  html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }

  .main { background: #07112E; }
  .stApp { background: linear-gradient(135deg, #07112E 0%, #0E2A6E 50%, #07112E 100%); }

  .hero-title {
    font-size: 3.2rem; font-weight: 700; color: #FFFFFF;
    text-align: center; letter-spacing: -1px; margin-bottom: 0.2rem;
  }
  .hero-sub {
    font-size: 1.1rem; color: #00BFFF; text-align: center;
    font-weight: 300; margin-bottom: 2rem;
  }
  .agent-card {
    background: rgba(14, 42, 110, 0.6); border: 1px solid rgba(0,191,255,0.3);
    border-radius: 12px; padding: 1rem 1.2rem; margin: 0.5rem 0;
    backdrop-filter: blur(10px);
  }
  .agent-card.active {
    border-color: #00BFFF; box-shadow: 0 0 20px rgba(0,191,255,0.3);
    background: rgba(0,191,255,0.1);
  }
  .agent-card.done {
    border-color: #00C853; box-shadow: 0 0 10px rgba(0,200,83,0.2);
  }
  .agent-name { font-size: 0.9rem; font-weight: 600; color: #00BFFF; }
  .agent-status { font-size: 0.8rem; color: #8896AA; font-family: 'JetBrains Mono', monospace; }
  .stat-card {
    background: rgba(14, 42, 110, 0.5); border: 1px solid rgba(0,191,255,0.2);
    border-radius: 10px; padding: 1rem; text-align: center;
  }
  .stat-number { font-size: 2rem; font-weight: 700; color: #00BFFF; }
  .stat-label { font-size: 0.75rem; color: #8896AA; text-transform: uppercase; letter-spacing: 1px; }
  .report-box {
    background: rgba(7, 17, 46, 0.8); border: 1px solid rgba(0,191,255,0.2);
    border-radius: 12px; padding: 1.5rem; color: #E8F0FE;
    font-family: 'Space Grotesk', sans-serif; line-height: 1.8;
  }
  .badge {
    display: inline-block; background: rgba(0,191,255,0.15);
    color: #00BFFF; border: 1px solid rgba(0,191,255,0.4);
    border-radius: 20px; padding: 2px 12px; font-size: 0.75rem;
    font-weight: 600; margin: 2px;
  }
  .stButton > button {
    background: linear-gradient(135deg, #00BFFF, #0E2A6E) !important;
    color: white !important; border: none !important;
    border-radius: 8px !important; font-weight: 600 !important;
    font-size: 1rem !important; padding: 0.6rem 2rem !important;
    width: 100% !important; transition: all 0.3s !important;
  }
  .stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(0,191,255,0.4) !important;
  }
  div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea {
    background: rgba(14,42,110,0.5) !important; color: white !important;
    border: 1px solid rgba(0,191,255,0.3) !important; border-radius: 8px !important;
  }
  .stSelectbox div[data-baseweb="select"] {
    background: rgba(14,42,110,0.5) !important;
  }
  div[data-testid="stSidebar"] { background: #07112E !important; border-right: 1px solid rgba(0,191,255,0.15); }
</style>
""", unsafe_allow_html=True)


# ── Session State ──────────────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "current_report" not in st.session_state:
    st.session_state.current_report = None


# ── Sidebar ────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🤖 AgentIQ")
    st.markdown("*Multi-Agent Research Assistant*")
    st.divider()

    api_key = st.text_input(
        "🔑 Anthropic API Key",
        type="password",
        value=st.session_state.api_key,
        placeholder="sk-ant-api03-...",
        help="Get your key from console.anthropic.com"
    )
    if api_key:
        st.session_state.api_key = api_key
        st.success("✅ API Key saved")

    st.divider()
    st.markdown("#### 🏗️ Agent Pipeline")

    agents_info = [
        ("🗺️", "Planner Agent",     "Decomposes goal into sub-tasks"),
        ("🔍", "Researcher Agent",  "Finds key facts & data"),
        ("🧠", "Analyzer Agent",    "Synthesizes & critiques findings"),
        ("✍️", "Writer Agent",      "Produces structured report"),
    ]
    for icon, name, desc in agents_info:
        st.markdown(f"""
        <div class="agent-card">
          <div class="agent-name">{icon} {name}</div>
          <div class="agent-status">{desc}</div>
        </div>""", unsafe_allow_html=True)

    st.divider()
    st.markdown("#### 📚 Session History")
    if st.session_state.history:
        for i, h in enumerate(reversed(st.session_state.history[-5:])):
            if st.button(f"📄 {h['topic'][:25]}...", key=f"hist_{i}"):
                st.session_state.current_report = h
    else:
        st.caption("No research sessions yet")

    st.divider()
    st.markdown("""
    <div style='color: #8896AA; font-size: 0.75rem; text-align:center;'>
    CSE435 Seminar Project<br>
    Built with Python + Streamlit + Claude API<br><br>
    <a href='https://github.com' style='color:#00BFFF;'>GitHub</a> ·
    <a href='https://linkedin.com' style='color:#00BFFF;'>LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)


# ── Hero Header ────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">🤖 AgentIQ</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Multi-Agent AI Research Assistant · Powered by Claude</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
stats = [("4", "AI Agents"), ("3", "Research Modes"), ("∞", "Topics"), ("100%", "Open Source")]
for col, (num, label) in zip([col1, col2, col3, col4], stats):
    with col:
        st.markdown(f"""
        <div class="stat-card">
          <div class="stat-number">{num}</div>
          <div class="stat-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ── Main Input ─────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🔬 New Research", "📋 View Report", "ℹ️ About"])

with tab1:
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown("#### 🎯 Research Topic")
        topic = st.text_input(
            "Enter your topic",
            placeholder="e.g., Agentic AI in Healthcare, Quantum Computing 2026, LLM Memory Systems...",
            label_visibility="collapsed"
        )

        depth = st.select_slider(
            "Research Depth",
            options=["Quick Overview", "Standard", "Deep Dive"],
            value="Standard"
        )

        focus_areas = st.multiselect(
            "Focus Areas (optional)",
            ["Technical Implementation", "Industry Applications", "Research Papers",
             "Ethical Implications", "Future Trends", "Comparisons & Benchmarks"],
            default=["Technical Implementation", "Industry Applications"]
        )

    with col_right:
        st.markdown("#### 💡 Suggested Topics")
        suggestions = get_topic_suggestions()
        for s in suggestions:
            if st.button(s, key=f"sug_{s}"):
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Launch Agent Pipeline", type="primary"):
        if not st.session_state.api_key:
            st.error("⚠️ Please enter your Anthropic API key in the sidebar first!")
        elif not topic.strip():
            st.error("⚠️ Please enter a research topic!")
        else:
            # ── Agent Pipeline Execution ────────────────────────────
            st.markdown("---")
            st.markdown("### ⚡ Agent Pipeline Running...")

            progress_cols = st.columns(4)
            placeholders = [c.empty() for c in progress_cols]
            agent_names = ["🗺️ Planner", "🔍 Researcher", "🧠 Analyzer", "✍️ Writer"]

            def update_status(idx, status, done=False, active=False):
                cls = "done" if done else ("active" if active else "")
                icon = "✅" if done else ("⏳" if active else "⬜")
                placeholders[idx].markdown(f"""
                <div class="agent-card {cls}">
                  <div class="agent-name">{agent_names[idx]}</div>
                  <div class="agent-status">{icon} {status}</div>
                </div>""", unsafe_allow_html=True)

            # Initialize all as waiting
            for i in range(4):
                update_status(i, "Waiting...")

            output_placeholder = st.empty()
            report_data = {"topic": topic, "sections": {}, "metadata": {}}

            try:
                # AGENT 1: Planner
                update_status(0, "Planning research strategy...", active=True)
                planner = PlannerAgent(st.session_state.api_key)
                with output_placeholder.container():
                    st.info("🗺️ **Planner Agent** is breaking down your topic...")
                plan = planner.run(topic, depth, focus_areas)
                report_data["sections"]["plan"] = plan
                update_status(0, "Plan created ✓", done=True)

                # AGENT 2: Researcher
                update_status(1, "Researching topic...", active=True)
                researcher = ResearcherAgent(st.session_state.api_key)
                with output_placeholder.container():
                    st.info("🔍 **Researcher Agent** is gathering information...")
                research = researcher.run(topic, plan, depth)
                report_data["sections"]["research"] = research
                update_status(1, "Research complete ✓", done=True)

                # AGENT 3: Analyzer
                update_status(2, "Analyzing findings...", active=True)
                analyzer = AnalyzerAgent(st.session_state.api_key)
                with output_placeholder.container():
                    st.info("🧠 **Analyzer Agent** is synthesizing insights...")
                analysis = analyzer.run(topic, research, focus_areas)
                report_data["sections"]["analysis"] = analysis
                update_status(2, "Analysis done ✓", done=True)

                # AGENT 4: Writer
                update_status(3, "Writing final report...", active=True)
                writer = WriterAgent(st.session_state.api_key)
                with output_placeholder.container():
                    st.info("✍️ **Writer Agent** is composing your report...")
                final_report = writer.run(topic, plan, research, analysis)
                report_data["sections"]["report"] = final_report
                report_data["metadata"] = {
                    "depth": depth,
                    "focus": focus_areas,
                    "agents_used": 4,
                    "timestamp": time.strftime("%Y-%m-%d %H:%M")
                }
                update_status(3, "Report ready ✓", done=True)

                output_placeholder.empty()
                st.session_state.current_report = report_data
                st.session_state.history.append(report_data)

                st.success("✅ All 4 agents completed! View your report in the **View Report** tab.")
                st.balloons()

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Tip: Check your API key and internet connection.")


with tab2:
    if st.session_state.current_report:
        r = st.session_state.current_report
        st.markdown(f"### 📋 Research Report: *{r['topic']}*")

        if r.get("metadata"):
            m = r["metadata"]
            cols = st.columns(4)
            meta_items = [
                ("Depth", m.get("depth", "N/A")),
                ("Agents", str(m.get("agents_used", 4))),
                ("Generated", m.get("timestamp", "N/A")),
                ("Focus Areas", str(len(m.get("focus", [])))),
            ]
            for col, (k, v) in zip(cols, meta_items):
                with col:
                    st.markdown(f"""
                    <div class="stat-card">
                      <div class="stat-number" style="font-size:1.2rem">{v}</div>
                      <div class="stat-label">{k}</div>
                    </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        sections = r.get("sections", {})

        if sections.get("plan"):
            with st.expander("🗺️ Research Plan", expanded=False):
                st.markdown(f'<div class="report-box">{sections["plan"]}</div>', unsafe_allow_html=True)

        if sections.get("research"):
            with st.expander("🔍 Research Findings", expanded=False):
                st.markdown(f'<div class="report-box">{sections["research"]}</div>', unsafe_allow_html=True)

        if sections.get("analysis"):
            with st.expander("🧠 Analysis & Insights", expanded=False):
                st.markdown(f'<div class="report-box">{sections["analysis"]}</div>', unsafe_allow_html=True)

        if sections.get("report"):
            st.markdown("#### 📄 Full Research Report")
            st.markdown(f'<div class="report-box">{sections["report"]}</div>', unsafe_allow_html=True)

        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            full_text = format_report(r)
            st.download_button(
                "📥 Download as Markdown",
                data=full_text,
                file_name=f"AgentIQ_{r['topic'][:30].replace(' ','_')}.md",
                mime="text/markdown",
            )
        with col_dl2:
            st.download_button(
                "📄 Download as Text",
                data=full_text,
                file_name=f"AgentIQ_{r['topic'][:30].replace(' ','_')}.txt",
                mime="text/plain",
            )
    else:
        st.markdown("""
        <div style='text-align:center; padding: 3rem; color: #8896AA;'>
          <div style='font-size: 3rem;'>📭</div>
          <div style='font-size: 1.2rem; margin-top: 1rem;'>No report generated yet.</div>
          <div style='font-size: 0.9rem; margin-top: 0.5rem;'>Go to <b>New Research</b> tab to start.</div>
        </div>
        """, unsafe_allow_html=True)


with tab3:
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        ### 🤖 About AgentIQ

        **AgentIQ** is a production-grade demonstration of **Agentic AI** — a system where
        multiple specialized AI agents collaborate to complete complex research tasks autonomously.

        #### 🏗️ Architecture
        - **Planner Agent** — Decomposes the research goal into a structured plan
        - **Researcher Agent** — Gathers comprehensive information on the topic
        - **Analyzer Agent** — Critically evaluates and synthesizes findings
        - **Writer Agent** — Produces a polished, structured final report

        #### 🛠️ Tech Stack
        - Python 3.10+ · Streamlit · Anthropic Claude API
        - LangChain-inspired agent patterns
        - Session state management
        - Markdown report generation
        """)

    with col_b:
        st.markdown("""
        #### 🎓 Academic Context
        This project was developed for **CSE435 Comprehensive Seminar (2025–26)**
        on the topic of *Agentic AI: Autonomous Multi-Agent Systems for Real-World Applications*.

        It demonstrates all 6 Course Outcomes (CO1–CO6) through practical implementation.

        #### 📊 CO Mapping
        | Feature | Course Outcome |
        |---------|---------------|
        | Topic selection & trend analysis | CO1 |
        | Literature-backed responses | CO2 |
        | Agent pipeline implementation | CO3 |
        | UI/UX & presentation | CO4 |
        | Documentation & ethics | CO5 |
        | Future directions module | CO6 |

        #### 🔗 Links
        - [GitHub Repository](#) · [Live Demo](#) · [Research Paper](#)
        """)
