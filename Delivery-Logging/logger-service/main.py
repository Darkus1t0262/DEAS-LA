from fastapi import FastAPI

app = FastAPI(title="Logger Service")

@app.get("/health")
async def health_check():
    """
    Health‐check endpoint.
    """
    return {"status": "ok", "service": "logger"}

@app.post("/log")
async def log_event(payload: dict):
    """
    Endpoint to register events.
    Fow now just the payload; later join to MongoDB.
    """
    # ALL: Insert on MongoDB
    return {"logged": payload}
