from typing import Optional

from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from fastapi import status

class Usuario(BaseModel):
    id: int
    username: str
    fullname: str
    institution: str
    is_active: bool
    
class UserUpdate(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    fullname: Optional[str] = None
    institution: Optional[str] = None
    is_active: Optional[bool] = None

app = FastAPI()

usuarios_router = APIRouter(prefix="/users", tags=["Usuarios"])

DB_FAKE = [
    {"id": 1, "username": "admin", "fullname": "Admin", "is_active": True,  "institution": "UChile"},
    {"id": 2, "username": "anaperez", "fullname": "Ana Pérez", "is_active": True,  "institution": "PUC"},
    {"id": 3, "username": "jperez", "fullname": "Juan Pérez", "is_active": False, "institution": "UChile"},
    {"id": 4, "username": "mlopez", "fullname": "María López", "is_active": True,  "institution": "USACH"},
    {"id": 5, "username": "crojas", "fullname": "Carlos Rojas", "is_active": False, "institution": "PUC"},
    {"id": 6, "username": "lmartinez", "fullname": "Laura Martínez", "is_active": True, "institution": "UChile"},
    {"id": 7, "username": "dtorres", "fullname": "Diego Torres", "is_active": True, "institution": "USACH"},
    {"id": 8, "username": "fsoto", "fullname": "Fernanda Soto", "is_active": False, "institution": "PUC"}
]

@usuarios_router.get("/usuarios")
async def obtener_usuarios() -> list[Usuario]:
    return DB_FAKE

@usuarios_router.get("/usuarios/{id}")
async def obtener_usuario(id:int) -> Usuario:
    for row in DB_FAKE:
        if row["id"] == id:
            return row
    return {"mensaje":"Usuario no encontrado"}

# @usuarios_router.get("/usuario/")
# async def obtener_usuario(id:int) -> dict:
#     for row in DB_FAKE:
#         if row["id"] == id:
#             return row
#     return {"mensaje":"Usuario no encontrado"}

@usuarios_router.post("/usuarios")
async def crear_usuario(data_user: Usuario) -> dict:
    print(data_user,data_user.model_dump())
    DB_FAKE.append(data_user.model_dump())
    return {"mensaje":"Usuario añadido correctamente"}

@usuarios_router.put("/usuarios/{id}")
async def actualizar_usuario(data: Usuario) -> dict:
    id = data.model_dump()["id"]
    for idx, row in enumerate(DB_FAKE):
        if row["id"] == id:
            DB_FAKE[idx] = data.model_dump()
            return {"mensaje":"Usuario actualizado correctamente"}
    return {"mensaje": "No se encontro el usuario"}

@usuarios_router.patch("/usuarios/{id}")
async def actualizar_parcialmente(id: int, data: UserUpdate): #-> dict:
    for row in DB_FAKE:
        if row["id"] == id:
            for key, value in data.model_dump(exclude_unset=True).items():
                row[key] = value
            return {"mensaje":"usuario actualizado correctamente"}    
    return {"mensaje":"Usuario no encontrado"} 
            
    
@usuarios_router.delete("/usuarios/{id}")
async def eliminar_usuario(id: int) -> dict:
    for idx, row in enumerate(DB_FAKE):
        if row["id"] == id:
            del DB_FAKE[idx]
            return {"mensaje":"Usuario eliminado correctamente"}
    
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

@usuarios_router.get("/usuarios/institution/{institution}/")
async def obtener_usurios_institucion(institution: str, state: bool = True) -> list[Usuario]:
    users = [row for row in DB_FAKE if(row["institution"]== institution and row["is_active"]== state)]
    return users

    # users = []
    # for row in DB_FAKE:
    #     if(row["institution"]== institution and row["is_active"]== state):
    #         users.usuarios_routerend(row)
    
app.include_router(usuarios_router)