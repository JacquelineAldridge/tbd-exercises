from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from database import get_db
from schemas import productos
from schemas.clientes import ClientCreate, ClientRead, ClientUpdate

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.get("/", response_model=list[ClientRead])
async def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.execute(select(models.Cliente)).scalars().all()
    return clientes


@router.get("/{cliente_id}", response_model=ClientRead)
async def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.get(models.Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente


@router.post("/", response_model=ClientRead, status_code=201)
async def crear_cliente(data: ClientCreate, db: Session = Depends(get_db)):
    nuevo = models.Cliente(**data.model_dump(exclude_none=True))
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.post("/clientes", status_code=201)
async def crear_clientes(
    clientes: list[ClientCreate],
    db: Session = Depends(get_db)
):

    nuevos_clientes = [
        models.Cliente(**cliente.model_dump())
        for cliente in clientes
    ]
    db.add_all(nuevos_clientes)
    
    db.commit()

    for cliente in nuevos_clientes:
        db.refresh(cliente)


    db.add_all(nuevos_clientes)
    
    db.commit()

    for cliente in nuevos_clientes:
        db.refresh(cliente)

    return nuevos_clientes

@router.patch("/{cliente_id}", response_model=ClientRead)
async def actualizar_cliente(cliente_id: int, data: ClientUpdate, db: Session = Depends(get_db)):
    cliente = db.get(models.Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    for campo, valor in data.model_dump(exclude_unset=True).items():
        setattr(cliente, campo, valor)
    db.commit()
    db.refresh(cliente)
    return cliente


@router.delete("/{cliente_id}", status_code=204)
async def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.get(models.Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    db.delete(cliente)
    db.commit()
