"""Rutas del formulario y listado de inscripciones."""

from flask import flash, redirect, render_template, request, url_for
from pymysql.err import IntegrityError

from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante
from flask_app.models.inscripcion import Inscripcion


@app.route("/")
def index():
    return render_template(
        "index.html",
        estudiantes=Estudiante.get_all(),
        cursos=Curso.get_all(),
        inscripciones=Inscripcion.get_all(),
    )


@app.route("/inscribir", methods=["POST"])
def inscribir():
    estudiante_id = request.form.get("estudiante_id", type=int)
    curso_id = request.form.get("curso_id", type=int)

    if not estudiante_id or not curso_id:
        flash("Se requieren un estudiante y un curso válidos.", "danger")
        return redirect(url_for("index"))

    if Estudiante.get_by_id(estudiante_id) is None:
        flash("El estudiante seleccionado no existe.", "danger")
        return redirect(url_for("index"))

    if Curso.get_by_id(curso_id) is None:
        flash("El curso seleccionado no existe.", "danger")
        return redirect(url_for("index"))

    datos = {"estudiante_id": estudiante_id, "curso_id": curso_id}
    if Inscripcion.existe(datos):
        flash("El estudiante ya está inscrito en este curso.", "warning")
        return redirect(url_for("index"))

    try:
        Inscripcion.inscribir_estudiante_en_curso(datos)
    except IntegrityError:
        # La PK compuesta también protege ante dos solicitudes simultáneas.
        flash("El estudiante ya está inscrito en este curso.", "warning")
    else:
        flash("Inscripción realizada correctamente.", "success")

    return redirect(url_for("index"))
