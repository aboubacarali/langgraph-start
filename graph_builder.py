from langgraph.graph import StateGraph, END

from state import SupportState
from nodes import (
    classify_question,
    handle_tech,
    handle_commercial,
    handle_faq
)


def route_question(state: SupportState):
    return state["category"]


def build_graph():
    graph = StateGraph(SupportState)

    graph.add_node("classify", classify_question)
    graph.add_node("tech", handle_tech)
    graph.add_node("commercial", handle_commercial)
    graph.add_node("faq", handle_faq)

    graph.set_entry_point("classify")

    graph.add_conditional_edges(
        "classify",
        route_question,
        {
            "tech": "tech",
            "commercial": "commercial",
            "faq": "faq"
        }
    )

    graph.add_edge("tech", END)
    graph.add_edge("commercial", END)
    graph.add_edge("faq", END)

    return graph.compile()
