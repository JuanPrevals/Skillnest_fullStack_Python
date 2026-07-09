from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Bienvenido al curso de Flask!"


@app.route("/contacto")
def conctacto():
    return "<h1>Pestaña de contactos</h1> <p>Estos son los contactos</p>"


@app.route("/exito")
def exito():
    return "Exito!"

if __name__ == "__main__":
    app.run(debug=True)