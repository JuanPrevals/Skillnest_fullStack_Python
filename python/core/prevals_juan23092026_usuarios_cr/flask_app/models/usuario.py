import os

from python.core.usuarios_cr.flask_app.config.mysqlconnection import connect_to_mysql


class Usuario:
    BASE_DE_DATOS = os.getenv("MYSQL_DATABASE", "esquema_usuarios")

    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.email = datos["email"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]

    @classmethod
    def get_all(cls):
        consulta = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            ORDER BY id;
        """
        filas = connect_to_mysql(cls.BASE_DE_DATOS).query_db(consulta)
        return [cls(fila) for fila in filas]

    @classmethod
    def get_by_id(cls, id):
        consulta = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            WHERE id = %(id)s;
        """
        filas = connect_to_mysql(cls.BASE_DE_DATOS).query_db(consulta, {"id": id})
        return cls(filas[0]) if filas else None

    @classmethod
    def save(cls, datos):
        consulta = """
            INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        return connect_to_mysql(cls.BASE_DE_DATOS).query_db(consulta, datos)

    @classmethod
    def update(cls, datos):
        consulta = """
            UPDATE usuarios
            SET nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s,
                updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connect_to_mysql(cls.BASE_DE_DATOS).query_db(consulta, datos)

    @classmethod
    def delete(cls, id):
        consulta = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connect_to_mysql(cls.BASE_DE_DATOS).query_db(consulta, {"id": id})
