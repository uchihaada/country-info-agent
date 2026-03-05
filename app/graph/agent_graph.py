from langgraph.graph import StateGraph, END

from app.model.state import AgentState
from app.agent_node.agent import intent_node
from app.agent_node.tool import tool_node
from app.agent_node.answer import answer_node

def build_agent_graph():

    graph = StateGraph(AgentState)

    # Register nodes
    graph.add_node("intent", intent_node)
    graph.add_node("tool", tool_node)
    graph.add_node("answer", answer_node)

    # Define execution flow
    graph.set_entry_point("intent")

    graph.add_edge("intent", "tool")
    graph.add_edge("tool", "answer")
    graph.add_edge("answer", END)

    return graph.compile()