import re

from flask import Flask, redirect, render_template, request, url_for
from pymysql import MySQLError

from estudiante import Estudiante

app = Flask(__name__)


def validar_estudiante(formulario):
    datos = {
        campo: formulario.get(campo, "").strip()
        for campo in ("nombre", "email")
    }
    errores = []

    if not datos["nombre"] or len(datos["nombre"]) > 100:
        errores.append("El nombre debe tener entre 1 y 100 caracteres.")
    if not datos["email"] or len(datos["email"]) > 100:
        errores.append("El e-mail debe tener entre 1 y 100 caracteres.")
    elif not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", datos["email"]):
        errores.append("Ingresa un e-mail válido.")

    return datos, errores


@app.get("/")
def index():
    return redirect(url_for("estudiantes"))


@app.get("/estudiantes")
def estudiantes():
    return render_template("estudiantes.html", estudiantes=Estudiante.get_all())


@app.get("/estudiantes/ver/<int:id_estudiante>")
def ver_estudiante(id_estudiante):
    estudiante = Estudiante.get_by_id(id_estudiante)
    if estudiante is None:
        return "Estudiante no encontrado", 404
    return render_template("estudiante_ver.html", estudiante=estudiante)


@app.get("/estudiantes/editar/<int:id_estudiante>")
def editar_estudiante(id_estudiante):
    estudiante = Estudiante.get_by_id(id_estudiante)
    if estudiante is None:
        return "Estudiante no encontrado", 404
    datos = {"nombre": estudiante.nombre, "email": estudiante.email}
    return render_template(
        "estudiante_editar.html",
        estudiante=estudiante,
        datos=datos,
        errores=[],
    )


@app.post("/actualizar_estudiante")
def actualizar_estudiante():
    id_texto = request.form.get("id_estudiante", "")
    if not id_texto.isdigit():
        return "ID de estudiante inválido", 400

    id_estudiante = int(id_texto)
    estudiante = Estudiante.get_by_id(id_estudiante)
    if estudiante is None:
        return "Estudiante no encontrado", 404

    datos, errores = validar_estudiante(request.form)
    if errores:
        return render_template(
            "estudiante_editar.html",
            estudiante=estudiante,
            datos=datos,
            errores=errores,
        ), 400

    Estudiante.actualizar({"id_estudiante": id_estudiante, **datos})
    return redirect(url_for("estudiantes"))


@app.post("/eliminar_estudiante/<int:id_estudiante>")
def eliminar_estudiante(id_estudiante):
    estudiante = Estudiante.get_by_id(id_estudiante)
    if estudiante is None:
        return "Estudiante no encontrado", 404
    Estudiante.eliminar({"id_estudiante": id_estudiante})
    return redirect(url_for("estudiantes"))


@app.errorhandler(MySQLError)
def error_mysql(error):
    app.logger.exception("No se pudo completar la operación en MySQL.")
    return render_template("error.html"), 503


if __name__ == "__main__":
    app.run()

