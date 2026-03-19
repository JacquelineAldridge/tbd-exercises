USE library;

-- 1. Obtener todos los libros con su título, precio y cantidad en stock.
SELECT title, price, stock_quantity FROM books;


-- 2. Mostrar todos los libros que cuesten más de $20.
SELECT title, price FROM books WHERE price > 20.00;


-- 3. Listar todos los autores ordenados alfabéticamente por apellido.
SELECT first_name, last_name FROM authors ORDER BY last_name;


-- 4. Encontrar todos los libros cuyo título contenga la palabra "amor".
SELECT title, price FROM books WHERE title LIKE '%amor%';


-- 5. Mostrar todos los libros de las categorías "Ficción" y "Romance".
SELECT b.title, c.name as category 
FROM books b 
JOIN categories c ON b.category_id = c.id 
WHERE c.name IN ('Ficción', 'Romance');


-- 6. Mostrar todos los libros con el nombre de su categoría.
SELECT b.title, c.name as category 
FROM books b 
JOIN categories c ON b.category_id = c.id;


-- 7. Listar todos los libros con su categoría y autor. Mostrar: título del libro, categoría, nombre completo del autor.
SELECT b.title, c.name as category, CONCAT(a.first_name, ' ', a.last_name) as author
FROM books b
JOIN categories c ON b.category_id = c.id
JOIN book_authors ba ON b.id = ba.book_id
JOIN authors a ON ba.author_id = a.id;


-- 8. Mostrar todas las categorías y la cantidad de libros que tienen (incluyendo categorías sin libros).
SELECT c.name, COUNT(b.id) as book_count
FROM categories c
LEFT JOIN books b ON c.id = b.category_id
GROUP BY c.id, c.name;


-- 9. Obtener todos los pedidos del cliente "Ana González" con los detalles de los libros comprados.
SELECT o.id as order_id, o.order_date, b.title, oi.quantity, oi.unit_price
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN books b ON oi.book_id = b.id
WHERE c.first_name = 'Ana' AND c.last_name = 'González';


-- 10. Mostrar el historial completo de pedidos incluyendo: nombre del cliente, fecha del pedido, título del libro, cantidad y precio unitario.
SELECT CONCAT(c.first_name, ' ', c.last_name) as customer, o.order_date, b.title, oi.quantity, oi.unit_price
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN books b ON oi.book_id = b.id
ORDER BY o.order_date, c.last_name;


-- 11. Mostrar los autores que han escrito libros en más de una categoría.
SELECT CONCAT(a.first_name, ' ', a.last_name) as author, COUNT(DISTINCT c.id) as different_categories
FROM authors a
JOIN book_authors ba ON a.id = ba.author_id
JOIN books b ON ba.book_id = b.id
JOIN categories c ON b.category_id = c.id
GROUP BY a.id, a.first_name, a.last_name
HAVING COUNT(DISTINCT c.id) > 1;


-- 12. Calcular el valor total del inventario (precio × stock) por categoría.
SELECT c.name as category, SUM(b.price * b.stock_quantity) as inventory_value
FROM categories c
JOIN books b ON c.id = b.category_id
GROUP BY c.id, c.name;


-- 13. Obtener el precio promedio de los libros por categoría.
SELECT c.name as category, AVG(b.price) as avg_price
FROM categories c
JOIN books b ON c.id = b.category_id
GROUP BY c.id, c.name;


-- 14. Encontrar el libro más caro y el más barato de cada categoría.
SELECT c.name as category, 
       MIN(b.price) as min_price, 
       MAX(b.price) as max_price
FROM categories c
JOIN books b ON c.id = b.category_id
GROUP BY c.id, c.name;


-- 15. Mostrar las categorías que tienen más de 2 libros.
SELECT c.name as category, COUNT(b.id) as book_count
FROM categories c
JOIN books b ON c.id = b.category_id
GROUP BY c.id, c.name
HAVING COUNT(b.id) > 2;


-- 16. Encontrar todos los libros que son más caros que el precio promedio.
SELECT title, price
FROM books 
WHERE price > (SELECT AVG(price) FROM books);


-- 17. Mostrar todos los autores que tienen al menos un libro publicado.
SELECT DISTINCT a.first_name, a.last_name
FROM authors a
JOIN book_authors ba ON a.id = ba.author_id;


