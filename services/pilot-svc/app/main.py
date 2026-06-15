from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn, os, socket

app = FastAPI(title="Pilot Service", version="1.0.0")
Instrumentator().instrument(app).expose(app)  # /metrics for Prometheus

PILOTS_DB = [
    {"id": 1, "name": "Omar Al-Rashid", "status": "available", "rating": 4.9},
    {"id": 2, "name": "Ahmed Khalil",   "status": "on_delivery", "rating": 4.7},
    {"id": 3, "name": "Adham Nour",     "status": "available", "rating": 4.8},
]

@app.get("/health")
def health():
    return {"status": "ok", "pod": socket.gethostname()}

@app.get("/api/pilots")
def list_pilots():
    return {"pilots": PILOTS_DB, "count": len(PILOTS_DB)}

@app.get("/api/pilots/{pilot_id}")
def get_pilot(pilot_id: int):
    pilot = next((p for p in PILOTS_DB if p["id"] == pilot_id), None)
    if not pilot:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Pilot not found")
    return pilot

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
