from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
import httpx, os, socket, uvicorn

app = FastAPI(title="Order Service", version="1.0.0")
Instrumentator().instrument(app).expose(app)

PILOT_SVC_URL = os.getenv("PILOT_SVC_URL", "http://127.0.0.1:5000")

ORDERS_DB = [
    {"id": "ORD-001", "pilot_id": 1, "destination": "Maadi", "status": "delivered"},
    {"id": "ORD-002", "pilot_id": 3, "destination": "New Cairo", "status": "in_progress"},
]

@app.get("/health")
def health():
    return {"status": "ok", "pod": socket.gethostname()}

@app.get("/api/orders")
def list_orders():
    return {"orders": ORDERS_DB, "count": len(ORDERS_DB)}

@app.get("/api/orders/{order_id}/pilot")
async def get_order_with_pilot(order_id: str):
    order = next((o for o in ORDERS_DB if o["id"] == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{PILOT_SVC_URL}/api/pilots/{order['pilot_id']}")
        resp.raise_for_status()
    return {**order, "pilot": resp.json()}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5001)
