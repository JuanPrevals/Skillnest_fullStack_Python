from flask import flash, redirect, render_template, request, session, url_for
from flask_bcrypt import Bcrypt
from pymysql import MySQLError

from flask_app import app
from flask_app.models.usuario import Usuario


bcrypt = Bcrypt(app)


def datos_registro(formulario):
    return {
        "nombre": formulario.get("nombre", "").strip(),
        "apellido": formulario.get("apellido", "").strip(),
        "email": formulario.get("email", "").strip().lower(),
        "password": formulario.get("password", ""),
        "confirmar_password": formulario.get("confirmar_password", ""),
        "fecha_nacimiento": formulario.get("fecha_nacimiento", "").strip(),
        "area_interes": formulario.get("area_interes", "").strip(),
        "modalidad": formulario.get("modalidad", "").strip(),
        "acepta_terminos": formulario.get("acepta_terminos") == "on",
    }


def conservar_formulario(datos):
    session["registro_formulario"] = {
        campo: datos[campo]
        for campo in (
            "nombre", "apellido", "email", "fecha_nacimiento",
            "area_interes", "modalidad", "acepta_terminos"
        )
    }


@app.get("/")
def inicio():
    if session.get("usuario_id"):
        return redirect(url_for("exito"))
    formulario = session.pop("registro_formulario", {})
    login_email = session.pop("login_email", "")
    return render_template("inicio.html", formulario=formulario, login_email=login_email)


@app.post("/registrar")
def registrar():
    datos = datos_registro(request.form)

    if not Usuario.validar_registro(datos):
        conservar_formulario(datos)
        return redirect(url_for("inicio"))

    if Usuario.buscar_por_email(datos["email"]):
        flash("El e-mail ya se encuentra registrado.", "registro")
        conservar_formulario(datos)
        return redirect(url_for("inicio"))

    password_hash = bcrypt.generate_password_hash(datos["password"]).decode("utf-8")
    usuario_id = Usuario.guardar({
        "nombre": datos["nombre"],
        "apellido": datos["apellido"],
        "email": datos["email"],
        "password": password_hash,
        "fecha_nacimiento": datos["fecha_nacimiento"],
        "area_interes": datos["area_interes"],
        "modalidad": datos["modalidad"],
        "acepta_terminos": datos["acepta_terminos"],
    })
    session.clear()
    session["usuario_id"] = usuario_id
    flash("Tu cuenta fue creada correctamente.", "exito")
    return redirect(url_for("exito"))


@app.post("/iniciar-sesion")
def iniciar_sesion():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    usuario = Usuario.buscar_por_email(email) if email else None

    if (
        usuario is None
        or not usuario.password
        or not bcrypt.check_password_hash(usuario.password, password)
    ):
        flash("E-mail o contraseña incorrectos.", "login")
        session["login_email"] = email
        return redirect(url_for("inicio"))

    session.clear()
    session["usuario_id"] = usuario.id
    return redirect(url_for("exito"))


@app.get("/exito")
def exito():
    usuario_id = session.get("usuario_id")
    if not usuario_id:
        flash("Debes iniciar sesión para ver esa página.", "login")
        return redirect(url_for("inicio"))

    usuario = Usuario.buscar_por_id(usuario_id)
    if usuario is None:
        session.clear()
        flash("Tu sesión ya no es válida. Inicia sesión nuevamente.", "login")
        return redirect(url_for("inicio"))
    return render_template("exito.html", usuario=usuario)


@app.post("/cerrar-sesion")
def cerrar_sesion():
    session.clear()
    return redirect(url_for("inicio"))


@app.errorhandler(MySQLError)
def error_mysql(error):
    app.logger.exception("Error al comunicarse con MySQL.")
    session.pop("usuario_id", None)
    flash(
        "No fue posible completar la operación. Revisa la conexión con MySQL.",
        "general",
    )
    return redirect(url_for("inicio"))
