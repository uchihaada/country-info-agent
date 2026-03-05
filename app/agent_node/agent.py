from typing import List
from pydantic import BaseModel
from langchain_core.messages import SystemMessage, HumanMessage

from app.llm.llm import get_llm
from app.model.state import AgentState
from app.utils.prompt_template import (
intent_system_prompt,
intent_user_prompt
)

class IntentOutput(BaseModel):
    country: str
    requested_fields: List[str]

def intent_node(state: AgentState) -> AgentState:
    question = state["question"]

    llm = get_llm()

    structured_llm = llm.with_structured_output(IntentOutput)

    messages = [
        SystemMessage(content=intent_system_prompt()),
        HumanMessage(content=intent_user_prompt(question)),
    ]

    result = structured_llm.invoke(messages)

    state["country"] = result.country
    state["requested_fields"] = result.requested_fields

    return state