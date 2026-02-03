def route_intent(question: str) -> str:
    if "plot" in question.lower():
        return "analysis"
    if "dataset" in question.lower():
        return "dataset"
    return "analysis"
