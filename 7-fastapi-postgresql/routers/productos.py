
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
import models

from database import get_db
from schemas.productos import ProductCreate, ProductRead

router = APIRouter(prefix="/products", tags=["Productos"])

@router.get("/", response_model=list[ProductRead])
async def listar_productos(db: Session = Depends(get_db)):
    productos = db.execute(select(models.Producto)).scalars().all()
    return productos

@router.post("/")
async def crear_producto(producto: ProductCreate ,db: Session = Depends(get_db)):
    print(f"{producto} \n {producto.model_dump()}")
    nuevo_producto = models.Producto(**producto.model_dump())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto







