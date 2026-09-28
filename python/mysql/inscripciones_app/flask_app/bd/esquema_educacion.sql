CREATE DATABASE IF NOT EXISTS `esquema_educacion`
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE `esquema_educacion`;

CREATE TABLE IF NOT EXISTS `estudiantes` (
    `id_estudiante` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(100) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id_estudiante`),
    UNIQUE KEY `uq_estudiantes_email` (`email`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `cursos` (
    `id_curso` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre_curso` VARCHAR(100) NOT NULL,
    `descripcion` TEXT,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id_curso`),
    UNIQUE KEY `uq_cursos_nombre` (`nombre_curso`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `inscripciones` (
    `estudiante_id` INT UNSIGNED NOT NULL,
    `curso_id` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`estudiante_id`, `curso_id`),
    KEY `idx_inscripciones_curso` (`curso_id`),
    CONSTRAINT `fk_inscripcion_estudiante`
        FOREIGN KEY (`estudiante_id`) REFERENCES `estudiantes` (`id_estudiante`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_inscripcion_curso`
        FOREIGN KEY (`curso_id`) REFERENCES `cursos` (`id_curso`)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

INSERT IGNORE INTO `estudiantes` (`nombre`, `email`) VALUES
    ('Juan Pérez', 'juan@email.com'),
    ('Ana González', 'ana@email.com'),
    ('Carlos Soto', 'carlos@email.com'),
    ('María López', 'maria@email.com');

INSERT IGNORE INTO `cursos` (`nombre_curso`, `descripcion`) VALUES
    ('MERN', 'Desarrollo web con MongoDB, Express, React y Node.js'),
    ('Python', 'Programación y desarrollo web con Python'),
    ('Java', 'Desarrollo de aplicaciones utilizando Java'),
    ('Fundamentos de la Web', 'HTML, CSS y conceptos fundamentales de desarrollo web');
