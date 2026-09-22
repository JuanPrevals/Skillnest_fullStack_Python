from datetime import datetime
from types import SimpleNamespace

import pytest

from flask_app import app
from flask_app.controllers import tacos as controlador


@pytest.fixture()
def client():
    app.config.update(TESTING=True, SECRET_KEY="tests")
    return app.test_client()


@pytest.fixture()
def taco():
    fecha = datetime(2026, 9, 22, 12, 30)
    return SimpleNamespace(
        id=1,
        tortilla="Maíz",
        guiso="Carne asada",
        salsa="Verde",
        created_at=fecha,
        updated_at=fecha,
    )


def test_inicio_muestra_formulario(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Crear taco" in response.data


def test_listado_muestra_tacos(client, monkeypatch, taco):
    monkeypatch.setattr(controlador.Taco, "get_all", lambda: [taco])
    response = client.get("/tacos")
    assert response.status_code == 200
    assert "Carne asada" in response.get_data(as_text=True)


def test_crear_valida_y_guarda(client, monkeypatch):
    guardado = {}
    monkeypatch.setattr(controlador.Taco, "save", lambda datos: guardado.update(datos))
    response = client.post(
        "/crear",
        data={"tortilla": " Maíz ", "guiso": "Pollo", "salsa": "Roja"},
    )
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/tacos")
    assert guardado == {"tortilla": "Maíz", "guiso": "Pollo", "salsa": "Roja"}


def test_crear_rechaza_campos_vacios(client, monkeypatch):
    monkeypatch.setattr(
        controlador.Taco,
        "save",
        lambda _datos: pytest.fail("No debe guardar datos inválidos"),
    )
    response = client.post(
        "/crear",
        data={"tortilla": "", "guiso": "Pollo", "salsa": "Roja"},
    )
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")


def test_detalle_inexistente_devuelve_404(client, monkeypatch):
    monkeypatch.setattr(controlador.Taco, "get_one", lambda _datos: None)
    response = client.get("/mostrar/999")
    assert response.status_code == 404


def test_actualizar_taco(client, monkeypatch):
    actualizado = {}
    monkeypatch.setattr(controlador.Taco, "update", lambda datos: actualizado.update(datos))
    response = client.post(
        "/actualizar/7",
        data={"tortilla": "Harina", "guiso": "Pastor", "salsa": "Verde"},
    )
    assert response.status_code == 302
    assert actualizado["id"] == 7


def test_eliminar_taco_por_post(client, monkeypatch):
    eliminado = {}
    monkeypatch.setattr(controlador.Taco, "delete", lambda datos: eliminado.update(datos))
    response = client.post("/borrar/4")
    assert response.status_code == 302
    assert eliminado == {"id": 4}

