from flask import flash, redirect, render_template, request, url_for
from pymysql import MySQLError

from flask_app import app
from flask_app.models.curso import Curso


@app.get("/")
def inicio():
    return redirect(url_for("cursos"))


@app.get("/cursos")
def cursos():
    return render_template("cursos.html", cursos=Curso.obtener_todos())


@app.post("/cursos/crear")
def crear_curso():
    nombre = request.form.get("nombre", "").strip()
    if len(nombre) < 2:
        flash("El nombre del curso debe tener al menos 2 caracteres.", "error")
    elif len(nombre) > 45:
        flash("El nombre del curso no puede superar los 45 caracteres.", "error")
    elif Curso.nombre_existe(nombre):
        flash("Ese curso ya se encuentra registrado.", "error")
    else:
        Curso.guardar({"nombre": nombre})
        flash("Curso creado correctamente.", "exito")
    return redirect(url_for("cursos"))


@app.get("/cursos/<int:curso_id>")
def mostrar_curso(curso_id):
    curso = Curso.obtener_con_estudiantes(curso_id)
    if curso is None:
        flash("El curso solicitado no existe.", "error")
        return redirect(url_for("cursos"))
    return render_template("mostrar_curso.html", curso=curso)


@app.errorhandler(MySQLError)
def error_mysql(error):
    app.logger.exception("Error al comunicarse con MySQL.")
    flash("No fue posible completar la operación en MySQL.", "error")
    return redirect(url_for("cursos"))
