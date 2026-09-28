import os
import re

from flask import flash

from flask_app.config.mysqlconnection import connect_to_mysql


EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)


class Usuario:
    BASE_DE_DATOS = os.getenv("MYSQL_DATABASE", "esquema_usuarios")

    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.email = datos["email"]
        self.password = datos.get("password")
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]

    @staticmethod
    def validar_usuario(usuario):
        """Valida el formulario y agrega un mensaje flash por cada error."""
        es_valido = True

        if not usuario.get("nombre", "").strip():
            flash("El nombre es obligatorio.", "nombre")
            es_valido = False
        elif len(usuario["nombre"]) > 45:
            flash("El nombre no puede superar los 45 caracteres.", "nombre")
            es_valido = False

        if not usuario.get("apellido", "").strip():
            flash("El apellido es obligatorio.", "apellido")
            es_valido = False
        elif len(usuario["apellido"]) > 45:
            flash("El apellido no puede superar los 45 caracteres.", "apellido")
            es_valido = False

        email = usuario.get("email", "").strip()
        if not email:
            flash("El email es obligatorio.", "email")
            es_valido = False
        elif len(email) > 45:
            flash("El email no puede superar los 45 caracteres.", "email")
            es_valido = False
        elif not EMAIL_REGEX.fullmatch(email):
            flash("El email no tiene un formato válido.", "email")
            es_valido = False

        if "password" in usuario:
            password = usuario.get("password", "")
            if not password:
                flash("La contraseña es obligatoria.", "password")
                es_valido = False
            elif len(password) < 8:
                flash(
                    "La contraseña debe tener al menos 8 caracteres.",
                    "password",
                )
                es_valido = False

        return es_valido

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
    def email_existe(cls, email, excluir_id=None):
        consulta = "SELECT id FROM usuarios WHERE email = %(email)s"
        datos = {"email": email}

        if excluir_id is not None:
            consulta += " AND id != %(excluir_id)s"
            datos["excluir_id"] = excluir_id

        consulta += " LIMIT 1;"
        filas = connect_to_mysql(cls.BASE_DE_DATOS).query_db(consulta, datos)
        return bool(filas)

    @classmethod
    def buscar_por_email(cls, email):
        consulta = """
            SELECT id, nombre, apellido, email, password, created_at, updated_at
            FROM usuarios
            WHERE email = %(email)s
            LIMIT 1;
        """
        filas = connect_to_mysql(cls.BASE_DE_DATOS).query_db(
            consulta, {"email": email}
        )
        return cls(filas[0]) if filas else None

    @classmethod
    def save(cls, datos):
        consulta = """
            INSERT INTO usuarios
                (nombre, apellido, email, password, created_at, updated_at)
            VALUES
                (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());
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
