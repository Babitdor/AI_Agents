from crewai import Agent, Task, Process
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from langchain_ollama import OllamaLLM
from typing import Type, Dict, List


class CriticInput(BaseModel):
    """Input schema for CriticInput."""

    content: Dict = Field(
        ...,
        description="Dictionary of containing summary, key points and research paper sources to analyze",
    )


class CriticTool(BaseTool):
    name: str = "Research Paper Analyzer"
    description: str = (
        "Analyzes multiple research papers to generate a concise summary, "
        "key points, and proper citations. Identifies agreements and contradictions."
    )
    args_schema: Type[BaseModel] = CriticInput

    def _run(self, content: Dict) -> Dict:  # type: ignore[index]
        """Analyze research papers and return structured findings.

        Args:
            content: Dictionary of research papers (title, authors, key_findings)

        Returns:
            Dict: {
                "summary": "Concise paragraph of main insights",
                "key_points": ["bullet points of key findings"],
                "citations": ["source titles and authors"]
            }
        """

        llm = OllamaLLM(model="mistral:latest")

        try:
            # Extract key information from sources
            claims = [content["key_points"] for list in content.values()]
            citations = [
                f"{list['title']} by {list['authors']}" for list in content.values()
            ]
            prompts = f""" Analyze the content about and write a concise, coherent paragraph 
            capturing the main ideas and key insights. Preserve the original context accurately 
            without redundancy. Focus on agreements and contradictions.

            Papers:
            {content}

            Write a professional academic summary paragraph:
            """

            return {
                "summary": content["summary"],
                "key_points": content["key_points"],
                "citations": citations,
            }

        except Exception as e:
            return {
                "summary": f"Analysis failed: {str(e)}",
                "key_points": [],
                "citations": [],
            }
