"""
Writer Agent — Produces polished, structured final research reports
"""

import anthropic


class WriterAgent:
    """
    The Writer Agent synthesizes all previous agent outputs into
    a polished, professionally structured final research report.
    """

    SYSTEM_PROMPT = """You are an expert Technical Writer Agent specializing in producing
clear, structured, and compelling research reports.

Your role is to synthesize the research plan, findings, and analysis into a final report.

The report must:
1. Have a clear executive summary (3–4 sentences max)
2. Follow a logical structure with proper headings
3. Integrate findings and analysis seamlessly
4. Use clear, professional language accessible to technical audiences
5. Include key statistics and examples
6. Have a strong conclusions section
7. End with actionable future directions

Report Structure:
## Executive Summary
## Introduction & Background
## Core Concepts & Architecture
## Key Findings
## Industry Applications
## Analysis & Insights
## Challenges & Limitations
## Future Directions
## Conclusion

Write in clear, engaging prose. Use bullet points for lists.
This is the final deliverable — make it publication-quality."""

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    def run(self, topic: str, plan: str, research: str, analysis: str) -> str:
        """
        Write the final comprehensive research report.

        Args:
            topic: The research topic
            plan: Research plan from PlannerAgent
            research: Findings from ResearcherAgent
            analysis: Analysis from AnalyzerAgent

        Returns:
            Final polished research report as a Markdown string
        """
        user_message = f"""You are the Writer Agent. Using all the information below,
produce a comprehensive, polished final research report.

**Topic:** {topic}

**Research Plan:**
{plan}

**Research Findings:**
{research}

**Analysis & Insights:**
{analysis}

---

Write a comprehensive, publication-quality research report that synthesizes all of the above.
The report should stand alone — someone who hasn't seen the other sections should be able to
fully understand the topic from this report alone.

Make it impressive, clear, and well-structured."""

        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": user_message}],
            system=self.SYSTEM_PROMPT,
        )

        return message.content[0].text
