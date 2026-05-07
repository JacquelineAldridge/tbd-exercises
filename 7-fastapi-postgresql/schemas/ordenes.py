import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from schemas.utils import ClientBase
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
    client_id: Optional[int] 
    cliente: Optional[ClientBase]
    

class OrdenUpdate(BaseModel):
    cantidad: Optional[int] = None
    estado: Optional[str] = None
    
    client_id: Optional[int] = None

