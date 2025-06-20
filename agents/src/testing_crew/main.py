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
    queries = [
        "Summarize all touchpoints between Isaac Gains and Luis Lawrence about the Backend Systems Upgrade.",
        "Which opportunities had both a LinkedIn message and a call associated with them in June?",
        "What objections were raised during in-person meetings about the Lab Renovation?",
        "Find all contacts who had more than one interaction within a 48-hour window.",
        "What actions were planned after the email to Brooke Bradley on 6/10/19?",
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
