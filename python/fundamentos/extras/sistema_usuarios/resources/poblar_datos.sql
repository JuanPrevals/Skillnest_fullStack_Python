USE usuarios_db;

INSERT INTO tipos_usuario (id, nombre)
VALUES
(1, 'ADMIN'),
(2, 'USER')
ON DUPLICATE KEY UPDATE
    nombre = VALUES(nombre),
    deleted_at = NULL;

INSERT INTO usuarios (id, usuario, password, tipo_usuario)
VALUES
(1, 'admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 1),
(2, 'juan', 'f6ccb3e8d609012238c0b39e60b2c9632b3cdede91e035dad1de43469768f4cc', 2),
(3, 'camila', '3c8ac57c21d7bcfc67049d8d4cef7fd609f43b5dbd102d26faac0dd3ee379a5d', 2)
ON DUPLICATE KEY UPDATE
    usuario = VALUES(usuario),
    password = VALUES(password),
    tipo_usuario = VALUES(tipo_usuario),
    deleted_at = NULL;
