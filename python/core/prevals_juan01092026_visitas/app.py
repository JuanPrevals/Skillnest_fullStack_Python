"""Aplicación Flask para practicar el manejo de datos en sesión."""

import os

from flask import Flask, flash, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "clave-local-solo-desarrollo")


def redirigir_sin_contar():
    """Redirige al inicio sin considerar la redirección como una nueva visita."""
    session["omitir_siguiente_visita"] = True
    return redirect(url_for("inicio"))


@app.route("/")
def inicio():
    """Inicializa el contador y registra cada visita directa a la página."""
    if "visitas" in session:
        if session.pop("omitir_siguiente_visita", False):
            pass
        else:
            session["visitas"] += 1
    else:
        session["visitas"] = 1

    if "reinicios" not in session:
        session["reinicios"] = 0

    return render_template(
        "index.html",
        visitas=session["visitas"],
        reinicios=session["reinicios"],
    )


@app.route("/aumentar-dos", methods=["POST"])
def aumentar_dos():
    """Aumenta el contador de visitas en dos."""
    session["visitas"] = session.get("visitas", 0) + 2
    return redirigir_sin_contar()


@app.route("/aumentar", methods=["POST"])
def aumentar():
    """Aumenta las visitas según el entero positivo enviado por formulario."""
    cantidad = request.form.get("cantidad", "").strip()

    try:
        incremento = int(cantidad)
        if incremento <= 0:
            raise ValueError
    except ValueError:
        flash("Ingresa un número entero mayor que cero.", "error")
        return redirigir_sin_contar()

    session["visitas"] = session.get("visitas", 0) + incremento
    flash(f"Se agregaron {incremento} visitas.", "success")
    return redirigir_sin_contar()


@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    """Reinicia las visitas y registra cuántas veces se realizó la acción."""
    session["visitas"] = 0
    session["reinicios"] = session.get("reinicios", 0) + 1
    flash("El contador de visitas fue reiniciado.", "success")
    return redirigir_sin_contar()


@app.route("/destruir_sesion")
def destruir_sesion():
    """Elimina todos los datos de sesión y redirige al inicio."""
    session.clear()
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
