"""Modelo de la relación muchos-a-muchos entre estudiantes y cursos."""

import os

from flask_app.config.mysqlconnection import connectToMySQL


class Inscripcion:
    @staticmethod
    def _database():
        return os.getenv("MYSQL_DATABASE", "esquema_educacion")

    @classmethod
    def existe(cls, datos):
        query = """
            SELECT estudiante_id, curso_id
            FROM inscripciones
            WHERE estudiante_id = %(estudiante_id)s
              AND curso_id = %(curso_id)s;
        """
        resultado = connectToMySQL(cls._database()).query_db(query, datos)
        return bool(resultado)

    @classmethod
    def inscribir_estudiante_en_curso(cls, datos):
        query = """
            INSERT INTO inscripciones (estudiante_id, curso_id)
            VALUES (%(estudiante_id)s, %(curso_id)s);
        """
        return connectToMySQL(cls._database()).query_db(query, datos)

    @classmethod
    def get_all(cls):
        query = """
            SELECT
                estudiantes.id_estudiante,
                estudiantes.nombre AS estudiante,
                estudiantes.email,
                cursos.id_curso,
                cursos.nombre_curso
            FROM inscripciones
            INNER JOIN estudiantes
                ON inscripciones.estudiante_id = estudiantes.id_estudiante
            INNER JOIN cursos
                ON inscripciones.curso_id = cursos.id_curso
            ORDER BY estudiantes.nombre, cursos.nombre_curso;
        """
        return connectToMySQL(cls._database()).query_db(query)
