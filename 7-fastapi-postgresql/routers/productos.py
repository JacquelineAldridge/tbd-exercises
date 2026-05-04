
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
import models

from database import get_db
from schemas.productos import ProductCreate, ProductRead, ProductUpdate

router = APIRouter(prefix="/products", tags=["Productos"])

@router.get("/", response_model=list[ProductRead])
async def listar_productos(db: Session = Depends(get_db)):
    productos = db.execute(select(models.Producto)).scalars().all()
    return productos

@router.post("/", status_code=204)
async def crear_producto(producto: ProductCreate ,db: Session = Depends(get_db)):
    print(f"{producto} \n {producto.model_dump()}")
    nuevo_producto = models.Producto(**producto.model_dump())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

@router.delete("/{id}", status_code=204)
async def eliminar_producto(id: int,db: Session = Depends(get_db) ):
    producto = db.get(models.Producto,id )
    print(producto)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(producto)
    db.commit()


@router.patch("/{id}")
async def actualizar_producto(id: int,data: ProductUpdate, db: Session = Depends(get_db)):
    producto = db.get(models.Producto, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    data_update = data.model_dump(exclude_unset=True)
    
    for key, value in data_update.items():
        setattr(producto, key, value)
        
    db.commit()
    db.refresh(producto)
    
    return producto

@router.get("/stock-critico")
async def productos_con_stock_critico( db: Session = Depends(get_db)):
    productos = (db.execute(
        select(models.Producto)
        .where(models.Producto.stock <6))
        .scalars().all() )
    return productos