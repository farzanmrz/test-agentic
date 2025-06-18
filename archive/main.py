import os

import dotenv
import pandas as pd
from crewai import Agent, Crew, Process, Task
from crewai.tools import tool
from openpyxl import load_workbook

# Load environment variables from a .env file
dotenv.load_dotenv()


# @tool("Excel Reader")
def read_excel_to_df(file_path: str, result_as_answer=True) -> str:
    """
    Reads the first sheet of an Excel file into a pandas DataFrame
    and returns it as a string.
    """
    try:
        # Use pandas for robust Excel reading, with specific parameters
        df = pd.read_excel(
            file_path,
            sheet_name=0,
            header=0,
            engine="openpyxl",
            # keep_default_na=False,
        )

        # Drop empty columns and rows
        df.dropna(how="all", inplace=True, axis=1)
        df.dropna(how="all", inplace=True, axis=0)

        # Remove unnamed columns
        df = df.loc[:, ~df.columns.str.startswith("Unnamed: ")]

        return df
    except FileNotFoundError:
        return "Error: The specified Excel file was not found."
    except Exception as e:
        return f"An error occurred while reading the Excel file: {e}"


def run_excel_reading_crew():
    """
    Sets up and runs a Crew to read an Excel file using a custom tool.
    """
    # Agent that uses the custom tool
    excel_reader_agent = Agent(
        role="Excel Data Extractor",
        goal="Accurately read the contents of an Excel file using the provided tool.",
        backstory="An expert at extracting data from Excel files and presenting it for further analysis.",
        tools=[read_excel_to_df],
        verbose=True,
    )

    # Task for the agent
    read_task = Task(
        description="Read the data from the Excel file located at 'knowledge/week_cover1.xlsx'.",
        agent=excel_reader_agent,
        expected_output="The full content of the Excel file's first sheet, formatted as a string.",
    )

    # Create and run the crew
    excel_crew = Crew(
        agents=[excel_reader_agent],
        tasks=[read_task],
        process=Process.sequential,
        verbose=True,
    )

    result = excel_crew.kickoff()
    return result


# Main function
def main():
    print("--- Running Excel Reading Crew ---")
    result = run_excel_reading_crew()
    print("\n--- Crew Final Result ---")
    print(result)


# Call the main function
if __name__ == "__main__":
    print(read_excel_to_df(file_path="knowledge/week_cover1.xlsx"))
