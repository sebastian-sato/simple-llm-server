from fastapi import FastAPI
import uvicorn
from llm import generate
app = FastAPI()

@app.post("/chat")
async def chat_endpoint(data: dict):
    if "payload" not in data:
        raise HTTPException(
            status_code=400,
            detail={"error": "Missing Required Field", "msg": "The 'payload' key must be provided."}
        )

    payload = data["payload"]

    # Handle optional fields with manual defaults
    max_tokens = data.get("max_tokens", 500)

    if not isinstance(max_tokens, int):
        raise HTTPException(status_code=400, detail="max_tokens must be an integer")

    response_text = generate(payload["messages"], max_tokens)

    return {"message": response_text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
