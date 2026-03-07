# ==============================================================
# FRONTEND (Streamlit UI)
# This file builds the user interface for interacting with
# the AI Agent system.
#
# Architecture Flow:
# User (Streamlit UI) → FastAPI Backend → LangGraph Agent → LLM
#
# The UI allows the user to:
# • Select an LLM provider (Gemini or OpenAI)
# • Select a model
# • Define the AI agent system prompt
# • Enable/disable web search
# • Send a query to the AI agent
# ==============================================================


# --------------------------------------------------------------
# Optional: Load environment variables from .env file
# Only required if you are NOT using pipenv or system env vars
# --------------------------------------------------------------
# from dotenv import load_dotenv
# load_dotenv()


# --------------------------------------------------------------
# Step 1: Import Streamlit
# Streamlit is used to build a simple interactive web UI
# --------------------------------------------------------------
import streamlit as st


# --------------------------------------------------------------
# Configure Streamlit page settings
# --------------------------------------------------------------
st.set_page_config(
    page_title="LangGraph Agent UI",
    layout="centered"
)


# --------------------------------------------------------------
# Application title and description
# --------------------------------------------------------------
st.title("AI Chatbot Agents")
st.write("Create and interact with customizable AI agents.")


# --------------------------------------------------------------
# Step 2: Define System Prompt Input
# The system prompt controls the personality and behavior
# of the AI agent.
#
# Example:
# "You are a helpful AI assistant specialized in coding."
# --------------------------------------------------------------
system_prompt = st.text_area(
    "Define your AI Agent:",
    height=70,
    placeholder="Type your system prompt here..."
)


# --------------------------------------------------------------
# Step 3: Define Available Models
# These models must match the models allowed in the backend.
# --------------------------------------------------------------
MODEL_NAMES_GEMINI = [
    "gemini-2.5-flash",
    "gemini-2.5-pro"
]

MODEL_NAMES_OPENAI = [
    "gpt-4o-mini"
]


# --------------------------------------------------------------
# Step 4: Select LLM Provider
# User chooses which AI provider to use
# --------------------------------------------------------------
provider = st.radio(
    "Select Provider:",
    ("Gemini", "OpenAI")
)


# --------------------------------------------------------------
# Step 5: Display model selection based on provider
# --------------------------------------------------------------
if provider == "Gemini":
    selected_model = st.selectbox(
        "Select Gemini Model:",
        MODEL_NAMES_GEMINI
    )

elif provider == "OpenAI":
    selected_model = st.selectbox(
        "Select OpenAI Model:",
        MODEL_NAMES_OPENAI
    )


# --------------------------------------------------------------
# Step 6: Optional Web Search Tool
# When enabled, the AI agent can use Tavily search
# to fetch real-time information from the internet.
# --------------------------------------------------------------
allow_web_search = st.checkbox("Allow Web Search")


# --------------------------------------------------------------
# Step 7: User Query Input
# The user types the question or prompt here.
# --------------------------------------------------------------
user_query = st.text_area(
    "Enter your query:",
    height=150,
    placeholder="Ask anything!"
)


# --------------------------------------------------------------
# Backend API URL
# This is the FastAPI endpoint that processes requests.
# --------------------------------------------------------------
API_URL = "http://127.0.0.1:9999/chat"


# --------------------------------------------------------------
# Step 8: Send Request to Backend
# When the user clicks the button, the query is sent to
# the FastAPI backend which runs the AI agent.
# --------------------------------------------------------------
if st.button("Ask Agent!"):

    # Ensure user entered a question
    if user_query.strip():

        # Import requests for HTTP communication
        import requests

        # ------------------------------------------------------
        # Prepare payload for the backend API
        # This must match the RequestState schema in backend.py
        # ------------------------------------------------------
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        # ------------------------------------------------------
        # Send POST request to FastAPI backend
        # ------------------------------------------------------
        response = requests.post(API_URL, json=payload)

        # ------------------------------------------------------
        # Handle backend response
        # ------------------------------------------------------
        if response.status_code == 200:

            response_data = response.json()

            # Check for backend errors
            if "error" in response_data:
                st.error(response_data["error"])

            else:
                # Display AI response
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")

