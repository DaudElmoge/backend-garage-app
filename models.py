class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)

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