from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import session
from models import Base, engine, get_db, Customer, ServiceRecord, RepairRecord