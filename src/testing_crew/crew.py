import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, llm, task, tool
from crewai_tools import PDFSearchTool
from dotenv import load_dotenv

load_dotenv()


@CrewBase
class TestingCrew:
    """CRM-focused crew using PDFSearchTool"""

    # Link YAML config files
    agents: "config/agents.yaml"
    tasks: "config/tasks.yaml"

    # 1. Tool: CRM PDF Search
    @tool
    def customerInteractionLogSearchTool(self):
        return PDFSearchTool(
            pdf_path="data/sale/crm_customer_interaction.pdf",
            name="Customer Interaction Logs Search Tool",
            description="Searches the CRM logs PDF for customer interaction history, notes, outcomes, and follow-ups.",
            config=dict(
                llm=dict(
                    provider="google",
                    config=dict(
                        model="gemini/gemini-2.5-flash-lite-preview-06-17",
                    ),
                ),
                embedder=dict(
                    provider="google",
                    config=dict(
                        model="models/embedding-001", task_type="retrieval_document"
                    ),
                ),
            ),
        )

    # 2. LLM: Gemini
    @llm
    def gemini_llm(self):
        return LLM(
            api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0,
            model="gemini/gemini-2.5-flash-lite-preview-06-17",
            stream=True,
        )

    # 3. Agent: CRM Log Agent
    @agent
    def crm_log_agent(self) -> Agent:
        return Agent(config=self.agents_config["crm_log_agent"], llm=self.gemini_llm())

    # 4. Task: Query CRM Logs
    @task
    def query_interaction_logs(self) -> Task:
        return Task(config=self.tasks_config["query_interaction_logs"])

    # 5. Crew: Compose and execute
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
