"""Punto de entrada de la aplicación."""

from flask_app import app
from flask_app.controllers import tacos  # noqa: F401  Registra las rutas.


if __name__ == "__main__":
    app.run(debug=True)

