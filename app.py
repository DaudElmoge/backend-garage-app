from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import session
from models import Base, engine, get_db, Customer, ServiceRecord, RepairRecord, CarMake, Mechanic
from schemas import CustomerSchema, ServiceRecordSchema ,RepairRecordSchema,CarMakeSchema,MechanicSchema
from seed import seed_data,RepairType,ServiceType

Base.metadata.create_all(bind=engine)

app = FastAPI()

#Frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
def on_startup():
    seed_data()

#Routes definition
@app.get("/")
def index():
    return {"message":"Welcome to AWAG garage management"}

#customers
@app.post("/customers")
def add_customer(customer: CustomerSchema, db: session = Depends(get_db)):
    new_customer = Customer(**customer.dict())
    db.add(new_customer)
    db.commit()
    return {"message":"Success"}

@app.get("/customers")
def get_customers(db:session=Depends(get_db)):
    return db.query(Customer).all()

@app.get("/customers/search/")
def search_customer(phone:str,db:session=Depends(get_db)):
    customer = db.query(Customer).filter(Customer.phone==phone).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
    
@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: session=Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id==customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"message":"Customer deleted successfully"}

#Service Records
@app.post("/services")
def add_service(service: ServiceRecordSchema,db: session=Depends(get_db)):
    new_service = ServiceRecord(**service.dict())
    db.add(new_service)
    db.commit()
    return {"message":"Service record added successfully"}

@app.get("/services")
def get_services(db: session=Depends(get_db)):
    return db.query(ServiceRecord).all()

@app.delete("/services/{service_id}")
def delete_service (service_id: int, db: session=Depends(get_db)):
    service= db.query(ServiceRecord).filter(ServiceRecord.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    db.delete(service)
    db.commit()
    return {"message":"Service deleted"}

#Repair Records
@app.post("/repairs",status_code=201)
def add_repair (repair: RepairRecordSchema, db: session=Depends(get_db)):
    new_repair = RepairRecord(**repair.dict())
    db.add(new_repair)
    db.commit()
    db.refresh(new_repair)
    return {"message":"Repair record added successfully", "id":new_repair.id}

@app.get("/repairs")
def get_repairs (db: session=Depends(get_db)):
    return db.query(RepairRecord).all()

@app.delete("/repairs/{repair_id}")
def delete_repair(repair_id: int, db: session=Depends(get_db)):
    repair = db.query(RepairRecord).filter(RepairRecord.id==repair_id).first()
    if not repair:
        raise HTTPException(status_code=404, detail="Repair not found")
    db.delete(repair)
    db.commit()
    return {"message": "Repair deleted"}

#Car Makes
@app.get("/car-makes")
def get_car_makes (db: session=Depends(get_db)):
    return db.query(CarMake).all()

#Mechanics
@app.get("/mechanics")
def get_mechanics (db: session=Depends(get_db)):
    return db.query(Mechanic).all()
                 
@app.get("/service-types")
def get_service_types(db: session = Depends(get_db)):
    return db.query(ServiceType).all()

@app.get("/repair-types")
def get_repair_types(db: session = Depends(get_db)):
    return db.query(RepairType).all()