CREATE DATABASE IF NOT EXISTS usuarios_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_spanish_ci;

USE usuarios_db;

CREATE TABLE IF NOT EXISTS tipos_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL UNIQUE,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    tipo_usuario INT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL,
    CONSTRAINT fk_usuarios_tipos_usuario
        FOREIGN KEY (tipo_usuario)
        REFERENCES tipos_usuario(id)
);
