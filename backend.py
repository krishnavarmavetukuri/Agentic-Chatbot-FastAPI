# ==============================================================
# BACKEND SERVER (FastAPI)
# This file exposes an API endpoint that allows the frontend
# (Streamlit UI) to interact with the LangGraph AI Agent.
#
# Flow:
# Streamlit Frontend → FastAPI Backend → AI Agent → LLM → Response
# ==============================================================


# --------------------------------------------------------------
# Optional: Load environment variables from .env file
# Only needed if you are NOT using pipenv or system env vars
# --------------------------------------------------------------
# from dotenv import load_dotenv
# load_dotenv()


# --------------------------------------------------------------
# Step 1: Define Request Schema using Pydantic
# Pydantic validates incoming API request data automatically.
# This ensures the request contains the required fields and types.
# --------------------------------------------------------------
from pydantic import BaseModel
from typing import List


class RequestState(BaseModel):
    """
    Request body structure expected from the frontend.
    """

    # Name of the AI model selected by the user
    model_name: str

    # AI provider (Gemini or OpenAI)
    model_provider: str

    # System prompt that defines the agent behavior
    system_prompt: str

    # List of user messages sent to the AI agent
    messages: List[str]

    # Boolean flag to enable/disable web search tool
    allow_search: bool


# --------------------------------------------------------------
# Step 2: Initialize FastAPI Application
# --------------------------------------------------------------
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent


# List of allowed models for security and validation
# Prevents users from calling unsupported models
ALLOWED_MODEL_NAMES = [
    "gemini-2.5-flash",
    "gemini-2.5-pro",
    "gpt-4o-mini"
]


# Create FastAPI application instance
app = FastAPI(title="LangGraph AI Agent")


# --------------------------------------------------------------
# Step 3: Create Chat API Endpoint
# This endpoint receives user input from the frontend,
# sends it to the AI agent, and returns the generated response.
# --------------------------------------------------------------
@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    Chat Endpoint

    This endpoint receives the user query from the frontend
    and routes it to the AI agent for processing.

    The agent dynamically selects:
    - LLM provider (Gemini / OpenAI)
    - Model
    - Whether to use web search
    - System prompt behavior
    """

    # ----------------------------------------------------------
    # Validate the requested model
    # ----------------------------------------------------------
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}


    # ----------------------------------------------------------
    # Extract parameters from the request body
    # ----------------------------------------------------------
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider


    # ----------------------------------------------------------
    # Call the AI Agent logic
    # This function creates the LangGraph agent and runs it
    # ----------------------------------------------------------
    response = get_response_from_ai_agent(
        llm_id,
        query,
        allow_search,
        system_prompt,
        provider
    )


    # ----------------------------------------------------------
    # Return the AI-generated response to the frontend
    # ----------------------------------------------------------
    return response


# --------------------------------------------------------------
# Step 4: Run the FastAPI server locally
# This starts the backend service.
# --------------------------------------------------------------
# API Base URL:
# http://127.0.0.1:9999
#
# Swagger Docs:
# http://127.0.0.1:9999/docs
# --------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=9999)