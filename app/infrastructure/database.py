from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cambia la URL de la base de datos según tu configuración
DATABASE_URL = "sqlite:///./database.db"  # Ejemplo para SQLite

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Para SQLite
# Para PostgreSQL, sería algo como:
# engine = create_engine("postgresql://user:password@localhost/dbname")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"} 