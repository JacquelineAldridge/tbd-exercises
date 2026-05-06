import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class OrdenCreate(BaseModel):
    cantidad: int
    estado: str = "pendiente"
    #creado_en: Optional[datetime] = None

class OrdenRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    cantidad: int
    estado: str
    creado_en: datetime

class OrdenUpdate(BaseModel):
    cantidad: Optional[int] = None
    estado: Optional[str] = None

