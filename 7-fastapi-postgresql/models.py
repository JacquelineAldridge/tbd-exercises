from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Producto(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    descripcion: Mapped[str] = mapped_column(String(350))
    precio: Mapped[int] = mapped_column(Integer)
    stock: Mapped[int] = mapped_column(Integer) 