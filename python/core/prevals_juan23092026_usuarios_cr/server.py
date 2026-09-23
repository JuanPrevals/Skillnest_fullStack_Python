from python.core.usuarios_cr.flask_app import app
from python.core.usuarios_cr.flask_app.controllers import usuarios  # noqa: F401


if __name__ == "__main__":
    app.run(debug=True)
