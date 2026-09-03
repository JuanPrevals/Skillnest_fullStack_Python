import random

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "clave-secreta-adivina-numero"


@app.route("/")
def index():
    if "numero_secreto" not in session:
        session["numero_secreto"] = random.randint(1, 10)

    if "intentos" not in session:
        session["intentos"] = 0

    if "mensaje" not in session:
        session["mensaje"] = "Adivina un número entre 1 y 10."

    if "resultado" not in session:
        session["resultado"] = ""

    return render_template(
        "index.html",
        mensaje=session["mensaje"],
        resultado=session["resultado"],
        intentos=session["intentos"],
    )


@app.route("/adivinar", methods=["POST"])
def adivinar():
    numero = int(request.form["numero"])
    numero_secreto = session["numero_secreto"]
    session["intentos"] += 1

    if numero < numero_secreto:
        session["mensaje"] = f"El número secreto es mayor que {numero}."
        session["resultado"] = "mayor"
    elif numero > numero_secreto:
        session["mensaje"] = f"El número secreto es menor que {numero}."
        session["resultado"] = "menor"
    else:
        session["mensaje"] = f"¡Correcto! El número secreto era {numero_secreto}."
        session["resultado"] = "correcto"

    return redirect(url_for("index"))


@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
