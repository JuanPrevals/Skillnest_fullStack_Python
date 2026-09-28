"""Modelo de canciones y consulta de usuarios relacionados."""

import os

from flask_app.config.mysqlconnection import connectToMySQL


class Cancion:
    def __init__(self, data):
        self.id = data["id"]
        self.titulo = data["titulo"]
        self.artista = data["artista"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.usuarios = []

    @staticmethod
    def _database():
        return os.getenv("MYSQL_DATABASE", "esquema_canciones")

    @classmethod
    def get_all(cls):
        query = """
            SELECT id, titulo, artista, created_at, updated_at
            FROM canciones
            ORDER BY titulo, id;
        """
        resultados = connectToMySQL(cls._database()).query_db(query)
        return [cls(registro) for registro in resultados]

    @classmethod
    def get_by_id(cls, cancion_id):
        query = """
            SELECT id, titulo, artista, created_at, updated_at
            FROM canciones
            WHERE id = %(id)s;
        """
        resultados = connectToMySQL(cls._database()).query_db(
            query,
            {"id": cancion_id},
        )
        return cls(resultados[0]) if resultados else None

    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO canciones (titulo, artista)
            VALUES (%(titulo)s, %(artista)s);
        """
        return connectToMySQL(cls._database()).query_db(query, datos)

    @classmethod
    def get_by_id_with_users(cls, datos):
        query = """
            SELECT
                canciones.id AS cancion_id,
                canciones.titulo AS cancion_titulo,
                canciones.artista AS cancion_artista,
                canciones.created_at AS cancion_created_at,
                canciones.updated_at AS cancion_updated_at,
                usuarios.id AS usuario_id,
                usuarios.nombre AS usuario_nombre,
                usuarios.email AS usuario_email,
                usuarios.contrasena AS usuario_contrasena,
                usuarios.created_at AS usuario_created_at,
                usuarios.updated_at AS usuario_updated_at
            FROM canciones
            LEFT JOIN favoritos ON favoritos.cancion_id = canciones.id
            LEFT JOIN usuarios ON favoritos.usuario_id = usuarios.id
            WHERE canciones.id = %(id)s
            ORDER BY usuarios.nombre;
        """
        resultados = connectToMySQL(cls._database()).query_db(query, datos)
        if not resultados:
            return None

        cancion = cls(
            {
                "id": resultados[0]["cancion_id"],
                "titulo": resultados[0]["cancion_titulo"],
                "artista": resultados[0]["cancion_artista"],
                "created_at": resultados[0]["cancion_created_at"],
                "updated_at": resultados[0]["cancion_updated_at"],
            }
        )

        for fila in resultados:
            if fila["usuario_id"] is None:
                continue
            cancion.usuarios.append(
                {
                    "id": fila["usuario_id"],
                    "nombre": fila["usuario_nombre"],
                    "email": fila["usuario_email"],
                    "contrasena": fila["usuario_contrasena"],
                    "created_at": fila["usuario_created_at"],
                    "updated_at": fila["usuario_updated_at"],
                }
            )

        return cancion

    @classmethod
    def get_not_favorited_by_user(cls, datos):
        query = """
            SELECT
                canciones.id,
                canciones.titulo,
                canciones.artista,
                canciones.created_at,
                canciones.updated_at
            FROM canciones
            LEFT JOIN favoritos
                ON favoritos.cancion_id = canciones.id
                AND favoritos.usuario_id = %(usuario_id)s
            WHERE favoritos.cancion_id IS NULL
            ORDER BY canciones.titulo;
        """
        resultados = connectToMySQL(cls._database()).query_db(query, datos)
        return [cls(registro) for registro in resultados]

    @classmethod
    def get_users_not_favorited(cls, datos):
        query = """
            SELECT
                usuarios.id,
                usuarios.nombre,
                usuarios.email,
                usuarios.contrasena,
                usuarios.created_at,
                usuarios.updated_at
            FROM usuarios
            LEFT JOIN favoritos
                ON favoritos.usuario_id = usuarios.id
                AND favoritos.cancion_id = %(cancion_id)s
            WHERE favoritos.usuario_id IS NULL
            ORDER BY usuarios.nombre;
        """
        return connectToMySQL(cls._database()).query_db(query, datos)
