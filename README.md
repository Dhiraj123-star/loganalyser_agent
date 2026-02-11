# 🛠️ Log Analyzer Agent

**An AI-powered diagnostic tool that transforms messy application logs into actionable intelligence.**

The Log Analyzer Agent leverages **FastAPI**, **LangChain**, and **OpenAI's GPT-4o-mini** to automatically parse logs, detect anomalies, and provide human-readable root cause analyses.

---

## 🚀 Key Features

* **📤 Effortless Ingestion:** Simple drag-and-drop interface for `.txt` log files.
* **🤖 Intelligent Analysis:** Context-aware log parsing using GPT-4o-mini.
* **🔍 Root Cause Identification:** Moves beyond error messages to explain *why* a failure occurred.
* **💡 Fix Recommendations:** Provides code-level suggestions and practical next steps.
* **🐳 Containerized Deployment:** Fully Dockerized with Docker Compose support.
* **⚡ High-Speed Builds:** Uses **Astral `uv**` for lightning-fast dependency installation.

---

## 🏗️ System Architecture

The tool follows a modern pipeline for processing large text files:

1. **Backend:** FastAPI server orchestrating the LangChain logic.
2. **Processing:** Recursive text splitting (**2000** character chunks with **200** character overlap) to maintain context.
3. **LLM Layer:** OpenAI API processing via LangChain chains.
4. **Frontend:** Minimalist HTML5/JavaScript UI for real-time interaction.

---

## 🔧 Setup & Installation

### Prerequisites

* Python 3.8+ or **Docker**
* OpenAI API Key

### Option A: Local Setup

```bash
cd loganalyzer
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

pip install -r requirements.txt

```

### Option B: Docker Setup (Recommended)

This project includes a **Dockerfile** optimized with `uv` and a **docker-compose.yml** for secret management.

1. Create a `.env` file and add your key: `OPENAI_API_KEY=sk-proj-...`
2. Build and run:

```bash
docker compose up --build -d

```

---

## 🚦 Running the App

If running locally (Option A), start the server:

```bash
python app.py

```

*Alternatively, run via Uvicorn:*

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000

```

**Access the UI at:** `http://localhost:8000`

---

## 🧪 API Reference

| Endpoint | Method | Description |
| --- | --- | --- |
| `/` | `GET` | Serves the web-based user interface. |
| `/analyze` | `POST` | Accepts `multipart/form-data` (file) and returns JSON analysis. |
| `/health` | `GET` | Returns system status and API key validation. |

---

## 📖 Usage Guide

1. Navigate to the web dashboard.
2. Upload a log file (e.g., use the provided `sample_log.txt`).
3. Click **Analyze Logs**.
4. Review the **Analysis Report**, which breaks down:
* **Identified Errors:** High-priority failures found in the log.
* **Root Cause:** The technical "why" behind the errors.
* **Suggested Fixes:** Specific steps to resolve the identified issues.
