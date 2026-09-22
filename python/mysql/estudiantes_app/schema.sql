CREATE DATABASE IF NOT EXISTS esquema_estudiantes CHARACTER SET utf8mb4;
USE esquema_estudiantes;

CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO estudiantes (nombre, email)
SELECT datos.nombre, datos.email
FROM (
    SELECT 'Joe Doe' AS nombre, 'joedoe@email.com' AS email
    UNION ALL SELECT 'Ana Pérez', 'ana@email.com'
    UNION ALL SELECT 'Carlos Soto', 'carlos@email.com'
    UNION ALL SELECT 'María González', 'maria@email.com'
) AS datos
WHERE NOT EXISTS (SELECT 1 FROM estudiantes LIMIT 1);
