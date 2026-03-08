# Agentic AI Chatbot with FastAPI, LangGraph, and Streamlit

This project is an **Agentic AI Chatbot** built using:

- **LangGraph** for building the AI agent
- **LangChain** for LLM integrations
- **FastAPI** for the backend API
- **Streamlit** for the frontend UI
- **Tavily Search** for optional web search
- **OpenAI / Gemini** as LLM providers

The chatbot allows users to:

- Select an LLM provider
- Choose a model
- Enable or disable web search
- Provide a custom system prompt
- Chat with an AI agent through a web interface

---

# Project Architecture

```
User (Browser)
      ↓
Streamlit Frontend
      ↓
FastAPI Backend
      ↓
LangGraph AI Agent
      ↓
LLM Provider (OpenAI / Gemini)
      ↓
Response returned to UI
```

---

# Project Structure

```
.
├── ai_agent.py      # AI Agent logic using LangGraph
├── backend.py       # FastAPI backend server
├── frontend.py      # Streamlit user interface
├── Pipfile          # Pipenv dependency manager
└── README.md
```

---

# Installation

This project uses **Pipenv** for dependency management.

Install the required packages using the following commands.

## Install LangChain and LLM Integrations

```bash
pipenv install langchain_openai langchain_community openai
```

## Install Gemini Support

```bash
pipenv install langchain-google-genai google-genai
```

## Install Backend Dependencies

```bash
pipenv install pydantic fastapi uvicorn
```

## Install Frontend Dependency

```bash
pipenv install streamlit
```

---

# Activate Virtual Environment

```bash
pipenv shell
```

---

# Environment Variables

Before running the project, set the required API keys.

Example `.env` variables:

```
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_gemini_key
TAVILY_API_KEY=your_tavily_key
```

These keys allow the chatbot to:

- Generate responses using LLMs
- Perform web search when enabled

---

# Running the Application

## Run the AI Agent (Optional Test)

```bash
python ai_agent.py
```

---

## Start the FastAPI Backend

```bash
python backend.py
```

The backend will run on:

```
http://localhost:8000
```

---

## Start the Streamlit Frontend

```bash
pipenv run streamlit run frontend.py
```

The frontend will run on:

```
http://localhost:8501
```

---

# Features

- Multiple LLM Provider Support
  - OpenAI
  - Gemini

- Agentic AI using **LangGraph**

- Optional **Web Search Tool (Tavily)**

- Custom **System Prompt Control**

- Interactive **Streamlit Chat UI**

---

# Example Workflow

1. Start the backend server
2. Launch the Streamlit UI
3. Select:
   - Provider (OpenAI / Gemini)
   - Model
   - Enable or disable web search
4. Enter your prompt
5. The AI agent generates a response

---

# Technologies Used

- Python
- LangChain
- LangGraph
- FastAPI
- Streamlit
- Tavily Search API
- OpenAI API
- Google Gemini API

---

# Future Improvements

- Conversation memory
- Document RAG support
- Streaming responses
- Deployment with Docker
- Authentication and API keys management

---

# License
Krishna Varma Vetukuri
