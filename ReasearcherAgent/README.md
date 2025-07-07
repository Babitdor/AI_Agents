# ResearchCrew

This is a **ResearchCrew** project, powered by [crewAI](https://crewai.com). 
This project is designed to help you set up a multi-agent AI system for conducting automated research and reporting, leveraging the powerful and flexible framework provided by crewAI. 
The goal is to enable an agents workflow to collaborate effectively on complex research tasks, maximizing their collective intelligence and capabilities.

---

## Installation

Ensure you have **Python >=3.10 <3.14** installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install `uv`:

```bash
pip install uv
```
Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

## Customizing
Before running the project, make sure to:

Add your `OPENAI_API_KEY` to the .env file.

You can customize your crew using the following configuration files:

- `src/research_crew/config/agents.yaml`: Define the agents (roles, goals, tools).
- `src/research_crew/config/tasks.yaml`: Define the research tasks each agent performs.
- `src/research_crew/crew.py`: Customize crew logic, add tools, or specify additional arguments.
- `src/research_crew/main.py`: Configure inputs and orchestrate execution.

## Running the Project
To launch your AI research crew and start task execution, run the following from the root directory:

```bash
crewai run
```

This command initializes the ResearchCrew, assembles the agents, and assigns them tasks as defined in your configurations.
By default, the example workflow will create a report.md in the root folder summarizing a research task (e.g., current developments in LLMs).

## Understanding Your Crew

The ResearchCrew is composed of multiple AI agents, each with defined roles, goals, and tools. These agents work together to complete tasks as outlined in:

- `config/agents.yaml`: Capabilities, names, and descriptions of each agent.
- `config/tasks.yaml`: The actual sequence of research-oriented tasks.

This modular design allows you to adapt the crew for a wide variety of research and knowledge-generation use cases.
