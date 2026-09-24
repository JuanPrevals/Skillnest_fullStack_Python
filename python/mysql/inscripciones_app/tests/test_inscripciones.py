from datetime import datetime
from types import SimpleNamespace

import pytest

from flask_app import app
from flask_app.controllers import inscripciones as controlador
from flask_app.models import inscripcion as inscripcion_modelo


@pytest.fixture()
def client():
    app.config.update(TESTING=True, SECRET_KEY="tests")
    return app.test_client()


@pytest.fixture()
def estudiante():
    return SimpleNamespace(
        id_estudiante=1,
        nombre="Juan Pérez",
        email="juan@email.com",
        created_at=datetime(2026, 9, 24),
    )


@pytest.fixture()
def curso():
    return SimpleNamespace(
        id_curso=3,
        nombre_curso="Python",
        descripcion="Programación con Python",
        created_at=datetime(2026, 9, 24),
    )


def preparar_inicio(monkeypatch, estudiante, curso, inscripciones=None):
    monkeypatch.setattr(controlador.Estudiante, "get_all", lambda: [estudiante])
    monkeypatch.setattr(controlador.Curso, "get_all", lambda: [curso])
    monkeypatch.setattr(
        controlador.Inscripcion,
        "get_all",
        lambda: inscripciones or [],
    )


def test_inicio_muestra_selectores(client, monkeypatch, estudiante, curso):
    preparar_inicio(monkeypatch, estudiante, curso)

    response = client.get("/")

    contenido = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Juan Pérez" in contenido
    assert "Python" in contenido
    assert 'name="estudiante_id"' in contenido
    assert 'name="curso_id"' in contenido


def test_inscripcion_valida_crea_relacion(client, monkeypatch, estudiante, curso):
    guardado = {}
    monkeypatch.setattr(controlador.Estudiante, "get_by_id", lambda _id: estudiante)
    monkeypatch.setattr(controlador.Curso, "get_by_id", lambda _id: curso)
    monkeypatch.setattr(controlador.Inscripcion, "existe", lambda _datos: False)
    monkeypatch.setattr(
        controlador.Inscripcion,
        "inscribir_estudiante_en_curso",
        lambda datos: guardado.update(datos),
    )

    response = client.post(
        "/inscribir",
        data={"estudiante_id": "1", "curso_id": "3"},
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")
    assert guardado == {"estudiante_id": 1, "curso_id": 3}


def test_rechaza_ids_ausentes(client, monkeypatch):
    monkeypatch.setattr(
        controlador.Inscripcion,
        "inscribir_estudiante_en_curso",
        lambda _datos: pytest.fail("No debe insertar datos inválidos"),
    )

    response = client.post("/inscribir", data={"estudiante_id": "", "curso_id": "3"})

    assert response.status_code == 302


def test_rechaza_estudiante_inexistente(client, monkeypatch):
    monkeypatch.setattr(controlador.Estudiante, "get_by_id", lambda _id: None)
    monkeypatch.setattr(
        controlador.Curso,
        "get_by_id",
        lambda _id: pytest.fail("No necesita consultar el curso"),
    )

    response = client.post(
        "/inscribir",
        data={"estudiante_id": "999", "curso_id": "3"},
    )

    assert response.status_code == 302


def test_rechaza_inscripcion_duplicada(client, monkeypatch, estudiante, curso):
    monkeypatch.setattr(controlador.Estudiante, "get_by_id", lambda _id: estudiante)
    monkeypatch.setattr(controlador.Curso, "get_by_id", lambda _id: curso)
    monkeypatch.setattr(controlador.Inscripcion, "existe", lambda _datos: True)
    monkeypatch.setattr(
        controlador.Inscripcion,
        "inscribir_estudiante_en_curso",
        lambda _datos: pytest.fail("No debe duplicar la relación"),
    )

    response = client.post(
        "/inscribir",
        data={"estudiante_id": "1", "curso_id": "3"},
        follow_redirects=False,
    )

    assert response.status_code == 302


def test_modelo_inserta_con_parametros_preparados(monkeypatch):
    llamada = {}

    class ConexionFalsa:
        def query_db(self, query, datos):
            llamada["query"] = query
            llamada["datos"] = datos
            return 1

    monkeypatch.setattr(
        inscripcion_modelo,
        "connectToMySQL",
        lambda _database: ConexionFalsa(),
    )
    datos = {"estudiante_id": 2, "curso_id": 4}

    resultado = inscripcion_modelo.Inscripcion.inscribir_estudiante_en_curso(datos)

    assert resultado == 1
    assert "%(estudiante_id)s" in llamada["query"]
    assert "%(curso_id)s" in llamada["query"]
    assert llamada["datos"] == datos


def test_get_all_usa_las_tres_tablas(monkeypatch):
    llamada = {}

    class ConexionFalsa:
        def query_db(self, query):
            llamada["query"] = query
            return []

    monkeypatch.setattr(
        inscripcion_modelo,
        "connectToMySQL",
        lambda _database: ConexionFalsa(),
    )

    assert inscripcion_modelo.Inscripcion.get_all() == []
    assert "FROM inscripciones" in llamada["query"]
    assert "INNER JOIN estudiantes" in llamada["query"]
    assert "INNER JOIN cursos" in llamada["query"]
