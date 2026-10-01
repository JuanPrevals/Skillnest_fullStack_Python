from flask_app.config.mysqlconnection import connect_to_mysql


class Favorito:
    DB = "bookhub_db"

    def __init__(self, data):
        self.id = data.get("id")
        self.usuario_id = data.get("usuario_id")
        self.libro_id = data.get("libro_id")
        self.created_at = data.get("created_at")

    @classmethod
    def agregar(cls, usuario_id, libro_id):
        query = """
            INSERT IGNORE INTO favoritos (usuario_id, libro_id)
            VALUES (%(usuario_id)s, %(libro_id)s);
        """
        return connect_to_mysql().query_db(query, {"usuario_id": usuario_id, "libro_id": libro_id})

    @classmethod
    def quitar(cls, usuario_id, libro_id):
        query = """
            DELETE FROM favoritos
            WHERE usuario_id = %(usuario_id)s AND libro_id = %(libro_id)s;
        """
        return connect_to_mysql().query_db(query, {"usuario_id": usuario_id, "libro_id": libro_id})

    @classmethod
    def del_usuario(cls, usuario_id):
        from flask_app.models.libro import Libro

        query = """
            SELECT l.*, CONCAT(u.nombre, ' ', u.apellido) AS publicado_por,
                   (SELECT COUNT(*) FROM favoritos fx WHERE fx.libro_id = l.id)
                       AS total_favoritos,
                   1 AS es_favorito
            FROM favoritos f
            JOIN libros l ON l.id = f.libro_id
            JOIN usuarios u ON u.id = l.usuario_id
            WHERE f.usuario_id = %(usuario_id)s
            ORDER BY f.created_at DESC;
        """
        filas = connect_to_mysql().query_db(query, {"usuario_id": usuario_id})
        return [Libro(fila) for fila in filas]

    @classmethod
    def usuarios_del_libro(cls, libro_id):
        query = """
            SELECT u.id, u.nombre, u.apellido
            FROM favoritos f
            JOIN usuarios u ON u.id = f.usuario_id
            WHERE f.libro_id = %(libro_id)s
            ORDER BY f.created_at DESC;
        """
        return connect_to_mysql().query_db(query, {"libro_id": libro_id})
