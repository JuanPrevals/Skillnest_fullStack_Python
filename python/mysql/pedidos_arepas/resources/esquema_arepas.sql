-- Forward Engineering del ERD de pedidos de arepas.
CREATE SCHEMA IF NOT EXISTS `esquema_arepas`
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE `esquema_arepas`;

CREATE TABLE IF NOT EXISTS `pedidos` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(100) NOT NULL,
    `cantidad` INT UNSIGNED NOT NULL,
    `relleno` VARCHAR(100) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    CONSTRAINT `chk_pedidos_cantidad_positiva` CHECK (`cantidad` > 0)
) ENGINE=InnoDB;

INSERT INTO `pedidos` (`nombre`, `cantidad`, `relleno`) VALUES
    ('Valeria', 3, 'pollo'),
    ('Cynthia', 2, 'carne'),
    ('Patricio', 5, 'queso'),
    ('Kevin', 3, 'jamón y queso');
