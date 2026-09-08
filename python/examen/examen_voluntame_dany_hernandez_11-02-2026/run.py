from flask_app import app

# Importación de controladores
from flask_app.controllers.controlador_usuarios import usuarios_bp
from flask_app.controllers.controlador_misiones import misiones_bp

# Registro de BluePrints
app.register_blueprint(usuarios_bp)
app.register_blueprint(misiones_bp)

if __name__ == "__main__":
    app.run(debug=True)