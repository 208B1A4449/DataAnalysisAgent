from typing import TypedDict, Any
from langgraph.graph import StateGraph, END

from agents.repair_agent import repair_agent
from agents.planner import planner_agent
from agents.executor import PandasCodeExecutor
from agents.synthesizer import synthesizer_agent
from agents.chart_agent import chart_agent
from agents.router import route_intent
from agents.profiler import profile_dataset


class AgentState(TypedDict):
    question: str
    df: Any
    intent: str
    code: str
    result: Any
    chart: Any
    answer: str


def planner_node(state: AgentState):
    schema = str(state["df"].dtypes)
    code = planner_agent(state["question"], schema)
    return {"code": code}

def executor_node(state: AgentState):
    executor = PandasCodeExecutor(state["df"])
    result = executor.execute(state["code"])

    # 🚑 AUTO-REPAIR LOOP (ONE RETRY)
    if isinstance(result, str) and "error" in result.lower():
        schema = str(state["df"].dtypes)
        fixed_code = repair_agent(
            state["question"],
            state["code"],
            result,
            schema
        )

        retry_result = executor.execute(fixed_code)

        return {
            "code": fixed_code,
            "result": retry_result
        }

    return {"result": result}

def synthesizer_node(state: AgentState):
    answer = synthesizer_agent(state["question"], state["result"])
    return {"answer": answer}

def chart_node(state: AgentState):
    fig = chart_agent(state["result"])
    return {"chart": fig}

def router_node(state: AgentState):
    intent = route_intent(state["question"])
    return {"intent": intent}

def dataset_node(state: AgentState):
    answer = profile_dataset(state["df"])
    return {"answer": answer}


graph = StateGraph(AgentState)

graph.add_node("router", router_node)
graph.add_node("dataset", dataset_node)
graph.add_node("planner", planner_node)
graph.add_node("executor", executor_node)
graph.add_node("chart", chart_node)
graph.add_node("synthesizer", synthesizer_node)

graph.set_entry_point("router")

def route_by_intent(state: AgentState):
    if state["intent"] == "dataset":
        return "dataset"
    else:
        return "planner"  # analysis + interpretation start here

graph.add_conditional_edges(
    "router",
    route_by_intent,
    {
        "dataset": "dataset",
        "planner": "planner"
    }
)

graph.add_edge("dataset", END)

graph.add_edge("planner", "executor")
graph.add_edge("executor", "chart")
graph.add_edge("chart", "synthesizer")
graph.add_edge("synthesizer", END)

app_graph = graph.compile()

