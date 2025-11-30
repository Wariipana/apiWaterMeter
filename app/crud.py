from sqlalchemy.orm import Session
from . import schemas
from app.database.models import medition

def crear_medicion(db: Session, data: schemas.MedicionCreate):
    medicion = medition.Medicion(**data.dict())
    db.add(medicion)
    db.commit()
    db.refresh(medicion)
    return medicion

def obtener_mediciones(db: Session, limit=1000):
    return db.query(medition.Medicion).order_by(medition.Medicion.id.desc()).limit(limit).all()
