from datetime import datetime

from sqlalchemy import Boolean, Integer, String, create_engine, func, or_, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

engine = create_engine("sqlite:///estudiante.sqlite3", echo=False)

class Base(DeclarativeBase):
    pass

class Estudiante(Base):
    __tablename__ = "estudiantes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    rut: Mapped[str] = mapped_column(String(12), unique=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    apellido: Mapped[str] = mapped_column(String(50), nullable=False)
    carrera: Mapped[str] = mapped_column(String(100), nullable=False)
    año_ingreso: Mapped[int]= mapped_column(Integer, nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    fecha_registro: Mapped[datetime] = mapped_column(default=datetime.now)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.carrera}"
    
    
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)

with Session() as session:
    estudiantes = [
        Estudiante(rut="12345678-9", nombre="Juan", apellido="Pérez", carrera="Ingeniería Civil", año_ingreso=2024),
        Estudiante(rut="98765432-1", nombre="María", apellido="González", carrera="Medicina", año_ingreso=2024),
        Estudiante(rut="11223344-5", nombre="Carlos", apellido="Rojas", carrera="Psicología", año_ingreso=2023),
        Estudiante(rut="55667788-9", nombre="Ana", apellido="Silva", carrera="Derecho", año_ingreso=2024),
        Estudiante(rut="99887766-3", nombre="Luis", apellido="Torres", carrera="Arquitectura", año_ingreso=2023),
        Estudiante(rut="44556677-8", nombre="Carmen", apellido="López", carrera="Ingeniería Civil", año_ingreso=2022),
        Estudiante(rut="33445566-7", nombre="Pedro", apellido="Martín", carrera="Medicina", año_ingreso=2023),
        Estudiante(rut="77889900-1", nombre="Laura", apellido="Díaz", carrera="Psicología", año_ingreso=2024),
    ]
    
    session.add_all(estudiantes)
    session.commit()
    
    # estudiante1 = Estudiante(rut="77889900-1", nombre="Laura", apellido="Díaz", carrera="Psicología", año_ingreso=2024),
    # session.add(estudiante1)
    
    ## consultas   
    
    print("------------ Todos los estudiantes ordenados por apellido ------------")
    query = select(Estudiante).order_by(Estudiante.apellido)
    results = session.execute(query).scalars().all()
    for result in results:
        print(result)


    print("------------ Estudiantes de año 2024 ------------")
    query = select(Estudiante).where(Estudiante.año_ingreso == 2024)
    results = session.execute(query).scalars()
    for result in results:
        print(result)

    print("------------ Buscar por RUT")
    query = select(Estudiante).where(Estudiante.rut == "12345678-9 ------------")
    result = session.execute(query).scalar_one_or_none()
    print(result)


    print("------------ Contar por año ------------")
    query = select(Estudiante.año_ingreso, func.count()).group_by(Estudiante.año_ingreso)
    results = session.execute(query)
    for año, total in results:
        print(año, total)


    print("------------ Estudiantes activos de Ingeniería Civil ------------")
    query = select(Estudiante).where(
        Estudiante.carrera == "Ingeniería Civil",
        Estudiante.activo == True
    )
    results = session.execute(query).scalars()
    for result in results:
        print(result)


    print("------------ Búsqueda por texto 'ar' ------------")
    query = select(Estudiante).where(
        or_(
            Estudiante.nombre.like("%ar%"),
            Estudiante.apellido.like("%ar%")
        )
    )
    results = session.execute(query).scalars()
    for result in results:
        print(result)

    print("------------ Filtros múltiples ------------")
    query = select(Estudiante).where(
        Estudiante.carrera.in_(["Medicina", "Psicología"]),
        Estudiante.año_ingreso.in_([2023, 2024])
    )
    results = session.execute(query).scalars()
    for result in results:
        print(result)


    print("------------ Rango + activos ------------")
    query = select(Estudiante).where(
        Estudiante.año_ingreso.between(2022, 2023),
        Estudiante.activo
    ).order_by(Estudiante.carrera, Estudiante.año_ingreso.desc())

    results = session.execute(query).scalars()
    for result in results:
        print(result)


    
    
    