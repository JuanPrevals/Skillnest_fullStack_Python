from datetime import datetime
from types import SimpleNamespace

import pytest

from flask_app import app
from flask_app.controllers import tacos as controlador
from flask_app.models import complemento as complemento_modelo


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


def test_complemento_convierte_filas_del_join_en_tacos(monkeypatch):
    fecha = datetime(2026, 9, 24, 9, 0)
    filas = [
        {
            "complemento_id": 3,
            "nombre_complemento": "Cilantro",
            "complemento_created_at": fecha,
            "complemento_updated_at": fecha,
            "taco_id": 1,
            "tortilla": "Maíz",
            "guiso": "Pastor",
            "salsa": "Verde",
            "taco_created_at": fecha,
            "taco_updated_at": fecha,
        },
        {
            "complemento_id": 3,
            "nombre_complemento": "Cilantro",
            "complemento_created_at": fecha,
            "complemento_updated_at": fecha,
            "taco_id": 2,
            "tortilla": "Harina",
            "guiso": "Pollo",
            "salsa": "Roja",
            "taco_created_at": fecha,
            "taco_updated_at": fecha,
        },
    ]

    class ConexionFalsa:
        def query_db(self, query, datos):
            assert "LEFT JOIN complementos_en_tacos" in query
            assert datos == {"id": 3}
            return filas

    monkeypatch.setattr(
        complemento_modelo,
        "connectToMySQL",
        lambda _database: ConexionFalsa(),
    )

    complemento = complemento_modelo.Complemento.get_complementos_y_tacos({"id": 3})

    assert complemento.nombre_complemento == "Cilantro"
    assert [taco.id for taco in complemento.en_tacos] == [1, 2]
    assert complemento.en_tacos[0].guiso == "Pastor"


def test_complemento_sin_tacos_conserva_lista_vacia(monkeypatch):
    fecha = datetime(2026, 9, 24, 9, 0)
    filas = [
        {
            "complemento_id": 4,
            "nombre_complemento": "Rábanos",
            "complemento_created_at": fecha,
            "complemento_updated_at": fecha,
            "taco_id": None,
            "tortilla": None,
            "guiso": None,
            "salsa": None,
            "taco_created_at": None,
            "taco_updated_at": None,
        }
    ]

    class ConexionFalsa:
        def query_db(self, _query, _datos):
            return filas

    monkeypatch.setattr(
        complemento_modelo,
        "connectToMySQL",
        lambda _database: ConexionFalsa(),
    )

    complemento = complemento_modelo.Complemento.get_complementos_y_tacos({"id": 4})

    assert complemento is not None
    assert complemento.en_tacos == []


def test_detalle_complemento_muestra_tacos_asociados(client, monkeypatch, taco):
    complemento = SimpleNamespace(
        id=2,
        nombre_complemento="Cebolla",
        en_tacos=[taco],
    )
    monkeypatch.setattr(
        controlador.Complemento,
        "get_complementos_y_tacos",
        lambda _datos: complemento,
    )
    monkeypatch.setattr(controlador.Taco, "get_all", lambda: [taco])

    response = client.get("/complementos/2")

    assert response.status_code == 200
    contenido = response.get_data(as_text=True)
    assert "Cebolla" in contenido
    assert "Carne asada" in contenido

