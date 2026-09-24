"""Modelo de usuarios."""

import os

from flask_app.config.mysqlconnection import connectToMySQL


class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    @staticmethod
    def _database():
        return os.getenv("MYSQL_DATABASE", "esquema_seguidores")

    @classmethod
    def get_all(cls):
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            ORDER BY nombre, apellido, id;
        """
        resultados = connectToMySQL(cls._database()).query_db(query)
        return [cls(registro) for registro in resultados]

    @classmethod
    def get_by_id(cls, usuario_id):
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
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
            INSERT INTO usuarios (nombre, apellido, email)
            VALUES (%(nombre)s, %(apellido)s, %(email)s);
        """
        return connectToMySQL(cls._database()).query_db(query, datos)
