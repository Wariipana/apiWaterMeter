from sqlalchemy import Column, Integer, Float, DateTime, func
from app.database.database import Base

class Medicion(Base):
    __tablename__ = "mediciones"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    nivel = Column(Integer)
    tds = Column(Float)
    temp = Column(Float)
    hum = Column(Float)
    pres = Column(Float)