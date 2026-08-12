from flask import Flask, render_template, request


app = Flask(__name__)

frutas = [
    {"id": "manzana", "nombre": "Manzana", "precio": 2.5, "imagen": "manzana.png"},
    {"id": "platano", "nombre": "Plátano", "precio": 1.8, "imagen": "platano.png"},
    {"id": "naranja", "nombre": "Naranja", "precio": 3.0, "imagen": "naranja.png"},
    {"id": "fresa", "nombre": "Fresa", "precio": 4.5, "imagen": "fresa.png"},
    {"id": "uva", "nombre": "Uva", "precio": 3.8, "imagen": "uva.png"},
    {"id": "pina", "nombre": "Piña", "precio": 5.0, "imagen": "pina.png"},
    {"id": "sandia", "nombre": "Sandía", "precio": 4.2, "imagen": "sandia.png"},
    {"id": "mango", "nombre": "Mango", "precio": 3.5, "imagen": "mango.png"},
]


@app.route("/")
def index():
    return render_template("index.html", frutas=frutas)


@app.route("/frutas")
def catalogo():
    return render_template("frutas.html", frutas=frutas)


@app.route("/checkout", methods=["POST"])
def checkout():
    nombre = request.form["nombre"]
    email = request.form["email"]
    direccion = request.form["direccion"]
    orden = []
    total_frutas = 0
    total_pagar = 0

    for fruta in frutas:
        cantidad = int(request.form[fruta["id"]])

        if cantidad > 0:
            subtotal = cantidad * fruta["precio"]
            orden.append({**fruta, "cantidad": cantidad, "subtotal": subtotal})
            total_frutas += cantidad
            total_pagar += subtotal

    return render_template(
        "checkout.html",
        nombre=nombre,
        email=email,
        direccion=direccion,
        orden=orden,
        total_frutas=total_frutas,
        total_pagar=total_pagar,
    )


if __name__ == "__main__":
    app.run(debug=True)
