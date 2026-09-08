CREATE DATABASE IF NOT EXISTS mascotas_db
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE mascotas_db;

CREATE TABLE IF NOT EXISTS mascotas (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    color VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Datos de prueba: no repetir mascotas que ya tengan estos mismos datos.
INSERT INTO mascotas (nombre, tipo, color)
SELECT ejemplo.nombre, ejemplo.tipo, ejemplo.color
FROM (
    SELECT 'Firulais' AS nombre, 'Perro' AS tipo, 'Café' AS color
    UNION ALL SELECT 'Michi', 'Gato', 'Negro'
    UNION ALL SELECT 'Luna', 'Perro', 'Blanco'
    UNION ALL SELECT 'Nala', 'Gato', 'Naranjo'
    UNION ALL SELECT 'Coco', 'Conejo', 'Blanco'
) AS ejemplo
WHERE NOT EXISTS (
    SELECT 1 FROM mascotas
    WHERE mascotas.nombre = ejemplo.nombre
      AND mascotas.tipo = ejemplo.tipo
      AND mascotas.color = ejemplo.color
);
