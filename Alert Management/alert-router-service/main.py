from fastapi import FastAPI

app = FastAPI(title="Alert Router Service")

@app.get("/health")
async def health_check():
    """
    Health‐check endpoint: return status 'ok' and service name.
    """
    return {"status": "ok", "service": "alert-router"}

@app.post("/route")
async def route_alert(payload: dict):
    """
    Principal root: Chose channel for recibe and alert resend.
    For now return the payload to test endpoint.
    """
    # ALL: Logic to choose channel (SMS, email, push) or on Kafka
    return {"routed": payload}
