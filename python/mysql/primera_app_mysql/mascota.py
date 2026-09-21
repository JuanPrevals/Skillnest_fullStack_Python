from mysqlconnection import connectToMySQL


class Mascota:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM mascotas;"
        resultados = connectToMySQL("primera_flask").query_db(query)
        if resultados is False:
            raise RuntimeError("No se pudieron consultar las mascotas.")
        mascotas = []
        for mascota in resultados:
            mascotas.append(cls(mascota))
        return mascotas

    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO mascotas (nombre, tipo, color, created_at, updated_at)
            VALUES (%(nombre)s, %(tipo)s, %(color)s, NOW(), NOW());
        """
        return connectToMySQL("primera_flask").query_db(query, datos)

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM mascotas WHERE id = %(id)s;"
        resultados = connectToMySQL("primera_flask").query_db(query, {"id": id})
        if resultados is False:
            raise RuntimeError("No se pudo consultar la mascota.")
        return cls(resultados[0]) if resultados else None
