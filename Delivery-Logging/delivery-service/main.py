# delivery-service/main.py
from fastapi import FastAPI

app = FastAPI(title="Delivery Service")

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "delivery"}

@app.post("/deliver")
async def deliver(payload: dict):
    return {"delivered": payload}
