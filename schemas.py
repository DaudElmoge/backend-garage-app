from pydantic import BaseModel
from datetime import date,time


class CustomerSchema(BaseModel):
    name: str
    phone: str

class ServiceRecordSchema(BaseModel):
    vehicle_number: str
    car_make: str
    car_model: str
    mechanic_name: str
    service_type: str
    service_date: date
    service_time: time
    comments: str
    customer_id: int

class RepairRecordSchema(BaseModel):
    vehicle_number: str
    car_make: str
    car_model: str
    mechanic_name: str
    repair_type: str
    repair_date: date
    repair_time: time
    comments: str
    customer_id: int

class CarMakeSchema(BaseModel):
    id:int
    name:str

class MechanicSchema(BaseModel):
    id:int
    name:str    