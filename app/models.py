from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base

class Evidencia(Base):
    __tablename__ = "evidencias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    uuid_dispositivo = Column(String, index=True, nullable=False)
    nombre_archivo = Column(String, nullable=False)
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    resultado_json = Column(Text, nullable=False)