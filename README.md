📊 AI-Powered Data Analysis Agent

Project Overview

The AI Data Analysis Agent is a Streamlit web application that allows users to upload datasets (CSV or Excel) and ask analytical questions in natural language. The system intelligently plans, executes, and explains the analysis, including visualizations, while ensuring safe and deterministic execution of Python code.

This project combines LangGraph, Groq LLMs, and custom Python modules to provide a structured, multi-step data analysis pipeline, including:

> Intent Detection – determines whether the user wants dataset profiling or analysis.

> Planner Agent – generates a multi-step analysis plan in JSON format.

> Executor Agent – safely executes Pandas code with an auto-repair mechanism for errors.

> Chart Agent – generates visualizations from the results.

> Synthesizer Agent – converts raw results into clear, human-readable explanations.

> Dataset Profiler – provides an overview of the dataset, including columns, types, and missing values.

Key Features

✅ Natural Language Data Queries – Ask questions like “What is the average age of customers?” or “Show me correlations between features.”

✅ Multi-step Analysis – Automatically plans and executes step-by-step operations.

✅ Safe Code Execution – Prevents unsafe Python code execution and validates generated code.

✅ Auto-Repair – Detects errors in generated code and attempts automatic fixes.

✅ Visualization Support – Generates charts for comparison, distributions, and group analyses.

✅ Dataset Profiling – Quickly understand any dataset’s structure, missing values, and types.

✅ Transparent Outputs – Shows generated code, raw results, and detected user intent for debugging or learning purposes.

Technologies Used

> Python – Core programming language

> Streamlit – Web interface for uploading data and interacting with the agent

> Pandas – Data manipulation and analysis

> Matplotlib – Visualizations

> LangGraph – Custom multi-node agent graph management

> Groq API / ChatGroq – LLM for planning, explanation, and code repair

> Python-dotenv – Environment variable management

Folder Structure

DataAnalysisAgent/
│
├─ app.py                  # Streamlit entry point
├─ graph.py                # Defines the agent nodes and graph workflow
├─ dataloader.py           # Loads CSV or Excel datasets
├─ plan_compiler.py        # Handles multi-step JSON analysis execution
├─ chart_agent.py          # Generates visualizations
├─ executor.py             # Executes Pandas code safely
├─ explainer.py            # Converts results into human-readable explanations
├─ planner.py              # Generates analysis plans (JSON) from user questions
├─ profiler.py             # Profiles dataset and summarizes structure
├─ repair_agent.py         # Repairs LLM-generated Pandas code
├─ router.py               # Determines intent of the user question
├─ synthesizer.py          # Synthesizes results into explanations
├─ requirements.txt        # Python dependencies
└─ .env                    # Stores GROQ_API_KEY and other secrets

Usage Instructions

Clone the repository

git clone https://github.com/208B1A4449/DataAnalysisAgent.git
cd DataAnalysisAgent


Install dependencies

    pip install -r requirements.txt


Setup environment variables

Create a .env file with your Groq API key:

    GROQ_API_KEY=your_groq_api_key_here
    MODEL_NAME=llama-3.1-8b-instant


Run the Streamlit app

    streamlit run app.py


Upload a dataset (CSV or Excel) and enter a question about the data. The agent will:

    Detect intent (dataset profiling or analysis)

    Generate a multi-step plan

    Execute Pandas code safely

    Display visualizations

    Provide natural language explanations

Example Questions

    “Give me a summary of the dataset.”

    “Which features are correlated with Sales?”

    “Show a comparison of Revenue across different regions.”

    “What is the average Age for customers with income > 50k?”

Project Highlights

    Custom StateGraph ensures a structured multi-step workflow.

    Auto-repair mechanism handles common code errors.

    Fully modular design – agents for planning, execution, charting, synthesis, and profiling.

    Human-friendly explanations powered by Groq LLM.

Future Enhancements

    Add support for larger datasets using Dask or Polars.

    Integrate more visualization options like Seaborn or Plotly.

    Allow interactive filtering and charting within Streamlit.

    Add history tracking for multiple user queries.