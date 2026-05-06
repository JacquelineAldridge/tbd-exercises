from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ClientRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    nombre: str
    email: EmailStr
    telefono: Optional[str]
    activo: bool
    creado_en: datetime
    
class ClientCreate(BaseModel):
    nombre: str = Field(max_length=100)
    email: EmailStr = Field(max_length=150)
    telefono: Optional[str] = Field(default=None, max_length= 20)
    activo: Optional[bool] = True
    #creaado_en: datetime = None
    
class ClientUpdate(BaseModel):
    nombre: Optional[str] =  Field(max_length=100, default = None)
    email: Optional[str]  =  Field(max_length=150, default = None)
    telefono: Optional[str]  =  Field(max_length=20, default = None)
    activo: Optional[str] = None