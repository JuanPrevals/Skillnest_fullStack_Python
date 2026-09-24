"""Punto de entrada de la aplicación."""

from flask_app import app
from flask_app.controllers import inscripciones  # noqa: F401


if __name__ == "__main__":
    app.run(debug=True)
