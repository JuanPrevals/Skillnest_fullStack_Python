from flask import Flask, abort, redirect, render_template, request

from mascota import Mascota
from usuario import Usuario

app = Flask(__name__)


@app.route("/")
def index():
    mascotas = Mascota.get_all()
    print(mascotas)
    return render_template("index.html", mascotas=mascotas)


@app.route("/crear_mascota", methods=["POST"])
def crear_mascota():
    datos = {
        "nombre": request.form["nombre"],
        "tipo": request.form["tipo"],
        "color": request.form["color"],
    }
    if Mascota.save(datos) is False:
        abort(500, description="No se pudo guardar la mascota.")
    return redirect("/")


@app.route("/usuarios")
def usuarios():
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=usuarios)


if __name__ == "__main__":
    app.run(debug=True)
