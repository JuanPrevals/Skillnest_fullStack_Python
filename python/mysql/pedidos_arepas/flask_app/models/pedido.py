from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL


class Pedido:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.cantidad = data["cantidad"]
        self.relleno = data["relleno"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = """
            SELECT id, nombre, cantidad, relleno, created_at, updated_at
            FROM pedidos
            ORDER BY id DESC;
        """
        resultados = connectToMySQL("esquema_arepas").query_db(query)
        return [cls(registro) for registro in resultados]

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO pedidos (nombre, cantidad, relleno)
            VALUES (%(nombre)s, %(cantidad)s, %(relleno)s);
        """
        return connectToMySQL("esquema_arepas").query_db(query, data)

    @staticmethod
    def validar_pedido(data):
        es_valido = True
        nombre = data.get("nombre", "").strip()
        relleno = data.get("relleno", "").strip()
        cantidad = data.get("cantidad", "").strip()

        if not nombre:
            flash("El nombre es obligatorio.", "danger")
            es_valido = False
        elif len(nombre) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "danger")
            es_valido = False

        if not cantidad:
            flash("La cantidad es obligatoria.", "danger")
            es_valido = False
        else:
            try:
                if int(cantidad) <= 0:
                    flash("La cantidad debe ser mayor que 0.", "danger")
                    es_valido = False
            except ValueError:
                flash("La cantidad debe ser un número entero válido.", "danger")
                es_valido = False

        if not relleno:
            flash("El relleno es obligatorio.", "danger")
            es_valido = False

        return es_valido
