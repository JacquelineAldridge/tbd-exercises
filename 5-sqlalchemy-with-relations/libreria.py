
from sqlalchemy import Date, Float, ForeignKey, Integer, create_engine, String, update
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from datetime import date


def actualizar_stock(session, isbn: str, nuevo_stock:int):
    libro = session.query(Book).filter_by(isbn=isbn).first()
    
    if libro:
        libro.stock_quantity = nuevo_stock
        session.commit()
    else:
        print("No existe el libro")
    
def cambiar_precio(session, isbn:str, nuevo_precio:int):
    results = session.execute(
        update(Book)
        .where(Book.isbn == isbn)
        .values(price= nuevo_precio)
    )
    if results.rowcount == 0:
        print("Libro no encontrado")
    
    session.commit()
    
def aplicar_descuento(session, nombre_categoria: str, porcentaje:float):
    stmt = (update(Book)
            .where(Book.category.has(Category.name == nombre_categoria))
            .values(price = Book.price * (1-porcentaje))
            )
    session.execute(stmt)
    session.commit()
    
class Base(DeclarativeBase):
    pass

# recuerden crear la base de datos antes con createdb
engine = create_engine("postgresql+psycopg:///libreria_db", echo=False)


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(200))
    
    books: Mapped[list["Book"]] = relationship(back_populates="category")

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    isbn: Mapped[str] = mapped_column(String(20))
    publication_date: Mapped[date] = mapped_column(Date)
    price: Mapped[float] = mapped_column(Float)
    stock_quantity: Mapped[int] = mapped_column(Integer)
    
    # Muchos a uno con categoría
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="books")
    
    authors: Mapped[list["Author"]] = relationship(back_populates="books", secondary="books_authors")

    orders: Mapped[list["Order"]] = relationship(back_populates="book")
    
class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    birth_date: Mapped[date] = mapped_column(Date)
    nationality: Mapped[str] = mapped_column(String(50))
    
    books: Mapped[list["Book"]] = relationship(back_populates="authors", secondary="books_authors")
    
class BookAuthor(Base):
    __tablename__ = "books_authors"
    
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), primary_key=True)

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer)
    order_date: Mapped[date] = mapped_column(Date)
    customer_name: Mapped[str] = mapped_column(String(100))
    
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    book: Mapped[list["Book"]] = relationship(back_populates="orders")
    
Session = sessionmaker(engine)

with Session() as session:
    ficcion = Category(name = "Ficción", description="Libros de ficción")
    ciencia = Category(name = "Ciencia", description="Libros de ciencia")
    historia = Category(name = "Historia", description="Libros de Historia")
    
    session.add_all([ficcion, ciencia, historia])
    
    a1 = Author(first_name = "Gabriel", last_name="García Márquez", birth_date=date(1927,3,6), nationality="Colombiano")
    a2 = Author(first_name="Isaac", last_name="Newton", birth_date=date(1643,1,4), nationality="Inglés")
    a3 = Author(first_name="Yuval", last_name="Harari", birth_date=date(1976,2,24), nationality="Israelí")
    a4 = Author(first_name="J.K.", last_name="Rowling", birth_date=date(1965,7,31), nationality="Británica")
    a5 = Author(first_name="Stephen", last_name="Hawking", birth_date=date(1942,1,8), nationality="Británico")    
    
    session.add_all([a1,a2,a3,a4,a5])
    
    libros = [
            Book(title="Cien años de soledad", isbn="111", publication_date=date(1967,5,30), price=20, stock_quantity=10, category=ficcion,authors=[a1]),
            Book(title="Harry Potter", isbn="222", publication_date=date(1997,6,26), price=25, stock_quantity=15, category=ficcion,authors=[a4]),
            Book(title="Breve historia del tiempo", isbn="333", publication_date=date(1988,4,1), price=30, stock_quantity=8, category=ciencia,authors=[a5]),
            Book(title="Sapiens", isbn="444", publication_date=date(2011,1,1), price=28, stock_quantity=12, category=historia, authors=[a3]),
        ]
    session.add_all(libros)
    ordenes = [  
    Order(quantity=2, order_date=date(2024, 5, 1), customer_name="Juan Pérez", book=libros[0]),  
    Order(quantity=1, order_date=date(2024, 5, 2), customer_name="María López", book=libros[1]),  
    Order(quantity=3, order_date=date(2024, 5, 3), customer_name="Carlos Díaz", book=libros[2]),  
    Order(quantity=1, order_date=date(2024, 5, 4), customer_name="Ana Torres", book=libros[3]),  
    Order(quantity=4, order_date=date(2024, 5, 5), customer_name="Pedro Rojas", book=libros[0]),  
    ]  
    session.add_all(ordenes)
    
    session.commit()
    
    print(session.query(Book).filter_by(isbn = "111").first().stock_quantity)
    actualizar_stock(session, "111", 35)
    print(session.query(Book).filter_by(isbn = "111").first().stock_quantity)
    cambiar_precio(session,"111",50)
    aplicar_descuento(session,"Ciencia", 0.2)
    
    print("1. Obtener todos los libros")
    libros = session.query(Book).all()
    for libro in libros:
        print(f"{libro.title} - ${libro.price}")

    print("Libros más caros que $X")
    libros = session.query(Book).filter(Book.price > 25).all()
    for libro in libros:
        print(f"{libro.title} - ${libro.price}")

    print("Autores ordenados alfabéticamente")
    autores = session.query(Author).order_by(Author.last_name).all()
    for autor in autores:
        print(f"{autor.first_name} {autor.last_name}")

    print("Buscar libros por título")
    libros = session.query(Book).filter(Book.title.ilike("%Harry%")).all()
    for libro in libros:
        print(libro.title)

    print("Libros con nombre de categoría")
    libros = session.query(Book).all()
    for libro in libros:
        print(f"{libro.title} - {libro.category.name}")

    print("Libros con autores")
    libros = session.query(Book).all()
    for libro in libros:
        for autor in libro.authors:
            print(f"{libro.title} - {autor.first_name} {autor.last_name}")

    print("Pedidos con información del libro")
    pedidos = session.query(Order).all()
    for pedido in pedidos:
        print(f"Pedido {pedido.id} - {pedido.customer_name} - {pedido.book.title} - Cantidad: {pedido.quantity}")