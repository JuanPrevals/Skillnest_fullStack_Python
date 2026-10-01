import os
import secrets
from datetime import date

from dotenv import load_dotenv
from flask import Flask, render_template, session
from flask_bcrypt import Bcrypt


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or secrets.token_hex(32)
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.getenv("SESSION_COOKIE_SECURE", "0") == "1",
)
bcrypt = Bcrypt(app)


@app.context_processor
def inject_csrf_token():
    """Entrega un token CSRF estable por sesión a todos los formularios."""
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(32)
    return {"csrf_token": session["csrf_token"], "today": date.today().isoformat()}


@app.errorhandler(404)
def pagina_no_encontrada(_error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def error_interno(_error):
    return render_template("errors/500.html"), 500


from flask_app.controllers import libros, usuarios  # noqa: E402, F401
