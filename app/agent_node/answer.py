from langchain_core.messages import SystemMessage, HumanMessage

from app.model.state import AgentState
from app.llm.llm import get_llm
from app.utils.prompt_template import (
answer_system_prompt,
answer_user_prompt
)

def answer_node(state: AgentState) -> AgentState:

    if state.get("error"):
        state["final_answer"] = state["error"]
        return state

    requested_fields = state.get("requested_fields")
    
    country_data = state.get("country_data")

    resolved_data = country_data.resolve_fields(requested_fields)

    # If no fields requested → ask user to clarify
    if not requested_fields:
        state["final_answer"] = (
            "Please specify what information you want about the country.\n"
            "Example: capital of India, population of India or anything else."
        )
        return state

    question = state["question"]
    country_data = state.get("country_data")

    llm = get_llm()

    messages = [
        SystemMessage(content=answer_system_prompt()),
        HumanMessage(content=answer_user_prompt(question, requested_fields, resolved_data)),
    ]

    response = llm.invoke(messages)

    state["final_answer"] = response.content

    return state