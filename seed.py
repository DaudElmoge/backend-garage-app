from fastapi import FastAPI
from models import CarMake, Mechanic, RepairType, ServiceType, Session
from sqlalchemy.orm import Session as DbSession

app=FastAPI()

@app.on_event("startup")
def seed_data():
    db=DbSession=Session()
    
    car_makes = [
        "Audi", "BMW", "Daihatsu", "Ford", "Honda", "Hyundai", "Isuzu", "Kia", 
        "Land Rover", "Lexus", "Mazda", "Mercedes-Benz", "Mitsubishi", 
        "Nissan", "Subaru", "Suzuki", "Toyota", "Volkswagen", "Volvo"
    ]
    mechanics = [
        "James Otieno", "Daud Ahmed", "Khalid Mabrux", "John Kamau",
        "Brian Ochieng", "Samuel Njoroge", "Amit Sharma"
    ]

    service_types = [
    "Engine Oil Change", "Gearbox Oil Change", "Tire Rotation",
    "Engine Diagnosis", "Battery Check", "Brake Inspection", "General Service"
    ]

    repair_types = [
    "Engine Repair", "Brake Replacement", "Suspension Fix",
    "Electrical Repair", "AC Repair", "Accident Damage", "Other"
    ]

    for make in car_makes:
       if not db.query(CarMake).filter_by(name=make).first():
          db.add(CarMake(name=make))

    for mech in mechanics:
        if not db.query(Mechanic).filter_by(name=mech).first():
            db.add(Mechanic(name=mech))
    for service in service_types:
        if not db.query(ServiceType).filter_by (name=service).first():
            db.add(ServiceType(name=service))
    for repair in repair_types:
        if not db.query(RepairType).filter_by(name=repair).first():
            db.add(RepairType(name=repair))

    db.commit()
    db.close()