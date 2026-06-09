from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers import productos, clientes, ordenes, users

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:5173"],
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )
Base.metadata.create_all(engine)

app.include_router(productos.router)
app.include_router(clientes.router)
app.include_router(ordenes.router)
app.include_router(users.router)