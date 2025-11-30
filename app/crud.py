from sqlalchemy.orm import Session
from . import schemas
from database.models.medition import Medicion

def crear_medicion(db: Session, data: schemas.MedicionCreate):
    medicion = Medicion(**data.dict())
    db.add(medicion)
    db.commit()
    db.refresh(medicion)
    return medicion

def obtener_mediciones(db: Session, limit=1000):
    return db.query(Medicion).order_by(Medicion.id.desc()).limit(limit).all()
