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