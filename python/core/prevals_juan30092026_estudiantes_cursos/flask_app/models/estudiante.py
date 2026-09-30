import os

from flask_app.config.mysqlconnection import connect_to_mysql


class Estudiante:
    BASE_DE_DATOS = os.getenv("MYSQL_DATABASE", "esquema_estudiantes_cursos")

    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.edad = datos["edad"]
        self.curso_id = datos["curso_id"]
        self.created_at = datos.get("created_at")
        self.updated_at = datos.get("updated_at")

    @classmethod
    def guardar(cls, datos):
        query = """
            INSERT INTO estudiantes (nombre, apellido, edad, curso_id)
            VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);
        """
        return connect_to_mysql(cls.BASE_DE_DATOS).query_db(query, datos)
