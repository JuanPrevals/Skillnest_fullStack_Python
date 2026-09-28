from datetime import datetime
from types import SimpleNamespace

import pytest

from flask_app import app
from flask_app.controllers import canciones as controlador
from flask_app.models import cancion as cancion_modelo
from flask_app.models import usuario as usuario_modelo


@pytest.fixture()
def client():
    app.config.update(TESTING=True, SECRET_KEY="tests")
    return app.test_client()


@pytest.fixture()
def fecha():
    return datetime(2026, 9, 24, 12, 0)


@pytest.fixture()
def usuario(fecha):
    return SimpleNamespace(
        id=1,
        nombre="Soraya Montenegro",
        email="soraya@email.com",
        contrasena="demo",
        created_at=fecha,
        updated_at=fecha,
        favoritos=[],
    )


@pytest.fixture()
def cancion(fecha):
    return SimpleNamespace(
        id=3,
        titulo="De Música Ligera",
        artista="Soda Stereo",
        created_at=fecha,
        updated_at=fecha,
        usuarios=[],
    )


def test_inicio_redirige_a_usuarios(client):
    response = client.get("/")
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/usuarios")


def test_usuarios_muestra_formulario_y_registros(client, monkeypatch, usuario):
    monkeypatch.setattr(controlador.Usuario, "get_all", lambda: [usuario])

    response = client.get("/usuarios")

    contenido = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Crear usuario" in contenido
    assert "Soraya Montenegro" in contenido


def test_crear_usuario_guarda_y_redirige(client, monkeypatch):
    guardado = {}
    monkeypatch.setattr(
        controlador.Usuario,
        "save",
        lambda datos: guardado.update(datos),
    )

    response = client.post(
        "/usuarios/crear",
        data={
            "nombre": " Soraya Montenegro ",
            "email": "SORAYA@EMAIL.COM",
            "contrasena": "demo",
        },
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/usuarios")
    assert guardado == {
        "nombre": "Soraya Montenegro",
        "email": "soraya@email.com",
        "contrasena": "demo",
    }


def test_crear_usuario_rechaza_datos_invalidos(client, monkeypatch):
    monkeypatch.setattr(
        controlador.Usuario,
        "save",
        lambda _datos: pytest.fail("No debe guardar datos inválidos"),
    )

    response = client.post(
        "/usuarios/crear",
        data={"nombre": "Soraya", "email": "correo-invalido", "contrasena": "x"},
    )

    assert response.status_code == 302


def test_mostrar_usuario_incluye_favoritos(client, monkeypatch, usuario, cancion):
    usuario.favoritos = [
        {"id": cancion.id, "titulo": cancion.titulo, "artista": cancion.artista}
    ]
    monkeypatch.setattr(
        controlador.Usuario,
        "get_by_id_with_favorites",
        lambda _datos: usuario,
    )
    monkeypatch.setattr(
        controlador.Cancion,
        "get_not_favorited_by_user",
        lambda _datos: [],
    )

    response = client.get("/usuarios/1")

    contenido = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Soraya Montenegro" in contenido
    assert "De Música Ligera" in contenido


def test_canciones_muestra_formulario_y_registros(client, monkeypatch, cancion):
    monkeypatch.setattr(controlador.Cancion, "get_all", lambda: [cancion])

    response = client.get("/canciones")

    contenido = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Crear canción" in contenido
    assert "Soda Stereo" in contenido


def test_agregar_favorito_desde_usuario(client, monkeypatch, usuario, cancion):
    guardado = {}
    monkeypatch.setattr(controlador.Usuario, "get_by_id", lambda _id: usuario)
    monkeypatch.setattr(controlador.Cancion, "get_by_id", lambda _id: cancion)
    monkeypatch.setattr(controlador.Favorito, "existe", lambda _datos: False)
    monkeypatch.setattr(
        controlador.Favorito,
        "agregar",
        lambda datos: guardado.update(datos),
    )

    response = client.post(
        "/favoritos/agregar",
        data={"usuario_id": "1", "cancion_id": "3", "origen": "usuario"},
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/usuarios/1")
    assert guardado == {"usuario_id": 1, "cancion_id": 3}


def test_agregar_favorito_desde_cancion_redirige_a_cancion(
    client, monkeypatch, usuario, cancion
):
    monkeypatch.setattr(controlador.Usuario, "get_by_id", lambda _id: usuario)
    monkeypatch.setattr(controlador.Cancion, "get_by_id", lambda _id: cancion)
    monkeypatch.setattr(controlador.Favorito, "existe", lambda _datos: False)
    monkeypatch.setattr(controlador.Favorito, "agregar", lambda _datos: 1)

    response = client.post(
        "/favoritos/agregar",
        data={"usuario_id": "1", "cancion_id": "3", "origen": "cancion"},
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/canciones/3")


def test_favorito_duplicado_no_se_inserta(client, monkeypatch, usuario, cancion):
    monkeypatch.setattr(controlador.Usuario, "get_by_id", lambda _id: usuario)
    monkeypatch.setattr(controlador.Cancion, "get_by_id", lambda _id: cancion)
    monkeypatch.setattr(controlador.Favorito, "existe", lambda _datos: True)
    monkeypatch.setattr(
        controlador.Favorito,
        "agregar",
        lambda _datos: pytest.fail("No debe duplicar el favorito"),
    )

    response = client.post(
        "/favoritos/agregar",
        data={"usuario_id": "1", "cancion_id": "3", "origen": "usuario"},
    )

    assert response.status_code == 302


def test_usuario_parsea_resultado_del_join(monkeypatch, fecha):
    filas = [
        {
            "usuario_id": 1,
            "usuario_nombre": "Soraya Montenegro",
            "usuario_email": "soraya@email.com",
            "usuario_contrasena": "demo",
            "usuario_created_at": fecha,
            "usuario_updated_at": fecha,
            "cancion_id": 3,
            "cancion_titulo": "De Música Ligera",
            "cancion_artista": "Soda Stereo",
            "cancion_created_at": fecha,
            "cancion_updated_at": fecha,
        }
    ]

    class ConexionFalsa:
        def query_db(self, query, datos):
            assert "LEFT JOIN favoritos" in query
            assert datos == {"id": 1}
            return filas

    monkeypatch.setattr(
        usuario_modelo,
        "connectToMySQL",
        lambda _database: ConexionFalsa(),
    )

    resultado = usuario_modelo.Usuario.get_by_id_with_favorites({"id": 1})

    assert resultado.nombre == "Soraya Montenegro"
    assert resultado.favoritos[0]["titulo"] == "De Música Ligera"


def test_bonus_excluye_usuarios_con_favorito(monkeypatch):
    llamada = {}

    class ConexionFalsa:
        def query_db(self, query, datos):
            llamada["query"] = query
            llamada["datos"] = datos
            return []

    monkeypatch.setattr(
        cancion_modelo,
        "connectToMySQL",
        lambda _database: ConexionFalsa(),
    )

    resultado = cancion_modelo.Cancion.get_users_not_favorited({"cancion_id": 3})

    assert resultado == []
    assert "favoritos.usuario_id IS NULL" in llamada["query"]
    assert llamada["datos"] == {"cancion_id": 3}
