"""Rutas de usuarios, canciones y favoritos."""

from flask import flash, redirect, render_template, request, url_for
from pymysql.err import IntegrityError

from flask_app import app
from flask_app.models.cancion import Cancion
from flask_app.models.favorito import Favorito
from flask_app.models.usuario import Usuario


@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))


@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", usuarios=Usuario.get_all())


@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "email": request.form.get("email", "").strip().lower(),
        "contrasena": request.form.get("contrasena", ""),
    }
    campos_validos = all(0 < len(valor) <= 45 for valor in datos.values())
    if not campos_validos or "@" not in datos["email"]:
        flash("Se requieren nombre, correo y contraseña válidos.", "danger")
        return redirect(url_for("usuarios"))

    try:
        Usuario.save(datos)
    except IntegrityError:
        flash("El correo ya está registrado.", "warning")
    else:
        flash("Usuario creado correctamente.", "success")
    return redirect(url_for("usuarios"))


@app.route("/usuarios/<int:usuario_id>")
def mostrar_usuario(usuario_id):
    usuario = Usuario.get_by_id_with_favorites({"id": usuario_id})
    if usuario is None:
        return render_template("404.html"), 404

    canciones_disponibles = Cancion.get_not_favorited_by_user(
        {"usuario_id": usuario_id}
    )
    return render_template(
        "mostrar_usuario.html",
        usuario=usuario,
        canciones=canciones_disponibles,
    )


@app.route("/canciones")
def canciones():
    return render_template("canciones.html", canciones=Cancion.get_all())


@app.route("/canciones/crear", methods=["POST"])
def crear_cancion():
    datos = {
        "titulo": request.form.get("titulo", "").strip(),
        "artista": request.form.get("artista", "").strip(),
    }
    if not all(0 < len(valor) <= 45 for valor in datos.values()):
        flash("Se requieren título y artista válidos.", "danger")
        return redirect(url_for("canciones"))

    try:
        Cancion.save(datos)
    except IntegrityError:
        flash("La canción ya está registrada para ese artista.", "warning")
    else:
        flash("Canción creada correctamente.", "success")
    return redirect(url_for("canciones"))


@app.route("/canciones/<int:cancion_id>")
def mostrar_cancion(cancion_id):
    cancion = Cancion.get_by_id_with_users({"id": cancion_id})
    if cancion is None:
        return render_template("404.html"), 404

    usuarios_disponibles = Cancion.get_users_not_favorited(
        {"cancion_id": cancion_id}
    )
    return render_template(
        "mostrar_cancion.html",
        cancion=cancion,
        usuarios=usuarios_disponibles,
    )


@app.route("/favoritos/agregar", methods=["POST"])
def agregar_favorito():
    usuario_id = request.form.get("usuario_id", type=int)
    cancion_id = request.form.get("cancion_id", type=int)
    origen = request.form.get("origen", "usuario")

    if not usuario_id or not cancion_id:
        flash("La relación requiere un usuario y una canción válidos.", "danger")
        return redirect(url_for("usuarios"))

    usuario = Usuario.get_by_id(usuario_id)
    cancion = Cancion.get_by_id(cancion_id)
    if usuario is None or cancion is None:
        flash("La relación contiene una entidad inexistente.", "danger")
        return redirect(url_for("usuarios"))

    datos = {"usuario_id": usuario_id, "cancion_id": cancion_id}
    if Favorito.existe(datos):
        flash("La canción ya figura entre los favoritos del usuario.", "warning")
    else:
        try:
            Favorito.agregar(datos)
        except IntegrityError:
            flash("La canción ya figura entre los favoritos del usuario.", "warning")
        else:
            flash("Favorito agregado correctamente.", "success")

    if origen == "cancion":
        return redirect(url_for("mostrar_cancion", cancion_id=cancion_id))
    return redirect(url_for("mostrar_usuario", usuario_id=usuario_id))


@app.errorhandler(404)
def pagina_no_encontrada(_error):
    return render_template("404.html"), 404
