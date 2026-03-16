"""
Analyzer Agent — Synthesizes, critiques, and extracts key insights
"""

import anthropic


class AnalyzerAgent:
    """
    The Analyzer Agent critically evaluates the research findings,
    identifies patterns, gaps, contradictions, and key insights.
    """

    SYSTEM_PROMPT = """You are an expert Critical Analysis Agent with deep expertise in
evaluating technical research and synthesizing insights.

Your role is to analyze research findings and extract meaningful insights.

When analyzing research:
1. Identify the 3–5 most important key insights or takeaways
2. Spot any gaps, limitations, or missing information in the research
3. Compare and contrast different approaches, technologies, or perspectives mentioned
4. Evaluate the practical vs theoretical value of the findings
5. Identify emerging trends and patterns
6. Make critical observations about challenges and opportunities
7. Suggest what aspects deserve deeper investigation

Format your analysis in Markdown with these sections:
## Key Insights (numbered, most important first)
## Strengths of Current Approaches
## Limitations & Challenges
## Comparative Analysis (if multiple approaches discussed)
## Emerging Trends
## Critical Observations

Be analytical, critical, and insightful. Challenge assumptions where appropriate."""

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    def run(self, topic: str, research: str, focus_areas: list = None) -> str:
        """
        Analyze the research findings.

        Args:
            topic: The research topic
            research: Research findings from ResearcherAgent
            focus_areas: Specific areas to focus analysis on

        Returns:
            Critical analysis and insights as a Markdown string
        """
        focus_text = ""
        if focus_areas:
            focus_text = f"\nPay special attention to: {', '.join(focus_areas)}"

        user_message = f"""You are the Analyzer Agent. Critically analyze the research findings below
and extract the most valuable insights.

**Topic:** {topic}
{focus_text}

**Research Findings to Analyze:**
{research}

---

Provide a rigorous critical analysis. Be specific, data-driven, and insightful.
Identify what's most important, what's missing, and what deserves attention."""

        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            messages=[{"role": "user", "content": user_message}],
            system=self.SYSTEM_PROMPT,
        )

        return message.content[0].text
