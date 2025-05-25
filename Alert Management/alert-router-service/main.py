from fastapi import FastAPI

app = FastAPI(title="Alert Router Service")

@app.get("/health")
async def health_check():
    """
    Health‐check endpoint: retorna status 'ok' y nombre del servicio.
    """
    return {"status": "ok", "service": "alert-router"}

@app.post("/route")
async def route_alert(payload: dict):
    """
    Ruta principal: decide el canal de entrega y reenvía la alerta.
    Por ahora devolvemos el payload para probar el endpoint.
    """
    # TODO: lógica para decidir canal (SMS, email, push) o encolar en Kafka
    return {"routed": payload}
