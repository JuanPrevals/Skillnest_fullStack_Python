from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():

    return """
    <h1>Bienvenido</h1>

    <p>Esta es mi primera página web.</p>
    """
@app.route("/html")
def html():

 return render_template("index.html", nombre="Juan", edad=18, ciudad="Santiago", anio="2026", profesor=False, tecnologias=["Python", "Flask", "Jinja2", "HTML", "CSS", "JavaScript"])

@app.route("/jugador")
def jugador():
    return render_template("jugador.html", jugador="Prevals", puntaje="1000", lider="false" )

@app.route("/macarena")
def macarena():
     return render_template('macarena.html', cancion="dale a tu cuerpo alegría macarena", repite=5)


if __name__ == "__main__":
    app.run(debug=True)
