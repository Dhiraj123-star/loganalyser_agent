FROM python:3.12-slim

# Use the official uv binary from the astral-sh image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy requirements and install using uv
COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

# Copy the rest of the application
COPY . .

EXPOSE 8000

# Start the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]