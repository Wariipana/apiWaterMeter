from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, engine
import app.database.models.medition
from app.crud import crear_medicion
from app.schemas import MedicionCreate


app.database.models.medition.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/mediciones")
def recibir_medicion(data: MedicionCreate, db: Session = Depends(get_db)):
    nueva = crear_medicion(db, data)
    return {"status": "ok", "id": nueva.id}

@app.get("/api/mediciones")
def listar_mediciones(db: Session = Depends(get_db)):
    return app.crud.obtener_mediciones(db)

