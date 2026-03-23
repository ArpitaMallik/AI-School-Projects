from fastapi import FastAPI, Form
import requests

app = FastAPI()

@app.post("/summarize/")
def summarize(text: str = Form(...)):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": f"""Summarize the following text clearly and concisely in bullet points.
                        Focus only on the main ideas.
                        Keep the summary under 150 words.\n\n{text}""",
            "stream": False
        }
    )
    result = response.json()
    if response.status_code == 200:
        result = response.json()
        return {"summary": result.get("response", "")}
    else:
        return {"error": "Model request failed"}