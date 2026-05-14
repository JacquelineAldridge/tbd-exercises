from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from schemas.users import Token, TokenData, UserCreate, UserRead
import models
from security import crear_access_token, crear_hash_password, verificar_password, verificar_token
from config import settings

router = APIRouter(prefix="/users", tags=["Users"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="users/login")

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

    access_token = crear_access_token(data = {"sub": usuario.username, "id": usuario.id}, 
                                      expires_delta=timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTOS))
    
    return Token(access_token=access_token, token_type="bearer") #{"mensaje":"Login exitoso"}

def obtener_usuario_actual(token:str = Depends(oauth2_schema), db: Session = Depends(get_db)): 
    payload = verificar_token(token)
    
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail = "Token invalido o expirado",
                            headers = {"WWW-Authenticate": "Bearer"}
                            )
    token_data = TokenData(id = payload.get("id"), username = payload.get("sub"))
    
    usuario = db.get(models.Usuario, token_data.id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/me", response_model=UserRead)
def obtener_usuario(usuario_actual: models.Usuario = Depends(obtener_usuario_actual)):
    return usuario_actual