from flask import Flask, render_template

from mascota import Mascota
from usuario import Usuario

app = Flask(__name__)


@app.route("/")
def index():
    mascotas = Mascota.get_all()
    print(mascotas)
    return render_template("index.html", mascotas=mascotas)


@app.route("/usuarios")
def usuarios():
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=usuarios)


if __name__ == "__main__":
    app.run(debug=True)