-- 18. Obtener los clientes que han realizado pedidos por un valor superior a $50.
SELECT DISTINCT c.first_name, c.last_name
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.total_amount > 50;


-- 19. Para cada categoría, mostrar el libro más caro de esa categoría.
SELECT c.name as category, b.title, b.price
FROM books b
JOIN categories c ON b.category_id = c.id
WHERE b.price = (
    SELECT MAX(price) 
    FROM books b2 
    WHERE b2.category_id = c.id
);


-- 20. Crear una consulta que muestre el ranking de clientes por total gastado.
SELECT c.first_name, c.last_name, SUM(o.total_amount) as total_spent
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.first_name, c.last_name
ORDER BY total_spent DESC;


-- 21. Clasificar los libros según su precio: "Económico" (<$20), "Medio" ($20-$30), "Caro" (>$30).
SELECT title, price,
       CASE 
              WHEN price < 20 THEN 'Cheap'
              WHEN price BETWEEN 20 AND 30 THEN 'Medium'
              ELSE 'Expensive'
       END as price_classification
FROM books;


-- 22. Mostrar el ranking de libros más vendidos (por cantidad total vendida).
SELECT b.title, SUM(oi.quantity) as total_sold
FROM books b
JOIN order_items oi ON b.id = oi.book_id
GROUP BY b.id, b.title
ORDER BY total_sold DESC;


-- 23. Calcular las ventas totales por autor.
SELECT CONCAT(a.first_name, ' ', a.last_name) as author, 
       SUM(oi.quantity * oi.unit_price) as total_sales
FROM authors a
JOIN book_authors ba ON a.id = ba.author_id
JOIN books b ON ba.book_id = b.id
JOIN order_items oi ON b.id = oi.book_id
GROUP BY a.id, a.first_name, a.last_name
ORDER BY total_sales DESC;


-- 24. Mostrar las ventas mensuales del año 2024.
SELECT YEAR(o.order_date) as year, 
       MONTH(o.order_date) as month,
       SUM(o.total_amount) as monthly_sales
FROM orders o
WHERE YEAR(o.order_date) = 2024
GROUP BY YEAR(o.order_date), MONTH(o.order_date)
ORDER BY month;


-- 25. Agregar un nuevo libro con su autor correspondiente.
INSERT INTO books (title, isbn, publication_date, price, stock_quantity, category_id, publisher, pages) 
VALUES ('Nuevo Libro Test', '9999999999999', '2024-01-01', 29.99, 10, 1, 'Editorial Test', 300);

INSERT INTO book_authors (book_id, author_id) 
VALUES (LAST_INSERT_ID(), 1);


-- 26. Actualizar el precio de todos los libros de la categoría "Tecnología" aumentándolo en un 10%.
UPDATE books 
SET price = price * 1.10 
WHERE category_id = (SELECT id FROM categories WHERE name = 'Tecnología');


-- 27. Mostrar los 5 libros más vendidos con cantidad total y ingresos generados.
SELECT b.title, 
       SUM(oi.quantity) as total_sold,
       SUM(oi.quantity * oi.unit_price) as total_income
FROM books b
JOIN order_items oi ON b.id = oi.book_id
GROUP BY b.id, b.title
ORDER BY total_sold DESC
LIMIT 5;


-- 28. Mostrar los libros que nunca han sido vendidos.
SELECT b.title, b.price, b.stock_quantity
FROM books b
LEFT JOIN order_items oi ON b.id = oi.book_id
WHERE oi.book_id IS NULL;


-- 29. Mostrar los libros con stock bajo (menos de 10 unidades).
SELECT title, stock_quantity
FROM books 
WHERE stock_quantity < 10;


-- 30. Mostrar los autores cuyos libros han generado más ingresos.
SELECT CONCAT(a.first_name, ' ', a.last_name) as author,
       SUM(oi.quantity * oi.unit_price) as total_income
FROM authors a
JOIN book_authors ba ON a.id = ba.author_id
JOIN books b ON ba.book_id = b.id
JOIN order_items oi ON b.id = oi.book_id
GROUP BY a.id, a.first_name, a.last_name
ORDER BY total_income DESC;
