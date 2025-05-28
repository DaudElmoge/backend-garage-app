from pydantic import BaseModel
from datetime import date,time


class CarMakeSchema(BaseModel):
    id:int
    name:str

class MechanicSchema(BaseModel):
    id:int
    name:str    