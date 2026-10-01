import re

from flask_app.config.mysqlconnection import connect_to_mysql


class Usuario:
    DB = "bookhub_db"
    EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    def __init__(self, data):
        self.id = data.get("id")
        self.nombre = data.get("nombre", "")
        self.apellido = data.get("apellido", "")
        self.email = data.get("email", "")
        self.password = data.get("password", "")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")

    @classmethod
    def crear(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod
    def obtener_por_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s LIMIT 1;"
        resultados = connect_to_mysql().query_db(query, {"email": email})
        return cls(resultados[0]) if resultados else None

    @classmethod
    def obtener_por_id(cls, usuario_id):
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios WHERE id = %(id)s LIMIT 1;
        """
        resultados = connect_to_mysql().query_db(query, {"id": usuario_id})
        return cls(resultados[0]) if resultados else None

    @staticmethod
    def validar_registro(formulario):
        errores = {}
        nombre = formulario.get("nombre", "").strip()
        apellido = formulario.get("apellido", "").strip()
        email = formulario.get("email", "").strip().lower()
        password = formulario.get("password", "")
        confirmacion = formulario.get("confirmacion", "")

        if len(nombre) < 2:
            errores["nombre"] = "El nombre debe tener al menos 2 caracteres."
        if len(apellido) < 2:
            errores["apellido"] = "El apellido debe tener al menos 2 caracteres."
        if not Usuario.EMAIL_REGEX.match(email):
            errores["email"] = "Ingresa un correo electrónico válido."
        elif Usuario.obtener_por_email(email):
            errores["email"] = "Este correo ya está registrado. Inicia sesión."
        if len(password) < 8:
            errores["password"] = "La contraseña debe tener al menos 8 caracteres."
        elif not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
            errores["password"] = "La contraseña debe incluir letras y números."
        if password != confirmacion:
            errores["confirmacion"] = "Las contraseñas no coinciden."
        return errores

    @staticmethod
    def validar_login(formulario):
        errores = {}
        email = formulario.get("email", "").strip().lower()
        if not Usuario.EMAIL_REGEX.match(email):
            errores["login_email"] = "Ingresa un correo electrónico válido."
        if not formulario.get("password"):
            errores["login_password"] = "Ingresa tu contraseña."
        return errores
