from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="MyProject",
    description="A simple FastAPI project to add two numbers."
)

class AddRequest(BaseModel):
    num1: float
    num2: float

class AddResponse(BaseModel):
    result: float
    message: str = "Addition successful!"

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to MyProject! Use /add to add two numbers."}

@app.post("/add", response_model=AddResponse, tags=["Calculator"])
async def add_numbers(request: AddRequest):
    """
    Adds two numbers provided in the request body.

    - **num1**: The first number (float).
    - **num2**: The second number (float).
    """
    result = request.num1 + request.num2
    return AddResponse(result=result)
