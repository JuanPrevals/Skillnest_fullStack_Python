import os

from mysqlconnection import connect_to_mysql


class Usuario:
    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.email = datos["email"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]

    @classmethod
    def get_all(cls):
        filas = connect_to_mysql(os.getenv("MYSQL_DATABASE", "esquema_usuarios")).query_db(
            "SELECT id, nombre, apellido, email, created_at, updated_at FROM usuarios ORDER BY id;"
        )
        return [cls(fila) for fila in filas]

    @classmethod
    def get_by_id(cls, id):
        filas = connect_to_mysql(os.getenv("MYSQL_DATABASE", "esquema_usuarios")).query_db(
            """SELECT id, nombre, apellido, email, created_at, updated_at
               FROM usuarios
               WHERE id = %(id)s;""",
            {"id": id},
        )
        return cls(filas[0]) if filas else None

    @classmethod
    def save(cls, datos):
        return connect_to_mysql(os.getenv("MYSQL_DATABASE", "esquema_usuarios")).query_db(
            """INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at)
               VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());""",
            datos,
        )

    @classmethod
    def update(cls, datos):
        return connect_to_mysql(os.getenv("MYSQL_DATABASE", "esquema_usuarios")).query_db(
            """UPDATE usuarios
               SET nombre = %(nombre)s,
                   apellido = %(apellido)s,
                   email = %(email)s,
                   updated_at = NOW()
               WHERE id = %(id)s;""",
            datos,
        )

    @classmethod
    def delete(cls, id):
        return connect_to_mysql(os.getenv("MYSQL_DATABASE", "esquema_usuarios")).query_db(
            "DELETE FROM usuarios WHERE id = %(id)s;",
            {"id": id},
        )
