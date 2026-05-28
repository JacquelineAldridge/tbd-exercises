from datetime import datetime
from typing import Optional
import uuid

from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    telefono: Optional[str]
    activo: bool
    creado_en: datetime
    
class OrdenBase(BaseModel):
    id: uuid.UUID
    cantidad: int
    estado: str
    creado_en: datetime
    
    