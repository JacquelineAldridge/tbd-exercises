CREATE DATABASE IF NOT EXISTS library;
USE library;

CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE authors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    nationality VARCHAR(50)
);

CREATE TABLE books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    isbn VARCHAR(13) UNIQUE,
    publication_date DATE,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    category_id INT,
    publisher VARCHAR(100),
    pages INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE book_authors (
    book_id INT,
    author_id INT,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);

CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    country VARCHAR(50),
    registration_date DATE DEFAULT (CURRENT_DATE)
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE DEFAULT (CURRENT_DATE),
    total_amount DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
    shipping_address TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO categories (name, description) VALUES
('Ficción', 'Novelas y cuentos de ficción'),
('No Ficción', 'Libros informativos y educativos'),
('Ciencia Ficción', 'Literatura de ciencia ficción y fantasía'),
('Historia', 'Libros sobre historia y biografías'),
('Tecnología', 'Libros sobre programación y tecnología'),
('Romance', 'Novelas románticas'),
('Misterio', 'Novelas de misterio y suspenso');

INSERT INTO authors (first_name, last_name, birth_date, nationality) VALUES
('Gabriel', 'García Márquez', '1927-03-06', 'Colombiano'),
('Isabel', 'Allende', '1942-08-02', 'Chilena'),
('Mario', 'Vargas Llosa', '1936-03-28', 'Peruano'),
('Jorge Luis', 'Borges', '1899-08-24', 'Argentino'),
('Octavio', 'Paz', '1914-03-31', 'Mexicano'),
('Pablo', 'Neruda', '1904-07-12', 'Chileno'),
('Julio', 'Cortázar', '1914-08-26', 'Argentino'),
('Carlos', 'Fuentes', '1928-11-11', 'Mexicano'),
('Laura', 'Esquivel', '1950-09-30', 'Mexicana'),
('Roberto', 'Bolaño', '1953-04-28', 'Chileno'),
('Frank', 'Herbert', '1920-10-08', 'Estadounidense'),
('Isaac', 'Asimov', '1920-01-02', 'Estadounidense'),
('Stephen', 'Hawking', '1942-01-08', 'Británico'),
('Yuval Noah', 'Harari', '1976-02-24', 'Israelí'),
('Robert C.', 'Martin', '1952-12-05', 'Estadounidense'),
('Eric', 'Matthes', '1972-03-15', 'Estadounidense'),
('Dan', 'Brown', '1964-06-22', 'Estadounidense'),
('Thomas', 'Harris', '1940-04-11', 'Estadounidense');

INSERT INTO books (title, isbn, publication_date, price, stock_quantity, category_id, publisher, pages) VALUES
('Cien años de soledad', '9780307474728', '1967-06-05', 25.99, 15, 1, 'Editorial Sudamericana', 417),
('La casa de los espíritus', '9780553383805', '1982-01-01', 22.50, 12, 1, 'Plaza & Janés', 433),
('La ciudad y los perros', '9788432217647', '1963-01-01', 19.99, 8, 1, 'Seix Barral', 409),
('Ficciones', '9780802130303', '1944-01-01', 18.75, 20, 1, 'Sur', 174),
('El laberinto de la soledad', '9786071113313', '1950-01-01', 16.99, 10, 2, 'Fondo de Cultura Económica', 191),
('Veinte poemas de amor y una canción desesperada', '9788437604947', '1924-01-01', 14.50, 25, 1, 'Cátedra', 128),
('Rayuela', '9788437604534', '1963-07-28', 28.99, 7, 1, 'Sudamericana', 635),
('La muerte de Artemio Cruz', '9786071113320', '1962-01-01', 21.25, 9, 1, 'Fondo de Cultura Económica', 307),
('Como agua para chocolate', '9780385721219', '1989-01-01', 17.99, 18, 6, 'Planeta', 246),
('Los detectives salvajes', '9788433920553', '1998-01-01', 32.50, 5, 1, 'Anagrama', 609),
('Dune', '9780441172719', '1965-08-01', 24.99, 14, 3, 'Chilton Books', 688),
('Fundación', '9780553293357', '1951-05-01', 19.95, 16, 3, 'Gnome Press', 244),
('Breve historia del tiempo', '9780553380163', '1988-04-01', 15.99, 22, 4, 'Bantam Books', 256),
('Sapiens', '9780062316097', '2011-01-01', 21.99, 18, 4, 'Harvill Secker', 443),
('Clean Code', '9780132350884', '2008-08-01', 42.99, 12, 5, 'Prentice Hall', 464),
('Python Crash Course', '9781593279288', '2015-11-01', 35.95, 8, 5, 'No Starch Press', 560),
('El código Da Vinci', '9780307474278', '2003-03-18', 18.99, 20, 7, 'Doubleday', 454),
('El silencio de los corderos', '9780312924584', '1988-06-01', 16.99, 15, NULL, 'St. Martins Press', 352);

