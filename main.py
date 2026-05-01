# main.py
from fastapi import FastAPI, HTTPException
from schemas import ShipmentRequest
from dhl_service import create_shipment, track_shipment

app = FastAPI(title="DHL Middleware API")

@app.get("/health")
def health():
    return {"status": "OK"}


@app.post("/shipments")
def create(data: ShipmentRequest):
    try:
        result = create_shipment(data)
        return {
            "message": "Spedizione creata",
            "tracking": result["tracking"],
            "label": result["label_file"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/track/{tracking}")
def track(tracking: str):
    try:
        status = track_shipment(tracking)
        return {
            "tracking": tracking,
            "status": status
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))