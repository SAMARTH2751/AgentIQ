"""
Planner Agent — Decomposes research goals into structured plans
"""

import anthropic
import re


class PlannerAgent:
    """
    The Planner Agent breaks a broad research topic into a structured,
    actionable research plan with clear sub-questions and scope.
    """

    SYSTEM_PROMPT = """You are an expert Research Planner Agent in a multi-agent AI system.
Your role is to create a structured research plan for a given topic.

When given a topic, you must:
1. Identify 4–6 key research questions that need to be answered
2. Define the scope and boundaries of the research
3. Suggest the most relevant subtopics to cover
4. Identify what type of information is needed (technical, statistical, case studies, etc.)
5. Prioritize the research questions by importance

Format your output as a clear, structured plan in Markdown with sections:
- ## Research Objective
- ## Key Research Questions (numbered list)
- ## Scope & Boundaries
- ## Research Priorities
- ## Expected Deliverables

Be concise but thorough. This plan will guide other AI agents."""

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    def run(self, topic: str, depth: str = "Standard", focus_areas: list = None) -> str:
        """
        Generate a research plan for the given topic.

        Args:
            topic: The research topic
            depth: "Quick Overview", "Standard", or "Deep Dive"
            focus_areas: List of specific areas to focus on

        Returns:
            A structured research plan as a Markdown string
        """
        depth_instructions = {
            "Quick Overview": "Create a brief plan with 3–4 key questions. Keep scope narrow.",
            "Standard": "Create a comprehensive plan with 4–6 key questions. Balanced scope.",
            "Deep Dive": "Create an exhaustive plan with 6–8 key questions. Broad, detailed scope.",
        }

        focus_text = ""
        if focus_areas:
            focus_text = f"\n\nSpecifically focus on these areas: {', '.join(focus_areas)}"

        user_message = f"""Create a research plan for the following topic:

**Topic:** {topic}
**Depth:** {depth}
{depth_instructions.get(depth, depth_instructions['Standard'])}
{focus_text}

Generate a structured research plan that will guide the research, analysis, and writing agents."""

        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            messages=[{"role": "user", "content": user_message}],
            system=self.SYSTEM_PROMPT,
        )

        return message.content[0].text
