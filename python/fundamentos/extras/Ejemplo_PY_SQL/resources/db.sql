CREATE DATABASE colegio;
USE colegio;

CREATE TABLE estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    curso VARCHAR(20) NOT NULL,

    -- Auditoría
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) DEFAULT 'system',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT DEFAULT 0
);

CREATE TABLE asignaturas (

    id_asignatura INT AUTO_INCREMENT PRIMARY KEY,
    nombre_asignatura VARCHAR(100) NOT NULL,

    -- Auditoría
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) DEFAULT 'system',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT DEFAULT 0

);
CREATE TABLE calificaciones (

    id_calificacion INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_asignatura INT NOT NULL,
    nota DECIMAL(3,1) NOT NULL,
    fecha_evaluacion DATE,

    -- Auditoría
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) DEFAULT 'system',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT DEFAULT 0,
    FOREIGN KEY (id_estudiante)
        REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (id_asignatura)
        REFERENCES asignaturas(id_asignatura)

);

INSERT INTO estudiantes
(
    nombre,
    curso,
    created_by
)
VALUES

('Martín González','3A','admin'),
('Sofía Rojas','3A','admin'),
('Benjamín Muñoz','3A','admin'),
('Valentina Pérez','3B','admin'),
('Tomás Herrera','3B','admin'),
('Isidora Castillo','3B','admin'),
('Vicente Rodriguez','4A','admin'),
('Emilia Contreras','4A','admin'),
('Joaquín Díaz','4A','admin'),
('Florencia Vargas','4B','admin'),
('Matías Fuentes','4B','admin'),
('Antonia Silva','4B','admin'),
('Lucas Torres','2A','admin'),
('Amanda Morales','2A','admin'),
('Diego Navarro','2B','admin');

UPDATE estudiantes
SET deleted = 1
WHERE id_estudiante IN (5, 12);

INSERT INTO asignaturas
(
    nombre_asignatura,
    created_by
)
VALUES

('Matemática','admin'),
('Lenguaje','admin'),
('Historia','admin'),
('Inglés','admin'),
('Ciencias','admin'),
('Programación','admin'),
('Base de Datos','admin'),
('Educación Física','admin');

UPDATE asignaturas
SET deleted = 1
WHERE id_asignatura = 8;


INSERT INTO calificaciones
(
    id_estudiante,
    id_asignatura,
    nota,
    fecha_evaluacion,
    created_by
)
VALUES

(1,1,6.3,'2026-03-10','profesor'),
(1,2,5.8,'2026-03-12','profesor'),
(1,6,6.7,'2026-03-20','profesor'),

(2,1,5.5,'2026-03-10','profesor'),
(2,2,6.4,'2026-03-12','profesor'),
(2,7,6.8,'2026-03-25','profesor'),

(3,1,4.9,'2026-03-10','profesor'),
(3,3,5.6,'2026-03-15','profesor'),
(3,6,6.1,'2026-03-22','profesor'),

(4,1,6.8,'2026-03-10','profesor'),
(4,4,6.2,'2026-03-18','profesor'),
(4,7,6.5,'2026-03-25','profesor'),

(5,1,3.9,'2026-03-10','profesor'),
(5,2,4.5,'2026-03-12','profesor'),

(6,1,5.7,'2026-03-10','profesor'),
(6,5,6.0,'2026-03-19','profesor'),

(7,1,6.9,'2026-03-10','profesor'),
(7,6,7.0,'2026-03-22','profesor'),
(7,7,6.8,'2026-03-25','profesor'),

(8,2,5.8,'2026-03-12','profesor'),
(8,4,6.3,'2026-03-18','profesor'),

(9,1,5.4,'2026-03-10','profesor'),
(9,7,6.0,'2026-03-25','profesor'),

(10,2,6.2,'2026-03-12','profesor'),
(10,3,5.8,'2026-03-15','profesor'),

(11,6,6.5,'2026-03-22','profesor'),
(11,7,6.4,'2026-03-25','profesor'),

(12,1,4.8,'2026-03-10','profesor'),
(12,2,5.1,'2026-03-12','profesor'),

(13,1,5.9,'2026-03-10','profesor'),
(13,5,6.1,'2026-03-19','profesor'),

(14,2,6.4,'2026-03-12','profesor'),
(14,4,6.0,'2026-03-18','profesor'),

(15,1,5.0,'2026-03-10','profesor'),
(15,3,5.3,'2026-03-15','profesor');


UPDATE calificaciones
SET deleted = 1
WHERE id_calificacion IN (5, 18, 29);


SELECT
    e.nombre,
    a.nombre_asignatura,
    c.nota
FROM calificaciones c
INNER JOIN estudiantes e
    ON c.id_estudiante = e.id_estudiante
INNER JOIN asignaturas a
    ON c.id_asignatura = a.id_asignatura
WHERE
    e.deleted = 0
    AND a.deleted = 0
    AND c.deleted = 0;
