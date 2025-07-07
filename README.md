# AI Agents

A repo of intelligent AI Agents leveraging **LangGraph**, **LlamaIndex**, **LangChain**, **CrewAI**, and **Ollama**-based models, designed with transferability in mind to support other Large Language Models (LLMs).

---

## Overview

This repository provides tools and components to build powerful AI Agents that can reason, plan, and execute complex tasks by orchestrating multiple AI components and knowledge sources. It integrates cutting-edge frameworks and libraries for language model interaction and knowledge retrieval:

- **LangGraph**: Define and manage complex agent workflows and decision graphs.
- **LlamaIndex**: Efficiently index and retrieve information from documents to augment agent knowledge.
- **LangChain**: Chain together prompts, LLM calls, and external tools in a modular way.
- **CrewAI**: Coordinate multiple autonomous agents collaboratively to handle complex multi-step tasks.
- **Ollama models**: Used local or hosted LLMs via Ollama, with seamless transferability to other LLM providers.

---

## Features

- **Modular Agent Design**: Compose agents using nodes in LangGraph workflows.
- **Hybrid Knowledge Retrieval**: Leverage LlamaIndex for document indexing and retrieval.
- **Flexible LLM Integration**: Use Ollama-hosted models or swap in other LLMs (OpenAI, HuggingFace pipelines, etc.) with minimal changes.
- **Collaborative Multi-Agent Support**: Orchestrate agents as collaborative teams using CrewAI.
- **Multi-tool Support**: Connect to APIs, databases, and custom logic from agent workflows.
- **Extensible**: Easily add new tools, models, and workflows.

---

## Installation

```bash
git clone https://github.com/Babitdor/AI_Agents.git
cd AI_Agents
pip install -r requirements.txt
