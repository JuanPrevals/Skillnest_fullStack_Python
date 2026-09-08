CREATE DATABASE IF NOT EXISTS voluntame_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE voluntame_db;

CREATE TABLE IF NOT EXISTS usuarios (
  id_usuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  contrasena VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_usuario),
  UNIQUE KEY email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS misiones (
  id_mision INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  fecha DATE NOT NULL,
  voluntarios_necesarios INT NOT NULL,
  descripcion TEXT NOT NULL,
  usuario_id INT NOT NULL,
  created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_mision),
  KEY usuario_id (usuario_id),
  CONSTRAINT misiones_ibfk_1 FOREIGN KEY (usuario_id)
    REFERENCES usuarios (id_usuario) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS voluntarios_misiones (
  usuario_id INT NOT NULL,
  mision_id INT NOT NULL,
  created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (usuario_id, mision_id),
  KEY mision_id (mision_id),
  CONSTRAINT voluntarios_misiones_ibfk_1 FOREIGN KEY (usuario_id)
    REFERENCES usuarios (id_usuario) ON DELETE CASCADE,
  CONSTRAINT voluntarios_misiones_ibfk_2 FOREIGN KEY (mision_id)
    REFERENCES misiones (id_mision) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT IGNORE INTO usuarios
  (id_usuario, nombre, apellido, email, contrasena, created_at, updated_at)
VALUES
  (1, 'Dany', 'Hernandez', 'dannyahg@gmail.com',
   '$2b$12$v1NDZPw.7pSKr7Qh.ojyBefEL4b5JjuBUiHToolH8zuLJKG0ZWkZq',
   '2026-02-11 19:27:30', '2026-02-11 19:27:30');

INSERT IGNORE INTO misiones
  (id_mision, nombre, fecha, voluntarios_necesarios, descripcion, usuario_id, created_at, updated_at)
VALUES
  (2, 'Limpieza de Liceo VVH', '2026-02-23', 15,
   'Necesitamos a voluntarios que nos ayuden a mejorar la limpieza del entorno escolar para recibirles',
   1, '2026-02-11 19:30:25', '2026-02-11 19:30:25');

INSERT IGNORE INTO voluntarios_misiones
  (usuario_id, mision_id, created_at)
VALUES
  (1, 2, '2026-02-11 19:30:30');
