import os
import re
from datetime import date

from flask import flash

from flask_app.config.mysqlconnection import connect_to_mysql


EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
NOMBRE_REGEX = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+(?:[ '-][A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)*$")


class Usuario:
    BASE_DE_DATOS = os.getenv("MYSQL_DATABASE", "login_registro")

    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.email = datos["email"]
        self.password = datos.get("password")
        self.fecha_nacimiento = datos.get("fecha_nacimiento")
        self.area_interes = datos.get("area_interes")
        self.modalidad = datos.get("modalidad")
        self.acepta_terminos = datos.get("acepta_terminos")
        self.created_at = datos.get("created_at")
        self.updated_at = datos.get("updated_at")

    @staticmethod
    def validar_registro(datos):
        es_valido = True

        for campo, etiqueta in (("nombre", "nombre"), ("apellido", "apellido")):
            valor = datos.get(campo, "").strip()
            if not valor:
                flash(f"El {etiqueta} es obligatorio.", "registro")
                es_valido = False
            elif len(valor) < 2:
                flash(f"El {etiqueta} debe tener al menos 2 caracteres.", "registro")
                es_valido = False
            elif len(valor) > 45:
                flash(f"El {etiqueta} no puede superar los 45 caracteres.", "registro")
                es_valido = False
            elif not NOMBRE_REGEX.fullmatch(valor):
                flash(f"El {etiqueta} solo puede contener letras.", "registro")
                es_valido = False

        email = datos.get("email", "").strip()
        if not email:
            flash("El e-mail es obligatorio.", "registro")
            es_valido = False
        elif len(email) > 120:
            flash("El e-mail no puede superar los 120 caracteres.", "registro")
            es_valido = False
        elif not EMAIL_REGEX.fullmatch(email):
            flash("El e-mail no tiene un formato válido.", "registro")
            es_valido = False

        password = datos.get("password", "")
        if not password:
            flash("La contraseña es obligatoria.", "registro")
            es_valido = False
        elif len(password) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            es_valido = False
        else:
            if not re.search(r"[A-Z]", password):
                flash("La contraseña debe incluir al menos una mayúscula.", "registro")
                es_valido = False
            if not re.search(r"\d", password):
                flash("La contraseña debe incluir al menos un número.", "registro")
                es_valido = False

        if datos.get("confirmar_password", "") != password:
            flash("La confirmación de contraseña no coincide.", "registro")
            es_valido = False

        try:
            nacimiento = date.fromisoformat(datos.get("fecha_nacimiento", ""))
            hoy = date.today()
            edad = hoy.year - nacimiento.year
            if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
                edad -= 1
            if nacimiento.year < 1900:
                flash("La fecha de nacimiento no es válida.", "registro")
                es_valido = False
            elif edad < 18:
                flash("Debes ser mayor de edad para registrarte.", "registro")
                es_valido = False
        except ValueError:
            flash("Ingresa una fecha de nacimiento válida.", "registro")
            es_valido = False

        if datos.get("area_interes") not in {"frontend", "backend", "datos"}:
            flash("Selecciona un área de interés.", "registro")
            es_valido = False

        if datos.get("modalidad") not in {"presencial", "online"}:
            flash("Selecciona una modalidad.", "registro")
            es_valido = False

        if not datos.get("acepta_terminos"):
            flash("Debes aceptar los términos para registrarte.", "registro")
            es_valido = False

        return es_valido

    @classmethod
    def buscar_por_email(cls, email):
        query = """
            SELECT id, nombre, apellido, email, password, fecha_nacimiento,
                   area_interes, modalidad, acepta_terminos, created_at, updated_at
            FROM usuarios
            WHERE email = %(email)s
            LIMIT 1;
        """
        filas = connect_to_mysql(cls.BASE_DE_DATOS).query_db(query, {"email": email})
        return cls(filas[0]) if filas else None

    @classmethod
    def buscar_por_id(cls, usuario_id):
        query = """
            SELECT id, nombre, apellido, email, fecha_nacimiento,
                   area_interes, modalidad, acepta_terminos, created_at, updated_at
            FROM usuarios
            WHERE id = %(id)s
            LIMIT 1;
        """
        filas = connect_to_mysql(cls.BASE_DE_DATOS).query_db(query, {"id": usuario_id})
        return cls(filas[0]) if filas else None

    @classmethod
    def guardar(cls, datos):
        query = """
            INSERT INTO usuarios (
                nombre, apellido, email, password, fecha_nacimiento,
                area_interes, modalidad, acepta_terminos
            )
            VALUES (
                %(nombre)s, %(apellido)s, %(email)s, %(password)s,
                %(fecha_nacimiento)s, %(area_interes)s, %(modalidad)s,
                %(acepta_terminos)s
            );
        """
        return connect_to_mysql(cls.BASE_DE_DATOS).query_db(query, datos)
