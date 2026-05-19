CREATE DATABASE administrador_datos;

USE administrador_datos;

-- Tipos de usuario: administrador o usuario normal
CREATE TABLE tipos_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Usuarios registrados en la plataforma
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_usuario_id INT,
    nombre VARCHAR(100),
    email VARCHAR(255),
    contrasena VARCHAR(255),
    creado_en DATETIME,
    actualizado_en DATETIME,
    -- Cada usuario pertenece a un tipo de usuario
    FOREIGN KEY (tipo_usuario_id) REFERENCES tipos_usuarios(id)
);

-- Mensajes enviados entre usuarios
CREATE TABLE mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_envia_id INT,
    usuario_recibe_id INT,
    mensaje TEXT,
    creado_en DATETIME,
    actualizado_en DATETIME,
    -- Usuario que envia el mensaje
    FOREIGN KEY (usuario_envia_id) REFERENCES usuarios(id),
    -- Usuario que recibe el mensaje
    FOREIGN KEY (usuario_recibe_id) REFERENCES usuarios(id)
);

-- Comentarios hechos sobre un mensaje
CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mensaje_id INT,
    usuario_id INT,
    comentario TEXT,
    creado_en DATETIME,
    actualizado_en DATETIME,
    -- Mensaje al que pertenece el comentario
    FOREIGN KEY (mensaje_id) REFERENCES mensajes(id),
    -- Usuario que escribe el comentario
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
