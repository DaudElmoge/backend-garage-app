from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import session
from models import Base, engine, get_db, Customer, ServiceRecord, RepairRecord, CarMake, Mechanic
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

#Frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Routes definition
@app.get("/")
def index():
    return {"message":"Welcome to AWAG garage management"}

