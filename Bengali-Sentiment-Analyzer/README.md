# Bengali Sentiment Analyzer using Sailor2 (Multilingual South-East Asia Model)

This project is a Bengali sentiment analysis application built using FastAPI, Streamlit, and the Sailor2 language model from Ollama. Sailor2 is a multilingual model designed specifically for South-East Asian languages, making it suitable for handling Bengali text with improved contextual understanding.

![UI](sentiment-analyzer-ui.png)


## Overview

The system takes a Bengali sentence as input and classifies it into one of three sentiment categories:

* ইতিবাচক (Positive)
* নেতিবাচক (Negative)
* নিরপেক্ষ (Neutral)

It combines a language model with rule-based post-processing to improve accuracy, especially for negation and context-sensitive cases.

## Features

* Bengali-first user interface using Streamlit
* FastAPI backend for handling inference requests
* Integration with Ollama running Sailor2 locally
* Rule-based correction layer to handle negation and common linguistic patterns
* Designed to reduce incorrect predictions for factual or neutral queries

## Architecture

* Frontend: Streamlit UI for user interaction
* Backend: FastAPI service for processing requests
* Model: Sailor2 (via Ollama API)
* Post-processing: Rule-based sentiment correction

## How It Works

1. User inputs a Bengali sentence in the UI
2. The sentence is sent to the FastAPI backend
3. A structured Bengali prompt is passed to the Sailor2 model
4. The model returns a sentiment label
5. A rule-based layer refines the result if needed
6. The final sentiment is displayed to the user

## Setup Instructions

1. Clone the repository and navigate to the project folder
2. Create and activate a virtual environment
3. Install dependencies:

   ```
   pip install fastapi uvicorn streamlit requests python-multipart
   ```
4. Ensure Ollama is running and the Sailor2 model is available:

   ```
   ollama pull sailor2:1b
   ```

## Running the Application

Start the backend:

```
uvicorn main:app --reload
```

Start the frontend:

```
streamlit run app.py
```

## Notes

* The model is optimized for multilingual usage, particularly South-East Asian languages
* Rule-based overrides are used to improve handling of negation and neutral queries
* Performance may vary due to the lightweight nature of the 1B model
