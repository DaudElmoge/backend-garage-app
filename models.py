from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String,Text,ForeignKey,Date,Time,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime


engine = create_engine("sqlite:///garage.db",echo=True)

Session = sessionmaker(bind=engine)

def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()

class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    services = relationship("ServiceRecord", back_populates="customer", cascade="all, delete")
    repairs = relationship("RepairRecord", back_populates="customer", cascade="all, delete")

class ServiceRecord(Base):
    __tablename__ = "service_records"

    id = Column(Integer,primary_key=True)
    vehicle_number = Column(String)
    car_make = Column(String)
    car_model = Column(String)
    mechanic_name = Column(String)
    service_type = Column(String)
    service_date = Column(Date)
    service_time = Column(Time)
    comments = Column(Text)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="services")

class RepairRecord(Base):
    __tablename__ ="repair_records"

    id = Column(Integer, primary_key=True)
    vehicle_number = Column(String)
    car_make = Column(String)
    car_model = Column(String)
    mechanic_name = Column(String)
    repair_type = Column(String)
    repair_date = Column(Date)
    repair_time = Column(Time)
    comments = Column(Text)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="repairs")   

class CarMake(Base):
    __tablename__ = "car_makes"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def _repr_(self):
        return f"<CarMake(name='{self.name}')>"
    
class Mechanic(Base):
    __tablename__ = "mechanics"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Mechanic(name='{self.name}')>"
    