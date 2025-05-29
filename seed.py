from fastapi import FastAPI
from models import CarMake, Mechanic, Session
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

    for make in car_makes:
       if not db.query(CarMake).filter_by(name=make).first():
          db.add(CarMake(name=make))

    for mech in mechanics:
        if not db.query(Mechanic).filter_by(name=mech).first():
            db.add(Mechanic(name=mech))

    db.commit()
    db.close()