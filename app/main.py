from fastapi import FastAPI
from pydantic import BaseModel
from core-lite.chain import run_chain

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/query")
async def query_rag(q: Query):
    answer = run_chain(q.question)
    return {"answer": answer}
