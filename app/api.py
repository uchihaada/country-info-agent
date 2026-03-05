from fastapi import FastAPI
from pydantic import BaseModel

from app.main import run

app = FastAPI(
title="Country Information AI Agent",
version="1.0.0"
)

class QuestionRequest(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    answer: str

@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    answer = run(request.question)

    return {
        "answer": answer
    }
