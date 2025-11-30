from pydantic import BaseModel

class MedicionCreate(BaseModel):
    nivel: int
    tds: float
    temp: float
    hum: float
    pres: float

class MedicionOut(MedicionCreate):
    id: int
    timestamp: str

    class Config:
        orm_mode = True
