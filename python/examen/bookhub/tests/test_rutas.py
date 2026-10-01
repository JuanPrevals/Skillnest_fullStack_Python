from types import SimpleNamespace

import pytest

from flask_app import app, bcrypt
from flask_app.models.favorito import Favorito
from flask_app.models.libro import Libro
from flask_app.models.usuario import Usuario


@pytest.fixture()
def cliente():
    app.config.update(TESTING=True, SECRET_KEY="testing-secret")
    with app.test_client() as cliente:
        yield cliente


def autenticar_sesion(cliente, usuario_id=1):
    with cliente.session_transaction() as sesion:
        sesion["usuario_id"] = usuario_id
        sesion["usuario_nombre"] = "Ana"
        sesion["csrf_token"] = "token-seguro"


def libro_falso(usuario_id=1, **cambios):
    base = dict(
        id=5,
        titulo="Cien años de soledad",
        autor="Gabriel García Márquez",
        genero="Novela",
        fecha_publicacion=__import__("datetime").date(1967, 6, 5),
        descripcion="Una descripción suficientemente extensa.",
        usuario_id=usuario_id,
        publicado_por="Ana Pérez",
        total_favoritos=2,
        es_favorito=False,
    )
    base.update(cambios)
    return SimpleNamespace(**base)


def test_ruta_privada_redirige_a_inicio(cliente):
    respuesta = cliente.get("/libros")
    assert respuesta.status_code == 302
    assert respuesta.headers["Location"].endswith("/")


def test_dashboard_autenticado_renderiza_datos(cliente, monkeypatch):
    autenticar_sesion(cliente)
    monkeypatch.setattr(Libro, "obtener_del_usuario", lambda _id: [libro_falso()])
    monkeypatch.setattr(Libro, "obtener_comunidad", lambda _id, limite=None: [])
    respuesta = cliente.get("/libros")
    assert respuesta.status_code == 200
    assert "Cien años de soledad".encode() in respuesta.data


def test_formulario_nuevo_renderiza_catalogo_de_generos(cliente):
    autenticar_sesion(cliente)
    respuesta = cliente.get("/libros/nuevo")
    assert respuesta.status_code == 200
    assert "Ciencia ficci".encode() in respuesta.data


def test_detalle_renderiza_relaciones(cliente, monkeypatch):
    autenticar_sesion(cliente)
    monkeypatch.setattr(Libro, "obtener_por_id", lambda _libro, _usuario: libro_falso())
    monkeypatch.setattr(
        Favorito,
        "usuarios_del_libro",
        lambda _libro: [{"nombre": "Carlos", "apellido": "Ruiz"}],
    )
    respuesta = cliente.get("/libros/5")
    assert respuesta.status_code == 200
    assert b"Carlos Ruiz" in respuesta.data


def test_explorar_renderiza_busqueda(cliente, monkeypatch):
    autenticar_sesion(cliente)
    recibido = {}

    def falso_explorar(usuario_id, termino, genero):
        recibido.update(usuario_id=usuario_id, termino=termino, genero=genero)
        return [libro_falso(usuario_id=2)]

    monkeypatch.setattr(Libro, "explorar", falso_explorar)
    respuesta = cliente.get("/explorar?q=soledad&genero=Novela")
    assert respuesta.status_code == 200
    assert recibido == {"usuario_id": 1, "termino": "soledad", "genero": "Novela"}


def test_favoritos_renderiza_lista(cliente, monkeypatch):
    autenticar_sesion(cliente)
    monkeypatch.setattr(Favorito, "del_usuario", lambda _id: [libro_falso(usuario_id=2)])
    respuesta = cliente.get("/favoritos")
    assert respuesta.status_code == 200
    assert "Mis libros favoritos".encode() in respuesta.data


def test_edicion_de_otro_usuario_es_bloqueada(cliente, monkeypatch):
    autenticar_sesion(cliente, usuario_id=1)
    monkeypatch.setattr(Libro, "obtener_por_id", lambda _libro, _usuario: libro_falso(usuario_id=99))
    respuesta = cliente.get("/libros/editar/5")
    assert respuesta.status_code == 302
    assert respuesta.headers["Location"].endswith("/libros/5")


def test_eliminacion_de_otro_usuario_no_ejecuta_modelo(cliente, monkeypatch):
    autenticar_sesion(cliente, usuario_id=1)
    monkeypatch.setattr(Libro, "obtener_por_id", lambda _libro, _usuario: libro_falso(usuario_id=99))
    llamado = {"eliminar": False}

    def falso_eliminar(*_args):
        llamado["eliminar"] = True

    monkeypatch.setattr(Libro, "eliminar", falso_eliminar)
    respuesta = cliente.post("/libros/eliminar/5", data={"csrf_token": "token-seguro"})
    assert respuesta.status_code == 302
    assert llamado["eliminar"] is False


def test_post_sin_csrf_no_crea_libro(cliente, monkeypatch):
    autenticar_sesion(cliente)
    llamado = {"crear": False}
    monkeypatch.setattr(Libro, "crear", lambda _datos: llamado.update(crear=True))
    respuesta = cliente.post("/libros/crear", data={})
    assert respuesta.status_code == 302
    assert llamado["crear"] is False


def test_crear_libro_valido(cliente, monkeypatch):
    autenticar_sesion(cliente)
    capturado = {}
    monkeypatch.setattr(Libro, "crear", lambda datos: capturado.update(datos) or 7)
    respuesta = cliente.post(
        "/libros/crear",
        data={
            "csrf_token": "token-seguro",
            "titulo": "1984",
            "autor": "George Orwell",
            "genero": "Ciencia ficción",
            "fecha_publicacion": "1949-06-08",
            "descripcion": "Una novela distópica sobre vigilancia y poder.",
        },
    )
    assert respuesta.status_code == 302
    assert capturado["usuario_id"] == 1


def test_alternar_favorito_agrega_si_no_existe(cliente, monkeypatch):
    autenticar_sesion(cliente)
    monkeypatch.setattr(Libro, "obtener_por_id", lambda _libro, _usuario: libro_falso(es_favorito=False))
    capturado = {}
    monkeypatch.setattr(Favorito, "agregar", lambda usuario, libro: capturado.update(usuario=usuario, libro=libro))
    respuesta = cliente.post("/libros/5/favorito", data={"csrf_token": "token-seguro"})
    assert respuesta.status_code == 302
    assert capturado == {"usuario": 1, "libro": 5}


def test_login_correcto_crea_sesion(cliente, monkeypatch):
    password_hash = bcrypt.generate_password_hash("lectura123").decode("utf-8")
    usuario = SimpleNamespace(id=3, nombre="Laura", password=password_hash)
    monkeypatch.setattr(Usuario, "obtener_por_email", lambda _email: usuario)
    with cliente.session_transaction() as sesion:
        sesion["csrf_token"] = "token-seguro"
    respuesta = cliente.post(
        "/login",
        data={"csrf_token": "token-seguro", "email": "laura@example.com", "password": "lectura123"},
    )
    assert respuesta.status_code == 302
    with cliente.session_transaction() as sesion:
        assert sesion["usuario_id"] == 3
        assert sesion["usuario_nombre"] == "Laura"
