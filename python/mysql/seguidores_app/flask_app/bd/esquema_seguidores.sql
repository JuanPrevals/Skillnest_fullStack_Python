CREATE DATABASE IF NOT EXISTS `esquema_seguidores`
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE `esquema_seguidores`;

CREATE TABLE IF NOT EXISTS `usuarios` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `email` VARCHAR(45) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uq_usuarios_email` (`email`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `seguidores` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `usuario_id` INT UNSIGNED NOT NULL,
    `seguidor_id` INT UNSIGNED NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uq_usuario_seguidor` (`usuario_id`, `seguidor_id`),
    KEY `idx_seguidores_seguidor` (`seguidor_id`),
    CONSTRAINT `chk_seguidores_distintos` CHECK (`usuario_id` <> `seguidor_id`),
    CONSTRAINT `fk_seguidores_usuario`
        FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_seguidores_seguidor`
        FOREIGN KEY (`seguidor_id`) REFERENCES `usuarios` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

INSERT IGNORE INTO `usuarios` (`nombre`, `apellido`, `email`) VALUES
    ('Soraya', 'Montenegro', 'soraya@email.com'),
    ('Luis F.', 'de la Vega', 'luis@email.com'),
    ('Beatriz', 'Pinzón', 'beatriz@email.com'),
    ('Armando', 'Mendoza', 'armando@email.com'),
    ('Mía', 'Colucci', 'mia@email.com'),
    ('Roberto', 'Pardo', 'roberto@email.com');

INSERT IGNORE INTO `seguidores` (`usuario_id`, `seguidor_id`)
SELECT seguido.id, seguidor.id
FROM usuarios AS seguido
CROSS JOIN usuarios AS seguidor
WHERE seguido.email = 'soraya@email.com' AND seguidor.email = 'luis@email.com';

INSERT IGNORE INTO `seguidores` (`usuario_id`, `seguidor_id`)
SELECT seguido.id, seguidor.id
FROM usuarios AS seguido
CROSS JOIN usuarios AS seguidor
WHERE seguido.email = 'soraya@email.com' AND seguidor.email = 'armando@email.com';

INSERT IGNORE INTO `seguidores` (`usuario_id`, `seguidor_id`)
SELECT seguido.id, seguidor.id
FROM usuarios AS seguido
CROSS JOIN usuarios AS seguidor
WHERE seguido.email = 'beatriz@email.com' AND seguidor.email = 'luis@email.com';

INSERT IGNORE INTO `seguidores` (`usuario_id`, `seguidor_id`)
SELECT seguido.id, seguidor.id
FROM usuarios AS seguido
CROSS JOIN usuarios AS seguidor
WHERE seguido.email = 'mia@email.com' AND seguidor.email = 'luis@email.com';

INSERT IGNORE INTO `seguidores` (`usuario_id`, `seguidor_id`)
SELECT seguido.id, seguidor.id
FROM usuarios AS seguido
CROSS JOIN usuarios AS seguidor
WHERE seguido.email = 'luis@email.com' AND seguidor.email = 'beatriz@email.com';
