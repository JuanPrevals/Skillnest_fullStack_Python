-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema tienda_videojuegos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tienda_videojuegos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tienda_videojuegos` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci ;
USE `tienda_videojuegos` ;

-- -----------------------------------------------------
-- Table `tienda_videojuegos`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_videojuegos`.`usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre_usuario` VARCHAR(80) NOT NULL,
  `correo` VARCHAR(120) NOT NULL,
  `password_hash` VARCHAR(64) NULL DEFAULT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` INT NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `deleted_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE INDEX `correo` (`correo` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_spanish_ci;

INSERT INTO `tienda_videojuegos`.`usuario`
(`id_usuario`, `nombre_usuario`, `correo`, `password_hash`)
VALUES
(1, 'admin', 'admin@tienda.cl', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9')
ON DUPLICATE KEY UPDATE
  password_hash = VALUES(password_hash),
  deleted_at = NULL;


-- -----------------------------------------------------
-- Table `tienda_videojuegos`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_videojuegos`.`cliente` (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `rut` VARCHAR(12) NOT NULL,
  `nombre` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(20) NULL DEFAULT NULL,
  `correo` VARCHAR(120) NULL DEFAULT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` INT NOT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `deleted_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE INDEX `rut` (`rut` ASC) VISIBLE,
  INDEX `created_by` (`created_by` ASC) VISIBLE,
  CONSTRAINT `cliente_ibfk_1`
    FOREIGN KEY (`created_by`)
    REFERENCES `tienda_videojuegos`.`usuario` (`id_usuario`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_spanish_ci;

INSERT INTO `tienda_videojuegos`.`cliente`
(`id_cliente`, `rut`, `nombre`, `telefono`, `correo`, `created_by`)
VALUES
(1, '11111111-1', 'Carlos Perez', '+56911111111', 'carlos.perez@mail.com', 1),
(2, '22222222-2', 'Ana Torres', '+56922222222', 'ana.torres@mail.com', 1),
(3, '33333333-3', 'Luis Ramirez', '+56933333333', 'luis.ramirez@mail.com', 1)
ON DUPLICATE KEY UPDATE
  nombre = VALUES(nombre),
  telefono = VALUES(telefono),
  correo = VALUES(correo),
  deleted_at = NULL;


-- -----------------------------------------------------
-- Table `tienda_videojuegos`.`plataforma`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_videojuegos`.`plataforma` (
  `id_plataforma` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` INT NOT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `deleted_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id_plataforma`),
  UNIQUE INDEX `nombre` (`nombre` ASC) VISIBLE,
  INDEX `created_by` (`created_by` ASC) VISIBLE,
  CONSTRAINT `plataforma_ibfk_1`
    FOREIGN KEY (`created_by`)
    REFERENCES `tienda_videojuegos`.`usuario` (`id_usuario`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_spanish_ci;

INSERT INTO `tienda_videojuegos`.`plataforma`
(`id_plataforma`, `nombre`, `created_by`)
VALUES
(1, 'PS5', 1),
(2, 'Xbox Series X', 1),
(3, 'PC', 1),
(4, 'Nintendo Switch', 1)
ON DUPLICATE KEY UPDATE
  nombre = VALUES(nombre),
  deleted_at = NULL;


-- -----------------------------------------------------
-- Table `tienda_videojuegos`.`genero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_videojuegos`.`genero` (
  `id_genero` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(60) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` INT NOT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `deleted_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id_genero`),
  UNIQUE INDEX `nombre` (`nombre` ASC) VISIBLE,
  INDEX `created_by` (`created_by` ASC) VISIBLE,
  CONSTRAINT `genero_ibfk_1`
    FOREIGN KEY (`created_by`)
    REFERENCES `tienda_videojuegos`.`usuario` (`id_usuario`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_spanish_ci;

INSERT INTO `tienda_videojuegos`.`genero`
(`id_genero`, `nombre`, `created_by`)
VALUES
(1, 'Accion', 1),
(2, 'Aventura', 1),
(3, 'Deportes', 1),
(4, 'Carreras', 1)
ON DUPLICATE KEY UPDATE
  nombre = VALUES(nombre),
  deleted_at = NULL;


-- -----------------------------------------------------
-- Table `tienda_videojuegos`.`formato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_videojuegos`.`formato` (
  `id_formato` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(30) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` INT NOT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `deleted_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id_formato`),
  UNIQUE INDEX `nombre` (`nombre` ASC) VISIBLE,
  INDEX `created_by` (`created_by` ASC) VISIBLE,
  CONSTRAINT `formato_ibfk_1`
    FOREIGN KEY (`created_by`)
    REFERENCES `tienda_videojuegos`.`usuario` (`id_usuario`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_spanish_ci;

INSERT INTO `tienda_videojuegos`.`formato`
(`id_formato`, `nombre`, `created_by`)
VALUES
(1, 'Fisico', 1),
(2, 'Digital', 1)
ON DUPLICATE KEY UPDATE
  nombre = VALUES(nombre),
  deleted_at = NULL;


-- -----------------------------------------------------
-- Table `tienda_videojuegos`.`juego`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_videojuegos`.`juego` (
  `id_juego` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(120) NOT NULL,
  `precio` DECIMAL(10,2) NOT NULL DEFAULT '0.00',
  `stock` INT NOT NULL DEFAULT '0',
  `id_plataforma` INT NOT NULL,
  `id_genero` INT NOT NULL,
  `id_formato` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` INT NOT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `deleted_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id_juego`),
  INDEX `id_plataforma` (`id_plataforma` ASC) VISIBLE,
  INDEX `id_genero` (`id_genero` ASC) VISIBLE,
  INDEX `id_formato` (`id_formato` ASC) VISIBLE,
  INDEX `created_by` (`created_by` ASC) VISIBLE,
  CONSTRAINT `juego_ibfk_1`
    FOREIGN KEY (`id_plataforma`)
    REFERENCES `tienda_videojuegos`.`plataforma` (`id_plataforma`),
  CONSTRAINT `juego_ibfk_2`
    FOREIGN KEY (`id_genero`)
    REFERENCES `tienda_videojuegos`.`genero` (`id_genero`),
  CONSTRAINT `juego_ibfk_3`
    FOREIGN KEY (`id_formato`)
    REFERENCES `tienda_videojuegos`.`formato` (`id_formato`),
  CONSTRAINT `juego_ibfk_4`
    FOREIGN KEY (`created_by`)
    REFERENCES `tienda_videojuegos`.`usuario` (`id_usuario`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_spanish_ci;

INSERT INTO `tienda_videojuegos`.`juego`
(`id_juego`, `titulo`, `precio`, `stock`, `id_plataforma`, `id_genero`, `id_formato`, `created_by`)
VALUES
(1, 'Spider-Man 2', 49990.00, 10, 1, 1, 1, 1),
(2, 'FIFA 25', 59990.00, 8, 1, 3, 2, 1),
(3, 'Forza Horizon 5', 45990.00, 6, 2, 4, 2, 1),
(4, 'Minecraft', 29990.00, 13, 3, 2, 2, 1),
(5, 'Mario Kart 8 Deluxe', 54990.00, 5, 4, 4, 1, 1)
ON DUPLICATE KEY UPDATE
  titulo = VALUES(titulo),
  precio = VALUES(precio),
  stock = VALUES(stock),
  id_plataforma = VALUES(id_plataforma),
  id_genero = VALUES(id_genero),
  id_formato = VALUES(id_formato),
  deleted_at = NULL;


-- -----------------------------------------------------
-- Table `tienda_videojuegos`.`compra_juego`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_videojuegos`.`compra_juego` (
  `id_compra` INT NOT NULL AUTO_INCREMENT,
  `id_cliente` INT NOT NULL,
  `id_juego` INT NOT NULL,
  `fecha` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `cantidad` INT NOT NULL DEFAULT '1',
  `precio_unitario` DECIMAL(10,2) NOT NULL DEFAULT '0.00',
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` INT NOT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `deleted_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id_compra`),
  INDEX `id_cliente` (`id_cliente` ASC) VISIBLE,
  INDEX `id_juego` (`id_juego` ASC) VISIBLE,
  INDEX `created_by` (`created_by` ASC) VISIBLE,
  CONSTRAINT `compra_juego_ibfk_1`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `tienda_videojuegos`.`cliente` (`id_cliente`),
  CONSTRAINT `compra_juego_ibfk_2`
    FOREIGN KEY (`id_juego`)
    REFERENCES `tienda_videojuegos`.`juego` (`id_juego`),
  CONSTRAINT `compra_juego_ibfk_3`
    FOREIGN KEY (`created_by`)
    REFERENCES `tienda_videojuegos`.`usuario` (`id_usuario`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_spanish_ci;

INSERT INTO `tienda_videojuegos`.`compra_juego`
(`id_compra`, `id_cliente`, `id_juego`, `cantidad`, `precio_unitario`, `created_by`)
VALUES
(1, 1, 1, 1, 49990.00, 1),
(2, 2, 4, 2, 29990.00, 1),
(3, 3, 2, 1, 59990.00, 1)
ON DUPLICATE KEY UPDATE
  id_cliente = VALUES(id_cliente),
  id_juego = VALUES(id_juego),
  cantidad = VALUES(cantidad),
  precio_unitario = VALUES(precio_unitario),
  deleted_at = NULL;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
