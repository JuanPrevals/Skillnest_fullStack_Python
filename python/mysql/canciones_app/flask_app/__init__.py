"""Inicialización compartida de Flask."""

import os

from flask import Flask


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "clave-local")
