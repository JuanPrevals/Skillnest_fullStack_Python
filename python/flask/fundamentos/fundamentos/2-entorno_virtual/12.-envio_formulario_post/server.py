"""
===========================================
Formulario de Prueba
===========================================

En esta aplicación aprenderemos cómo
recibir información enviada desde un
formulario HTML utilizando solicitudes POST.
"""

# ==========================================
# Importaciones
# ==========================================

from flask import (

    Flask,

    render_template,

    request,

    redirect

)

# ==========================================
# Crear aplicación Flask
# ==========================================

app = Flask(__name__)

# ==========================================
# Ruta principal
# ==========================================

@app.route("/")
def index():

    return render_template("index.html")


# ==========================================
# Procesar formulario
# ==========================================

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():

    print("========== NUEVO USUARIO ==========")

    print(request.form)

    print("-----------------------------------")

    print("Nombre:", request.form["nombre"])

    print("Correo:", request.form["email"])
    
    print("Edad:", request.form["edad"])

    print("Ciudad:", request.form["ciudad"])

    print("===================================")

    # Nunca renderizamos una plantilla
    # directamente desde una solicitud POST.

    return redirect("/")


# ==========================================
# Ejecutar servidor
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)