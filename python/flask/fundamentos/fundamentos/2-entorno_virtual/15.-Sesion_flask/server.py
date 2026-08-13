"""Ejemplo de persistencia entre solicitudes mediante sesiones de Flask."""

import os

from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)

# En producción, la clave debe configurarse mediante una variable de entorno.
# El valor alternativo se utiliza únicamente para ejecutar este ejercicio local.
app.secret_key = 'poppy'


@app.route("/")
def index():
    """Muestra el formulario de creación de usuario."""
    return render_template("index.html")


@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    """Recibe el formulario, almacena sus datos en sesión y redirige."""
    nombre = request.form["nombre"]
    email = request.form["email"]
    ciudad = request.form["ciudad"]

    session["nombre_usuario"] = nombre
    session["email_usuario"] = email
    session["ciudad_usuario"] = ciudad

    print("===================================")
    print("Información recibida y guardada en sesión")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Ciudad: {ciudad}")
    print("===================================")

    return redirect(url_for("mostrar_usuario"))


def hay_usuario_en_sesion():
    """Indica si la sesión contiene todos los datos requeridos."""
    return all(
        clave in session
        for clave in ("nombre_usuario", "email_usuario", "ciudad_usuario")
    )


@app.route("/mostrar_usuario")
def mostrar_usuario():
    """Muestra los datos conservados después de la redirección."""
    if not hay_usuario_en_sesion():
        return redirect(url_for("index"))

    print("===================================")
    print("Usuario redirigido")
    print(f"Nombre: {session['nombre_usuario']}")
    print(f"Email: {session['email_usuario']}")
    print(f"Ciudad: {session['ciudad_usuario']}")
    print("===================================")

    return render_template("mostrar.html")


@app.route("/perfil")
def perfil():
    """Presenta un perfil usando exclusivamente los datos de la sesión."""
    if not hay_usuario_en_sesion():
        return redirect(url_for("index"))

    return render_template("perfil.html")


if __name__ == "__main__":
    app.run(debug=True)
