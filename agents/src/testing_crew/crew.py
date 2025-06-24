import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, llm, task, tool
from crewai_tools import PDFSearchTool
from dotenv import load_dotenv

load_dotenv()

# Create a RAG tool with default settings


@CrewBase
class TestingCrew:
    """Board minutes analysis crew"""

    # Link YAML config files
    agents: "config/agents.yaml"
    tasks: "config/tasks.yaml"

    # 2. LLM: Gemini
    @llm
    def gemini_llm(self):
        return LLM(
            api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0,
            model="gemini/gemini-2.5-pro",
            stream=True,
        )

    # 3. Agent: Board Minutes Analyst
    @agent
    def board_minutes_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["board_minutes_analyst"],
            llm=self.gemini_llm(),
            tools=[
                PDFSearchTool(
                    pdf="/Users/farzanmirza/Desktop/Drive/Coding/Git/test-agentic/data/admin/board_mins/skateboard.pdf"
                )
            ],
        )

    # 4. Task: Analyze Board Minutes
    @task
    def analyze_board_minutes(self) -> Task:
        return Task(config=self.tasks_config["analyze_board_minutes"])

    # 5. Crew: Compose and execute
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
