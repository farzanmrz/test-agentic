# Imports General
import sys
import warnings
from datetime import datetime

# Load API keys
from dotenv import load_dotenv

load_dotenv()

# Init AgentOps
import agentops

agentops.init()

# Filter out specific warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Import the crew
from testing_crew.crew import TestingCrew

"""
Main Coding Stuff Begins
"""


# Run the crew
def run():
    """
    Run the CRM-focused crew with a query on customer interaction logs.
    """
    inputs = {
        "query": "What were the notes from the last call with Luis Lawrence about the Backend Systems Upgrade?"
    }

    try:
        result = TestingCrew().crew().kickoff(inputs=inputs)
        print("\n📝 Result:")
        print(result)

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


# Replay the crew execution from a specific task
def replay():
    try:
        TestingCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


# Test the crew execution and return the results
def test():
    inputs = {"query": "Summarize the last in-person meeting with Saul Reid."}

    try:
        TestingCrew().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
