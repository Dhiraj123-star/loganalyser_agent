from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, HTMLResponse, StreamingResponse
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Log Analyzer Agent")

# Log analysis prompt template
log_analysis_prompt_text = """
You are a senior site reliability engineer.

Analyze the following application logs.

1. Identify the main errors or failures.
2. Explain the likely root cause in simple terms.
3. Suggest practical next steps to fix or investigate.
4. Mention any suspicious patterns or repeated issues.

Logs:
{log_data}

Respond in clear paragraphs. Avoid jargon where possible.
"""

# Initialize LLM
llm = ChatOpenAI(
    temperature=0.2,
    model="gpt-4o-mini",
    streaming=True  # Enabled streaming at the model level
)


def split_logs(log_text: str):
    """Split log text into manageable chunks"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )
    return splitter.split_text(log_text)


async def analyze_logs_stream(log_text: str):
    """Generator that analyzes logs and yields results chunk by chunk"""
    chunks = split_logs(log_text)

    for i, chunk in enumerate(chunks):
        formatted_prompt = log_analysis_prompt_text.format(log_data=chunk)
        
        # Stream the response from OpenAI for each chunk
        async for chunk_response in llm.astream(formatted_prompt):
            content = chunk_response.content
            if content:
                yield content
        
        # Add spacing between chunk analyses
        yield "\n\n---\n\n"


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main HTML page"""
    with open("index.html", "r") as f:
        return f.read()


@app.post("/analyze")
async def analyze_log_file(file: UploadFile = File(...)):
    """Analyze uploaded log file with streaming response"""
    if not file.filename.endswith(".txt"):
        return JSONResponse(
            status_code=400,
            content={"error": "Only .txt log files are supported"}
        )

    try:
        content = await file.read()
        log_text = content.decode("utf-8", errors="ignore")

        if not log_text.strip():
            return JSONResponse(
                status_code=400,
                content={"error": "Log file is empty"}
            )

        return StreamingResponse(
            analyze_logs_stream(log_text),
            media_type="text/plain"
        )
    
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Error analyzing logs: {str(e)}"}
        )


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    api_key_set = bool(os.getenv("OPENAI_API_KEY"))
    return {
        "status": "healthy",
        "openai_api_key_configured": api_key_set
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)