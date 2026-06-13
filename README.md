# Agentic AI Workspace

A comprehensive learning workspace covering Agentic AI concepts, workflows, and end-to-end projects built with **LangGraph**, **LangChain**, and related tools.

---

## Workspace Structure

### 1. LangGraph Basics (`1-LangGraph-Basic/`)
Foundational notebooks covering core LangGraph concepts:

| Notebook | Topic |
|---|---|
| `1-simplegraph.ipynb` | Building a simple graph |
| `2-chatbot.ipynb` | Basic chatbot with LangGraph |
| `3-dataclassstateschema.ipynb` | State management using dataclasses |
| `4-pydantic.ipynb` | Pydantic-based state schemas |
| `5-chainsusinglanggraph.ipynb` | Building chains using LangGraph |
| `6-chatbotwithmultipletools.ipynb` | Chatbot with multiple tool integrations |
| `7-ReActAgent.ipynb` | ReAct agent implementation |

---

### 2. LangGraph Advanced (`2-LangGraph-Advance/`)
| Notebook | Topic |
|---|---|
| `1-streaming.ipynb` | Streaming responses with LangGraph |

---

### 3. Debugging (`3-Debugging/`)
Debugging a LangGraph agent using **LangGraph Studio**:
- `groq_Agent.py` — Groq-powered agent for local debugging
- `langgraph.json` — LangGraph Studio configuration

---

### 4. Workflows (`4-Workflows/`)
Agentic workflow patterns:

| Notebook | Pattern |
|---|---|
| `1-prompting-chaining.ipynb` | Prompt chaining |
| `2-parallelization.ipynb` | Parallel execution |
| `3-Routing.ipynb` | Conditional routing |
| `4-orchestrator-workers.ipynb` | Orchestrator-worker pattern |
| `5-Evaluator-optimizer.ipynb` | Evaluator-optimizer loop |

---

### 5. Human in the Loop (`5-Humanintheloop/`)
| Notebook | Topic |
|---|---|
| `1-humanintheloop.ipynb` | Implementing human approval and intervention steps |

---

### 6. RAGs (`6-RAGs/`)
Retrieval-Augmented Generation patterns:

| Notebook | Pattern |
|---|---|
| `1-Agentic-RAG.ipynb` | Agentic RAG |
| `2-Corrective-RAG.ipynb` | Corrective RAG (CRAG) |
| `3-Adaptive-RAG.ipynb` | Adaptive RAG |

---

### 7. Vectorless RAG (`7-Vectorless-RAG/`)
| Notebook | Topic |
|---|---|
| `PageIndex_Vectorless_RAG_CrashCourse.ipynb` | RAG without vector databases using page indexing |

---

### 8. Guardrails (`8-Gaurdrails/`)
| Notebook | Topic |
|---|---|
| `langchain_guardrails_crash_course.ipynb` | Input/output guardrails with LangChain |

---

### 9. MCP + LangChain (`9-MCPLANGCHAIN/`)
Integration of **Model Context Protocol (MCP)** with LangChain:
- `mathserver.py` — MCP math tool server
- `weather.py` — MCP weather tool server
- `client.py` — MCP client connecting to servers
- `main.py` — Entry point

---

### AgenticChatbot (`AgenticChatbot/`)
An end-to-end production-style **Agentic AI Chatbot** built with LangGraph and Streamlit.

**Use cases supported:**
- **Basic Chatbot** — Conversational chatbot using Groq LLM
- **Chatbot with Web Search** — Chatbot with real-time web search tool integration
- **AI News** — Fetches, summarizes, and saves the latest AI news

**Project structure:**
```
AgenticChatbot/
├── app.py                        # Streamlit app entry point
├── src/langgraphagenticai/
│   ├── graph/graph_builder.py    # LangGraph graph setup for each use case
│   ├── nodes/                    # Chatbot, tool, and AI news nodes
│   ├── state/state.py            # Shared graph state definition
│   ├── tools/search_tool.py      # Web search tool
│   ├── LLMs/groq_llm.py         # Groq LLM configuration
│   └── ui/streamlitui/           # Streamlit UI components
└── AINews/weekly_summary.md      # Auto-generated AI news summaries
```

**Run the chatbot:**
```bash
streamlit run app.py
```

---

## Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph) — Agent graph framework
- [LangChain](https://github.com/langchain-ai/langchain) — LLM application framework
- [Groq](https://groq.com/) — Fast LLM inference
- [Streamlit](https://streamlit.io/) — UI for the chatbot
- [FAISS](https://github.com/facebookresearch/faiss) — Vector similarity search
- [MCP](https://modelcontextprotocol.io/) — Model Context Protocol

---

## Setup

1. Clone the repository:
```bash
git clone https://github.com/tejashwin-05/Agentic-AI-workspace.git
cd Agentic-AI-workspace
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your API keys:
```
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

4. Run notebooks in Jupyter or launch the chatbot with `streamlit run AgenticChatbot/app.py`
