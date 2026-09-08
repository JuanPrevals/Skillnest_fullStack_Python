from flask import Flask, render_template

from mascota import Mascota

app = Flask(__name__)


@app.route("/")
def index():
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)


@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    mascota = Mascota.get_by_id(id)
    if mascota is None:
        return "Mascota no encontrada", 404
    return render_template("mascota.html", mascota=mascota)


@app.route("/mascota/nombre/<nombre>")
def buscar_por_nombre(nombre):
    mascota = Mascota.get_by_name(nombre)
    if mascota is None:
        return "Mascota no encontrada", 404
    return render_template("mascota.html", mascota=mascota)


if __name__ == "__main__":
    app.run(debug=True)
