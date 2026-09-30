import re

from flask import flash, redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante


NOMBRE_REGEX = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+(?:[ '-][A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)*$")


@app.get("/estudiantes/nuevo")
def nuevo_estudiante():
    return render_template("nuevo_estudiante.html", cursos=Curso.obtener_todos())


@app.post("/estudiantes/crear")
def crear_estudiante():
    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "edad": request.form.get("edad", type=int),
        "curso_id": request.form.get("curso_id", type=int),
    }
    es_valido = True

    for campo, etiqueta in (("nombre", "nombre"), ("apellido", "apellido")):
        valor = datos[campo]
        if len(valor) < 2 or len(valor) > 45 or not NOMBRE_REGEX.fullmatch(valor):
            flash(f"Ingresa un {etiqueta} válido.", "error")
            es_valido = False

    if datos["edad"] is None or not 1 <= datos["edad"] <= 120:
        flash("La edad debe estar entre 1 y 120 años.", "error")
        es_valido = False

    if datos["curso_id"] is None or Curso.obtener_por_id(datos["curso_id"]) is None:
        flash("Selecciona un curso válido.", "error")
        es_valido = False

    if not es_valido:
        return redirect(url_for("nuevo_estudiante"))

    Estudiante.guardar(datos)
    flash("Estudiante creado correctamente.", "exito")
    return redirect(url_for("cursos"))
