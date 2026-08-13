"""Aplicación de ejemplo del patrón POST -> Redirect -> GET."""

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route("/")
def index():
    """Muestra el formulario para registrar un producto."""
    return render_template("index.html")


@app.route("/registrar", methods=["POST"])
def registrar():
    """Procesa los datos del formulario y redirige a una ruta GET."""
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    print("============================")
    print("Producto recibido")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Categoría: {categoria}")
    print("============================")

    return redirect(url_for("resultado"))


@app.route("/resultado")
def resultado():
    """Muestra la confirmación luego de la redirección."""
    print("Producto registrado; el usuario fue redirigido.")
    print(f"Datos disponibles en request.form: {request.form}")
    return render_template("resultado.html")


@app.route("/ayuda")
def ayuda():
    """Explica los métodos HTTP y el patrón PRG usado en el ejercicio."""
    return render_template("ayuda.html")


if __name__ == "__main__":
    app.run(debug=True)
