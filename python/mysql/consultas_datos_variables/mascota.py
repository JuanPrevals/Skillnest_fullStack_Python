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
        return [cls(mascota) for mascota in resultados]

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM mascotas WHERE id = %(id_mascota)s;"
        data = {"id_mascota": id}
        resultados = connectToMySQL("primera_flask").query_db(query, data)
        if resultados is False:
            raise RuntimeError("No se pudo consultar la mascota.")
        return cls(resultados[0]) if resultados else None

    @classmethod
    def get_by_name(cls, nombre):
        query = "SELECT * FROM mascotas WHERE nombre = %(nombre_mascota)s;"
        data = {"nombre_mascota": nombre}
        resultados = connectToMySQL("primera_flask").query_db(query, data)
        if resultados is False:
            raise RuntimeError("No se pudo consultar la mascota.")
        return cls(resultados[0]) if resultados else None

    @classmethod
    def get_by_tipo(cls, tipo):
        query = "SELECT * FROM mascotas WHERE tipo = %(tipo_mascota)s;"
        data = {"tipo_mascota": tipo}
        resultados = connectToMySQL("primera_flask").query_db(query, data)
        if resultados is False:
            raise RuntimeError("No se pudieron consultar las mascotas.")
        return [cls(mascota) for mascota in resultados]
