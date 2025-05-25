from fastapi import FastAPI

app = FastAPI(title="Alert Generator Service")

@app.get("/health")
async def health_check():
    """
    Health‐check endpoint: retorna status 'ok' y nombre del servicio.
    """
    return {"status": "ok", "service": "alert-generator"}

@app.post("/alerts")
async def create_alert(payload: dict):
    # aquí iría la lógica de validación y envío a Kafka
    return {"received": payload}
