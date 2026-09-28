from datetime import datetime
from types import SimpleNamespace

import pytest

from flask_app import app
from flask_app.controllers import usuarios as controlador
from flask_app.models import seguidor as seguidor_modelo


@pytest.fixture()
def client():
    app.config.update(TESTING=True, SECRET_KEY="tests")
    return app.test_client()


@pytest.fixture()
def usuarios():
    fecha = datetime(2026, 9, 24, 12, 0)
    return [
        SimpleNamespace(
            id=1,
            nombre="Soraya",
            apellido="Montenegro",
            nombre_completo="Soraya Montenegro",
            email="soraya@email.com",
            created_at=fecha,
            updated_at=fecha,
        ),
        SimpleNamespace(
            id=2,
            nombre="Luis F.",
            apellido="de la Vega",
            nombre_completo="Luis F. de la Vega",
            email="luis@email.com",
            created_at=fecha,
            updated_at=fecha,
        ),
    ]


def test_inicio_redirige_a_usuarios(client):
    response = client.get("/")
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/usuarios")


def test_usuarios_muestra_relaciones_y_formularios(client, monkeypatch, usuarios):
    monkeypatch.setattr(controlador.Usuario, "get_all", lambda: usuarios)
    monkeypatch.setattr(
        controlador.Seguidor,
        "get_all",
        lambda: [
            {
                "usuario_nombre": "Soraya Montenegro",
                "seguidor_nombre": "Luis F. de la Vega",
            }
        ],
    )

    response = client.get("/usuarios")

    contenido = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Soraya Montenegro" in contenido
    assert "Luis F. de la Vega" in contenido
    assert 'name="usuario_id"' in contenido
    assert 'name="seguidor_id"' in contenido


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
            "nombre": " Soraya ",
            "apellido": " Montenegro ",
            "email": "SORAYA@EMAIL.COM",
        },
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/usuarios")
    assert guardado == {
        "nombre": "Soraya",
        "apellido": "Montenegro",
        "email": "soraya@email.com",
    }


def test_crear_usuario_rechaza_correo_invalido(client, monkeypatch):
    monkeypatch.setattr(
        controlador.Usuario,
        "save",
        lambda _datos: pytest.fail("No debe guardar datos inválidos"),
    )

    response = client.post(
        "/usuarios/crear",
        data={"nombre": "Soraya", "apellido": "Montenegro", "email": "correo"},
    )

    assert response.status_code == 302


def test_seguir_crea_relacion(client, monkeypatch, usuarios):
    guardado = {}
    monkeypatch.setattr(
        controlador.Usuario,
        "get_by_id",
        lambda usuario_id: next((u for u in usuarios if u.id == usuario_id), None),
    )
    monkeypatch.setattr(controlador.Seguidor, "existe", lambda _datos: False)
    monkeypatch.setattr(
        controlador.Seguidor,
        "seguir",
        lambda datos: guardado.update(datos),
    )

    response = client.post(
        "/seguir",
        data={"usuario_id": "1", "seguidor_id": "2"},
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/usuarios")
    assert guardado == {"usuario_id": 1, "seguidor_id": 2}


def test_auto_seguimiento_se_rechaza(client, monkeypatch):
    monkeypatch.setattr(
        controlador.Usuario,
        "get_by_id",
        lambda _id: pytest.fail("No requiere consultar la base de datos"),
    )
    monkeypatch.setattr(
        controlador.Seguidor,
        "seguir",
        lambda _datos: pytest.fail("No debe crear auto-seguimiento"),
    )

    response = client.post(
        "/seguir",
        data={"usuario_id": "1", "seguidor_id": "1"},
    )

    assert response.status_code == 302


def test_relacion_duplicada_no_se_inserta(client, monkeypatch, usuarios):
    monkeypatch.setattr(
        controlador.Usuario,
        "get_by_id",
        lambda usuario_id: next((u for u in usuarios if u.id == usuario_id), None),
    )
    monkeypatch.setattr(controlador.Seguidor, "existe", lambda _datos: True)
    monkeypatch.setattr(
        controlador.Seguidor,
        "seguir",
        lambda _datos: pytest.fail("No debe duplicar la relación"),
    )

    response = client.post(
        "/seguir",
        data={"usuario_id": "1", "seguidor_id": "2"},
    )

    assert response.status_code == 302


def test_usuario_inexistente_se_rechaza(client, monkeypatch, usuarios):
    monkeypatch.setattr(
        controlador.Usuario,
        "get_by_id",
        lambda usuario_id: usuarios[0] if usuario_id == 1 else None,
    )
    monkeypatch.setattr(
        controlador.Seguidor,
        "seguir",
        lambda _datos: pytest.fail("No debe crear una relación inválida"),
    )

    response = client.post(
        "/seguir",
        data={"usuario_id": "1", "seguidor_id": "999"},
    )

    assert response.status_code == 302


def test_get_all_utiliza_self_join(monkeypatch):
    llamada = {}

    class ConexionFalsa:
        def query_db(self, query):
            llamada["query"] = query
            return []

    monkeypatch.setattr(
        seguidor_modelo,
        "connectToMySQL",
        lambda _database: ConexionFalsa(),
    )

    assert seguidor_modelo.Seguidor.get_all() == []
    assert "INNER JOIN usuarios AS u" in llamada["query"]
    assert "INNER JOIN usuarios AS s" in llamada["query"]


def test_seguir_utiliza_parametros_preparados(monkeypatch):
    llamada = {}

    class ConexionFalsa:
        def query_db(self, query, datos):
            llamada["query"] = query
            llamada["datos"] = datos
            return 1

    monkeypatch.setattr(
        seguidor_modelo,
        "connectToMySQL",
        lambda _database: ConexionFalsa(),
    )
    datos = {"usuario_id": 1, "seguidor_id": 2}

    resultado = seguidor_modelo.Seguidor.seguir(datos)

    assert resultado == 1
    assert "%(usuario_id)s" in llamada["query"]
    assert "%(seguidor_id)s" in llamada["query"]
    assert llamada["datos"] == datos
