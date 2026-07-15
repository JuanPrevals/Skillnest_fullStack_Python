from flask import Flask, render_template

app = Flask(__name__)


# Datos de jugadores con sus puntajes
jugadores = [
    {"nombre": "AlexGamer", "puntaje": 5000},
    {"nombre": "PixelMaster", "puntaje": 7500},
    {"nombre": "ShadowNinja", "puntaje": 8200},
    {"nombre": "CyberWarrior", "puntaje": 9100},
    {"nombre": "UltraNoob", "puntaje": 3000},
]

ranking = sorted(jugadores, key=lambda jugador: jugador["puntaje"], reverse=True)


# Ruta para mostrar el ranking completo

@app.route("/ranking")
def ranking_completo():
    return render_template("ranking.html", jugadores=ranking)


# Ruta para mostrar un número limitado de jugadores

@app.route("/ranking/<int:limite>")
def ranking_limite(limite):
    return render_template(
        "ranking.html",
        jugadores=ranking[:limite],
    )

# Ruta para personalizar el color de fondo del ranking

@app.route("/ranking/<int:limite>/<color>")
def ranking_color(limite, color):
    return render_template(
        "ranking.html",
        jugadores=ranking[:limite],
        color=color,
    )

if __name__ == "__main__":
    app.run(debug=True)
