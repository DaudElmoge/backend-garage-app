from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import session
from models import Base, engine, get_db, Customer, ServiceRecord, RepairRecord, CarMake, Mechanic
from schemas import CustomerSchema

Base.metadata.create_all(bind=engine)

app = FastAPI()

#Frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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