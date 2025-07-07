from crewai import Agent, Crew, Process, Task, LLM
from langchain_ollama import OllamaLLM
from crewai.project import CrewBase, agent, crew, task
from crewai.tasks.hallucination_guardrail import HallucinationGuardrail
from crewai.agents.agent_builder.base_agent import BaseAgent
from .tools.arvix_tool import ArxivQueryTool
from .tools.pubmed_tool import PubMedQueryTool
from crewai_tools.tools import GithubSearchTool, WebsiteSearchTool
from typing import List
from dotenv import load_dotenv
from crewai import LLM
import os


llm = LLM(model="ollama/llama3.1:latest", base_url="http://localhost:11434")

load_dotenv()
url_guardrail = HallucinationGuardrail(
    context="""
    Instructions for the LLM:
    - Do not generate or invent any URLs, links, or web addresses unless they are explicitly provided in the context below.
    - If you reference a source, it must be a real, verifiable source, and you should explicitly mention that the URL was user-provided.
    - If you don't have a real URL to share, respond with: "I don't have a verified source/link for this."
    - Never hallucinate fake websites, domains, or links.
    
    User-provided verified links (if any):
    - [None in this case]
    """,
    llm=llm,  # type: ignore[index]
)


@CrewBase
class ResearcherCrew:
    """TicketRoutingCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def research_analysizer(self) -> Agent:
        return Agent(
            config=self.agents_config["research_analysizer"],  # type: ignore[index]
            verbose=True,
            llm=llm,
            reasoning=True,
            allow_delegation=False,
            max_reasoning_attempts=3,
        )

    @agent
    def senior_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_analyst"],  # type: ignore[index]
            verbose=True,
            llm="ollama/mistral",
            reasoning=True,
            tools=[
                ArxivQueryTool(),
                PubMedQueryTool(),
                GithubSearchTool(gh_token=os.getenv("GITHUB_TOKEN")),
                WebsiteSearchTool(),
            ],
            allow_delegation=False,
            max_reasoning_attempts=3,
        )

    @agent
    def summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["summarizer_agent"],  # type: ignore[index]
            verbose=True,
            llm=llm,
            allow_delegation=False,
        )

    @task
    def analyse_question(self) -> Task:
        return Task(config=self.tasks_config["analyse_question"], guardrail=url_guardrail)  # type: ignore[index]

    @task
    def do_research(self) -> Task:
        return Task(config=self.tasks_config["do_research"], guardrail=url_guardrail)  # type: ignore[index]

    @task
    def summarise_task(self) -> Task:
        return Task(config=self.tasks_config["summarise_task"], guardrail=url_guardrail)  # type: ignore[index]

    @crew
    def crew(self) -> Crew:
        """TicketRoutingCrew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
