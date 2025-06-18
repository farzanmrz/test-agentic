import streamlit as st

from main import complex_task_multiple_agents

st.title("CrewAI Task Interface")

st.info("Enter a description for the task you want the AI agent to perform.")

description = st.text_area("Task Description", height=150)

if st.button("Run Task"):
    if description:
        with st.spinner("The agent is working on your task..."):
            try:
                result = complex_task_multiple_agents(description)
                st.success("Task completed!")
                st.markdown("### Result")
                st.write(result)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a task description.")
