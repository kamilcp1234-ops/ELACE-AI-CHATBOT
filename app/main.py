from fastapi import FastAPI
from app.rag_pipeline import ask_question
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Support Knowledge Copilot")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Support Knowledge Copilot is running"
    }


@app.get("/ask")
def ask(query: str):
    answer = ask_question(query)

    return {
        "question": query,
        "answer": answer
    }