import os

from mysqlconnection import connect_to_mysql


class Mascota:
    db = os.environ.get("MYSQL_DATABASE", "mascotas_db")

    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.tipo = datos["tipo"]
        self.color = datos["color"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]

    @classmethod
    def get_all(cls):
        resultados = connect_to_mysql(cls.db).query_db(
            "SELECT * FROM mascotas ORDER BY id;"
        )
        return [cls(fila) for fila in resultados]

    @classmethod
    def get_by_tipo(cls, tipo):
        resultados = connect_to_mysql(cls.db).query_db(
            "SELECT * FROM mascotas WHERE tipo = %(tipo)s ORDER BY id;",
            {"tipo": tipo},
        )
        return [cls(fila) for fila in resultados]

    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO mascotas (nombre, tipo, color)
            VALUES (%(nombre)s, %(tipo)s, %(color)s);
        """
        return connect_to_mysql(cls.db).query_db(query, datos)
