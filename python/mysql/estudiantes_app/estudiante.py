import os

from mysqlconnection import connect_to_mysql


class Estudiante:
    def __init__(self, data):
        self.id_estudiante = data["id_estudiante"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.created_at = data["created_at"]

    @classmethod
    def _connection(cls):
        return connect_to_mysql(os.getenv("MYSQL_DATABASE", "esquema_estudiantes"))

    @classmethod
    def get_all(cls):
        rows = cls._connection().query_db(
            """SELECT id_estudiante, nombre, email, created_at
               FROM estudiantes
               ORDER BY id_estudiante;"""
        )
        return [cls(row) for row in rows]

    @classmethod
    def get_by_id(cls, id_estudiante):
        rows = cls._connection().query_db(
            """SELECT id_estudiante, nombre, email, created_at
               FROM estudiantes
               WHERE id_estudiante = %(id_estudiante)s;""",
            {"id_estudiante": id_estudiante},
        )
        return cls(rows[0]) if rows else None

    @classmethod
    def actualizar(cls, data):
        return cls._connection().query_db(
            """UPDATE estudiantes
               SET nombre = %(nombre)s,
                   email = %(email)s
               WHERE id_estudiante = %(id_estudiante)s;""",
            data,
        )

    @classmethod
    def eliminar(cls, data):
        return cls._connection().query_db(
            """DELETE FROM estudiantes
               WHERE id_estudiante = %(id_estudiante)s;""",
            data,
        )

