CREATE DATABASE IF NOT EXISTS esquema_estudiantes_cursos
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE esquema_estudiantes_cursos;

CREATE TABLE IF NOT EXISTS cursos (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_cursos_nombre (nombre)
);

CREATE TABLE IF NOT EXISTS estudiantes (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    edad TINYINT UNSIGNED NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    curso_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    KEY idx_estudiantes_curso_id (curso_id),
    CONSTRAINT fk_estudiantes_curso
        FOREIGN KEY (curso_id) REFERENCES cursos(id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

INSERT IGNORE INTO cursos (nombre) VALUES
    ('MERN'),
    ('Java'),
    ('Python'),
    ('Fundamentos de la Web');

INSERT INTO estudiantes (nombre, apellido, edad, curso_id)
SELECT 'Valeria', 'Romero', 25, id FROM cursos
WHERE nombre = 'MERN'
  AND NOT EXISTS (
      SELECT 1 FROM estudiantes
      WHERE nombre = 'Valeria' AND apellido = 'Romero'
  );

INSERT INTO estudiantes (nombre, apellido, edad, curso_id)
SELECT 'Cynthia', 'Castillo', 26, id FROM cursos
WHERE nombre = 'MERN'
  AND NOT EXISTS (
      SELECT 1 FROM estudiantes
      WHERE nombre = 'Cynthia' AND apellido = 'Castillo'
  );

INSERT INTO estudiantes (nombre, apellido, edad, curso_id)
SELECT 'Patricio', 'Fuentelba', 27, id FROM cursos
WHERE nombre = 'MERN'
  AND NOT EXISTS (
      SELECT 1 FROM estudiantes
      WHERE nombre = 'Patricio' AND apellido = 'Fuentelba'
  );

INSERT INTO estudiantes (nombre, apellido, edad, curso_id)
SELECT 'Kevin', 'Duque', 27, id FROM cursos
WHERE nombre = 'MERN'
  AND NOT EXISTS (
      SELECT 1 FROM estudiantes
      WHERE nombre = 'Kevin' AND apellido = 'Duque'
  );
