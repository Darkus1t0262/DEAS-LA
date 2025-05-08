from fastapi import FastAPI

app = FastAPI(title="Alert Generator")

@app.post("/alerts")
async def create_alert(payload: dict):
    # aquí iría la lógica de validación y envío a Kafka
    return {"received": payload}
