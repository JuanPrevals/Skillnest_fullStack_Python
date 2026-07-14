from flask import Flask
app = Flask(__name__)

# Ruta raíz - Página de inicio

@app.route("/")
def inicio():
    return "Bienvenido a casa, esta es la página de inicio de Flask!"

# Ruta genérica para explorar enrutamiento

@app.route("/explorar")
def exito():
    return "Aqui tienes una lista de las rutas para que pruebes: /saludo/nombre por ejemplo  "

# Rutas dinámicas para personalización

@app.route("/perfil/<nombre>")
def perfil(nombre):
    return f"Hola {nombre}!"

# Ruta que repite un mensaje varias veces

@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):
    return (f"Hola {nombre}!<br>") * veces

# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "⚠️ ¡Sobrecarga de rutas! No encontramos a dónde quieres ir, inténtalo de nuevo.", 404

# Ejecuta el servidor
if __name__ == "__main__":
   app.run(debug=True)
   
   
from flask import Flask

app = Flask(__name__)







