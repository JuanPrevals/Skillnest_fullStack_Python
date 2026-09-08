from flask import Flask, redirect, render_template, request, url_for
from pymysql import MySQLError

from mascota import Mascota

app = Flask(__name__)


@app.errorhandler(MySQLError)
def error_mysql(error):
    app.logger.error("No se pudo consultar MySQL: %s", error)
    return render_template(
        "index.html", todas_mascotas=[],
        error_db="No se pudo conectar con la base de datos. Revisa la configuración de MySQL.",
        datos=request.form,
    ), 503


@app.route("/")
def index():
    mascotas = Mascota.get_all()
    print(mascotas)
    return render_template("index.html", todas_mascotas=mascotas)


@app.route("/mascotas/perros")
def perros():
    mascotas = Mascota.get_by_tipo("Perro")
    return render_template("index.html", todas_mascotas=mascotas, solo_perros=True)


@app.route("/mascotas", methods=["POST"])
def crear_mascota():
    datos = {campo: request.form.get(campo, "").strip()
             for campo in ("nombre", "tipo", "color")}
    if any(not valor or len(valor) > 100 for valor in datos.values()):
        return render_template(
            "index.html", todas_mascotas=Mascota.get_all(), datos=datos,
            error="Completa todos los campos con entre 1 y 100 caracteres.",
        ), 400
    Mascota.save(datos)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
