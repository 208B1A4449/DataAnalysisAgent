import pandas as pd
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0.2,
    api_key=GROQ_API_KEY
)

def profile_dataset(df: pd.DataFrame) -> str:
    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isna().sum().to_dict()
    }

    prompt = f"""
You are a data analyst describing a dataset.

Dataset summary (ground truth):
{summary}

Rules:
- Do NOT guess business context
- Do NOT invent meaning
- Describe only what is visible
- Be neutral and factual
- Short paragraphs, no bullets

Explain what this dataset contains.
"""
    return llm.invoke(prompt).content
