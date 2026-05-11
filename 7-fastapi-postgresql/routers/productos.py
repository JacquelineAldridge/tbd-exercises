
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import Session
import models

from database import get_db
from schemas.productos import ProductCreate, ProductRead, ProductUpdate

router = APIRouter(prefix="/products", tags=["Productos"])

@router.get("/", response_model=list[ProductRead])
async def listar_productos(db: Session = Depends(get_db)):
    productos = db.execute(select(models.Producto)).scalars().all()
    return productos

@router.post("/", status_code=201)
async def crear_producto(producto: ProductCreate ,db: Session = Depends(get_db)):
    print(f"{producto} \n {producto.model_dump()}")
    nuevo_producto = models.Producto(**producto.model_dump())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

@router.post("/productos", status_code=201)
async def crear_productos(
    productos: list[ProductCreate],
    db: Session = Depends(get_db)
):
    # Método 1
    # nuevos_productos = []

    # for producto in productos:
    #     nuevo_producto = models.Producto(**producto.model_dump())
    #     db.add(nuevo_producto)
    #     nuevos_productos.append(nuevo_producto)

    # db.commit()

    # Método 2
    nuevos_productos = [
        models.Producto(**producto.model_dump())
        for producto in productos
    ]
    db.add_all(nuevos_productos)
    
    db.commit()

    for producto in nuevos_productos:
        db.refresh(producto)

    return nuevos_productos

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

@router.get("/productos-ordenes-pendientes", response_model=list[ProductRead])
async def producots_ordenes_pendientes(db: Session = Depends(get_db)):
    
    # Forma 1
    # productos = db.execute(select(models.Producto)).scalars().all()
    
    # print(productos)
    # productos_pendientes = []
    # for producto in productos:
    #     pendiente = False
    #     for o in producto.ordenes:
    #         if(o.estado == "Pendiente"):
    #             pendiente= True
    #             break
    #     if(pendiente):
    #         productos_pendientes.append(producto)
    #     print(producto)
    
    
    #productos_pendientes = [producto for p in productos if(any(o.estado == "Pendiente" for o in p.ordenes))] 
    
    # Forma 2
    productos_pendientes = (db.execute(
        select(models.Producto)
        .join(models.Producto.ordenes)
        .where(models.Orden.estado == "Pendiente")
        .distinct()
        )
        .scalars().all())
    
    return productos_pendientes

@router.get("/populares", response_model=list[ProductRead])
async def productos_populares(min_orders: int = 1, db: Session = Depends(get_db)):
    
    productos = (db.execute(
        select(models.Producto)
        .join(models.Producto.ordenes)
        .group_by(models.Producto.id)
        .having(func.count(models.Orden.id)> min_orders)
        .distinct()
        )
        .scalars().all())
    
    return productos


@router.get("/sin-ordenes", response_model=list[ProductRead])
async def productos_sin_ordenes(db: Session = Depends(get_db)):

    productos = db.execute(
        select(models.Producto)
        .outerjoin(models.Producto.ordenes)
        .where(models.Orden.id.is_(None))
    ).scalars().all()
    
    return productos
