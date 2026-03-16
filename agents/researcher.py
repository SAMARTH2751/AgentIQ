"""
Researcher Agent — Gathers comprehensive information on the topic
"""

import anthropic


class ResearcherAgent:
    """
    The Researcher Agent uses its knowledge to gather comprehensive,
    factual information based on the Planner's research plan.
    """

    SYSTEM_PROMPT = """You are an expert Research Agent with deep knowledge in Computer Science,
AI, technology, and engineering. You are part of a multi-agent research pipeline.

Your role is to gather comprehensive, accurate information based on a research plan.

For each topic you research:
1. Provide factual, detailed information on all key research questions
2. Include specific examples, statistics, and real-world data where possible
3. Reference real papers, frameworks, tools, and industry examples
4. Cover both technical depth and practical applications
5. Note the most recent developments (up to your knowledge cutoff)
6. Include multiple perspectives and viewpoints

Format your output in Markdown with clear sections matching the research plan.
Use headers (##, ###), bullet points, bold for key terms, and code blocks for technical content.

Be authoritative, specific, and data-driven. Avoid vague generalizations."""

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    def run(self, topic: str, plan: str, depth: str = "Standard") -> str:
        """
        Research the topic based on the provided plan.

        Args:
            topic: The research topic
            plan: The structured plan from PlannerAgent
            depth: Research depth level

        Returns:
            Comprehensive research findings as a Markdown string
        """
        depth_tokens = {
            "Quick Overview": 800,
            "Standard": 1200,
            "Deep Dive": 1500,
        }
        max_tokens = depth_tokens.get(depth, 1200)

        user_message = f"""You are the Researcher Agent. Based on the research plan below,
gather comprehensive information on the topic.

**Topic:** {topic}

**Research Plan to Follow:**
{plan}

---

Now provide detailed research findings that address all the key research questions in the plan.
Include specific examples, real frameworks/tools, statistics, and industry use cases.
Format clearly in Markdown with appropriate headers and structure."""

        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": user_message}],
            system=self.SYSTEM_PROMPT,
        )

        return message.content[0].text
