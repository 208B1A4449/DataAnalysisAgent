import streamlit as st
from utils.data_loader import load_data
from graph import app_graph


# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="📊 AI Data Analyst Agent",
    layout="wide"
)

st.title("📊 AI-Powered Data Analysis Agent")
st.caption(
    "Upload a dataset and ask analytical questions in natural language. "
    "The system plans, executes, and explains the analysis safely."
)


# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

# -------------------------------
# Question Input
# -------------------------------
question = st.text_input(
    "Ask a question about the data",
    placeholder="e.g., What is this dataset about? | Is there a correlation between X and Y?"
)


# -------------------------------
# Main Execution
# -------------------------------
if uploaded_file and question:

    try:
        df = load_data(uploaded_file)
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        st.stop()

    # Optional: show dataset preview
    with st.expander("📄 Preview Dataset"):
        st.dataframe(df.head())

    with st.spinner("Analyzing..."):
        result = app_graph.invoke(
            {
                "question": question,
                "df": df
            }
        )

    # -------------------------------
    # Answer Section
    # -------------------------------
    st.subheader("🧠 Answer")
    st.write(result.get("answer", "No answer generated."))

    # -------------------------------
    # Optional Debug / Transparency
    # -------------------------------
    if "intent" in result:
        st.caption(f"🔍 Detected intent: `{result['intent']}`")

    # -------------------------------
    # Generated Code (Analysis Only)
    # -------------------------------
    if "code" in result and result["code"]:
        with st.expander("🧪 Generated Pandas Code"):
            st.code(result["code"], language="python")

    # -------------------------------
    # Raw Execution Result
    # -------------------------------
    if "result" in result:
        with st.expander("📄 Raw Result"):
            st.write(result["result"])

    # -------------------------------
    # Visualization
    # -------------------------------
    if result.get("chart") is not None:
        st.subheader("📊 Visualization")
        st.pyplot(result["chart"])

else:
    st.info("⬆️ Upload a dataset and enter a question to begin.")
