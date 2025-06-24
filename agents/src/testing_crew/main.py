# Imports General
import sys
import warnings
from datetime import datetime

# Load API keys
from dotenv import load_dotenv

load_dotenv()

# Init AgentOps
import agentops
from testing_crew.crew import TestingCrew

agentops.init()

# Filter out specific warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Import the crew


"""
Main Coding Stuff Begins
"""


# Run the crew
def run():
    """
    Run the crew to analyze the skateboard club's meeting minutes.
    """
    inputs = {
        "query": "The structure of the meeting was too complicated for me to understand, can you please explain in simple human-understandable terms how to understand the meeting structure?"
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
    queries = [
        "How much money was approved for the DJ at Skate-a-Palooza, and which account was it paid from?",
        "Who volunteered to reserve Webb Lawn for the Skateboard workshop?",
        "What was the final vote count for Motion #13 concerning meals for the NY trip?",
        "List all attendees of the meeting on 3.21.07.",
        "What is the balance of the fundraising account (BAMK08) according to the Treasurer's Report?",
    ]

    try:
        for i, query in enumerate(queries, 1):
            print(f"\n🔍 [Query {i}] {query}")
            result = (
                TestingCrew()
                .crew()
                .test(
                    n_iterations=int(sys.argv[1]),
                    eval_llm=sys.argv[2],
                    inputs={"query": query},
                )
            )
            print(f"✅ [Result {i}]\n{result}\n")

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

        raise Exception(f"An error occurred while testing the crew: {e}")
