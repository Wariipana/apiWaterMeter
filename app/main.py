from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, engine
import app.database.models.medition
import app.crud, app.schemas


app.database.models.medition.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/mediciones")
def recibir_medicion(data: app.schemas.MedicionCreate, db: Session = Depends(get_db)):
    nueva = app.crud.crear_medicion(db, data)
    return {"status": "ok", "id": nueva.id}

@app.get("/api/mediciones")
def listar_mediciones(db: Session = Depends(get_db)):
    return app.crud.obtener_mediciones(db)

