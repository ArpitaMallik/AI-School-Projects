from fastapi import FastAPI, UploadFile, File, HTTPException
import base64
import httpx

app = FastAPI()

@app.post("/caption/")
async def caption_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "moondream:v2",
                    "prompt": "Generate a description of this image.",
                    "images": [image_base64],
                    "stream": False
                },
                timeout=500.0
            )

        response.raise_for_status()
        result = response.json()
        caption = result.get("response", "").strip()

        return {"caption": caption}

    except httpx.RequestError:
        raise HTTPException(status_code=500, detail="Model server unreachable")

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=500, detail=f"Ollama error: {e.response.text}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))