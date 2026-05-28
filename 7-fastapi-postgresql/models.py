from datetime import datetime
from typing import Optional
import uuid

from sqlalchemy import UUID, Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    fullname: Mapped[str] = mapped_column(String(100))
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
class OrdenProducto(Base):
    __tablename__ = "ordenes_productos"
    
    orden_id: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("ordenes.id", ondelete="CASCADE"), primary_key=True)
    producto_id: Mapped[int] = mapped_column(Integer, ForeignKey("productos.id", ondelete="CASCADE"), primary_key=True)

class Producto(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    descripcion: Mapped[str] = mapped_column(String(350))
    precio: Mapped[int] = mapped_column(Integer)
    stock: Mapped[int] = mapped_column(Integer) 
    
    ordenes: Mapped[list["Orden"]] = relationship(back_populates="productos", secondary="ordenes_productos")
class Cliente(Base):
    __tablename__ = "clientes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True)
    telefono: Mapped[str] = mapped_column(String(20), nullable = True)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    creado_en: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)
    
    ordenes: Mapped[list["Orden"]] = relationship(back_populates="cliente", cascade="all")
class Orden(Base):
    __tablename__  ="ordenes"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    cantidad: Mapped[int] = mapped_column(Integer)
    estado: Mapped[str] = mapped_column(String, default="pendiente")
    creado_en: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)
    
    client_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("clientes.id", ondelete="CASCADE"), nullable=True)
    cliente: Mapped[Optional["Cliente"]] = relationship(back_populates="ordenes")
    
    productos: Mapped[list["Producto"]] = relationship(back_populates="ordenes", secondary="ordenes_productos")
