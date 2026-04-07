from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/chat/stream")
def chat_stream(query: str):
    def generate():
        yield "data: Thinking...\n\n"
        yield f"data: You asked: {query}\n\n"
        yield "data: (Bedrock integration coming next)\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")
