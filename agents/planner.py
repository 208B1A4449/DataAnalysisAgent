from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME
import json

llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0,
    api_key=GROQ_API_KEY
)

def planner_agent(question: str, schema: dict) -> dict:
    prompt = f"""
You are an AI Data Analyst Planner.

Dataset schema:
{schema}

User question:
{question}

Your task:
- Create a MULTI-STEP JSON analysis plan
- Each step must be atomic and deterministic
- No code, no pandas, no explanations

Allowed actions:
- compute_quantile
- filter
- group_mean
- mean
- histogram_compare
- compare_values

Rules:
- Output VALID JSON only
- Each step must have: id, action, output
- Steps may reference previous outputs by name
- Do NOT explain anything

Return ONLY the JSON plan.
"""

    response = llm.invoke(prompt).content
    return json.loads(response)
