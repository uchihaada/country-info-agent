from typing import Optional, List, Dict, TypedDict

class AgentState(TypedDict):
    question: str
    country: Optional[str]
    requested_fields: Optional[List[str]]
    country_data: Optional[Dict]
    final_answer: Optional[str]
    error: Optional[str]
