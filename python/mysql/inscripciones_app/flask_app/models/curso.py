"""Modelo de cursos."""

import os

from flask_app.config.mysqlconnection import connectToMySQL


class Curso:
    def __init__(self, data):
        self.id_curso = data["id_curso"]
        self.nombre_curso = data["nombre_curso"]
        self.descripcion = data["descripcion"]
        self.created_at = data["created_at"]

    @staticmethod
    def _database():
        return os.getenv("MYSQL_DATABASE", "esquema_educacion")

    @classmethod
    def get_all(cls):
        query = """
            SELECT id_curso, nombre_curso, descripcion, created_at
            FROM cursos
            ORDER BY nombre_curso, id_curso;
        """
        resultados = connectToMySQL(cls._database()).query_db(query)
        return [cls(registro) for registro in resultados]

    @classmethod
    def get_by_id(cls, id_curso):
        query = """
            SELECT id_curso, nombre_curso, descripcion, created_at
            FROM cursos
            WHERE id_curso = %(id_curso)s;
        """
        resultados = connectToMySQL(cls._database()).query_db(
            query,
            {"id_curso": id_curso},
        )
        return cls(resultados[0]) if resultados else None
