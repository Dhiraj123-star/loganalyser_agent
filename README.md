
# 🛠️ Log Analyzer Agent

**An AI-powered diagnostic tool that transforms messy application logs into actionable intelligence.**

The Log Analyzer Agent leverages **FastAPI**, **LangChain**, and **OpenAI's GPT-4o-mini** to automatically parse logs, detect anomalies, and provide human-readable root cause analyses.

---

## 🚀 Key Features

* **📤 Effortless Ingestion:** Simple drag-and-drop interface for `.txt` log files.
* **🌊 Real-time Streaming:** Watch the AI analyze your logs word-by-word with instant feedback.
* **📝 Markdown Formatting:** Beautifully rendered reports with code snippets, bold text, and structured lists for better readability.
* **🔍 Root Cause Identification:** Moves beyond error messages to explain *why* a failure occurred.
* **💡 Fix Recommendations:** Provides code-level suggestions and practical next steps.
* **🐳 Containerized Deployment:** Fully Dockerized with Docker Compose support.
* **⚡ High-Speed Builds:** Uses **Astral `uv**` for lightning-fast dependency installation.
* **🤖 Automated Quality Assurance:** Integrated **CI/CD pipeline** via GitHub Actions that automatically lints code and runs test suites on every push.
* **🧪 Robust Integration Testing:** Custom test suite using `pytest` and `httpx` to verify endpoint health and API reliability without incurring AI costs.
* **📦 Automated Image Delivery:** Seamlessly builds and pushes verified Docker images to **Docker Hub** upon successful testing.

---

## 🏗️ System Architecture

The tool follows a modern pipeline for processing large text files:

1. **Backend:** FastAPI server orchestrating the LangChain logic using `StreamingResponse`.
2. **Processing:** Recursive text splitting (**2000** character chunks with **200** character overlap) to maintain context.
3. **LLM Layer:** OpenAI API processing via LangChain `astream` for token-by-token generation.
4. **Frontend:** Vanilla JS with `ReadableStream` API and `Marked.js` for real-time Markdown rendering.
5. **DevOps:** GitHub Actions pipeline utilizing `uv` virtual environments for secure, isolated testing.

---

## 🔧 Setup & Installation

### Prerequisites

* Python 3.8+ or **Docker**
* OpenAI API Key

### Option A: Local Setup

```bash
cd loganalyzer
# Using uv for 10x faster setup
uv venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

uv pip install -r requirements.txt

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

**Access the UI at:** `http://localhost:8000`

---

## 🧪 Testing

The project includes an automated test suite to ensure the API and UI plumbing are working correctly.

```bash
# Run tests locally via Docker
docker compose run --rm -e PYTHONPATH=. -v "$(pwd)/tests:/app/tests" log-analyzer uv run --with pytest --with httpx pytest tests/

```

---

## 🚦 API Reference

| Endpoint | Method | Description |
| --- | --- | --- |
| `/` | `GET` | Serves the web-based user interface. |
| `/analyze` | `POST` | Accepts `multipart/form-data` (file) and returns a **Text Stream**. |
| `/health` | `GET` | Returns system status and API key validation. |

---

## 📖 Usage Guide

1. Navigate to the web dashboard.
2. Upload a log file (e.g., use the provided `sample_log.txt`).
3. Click **Analyze Logs**.
4. Watch the **Real-time Report** generate, which breaks down:
* **Identified Errors:** High-priority failures found in the log.
* **Root Cause:** The technical "why" behind the errors.
* **Suggested Fixes:** Specific steps to resolve the identified issues.



---
