from flask import flash, redirect, render_template, request, session, url_for
from flask_bcrypt import Bcrypt
from pymysql import MySQLError

from flask_app import app
from flask_app.models.usuario import Usuario


bcrypt = Bcrypt(app)


def obtener_datos_formulario(formulario):
    datos = {
        campo: formulario.get(campo, "").strip()
        for campo in ("nombre", "apellido", "email")
    }
    datos["email"] = datos["email"].lower()
    return datos


def conservar_datos_formulario(datos):
    """Conserva los campos no sensibles; la contraseña nunca va a sesión."""
    session["datos_formulario"] = {
        campo: datos[campo] for campo in ("nombre", "apellido", "email")
    }


@app.get("/")
def index():
    return redirect(url_for("usuarios"))


@app.get("/usuarios")
def usuarios():
    return render_template("index.html", usuarios=Usuario.get_all())


@app.get("/usuarios/nuevo")
def nuevo_usuario():
    datos = session.pop("datos_formulario", {})
    return render_template("nuevo.html", datos=datos)


@app.post("/usuarios/crear")
def crear_usuario():
    datos = obtener_datos_formulario(request.form)
    datos["password"] = request.form.get("password", "")

    if not Usuario.validar_usuario(datos):
        conservar_datos_formulario(datos)
        return redirect(url_for("nuevo_usuario"))

    if Usuario.email_existe(datos["email"]):
        flash("El email ingresado ya está registrado.", "email")
        conservar_datos_formulario(datos)
        return redirect(url_for("nuevo_usuario"))

    datos["password"] = bcrypt.generate_password_hash(
        datos["password"]
    ).decode("utf-8")
    Usuario.save(datos)
    session.pop("datos_formulario", None)
    return redirect(url_for("usuarios"))


@app.get("/login")
def formulario_login():
    if session.get("usuario_id"):
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.post("/login")
def login():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    usuario = Usuario.buscar_por_email(email)

    if (
        usuario is None
        or not usuario.password
        or not bcrypt.check_password_hash(usuario.password, password)
    ):
        flash("Email o contraseña incorrectos.", "login")
        return redirect(url_for("formulario_login"))

    session["usuario_id"] = usuario.id
    return redirect(url_for("dashboard"))


@app.get("/dashboard")
def dashboard():
    usuario_id = session.get("usuario_id")
    if not usuario_id:
        flash("Debes iniciar sesión.", "login")
        return redirect(url_for("formulario_login"))

    usuario = Usuario.get_by_id(usuario_id)
    if usuario is None:
        session.clear()
        flash("La sesión ya no es válida.", "login")
        return redirect(url_for("formulario_login"))

    return render_template("dashboard.html", usuario=usuario)


@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("formulario_login"))


@app.get("/usuarios/<int:id>")
def ver_usuario(id):
    usuario = Usuario.get_by_id(id)
    if usuario is None:
        return "Usuario no encontrado", 404
    return render_template("detalle.html", usuario=usuario)


@app.get("/usuarios/editar/<int:id>")
def editar_usuario(id):
    usuario = Usuario.get_by_id(id)
    if usuario is None:
        return "Usuario no encontrado", 404

    datos = {
        "nombre": usuario.nombre,
        "apellido": usuario.apellido,
        "email": usuario.email,
    }
    return render_template("editar.html", usuario=usuario, datos=datos)


@app.post("/usuarios/<int:id>/actualizar")
def actualizar_usuario(id):
    usuario = Usuario.get_by_id(id)
    if usuario is None:
        return "Usuario no encontrado", 404

    datos = obtener_datos_formulario(request.form)
    if not Usuario.validar_usuario(datos):
        return render_template("editar.html", usuario=usuario, datos=datos), 400

    if Usuario.email_existe(datos["email"], excluir_id=id):
        flash("El email ingresado ya está registrado.", "email")
        return render_template("editar.html", usuario=usuario, datos=datos), 400

    Usuario.update({"id": id, **datos})
    return redirect(url_for("usuarios"))


@app.get("/usuarios/borrar/<int:id>")
def borrar_usuario(id):
    Usuario.delete(id)
    return redirect(url_for("usuarios"))


@app.errorhandler(MySQLError)
def error_mysql(error):
    app.logger.exception("No se pudo completar la operación en MySQL.")
    mensaje = (
        "No se pudo completar la operación. Revisa la conexión y el esquema "
        "de MySQL e intenta nuevamente."
    )

    if request.endpoint == "crear_usuario":
        session["datos_formulario"] = obtener_datos_formulario(request.form)
        flash(mensaje, "general")
        return redirect(url_for("nuevo_usuario"))

    return render_template("index.html", usuarios=[], error=mensaje), 503
