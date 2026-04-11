# Image Caption Generator using Moondream:v2 (Ollama)

This project is an end-to-end application that generates captions for images using a FastAPI backend and a Streamlit frontend. It demonstrates how to integrate a web interface with a model-serving API for multimodal tasks.

## Features

* Upload an image through a simple Streamlit UI
* Backend processing using FastAPI
* Image encoding and API-based model inference
* Returns a generated caption for the uploaded image

## Project Structure

* `frontend/` – Streamlit application for user interaction
* `backend/` – FastAPI server handling image processing and model requests
* `requirements.txt` – Project dependencies

## How It Works

1. The user uploads an image via the Streamlit interface
2. The image is sent to the FastAPI backend
3. The backend encodes the image and forwards it to a model API
4. The model generates a caption and returns it to the frontend

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
uv venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 3. Run the backend

```bash
uvicorn main:app --reload
```

### 4. Run the frontend

```bash
streamlit run frontend/app.py
```

## Notes
This project depends on external vision-language models. Performance and successful execution may vary depending on available system resources.

## License

This project is licensed under the MIT License.
