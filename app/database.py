import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# El archivo de base de datos se creará de forma automática en la raíz del proyecto
SQLALCHEMY_DATABASE_URL = "sqlite:///./callshield.db"

engine = create_engine(
    # check_same_thread=False es obligatorio únicamente para SQLite en entornos asíncronos/multihilo como FastAPI
    # Evita conflictos cuando múltiples peticiones móviles entran simultáneamente
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia inyectable para abrir y cerrar sesiones limpiamente en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()