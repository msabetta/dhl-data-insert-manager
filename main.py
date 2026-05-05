# main.py
from fastapi import FastAPI, HTTPException
from schemas import ShipmentRequest, UpdateWaybillRequest, CancelWaybillRequest, ImportDataRequest, LoginRequest


app = FastAPI(title="DHL Middleware API")

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/GenerateWaybill")
def generate_waybill(data: ShipmentRequest):
    try:
        result = generate_waybill(data)
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/UpdateWaybill")
def update_waybill(data: UpdateWaybillRequest):
    try:
        result = update_waybill(data)
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/CancelWaybill")
def cancel_waybill(data: CancelWaybillRequest):
    try:
        result = cancel_waybill(data)
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ImportData")
def import_data(data: ImportDataRequest):
    try:
        result = import_data(data)
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/login")
def login(data: LoginRequest):
    try:
        result = login(data)
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))