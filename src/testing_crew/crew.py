import os
from typing import List

from crewai import LLM, Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, llm, task
from crewai_tools import BraveSearchTool
from dotenv import load_dotenv

load_dotenv()


@CrewBase
class TestingCrew:
    """TestingCrew crew"""

    # Define the agents and tasks configuration files
    agents: "config/agents.yaml"
    tasks: "config/tasks.yaml"

    """
    1. LLMs
    """

    @llm
    def gemini_llm(self):
        return LLM(
            api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0,
            model="gemini/gemini-2.5-flash-lite-preview-06-17",
            stream=True,
        )

    """
    2. Agents
    """

    # 1. Vibe checker agent
    @agent
    def vibe_checker(self) -> Agent:
        agt_vibe_checker = Agent(
            config=self.agents_config["vibe_checker"],
            tools=[BraveSearchTool(n_results=2)],
            llm=self.gemini_llm(),
        )
        return agt_vibe_checker

    # 2. Plan Setter agent
    @agent
    def plan_setter(self) -> Agent:
        agt_plan_setter = Agent(
            config=self.agents_config["plan_setter"],
            tools=[BraveSearchTool(n_results=5)],
            llm=self.gemini_llm(),
        )
        return agt_plan_setter

    """
    3. Tasks
    """

    # 1. Check vibe task
    @task
    def check_vibe(self) -> Task:
        tsk_check_vibe = Task(
            config=self.tasks_config["check_vibe"],
        )
        return tsk_check_vibe

    # 2. Set plan task
    @task
    def set_plan(self) -> Task:
        tsk_set_plan = Task(
            config=self.tasks_config["set_plan"],
        )
        return tsk_set_plan

    """
    4. Crew
    """

    @crew
    def crew(self) -> Crew:
        """Creates the TestingCrew crew"""

        # Return the crew
        crw_initial_crew = Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
        return crw_initial_crew
