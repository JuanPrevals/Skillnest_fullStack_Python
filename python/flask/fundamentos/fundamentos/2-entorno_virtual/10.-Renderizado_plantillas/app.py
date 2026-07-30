from flask import Flask, render_template

app = Flask(__name__)

@app.route("/listas")
def renderizar_listas():

    # Lista de números

    numeros = [7, 15, 22]

    # Lista de diccionarios

    listado_estudiantes = [

        {
            "nombre":"Florencia",
            "edad":25
        },

        {
            "nombre":"Valentina",
            "edad":30
        },

        {
            "nombre":"José",
            "edad":27
        },

        {
            "nombre":"Patricio",
            "edad":21
        }

    ]

    return render_template(

        "listas.html",

        numeros=numeros,

        estudiantes=listado_estudiantes

    )


@app.route("/videojuegos")
def mostrar_videojuegos():
    listado_videojuegos = [
        {
            "nombre": "Minecraft",
            "plataforma": "PC",
            "anio": 2011
        },
        {
            "nombre": "Call Of Duty: Modern Warfare 4",
            "plataforma": "PC",
            "anio": 2026
        },
        {
            "nombre": "The Last of Us Part II",
            "plataforma": "PlayStation 4",
            "anio": 2020
        },
        {
            "nombre": "Halo Infinite",
            "plataforma": "Xbox Series X/S",
            "anio": 2021
        },
        {
            "nombre": "Stardew Valley",
            "plataforma": "PC",
            "anio": 2016
        },
        {
            "nombre": "Resident Evil Requiem",
            "plataforma": "PlayStation 5",
            "anio": 2026
        }
    ]

    return render_template(
        "videojuegos.html",
        videojuegos=listado_videojuegos
    )


if __name__ == "__main__":
    app.run(debug=True)
