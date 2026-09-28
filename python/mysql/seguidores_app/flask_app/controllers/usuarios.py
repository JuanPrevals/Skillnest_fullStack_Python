"""Rutas de usuarios y relaciones de seguimiento."""

from flask import flash, redirect, render_template, request, url_for
from pymysql.err import IntegrityError

from flask_app import app
from flask_app.models.seguidor import Seguidor
from flask_app.models.usuario import Usuario


@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))


@app.route("/usuarios")
def usuarios():
    return render_template(
        "usuarios.html",
        usuarios=Usuario.get_all(),
        relaciones=Seguidor.get_all(),
    )


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip().lower(),
    }
    campos_validos = all(0 < len(valor) <= 45 for valor in datos.values())
    if not campos_validos or "@" not in datos["email"]:
        flash("Se requieren nombre, apellido y correo válidos.", "danger")
        return redirect(url_for("usuarios"))

    try:
        Usuario.save(datos)
    except IntegrityError:
        flash("El correo ya está registrado.", "warning")
    else:
        flash("Usuario creado correctamente.", "success")
    return redirect(url_for("usuarios"))


@app.route("/seguir", methods=["POST"])
def seguir():
    usuario_id = request.form.get("usuario_id", type=int)
    seguidor_id = request.form.get("seguidor_id", type=int)

    if not usuario_id or not seguidor_id:
        flash("La relación requiere dos usuarios válidos.", "danger")
        return redirect(url_for("usuarios"))

    if usuario_id == seguidor_id:
        flash("El auto-seguimiento no está permitido.", "warning")
        return redirect(url_for("usuarios"))

    if Usuario.get_by_id(usuario_id) is None or Usuario.get_by_id(seguidor_id) is None:
        flash("La relación contiene un usuario inexistente.", "danger")
        return redirect(url_for("usuarios"))

    datos = {"usuario_id": usuario_id, "seguidor_id": seguidor_id}
    if Seguidor.existe(datos):
        flash("La relación de seguimiento ya existe.", "warning")
        return redirect(url_for("usuarios"))

    try:
        Seguidor.seguir(datos)
    except IntegrityError:
        flash("La relación de seguimiento ya existe.", "warning")
    else:
        flash("Relación de seguimiento creada correctamente.", "success")

    return redirect(url_for("usuarios"))
