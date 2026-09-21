import re

from flask import Flask, redirect, render_template, request, url_for
from pymysql import MySQLError

from usuario import Usuario

app = Flask(__name__)


@app.get("/")
def index():
    return redirect(url_for("usuarios"))


@app.get("/usuarios")
def usuarios():
    return render_template("usuarios.html", usuarios=Usuario.get_all())


@app.get("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("usuario_nuevo.html", datos={}, errores=[])


@app.post("/usuarios/crear")
def crear_usuario():
    datos = {campo: request.form.get(campo, "").strip()
             for campo in ("nombre", "apellido", "email")}
    errores = []
    for campo, valor in datos.items():
        if not valor or len(valor) > 45:
            errores.append(f"El campo {campo} debe tener entre 1 y 45 caracteres.")
    if datos["email"] and not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", datos["email"]):
        errores.append("Ingresa un e-mail válido.")
    if errores:
        return render_template("usuario_nuevo.html", datos=datos, errores=errores), 400
    Usuario.save(datos)
    return redirect(url_for("usuarios"))


@app.errorhandler(MySQLError)
def error_mysql(error):
    app.logger.exception("No se pudo completar la operación en MySQL.")
    mensaje = "No se pudo completar la operación. Revisa la conexión y el esquema de MySQL e intenta nuevamente."
    if request.endpoint == "crear_usuario":
        return render_template("usuario_nuevo.html", datos=request.form, errores=[mensaje]), 503
    return render_template("usuarios.html", usuarios=[], error=mensaje), 503


if __name__ == "__main__":
    app.run()
