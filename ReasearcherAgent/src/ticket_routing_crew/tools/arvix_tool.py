from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_community.utilities import ArxivAPIWrapper


class ArxivQueryInput(BaseModel):
    """Input schema for ArxivQueryTool."""

    query: str = Field(..., description="Search query to look up on ArXiv.")


class ArxivQueryTool(BaseTool):
    name: str = "Arxiv Research Tool"
    description: str = (
        "A tool that searches ArXiv for research papers and returns summaries of relevant papers. "
        "Useful for finding and summarizing academic papers on specific topics."
    )
    args_schema: Type[BaseModel] = ArxivQueryInput

    def _run(self, query: str) -> str:
        """Execute the ArXiv search and return results.

        Args:
            query: The search query to look up on ArXiv.

        Returns:
            str: A summary of the most relevant papers found on ArXiv.
        """
        try:
            # Run the LangChain ArXiv tool
            arxiv_tool = ArxivAPIWrapper()  # type: ignore[index]
            result = arxiv_tool.run(query)

            # If the result is too long, truncate it to avoid token limits
            max_length = 4000
            if len(result) > max_length:
                result = result[:max_length] + "... [truncated]"

            return result
        except Exception as e:
            return f"An error occurred while searching ArXiv: {str(e)}"
