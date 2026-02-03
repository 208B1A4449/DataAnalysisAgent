from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0.3,
    api_key=GROQ_API_KEY
)

def synthesizer_agent(question: str, result) -> str:
    prompt = f"""
You are an expert data analyst.

User question:
{question}

Analysis output:
{result}

Your response MUST:
1. Directly answer the user's question first
2. Clearly explain what the numbers mean
3. Mention trends, correlations, or comparisons
4. Avoid technical jargon unless necessary
5. Be confident and insight-driven
6. Use short paragraphs (not bullet spam)

If correlation:
- Explain strength (weak/moderate/strong)
- Explain direction (positive/negative)
- Explain real-world meaning

End with:
"Would you like a deeper breakdown or a visualization-based comparison?"

Do NOT mention pandas, DataFrames, or code.
"""
    return llm.invoke(prompt).content
