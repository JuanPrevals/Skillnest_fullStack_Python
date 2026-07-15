from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():

    return """
    <h1>Bienvenido</h1>

    <p>Esta es mi primera página web.</p>
    """

@app.route("/macarena")
def macarena():
     return render_template('macarena.html', cancion="dale a tu cuerpo alegría macarena", repite=20)


if __name__ == "__main__":
    app.run(debug=True)
