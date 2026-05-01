# schemas.py
from pydantic import BaseModel

class Address(BaseModel):
    identification_number: str
    name: str
    address: str
    city: str
    postal_code: str
    country: str
    phone: str
    state: str
    business_type: str
    available_days: str
    fiscal_id: str
    attention: str
    registration_number: str
    available_timing: str

class Package(BaseModel):
    weight: float
    length: int
    width: int
    height: int
    
class Service(BaseModel):
    special_instruction: str
    pickup_mode: str = "P" # Express default
    declared_value: int 
    

class ShipmentRequest(BaseModel):
    shipper: Address
    receiver: Address
    package: Package
    service: Service  
