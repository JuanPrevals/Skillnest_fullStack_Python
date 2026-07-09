from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Bienvenido a Flask"


@app.route("/exito")
def exito():
    return "Exito!"


@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola {nombre}!"


@app.route("/color/<nombre>/<color>")
def color_favorito(nombre, color):
    return f"Hola {nombre}, tu color favorito es {color}."


@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):
    return (f"Hola {nombre}!<br>") * veces


@app.route("/despedida/<nombre>")
def despedida(nombre):
    return f"Hasta luego {nombre}! Esperamos verte pronto!"


@app.route("/presentacion/<nombre>/<int:edad>")
def presentacion(nombre, edad):
    return f"Hola {nombre}, tienes {edad} anos."


@app.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    return f"La suma es: {a + b}"


@app.route("/multiplicar/<int:a>/<int:b>")
def multiplicar(a, b):
    return f"El resultado es: {a * b}"


@app.route("/paridad/<int:numero>")
def paridad(numero):
    if numero % 2 == 0:
        return f"El numero {numero} es PAR."
    return f"El numero {numero} es IMPAR."


if __name__ == "__main__":
    app.run(debug=True)
