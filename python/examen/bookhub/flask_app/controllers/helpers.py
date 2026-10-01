from functools import wraps
import secrets

from flask import flash, redirect, request, session, url_for


def login_requerido(funcion):
    @wraps(funcion)
    def decorada(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Inicia sesión para acceder a esa página.", "warning")
            return redirect(url_for("inicio"))
        return funcion(*args, **kwargs)

    return decorada


def csrf_valido():
    token_formulario = request.form.get("csrf_token", "")
    token_sesion = session.get("csrf_token", "")
    return bool(
        token_formulario
        and token_sesion
        and secrets.compare_digest(token_formulario, token_sesion)
    )


def exigir_csrf():
    if not csrf_valido():
        flash("La sesión del formulario expiró. Intenta nuevamente.", "danger")
        return False
    return True
