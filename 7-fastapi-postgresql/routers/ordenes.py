import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from database import get_db
from schemas.ordenes import OrdenCreate, OrdenRead, OrdenUpdate

router = APIRouter(prefix="/ordenes", tags=["Ordenes"])

@router.get("/", response_model=list[OrdenRead])
async def listar_ordenes(db: Session = Depends(get_db)):
    ordenes = db.execute(select(models.Orden)).scalars().all()
    return ordenes


@router.get("/{orden_id}", response_model=OrdenRead)
async def obtener_orden(orden_id: uuid.UUID, db: Session = Depends(get_db)):
    orden = db.get(models.Orden, orden_id)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return orden


@router.post("/", response_model=OrdenRead, status_code=201)
async def crear_orden(data: OrdenCreate, db: Session = Depends(get_db)):
    # recuperar los productos
    productos = (db
                 .execute(select(models.Producto)
                  .where(models.Producto.id.in_(data.productos_ids)))
                  
                ).scalars().all()
    
    print(productos)
    nueva = models.Orden(**data.model_dump(exclude_none=True, exclude={"productos_ids"}))
    nueva.productos = productos
    
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@router.post("/ordenes", status_code=201)
async def crear_ordenes(
    ordenes: list[OrdenCreate],
    db: Session = Depends(get_db)
):

    nuevas_ordenes = [
        models.Orden(**orden.model_dump())
        for orden in ordenes
    ]
    db.add_all(nuevas_ordenes)
    
    db.commit()

    for orden in nuevas_ordenes:
        db.refresh(orden)

    return nuevas_ordenes


@router.patch("/{orden_id}", response_model=OrdenRead)
async def actualizar_orden(orden_id: uuid.UUID, data: OrdenUpdate, db: Session = Depends(get_db)):
    orden = db.get(models.Orden, orden_id)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    for campo, valor in data.model_dump(exclude_unset=True).items():
        setattr(orden, campo, valor)
    db.commit()
    db.refresh(orden)
    return orden


@router.delete("/{orden_id}", status_code=204)
async def eliminar_orden(orden_id: uuid.UUID, db: Session = Depends(get_db)):
    orden = db.get(models.Orden, orden_id)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    db.delete(orden)
    db.commit()
    
## obtener producots con ordenes pendiente
## obtener productos popular ()
## productos que no tienen ordenes