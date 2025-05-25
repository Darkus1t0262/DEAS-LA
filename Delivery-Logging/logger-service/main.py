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
    Endpoint para registrar eventos.
    Hoy solo devolvemos el payload; luego conectaremos MongoDB.
    """
    # TODO: inserción en MongoDB
    return {"logged": payload}
