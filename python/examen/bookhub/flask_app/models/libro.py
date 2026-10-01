from datetime import date, datetime

from flask_app.config.mysqlconnection import connect_to_mysql


class Libro:
    DB = "bookhub_db"
    GENEROS = (
        "Aventura",
        "Ciencia ficción",
        "Desarrollo personal",
        "Fantasía",
        "Historia",
        "Misterio",
        "Novela",
        "Poesía",
        "Romance",
        "Terror",
    )

    def __init__(self, data):
        self.id = data.get("id")
        self.titulo = data.get("titulo", "")
        self.autor = data.get("autor", "")
        self.genero = data.get("genero", "")
        self.fecha_publicacion = data.get("fecha_publicacion")
        self.descripcion = data.get("descripcion", "")
        self.usuario_id = data.get("usuario_id")
        self.publicado_por = data.get("publicado_por", "")
        self.total_favoritos = int(data.get("total_favoritos", 0) or 0)
        self.es_favorito = bool(data.get("es_favorito", False))
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")

    @classmethod
    def crear(cls, data):
        query = """
            INSERT INTO libros
                (titulo, autor, genero, fecha_publicacion, descripcion, usuario_id)
            VALUES
                (%(titulo)s, %(autor)s, %(genero)s, %(fecha_publicacion)s,
                 %(descripcion)s, %(usuario_id)s);
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod
    def obtener_por_id(cls, libro_id, usuario_actual_id=None):
        query = """
            SELECT l.*, CONCAT(u.nombre, ' ', u.apellido) AS publicado_por,
                   COUNT(DISTINCT f.usuario_id) AS total_favoritos,
                   MAX(CASE WHEN f.usuario_id = %(usuario_actual_id)s THEN 1 ELSE 0 END)
                       AS es_favorito
            FROM libros l
            JOIN usuarios u ON u.id = l.usuario_id
            LEFT JOIN favoritos f ON f.libro_id = l.id
            WHERE l.id = %(libro_id)s
            GROUP BY l.id, u.id;
        """
        datos = {"libro_id": libro_id, "usuario_actual_id": usuario_actual_id or 0}
        resultados = connect_to_mysql().query_db(query, datos)
        return cls(resultados[0]) if resultados else None

    @classmethod
    def obtener_del_usuario(cls, usuario_id):
        query = """
            SELECT l.*, COUNT(f.usuario_id) AS total_favoritos
            FROM libros l
            LEFT JOIN favoritos f ON f.libro_id = l.id
            WHERE l.usuario_id = %(usuario_id)s
            GROUP BY l.id
            ORDER BY l.created_at DESC;
        """
        return [cls(fila) for fila in connect_to_mysql().query_db(query, {"usuario_id": usuario_id})]

    @classmethod
    def obtener_comunidad(cls, usuario_id, limite=None):
        limite_sql = " LIMIT %(limite)s" if limite else ""
        query = f"""
            SELECT l.*, CONCAT(u.nombre, ' ', u.apellido) AS publicado_por,
                   COUNT(DISTINCT f.usuario_id) AS total_favoritos,
                   MAX(CASE WHEN f.usuario_id = %(usuario_id)s THEN 1 ELSE 0 END)
                       AS es_favorito
            FROM libros l
            JOIN usuarios u ON u.id = l.usuario_id
            LEFT JOIN favoritos f ON f.libro_id = l.id
            WHERE l.usuario_id <> %(usuario_id)s
            GROUP BY l.id, u.id
            ORDER BY l.created_at DESC{limite_sql};
        """
        data = {"usuario_id": usuario_id}
        if limite:
            data["limite"] = int(limite)
        return [cls(fila) for fila in connect_to_mysql().query_db(query, data)]

    @classmethod
    def explorar(cls, usuario_id, termino="", genero=""):
        filtros = ["1 = 1"]
        data = {"usuario_id": usuario_id}
        if termino:
            filtros.append("(l.titulo LIKE %(termino)s OR l.autor LIKE %(termino)s)")
            data["termino"] = f"%{termino}%"
        if genero in cls.GENEROS:
            filtros.append("l.genero = %(genero)s")
            data["genero"] = genero
        query = f"""
            SELECT l.*, CONCAT(u.nombre, ' ', u.apellido) AS publicado_por,
                   COUNT(DISTINCT f.usuario_id) AS total_favoritos,
                   MAX(CASE WHEN f.usuario_id = %(usuario_id)s THEN 1 ELSE 0 END)
                       AS es_favorito
            FROM libros l
            JOIN usuarios u ON u.id = l.usuario_id
            LEFT JOIN favoritos f ON f.libro_id = l.id
            WHERE {' AND '.join(filtros)}
            GROUP BY l.id, u.id
            ORDER BY l.created_at DESC;
        """
        return [cls(fila) for fila in connect_to_mysql().query_db(query, data)]

    @classmethod
    def actualizar(cls, libro_id, usuario_id, data):
        query = """
            UPDATE libros
            SET titulo = %(titulo)s, autor = %(autor)s, genero = %(genero)s,
                fecha_publicacion = %(fecha_publicacion)s,
                descripcion = %(descripcion)s
            WHERE id = %(libro_id)s AND usuario_id = %(usuario_id)s;
        """
        data = {**data, "libro_id": libro_id, "usuario_id": usuario_id}
        return connect_to_mysql().query_db(query, data)

    @classmethod
    def eliminar(cls, libro_id, usuario_id):
        query = "DELETE FROM libros WHERE id = %(id)s AND usuario_id = %(usuario_id)s;"
        return connect_to_mysql().query_db(query, {"id": libro_id, "usuario_id": usuario_id})

    @staticmethod
    def validar(formulario):
        errores = {}
        titulo = formulario.get("titulo", "").strip()
        autor = formulario.get("autor", "").strip()
        genero = formulario.get("genero", "").strip()
        fecha_texto = formulario.get("fecha_publicacion", "").strip()
        descripcion = formulario.get("descripcion", "").strip()

        if len(titulo) < 2:
            errores["titulo"] = "El título debe tener al menos 2 caracteres."
        if len(autor) < 2:
            errores["autor"] = "El autor debe tener al menos 2 caracteres."
        if genero not in Libro.GENEROS:
            errores["genero"] = "Selecciona un género válido."
        try:
            fecha = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
            if fecha > date.today():
                errores["fecha_publicacion"] = "La fecha de publicación no puede ser futura."
        except ValueError:
            errores["fecha_publicacion"] = "Ingresa una fecha de publicación válida."
        if len(descripcion) < 10:
            errores["descripcion"] = "La descripción debe tener al menos 10 caracteres."
        elif len(descripcion) > 2000:
            errores["descripcion"] = "La descripción no puede superar 2000 caracteres."
        return errores
