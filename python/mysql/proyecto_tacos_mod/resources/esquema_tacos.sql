CREATE SCHEMA IF NOT EXISTS `esquema_tacos`
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE `esquema_tacos`;

CREATE TABLE IF NOT EXISTS `tacos` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `tortilla` VARCHAR(45) NOT NULL,
    `guiso` VARCHAR(45) NOT NULL,
    `salsa` VARCHAR(45) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `complementos` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre_complemento` VARCHAR(45) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uq_complementos_nombre` (`nombre_complemento`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `complementos_en_tacos` (
    `complemento_id` INT UNSIGNED NOT NULL,
    `taco_id` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`complemento_id`, `taco_id`),
    KEY `idx_complementos_en_tacos_taco` (`taco_id`),
    CONSTRAINT `fk_complementos_en_tacos_complemento`
        FOREIGN KEY (`complemento_id`) REFERENCES `complementos` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_complementos_en_tacos_taco`
        FOREIGN KEY (`taco_id`) REFERENCES `tacos` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

