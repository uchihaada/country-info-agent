from app.graph.agent_graph import build_agent_graph

def run(question: str) -> str:
    graph = build_agent_graph()

    state = {
        "question": question,
        "country": None,
        "requested_fields": None,
        "country_data": None,
        "final_answer": None,
        "error": None
    }

    result = graph.invoke(state)

    return result["final_answer"]

