"""Modelo de usuarios y consulta de canciones favoritas."""

import os

from flask_app.config.mysqlconnection import connectToMySQL


class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.contrasena = data["contrasena"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.favoritos = []

    @staticmethod
    def _database():
        return os.getenv("MYSQL_DATABASE", "esquema_canciones")

    @classmethod
    def get_all(cls):
        query = """
            SELECT id, nombre, email, contrasena, created_at, updated_at
            FROM usuarios
            ORDER BY nombre, id;
        """
        resultados = connectToMySQL(cls._database()).query_db(query)
        return [cls(registro) for registro in resultados]

    @classmethod
    def get_by_id(cls, usuario_id):
        query = """
            SELECT id, nombre, email, contrasena, created_at, updated_at
            FROM usuarios
            WHERE id = %(id)s;
        """
        resultados = connectToMySQL(cls._database()).query_db(
            query,
            {"id": usuario_id},
        )
        return cls(resultados[0]) if resultados else None

    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO usuarios (nombre, email, contrasena)
            VALUES (%(nombre)s, %(email)s, %(contrasena)s);
        """
        return connectToMySQL(cls._database()).query_db(query, datos)

    @classmethod
    def get_by_id_with_favorites(cls, datos):
        query = """
            SELECT
                usuarios.id AS usuario_id,
                usuarios.nombre AS usuario_nombre,
                usuarios.email AS usuario_email,
                usuarios.contrasena AS usuario_contrasena,
                usuarios.created_at AS usuario_created_at,
                usuarios.updated_at AS usuario_updated_at,
                canciones.id AS cancion_id,
                canciones.titulo AS cancion_titulo,
                canciones.artista AS cancion_artista,
                canciones.created_at AS cancion_created_at,
                canciones.updated_at AS cancion_updated_at
            FROM usuarios
            LEFT JOIN favoritos ON favoritos.usuario_id = usuarios.id
            LEFT JOIN canciones ON favoritos.cancion_id = canciones.id
            WHERE usuarios.id = %(id)s
            ORDER BY canciones.titulo;
        """
        resultados = connectToMySQL(cls._database()).query_db(query, datos)
        if not resultados:
            return None

        usuario = cls(
            {
                "id": resultados[0]["usuario_id"],
                "nombre": resultados[0]["usuario_nombre"],
                "email": resultados[0]["usuario_email"],
                "contrasena": resultados[0]["usuario_contrasena"],
                "created_at": resultados[0]["usuario_created_at"],
                "updated_at": resultados[0]["usuario_updated_at"],
            }
        )

        for fila in resultados:
            if fila["cancion_id"] is None:
                continue
            usuario.favoritos.append(
                {
                    "id": fila["cancion_id"],
                    "titulo": fila["cancion_titulo"],
                    "artista": fila["cancion_artista"],
                    "created_at": fila["cancion_created_at"],
                    "updated_at": fila["cancion_updated_at"],
                }
            )

        return usuario
