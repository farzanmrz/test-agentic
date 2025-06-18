# Imports General
import sys
import warnings
from datetime import datetime

# Load API keys
from dotenv import load_dotenv

load_dotenv()

# Init AgentOps
import agentops

# Import the crew
from testing_crew.crew import TestingCrew

agentops.init()

# Filter out specific warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

"""
Main Coding Stuff Begins
"""


# Run the crew
def run():
    """
    Run the crew.
    """
    inputs = {
        "user_input": "Hi helpful assistant what is the vibe in New York today?",
    }

    try:
        TestingCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


# Uncomment the following function if you want to implement training functionality
# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         TestingCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")


# Replay the crew execution from a specific task
def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TestingCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


# Test the crew execution and return the results
def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "user_input": "Hi helpful assistant what is the vibe today?",
    }

    try:
        TestingCrew().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
