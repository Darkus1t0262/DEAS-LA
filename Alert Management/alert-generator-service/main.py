from fastapi import FastAPI

app = FastAPI(title="Alert Generator Service")

@app.get("/health")
async def health_check():
    """
    Health‐check endpoint: return 'ok' and name of the service.
    """
    return {"status": "ok", "service": "alert-generator"}

@app.post("/alerts")
async def create_alert(payload: dict):
    # Validation logic for the kafka
    return {"received": payload}
