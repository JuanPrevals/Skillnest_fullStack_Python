import os

from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app.models.estudiante import Estudiante


class Curso:
    BASE_DE_DATOS = os.getenv("MYSQL_DATABASE", "esquema_estudiantes_cursos")

    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.created_at = datos.get("created_at")
        self.updated_at = datos.get("updated_at")
        self.estudiantes = []

    @classmethod
    def obtener_todos(cls):
        query = """
            SELECT id, nombre, created_at, updated_at
            FROM cursos
            ORDER BY nombre;
        """
        filas = connect_to_mysql(cls.BASE_DE_DATOS).query_db(query)
        return [cls(fila) for fila in filas]

    @classmethod
    def obtener_por_id(cls, curso_id):
        query = """
            SELECT id, nombre, created_at, updated_at
            FROM cursos
            WHERE id = %(id)s;
        """
        filas = connect_to_mysql(cls.BASE_DE_DATOS).query_db(query, {"id": curso_id})
        return cls(filas[0]) if filas else None

    @classmethod
    def nombre_existe(cls, nombre):
        query = "SELECT id FROM cursos WHERE nombre = %(nombre)s LIMIT 1;"
        filas = connect_to_mysql(cls.BASE_DE_DATOS).query_db(query, {"nombre": nombre})
        return bool(filas)

    @classmethod
    def guardar(cls, datos):
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s);"
        return connect_to_mysql(cls.BASE_DE_DATOS).query_db(query, datos)

    @classmethod
    def obtener_con_estudiantes(cls, curso_id):
        query = """
            SELECT
                c.id AS curso_id,
                c.nombre AS curso_nombre,
                c.created_at AS curso_created_at,
                c.updated_at AS curso_updated_at,
                e.id AS estudiante_id,
                e.nombre AS estudiante_nombre,
                e.apellido AS estudiante_apellido,
                e.edad AS estudiante_edad,
                e.created_at AS estudiante_created_at,
                e.updated_at AS estudiante_updated_at
            FROM cursos c
            LEFT JOIN estudiantes e ON c.id = e.curso_id
            WHERE c.id = %(id)s
            ORDER BY e.nombre, e.apellido;
        """
        filas = connect_to_mysql(cls.BASE_DE_DATOS).query_db(query, {"id": curso_id})
        if not filas:
            return None

        curso = cls({
            "id": filas[0]["curso_id"],
            "nombre": filas[0]["curso_nombre"],
            "created_at": filas[0]["curso_created_at"],
            "updated_at": filas[0]["curso_updated_at"],
        })

        for fila in filas:
            if fila["estudiante_id"] is not None:
                curso.estudiantes.append(Estudiante({
                    "id": fila["estudiante_id"],
                    "nombre": fila["estudiante_nombre"],
                    "apellido": fila["estudiante_apellido"],
                    "edad": fila["estudiante_edad"],
                    "curso_id": curso.id,
                    "created_at": fila["estudiante_created_at"],
                    "updated_at": fila["estudiante_updated_at"],
                }))
        return curso
