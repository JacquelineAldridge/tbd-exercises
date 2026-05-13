from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from schemas.users import UserCreate, UserRead
import models
from security import crear_hash_password, verificar_password

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserRead])
async def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.execute(select(models.Usuario)).scalars().all()
    return usuarios

@router.post("/registro", response_model=UserRead)
async def crear_usuario(usuario: UserCreate, db: Session = Depends(get_db)):
    print(usuario)
    existe_usuairo = (db.execute(
                select(models.Usuario)
                .where(models.Usuario.username == usuario.username)
    )).scalar_one_or_none()
    # if existe:
    #     raise HTTPException(status_code=409, detail="Ya existe la información en la base de datos")
    
    existe_email = (db.execute(
                select(models.Usuario)
                .where(models.Usuario.email == usuario.email)
    )).scalar_one_or_none()
    # if existe:
    #     raise HTTPException(status_code=409, detail="Ya existe la información en la base de datos")
    if existe_usuairo or existe_email:
        raise HTTPException(status_code=409, detail="Información ya registrado")
    
    db_usuario = models.Usuario(
        username = usuario.username,
        email = usuario.email,
        fullname = usuario.fullname,
        hashed_password = crear_hash_password(usuario.password)      
    )
    
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.post("/login")
async def login(credenciales_usuario: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = (db.execute(
                select(models.Usuario)
                .where(models.Usuario.username == credenciales_usuario.username)
    )).scalar_one_or_none()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Credenciales no validas")
    
    if not verificar_password(credenciales_usuario.password, usuario.hashed_password ):
        raise HTTPException(status_code=401, detail="Credenciales no validas")

    return {"mensaje":"Login exitoso"}