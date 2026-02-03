from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0.3,
    api_key=GROQ_API_KEY
)

def explainer_agent(question: str, results: dict) -> str:
    prompt = f"""
You are an expert data analyst.

User question:
{question}

Analysis results:
{results}

Explain:
- What the results show
- Comparisons or trends
- Practical meaning

Rules:
- No technical jargon
- No pandas references
- No code
- Be confident and concise
"""

    return llm.invoke(prompt).content
