# Tarea Práctica: Sistema de Librería con SQLAlchemy

## Descripción

Implementar un sistema de librería online usando SQLAlchemy.

## Objetivos

- Crear modelos con relaciones usando SQLAlchemy
- Agregar y modificar datos usando ORM
- Realizar consultas usando SQLAlchemy

## Parte 1: Modelos y Relaciones

### Modelos Requeridos

**Category**
- `id, name, description`
- Relación: Uno a muchos con Book

**Author**
- `id, first_name, last_name, birth_date, nationality`
- Relación: Muchos a muchos con Book

**Book**
- `id, title, isbn, publication_date, price, stock_quantity, category_id`
- Relaciones: Muchos a uno con Category, muchos a muchos con Author

**Order**
- `id, book_id, quantity, order_date, customer_name`
- Relación: Muchos a uno con Book

## Parte 2: Agregar Datos

Crear función que genere al menos:
- 3 categorías (Ficción, Ciencia, Historia)
- 5 autores
- 10 libros distribuidos entre categorías
- 8 pedidos con nombres de clientes

## Parte 3: Modificar Datos

### Operaciones de Actualización

Crear funciones que permitan:
- Actualizar stock de libros
- Cambiar precio de libros
- Aplicar descuentos por categoría

## Parte 4: Consultas

Crea funciones que consulten la base de datos usando SQLAlchemy, y que impriman los resultados de forma básica.

Consultas:

1. Obtener todos los libros
2. Libros más caros que $X
3. Autores ordenados alfabéticamente
4. Buscar libros por título (que contenga palabra)
5. Libros con nombre de categoría
6. Libros con autores (mostrar nombres)
7. Pedidos con información del libro