INSERT INTO book_authors (book_id, author_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18);

INSERT INTO customers (first_name, last_name, email, phone, address, city, country, registration_date) VALUES
('Ana', 'González', 'ana.gonzalez@email.com', '+34-123-456-789', 'Calle Mayor 123', 'Madrid', 'España', '2023-01-15'),
('Carlos', 'Rodríguez', 'carlos.rodriguez@email.com', '+52-555-123-456', 'Av. Reforma 456', 'Ciudad de México', 'México', '2023-02-20'),
('María', 'López', 'maria.lopez@email.com', '+54-11-123-4567', 'Av. Corrientes 789', 'Buenos Aires', 'Argentina', '2023-03-10'),
('José', 'Martínez', 'jose.martinez@email.com', '+57-1-234-5678', 'Carrera 7 #123-45', 'Bogotá', 'Colombia', '2023-04-05'),
('Carmen', 'Sánchez', 'carmen.sanchez@email.com', '+56-2-345-6789', 'Av. Providencia 234', 'Santiago', 'Chile', '2023-05-12'),
('Roberto', 'Fernández', 'roberto.fernandez@email.com', '+51-1-456-7890', 'Av. Arequipa 567', 'Lima', 'Perú', '2023-06-18'),
('Laura', 'García', 'laura.garcia@email.com', '+34-987-654-321', 'Gran Vía 890', 'Barcelona', 'España', '2023-07-22'),
('Diego', 'Morales', 'diego.morales@email.com', '+52-33-234-5678', 'Av. Chapultepec 345', 'Guadalajara', 'México', '2023-08-14');

INSERT INTO orders (customer_id, order_date, total_amount, status, shipping_address) VALUES
(1, '2024-01-15', 48.49, 'delivered', 'Calle Mayor 123, Madrid, España'),
(2, '2024-01-20', 25.99, 'delivered', 'Av. Reforma 456, Ciudad de México, México'),
(3, '2024-02-05', 67.24, 'shipped', 'Av. Corrientes 789, Buenos Aires, Argentina'),
(4, '2024-02-10', 33.24, 'processing', 'Carrera 7 #123-45, Bogotá, Colombia'),
(1, '2024-02-15', 22.50, 'delivered', 'Calle Mayor 123, Madrid, España'),
(5, '2024-02-20', 89.97, 'shipped', 'Av. Providencia 234, Santiago, Chile'),
(6, '2024-03-01', 19.99, 'delivered', 'Av. Arequipa 567, Lima, Perú'),
(7, '2024-03-05', 44.49, 'pending', 'Gran Vía 890, Barcelona, España'),
(8, '2024-03-10', 17.99, 'processing', 'Av. Chapultepec 345, Guadalajara, México'),
(2, '2024-03-15', 51.24, 'delivered', 'Av. Reforma 456, Ciudad de México, México'),
(3, '2024-03-20', 24.99, 'delivered', 'Av. Corrientes 789, Buenos Aires, Argentina'),
(4, '2024-03-25', 42.99, 'processing', 'Carrera 7 #123-45, Bogotá, Colombia'),
(5, '2024-04-01', 18.99, 'shipped', 'Av. Providencia 234, Santiago, Chile'),
(6, '2024-04-05', 35.95, 'delivered', 'Av. Arequipa 567, Lima, Perú');

INSERT INTO order_items (order_id, book_id, quantity, unit_price) VALUES
(1, 1, 1, 25.99),
(1, 6, 1, 14.50),
(1, 2, 1, 22.50),
(2, 1, 1, 25.99),
(3, 7, 1, 28.99),
(3, 4, 2, 18.75),
(3, 5, 1, 16.99),
(4, 8, 1, 21.25),
(4, 3, 1, 19.99),
(5, 2, 1, 22.50),
(6, 10, 1, 32.50),
(6, 7, 1, 28.99),
(6, 1, 1, 25.99),
(7, 3, 1, 19.99),
(8, 9, 1, 17.99),
(8, 1, 1, 25.99),
(9, 9, 1, 17.99),
(10, 4, 1, 18.75),
(10, 10, 1, 32.50),
(11, 11, 1, 24.99),
(12, 15, 1, 42.99),
(13, 17, 1, 18.99),
(14, 16, 1, 35.95);