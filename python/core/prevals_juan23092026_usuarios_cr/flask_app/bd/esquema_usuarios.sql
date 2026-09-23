-- Ejecutar una vez para crear la base de datos, la tabla y datos de demostración.
CREATE DATABASE IF NOT EXISTS esquema_usuarios
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE esquema_usuarios;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO usuarios (nombre, apellido, email) VALUES
    ('Ricky', 'Martin', 'ricky@codingdojo.com'),
    ('Enrique', 'Iglesias', 'enrique@codingdojo.com'),
    ('Celia', 'Cruz', 'celia@codingdojo.com'),
    ('Ricardo', 'Montaner', 'ricardo@codingdojo.com');
