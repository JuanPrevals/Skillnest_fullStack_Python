-- Instalación inicial. No elimina ni modifica tablas existentes.
CREATE DATABASE IF NOT EXISTS esquema_usuarios CHARACTER SET utf8mb4;
USE esquema_usuarios;
CREATE TABLE IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);
-- Si ya existía la tabla, verificar especialmente AUTO_INCREMENT en id.
DESCRIBE usuarios;
