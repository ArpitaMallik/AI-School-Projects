# LLaMA Text Summarizer using Ollama

A local text summarization application built using FastAPI, Streamlit, and Ollama (LLaMA models).
It supports summarizing long text inputs using a chunking-based approach for improved performance and accuracy.

---

## Features

* Summarizes text into clear, concise bullet points
* Runs entirely locally using Ollama (no external API required)
* Handles long inputs using chunking and map-reduce summarization
* Simple and clean user interface with Streamlit
* FastAPI backend for modular design

---

## Project Structure

```
text-summarizer/
├── .venv/
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd text-summarizer
```

### 2. Create virtual environment (using uv)

```bash
uv venv
```

### 3. Activate the environment

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
.venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
uv pip install fastapi uvicorn streamlit requests python-multipart
```

(Optional)

```bash
uv pip freeze > requirements.txt
```

---

## Ollama Setup

Make sure Ollama is installed and running:

```bash
ollama pull llama3.2:1b
```

The backend expects Ollama at:

```
http://localhost:11434
```

---

## Running the Application

### Start backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

### Start frontend (Streamlit)

In a new terminal:

```bash
streamlit run frontend/app.py
```

Frontend runs at:

```
http://localhost:8501
```

---

## How It Works

1. User inputs text in the Streamlit UI
2. Frontend sends request to FastAPI backend
3. Backend splits text into chunks (if long)
4. Each chunk is summarized individually
5. Partial summaries are combined and summarized again
6. Final summary is returned to the user

---

## Requirements

* Python 3.9+
* uv (for environment management)
* Ollama with a LLaMA model installed

---

## Notes

* For short text, chunking is skipped automatically
* For long text, chunking improves accuracy and prevents model overload
* You can adjust chunk size and overlap in the backend for tuning performance
