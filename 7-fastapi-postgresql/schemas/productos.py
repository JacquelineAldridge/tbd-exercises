from pydantic import BaseModel, ConfigDict


class ProductRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str
    descripcion: str
    precio: int
    stock: int
    
class ProductCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    nombre: str
    descripcion: str
    precio: int
    stock: int