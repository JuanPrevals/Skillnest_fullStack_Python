"""Modelo de estudiantes."""

import os

from flask_app.config.mysqlconnection import connectToMySQL


class Estudiante:
    def __init__(self, data):
        self.id_estudiante = data["id_estudiante"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.created_at = data["created_at"]

    @staticmethod
    def _database():
        return os.getenv("MYSQL_DATABASE", "esquema_educacion")

    @classmethod
    def get_all(cls):
        query = """
            SELECT id_estudiante, nombre, email, created_at
            FROM estudiantes
            ORDER BY nombre, id_estudiante;
        """
        resultados = connectToMySQL(cls._database()).query_db(query)
        return [cls(registro) for registro in resultados]

    @classmethod
    def get_by_id(cls, id_estudiante):
        query = """
            SELECT id_estudiante, nombre, email, created_at
            FROM estudiantes
            WHERE id_estudiante = %(id_estudiante)s;
        """
        resultados = connectToMySQL(cls._database()).query_db(
            query,
            {"id_estudiante": id_estudiante},
        )
        return cls(resultados[0]) if resultados else None
