import sys
import os

from fastapi import FastAPI, Request
from pydantic import BaseModel
from core_lite.chain import run_chain

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_endpoint(request: QueryRequest):
    result = run_chain(request.question)
    return {"answer": result}
