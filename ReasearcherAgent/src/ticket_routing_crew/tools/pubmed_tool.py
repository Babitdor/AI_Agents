from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools.pubmed.tool import PubmedQueryRun


class PubMedInput(BaseModel):
    """Input schema for PubMedQueryTool."""

    query: str = Field(..., description="Search query to look up on PubMed.")


class PubMedQueryTool(BaseTool):
    name: str = "Arxiv Research Tool"
    description: str = (
        "A tool that searches PubMed for research papers and returns summaries of relevant papers. "
        "Useful for finding and summarizing academic papers on specific topics."
    )
    args_schema: Type[BaseModel] = PubMedInput

    def _run(self, query: str) -> str:
        """Execute the PubMed search and return results.

        Args:
            query: The search query to look up on PubMed.

        Returns:
            str: A summary of the most relevant papers found on PubMed.
        """
        try:
            # Run the LangChain PubMed tool
            pubmed_tool = PubmedQueryRun()  # type: ignore[index]
            result = pubmed_tool.invoke(query)

            # If the result is too long, truncate it to avoid token limits
            max_length = 4000
            if len(result) > max_length:
                result = result[:max_length] + "... [truncated]"

            return result
        except Exception as e:
            return f"An error occurred while searching ArXiv: {str(e)}"
