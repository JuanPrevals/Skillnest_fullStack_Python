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


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
