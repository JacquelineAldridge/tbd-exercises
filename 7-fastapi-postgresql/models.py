from datetime import datetime
import uuid

from sqlalchemy import UUID, Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Producto(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    descripcion: Mapped[str] = mapped_column(String(350))
    precio: Mapped[int] = mapped_column(Integer)
    stock: Mapped[int] = mapped_column(Integer) 
    
class Cliente(Base):
    __tablename__ = "clientes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True)
    telefono: Mapped[str] = mapped_column(String(20), nullable = True)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    creado_en: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)
    
class Orden(Base):
    __tablename__  ="ordenes"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    cantidad: Mapped[int] = mapped_column(Integer)
    estado: Mapped[str] = mapped_column(String, default="pendiente")
    creado_en: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)
