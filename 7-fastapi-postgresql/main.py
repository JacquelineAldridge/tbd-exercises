from fastapi import FastAPI

from database import Base, engine
from routers import productos

app = FastAPI()
Base.metadata.create_all(engine)

app.include_router(productos.router)