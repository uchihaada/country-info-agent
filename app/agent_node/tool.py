from app.model.state import AgentState
from app.tools.tool import fetch_country_data

def tool_node(state: AgentState) -> AgentState:
    country = state.get("country")

    if not country:
        state["error"] = "No country found in the request."
        return state

    try:
        country_data = fetch_country_data(country)
        state["country_data"] = country_data
    except Exception as e:
        state["error"] = str(e)

    return state

