from flask import flash, redirect, render_template, request, session, url_for
from pymysql import MySQLError

from flask_app import app, bcrypt
from flask_app.controllers.helpers import exigir_csrf, login_requerido
from flask_app.models.usuario import Usuario


@app.get("/")
def inicio():
    if "usuario_id" in session:
        return redirect(url_for("mis_libros"))
    return render_template("auth/inicio.html", registro={}, login={}, errores={})


@app.post("/registro")
def registrar():
    if not exigir_csrf():
        return redirect(url_for("inicio"))
    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip().lower(),
        "password": request.form.get("password", ""),
        "confirmacion": request.form.get("confirmacion", ""),
    }
    try:
        errores = Usuario.validar_registro(datos)
        if errores:
            return render_template(
                "auth/inicio.html", registro=datos, login={}, errores=errores
            ), 422
        datos["password"] = bcrypt.generate_password_hash(datos["password"]).decode("utf-8")
        usuario_id = Usuario.crear(datos)
    except MySQLError:
        app.logger.exception("Error de MySQL durante el registro de usuario")
        flash("No pudimos completar el registro. Verifica la conexión e intenta nuevamente.", "danger")
        return render_template("auth/inicio.html", registro=datos, login={}, errores={}), 503

    session.clear()
    session["usuario_id"] = usuario_id
    session["usuario_nombre"] = datos["nombre"]
    flash(f"¡Bienvenido a BookHub, {datos['nombre']}! Tu cuenta está lista.", "success")
    return redirect(url_for("mis_libros"))


@app.post("/login")
def login():
    if not exigir_csrf():
        return redirect(url_for("inicio"))
    datos = {
        "email": request.form.get("email", "").strip().lower(),
        "password": request.form.get("password", ""),
    }
    errores = Usuario.validar_login(datos)
    usuario = None
    try:
        if not errores:
            usuario = Usuario.obtener_por_email(datos["email"])
    except MySQLError:
        app.logger.exception("Error de MySQL durante el inicio de sesión")
        flash("No se pudo conectar con la base de datos. Intenta nuevamente.", "danger")
        return render_template("auth/inicio.html", registro={}, login=datos, errores={}), 503

    if not usuario or not bcrypt.check_password_hash(usuario.password, datos["password"]):
        errores["login_general"] = "Correo o contraseña incorrectos."
    if errores:
        return render_template(
            "auth/inicio.html", registro={}, login=datos, errores=errores
        ), 401

    session.clear()
    session["usuario_id"] = usuario.id
    session["usuario_nombre"] = usuario.nombre
    flash(f"¡Qué bueno verte de nuevo, {usuario.nombre}!", "success")
    return redirect(url_for("mis_libros"))


@app.post("/logout")
@login_requerido
def logout():
    if not exigir_csrf():
        return redirect(url_for("mis_libros"))
    session.clear()
    flash("Tu sesión se cerró correctamente.", "info")
    return redirect(url_for("inicio"))
