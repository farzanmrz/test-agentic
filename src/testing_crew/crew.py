import os
from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

load_dotenv()


@CrewBase
class TestingCrew:
    """TestingCrew crew"""

    # Define the agents and tasks configuration files
    agents: "config/agents.yaml"
    tasks: "config/tasks.yaml"

    """
    1. Agents
    """

    # Initial agent
    @agent
    def initial_tester(self) -> Agent:
        return Agent(config=self.agents_config["initial_tester"])

    """
    2. Tasks
    """

    # Initial task
    @task
    def initial_task(self) -> Task:
        return Task(
            config=self.tasks_config["initial_task"],
        )

    """
    3. Crew
    """

    @crew
    def crew(self) -> Crew:
        """Creates the TestingCrew crew"""

        # Return the crew
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=False,
        )
