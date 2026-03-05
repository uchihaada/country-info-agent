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

    question = state["question"]
    requested_fields = state.get("requested_fields")
    country_data = state.get("country_data")

    llm = get_llm()

    messages = [
        SystemMessage(content=answer_system_prompt()),
        HumanMessage(content=answer_user_prompt(question, requested_fields, country_data)),
    ]

    response = llm.invoke(messages)

    state["final_answer"] = response.content

    return state