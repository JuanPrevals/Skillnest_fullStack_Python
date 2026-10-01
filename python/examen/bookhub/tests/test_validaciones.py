from datetime import date, timedelta

from flask_app.models.libro import Libro
from flask_app.models.usuario import Usuario


def datos_usuario_validos():
    return {
        "nombre": "Ana",
        "apellido": "Pérez",
        "email": "ana@example.com",
        "password": "lectura123",
        "confirmacion": "lectura123",
    }


def datos_libro_validos():
    return {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "genero": "Novela",
        "fecha_publicacion": "1967-06-05",
        "descripcion": "Una historia inolvidable sobre la familia Buendía.",
    }


def test_registro_valido_no_genera_errores(monkeypatch):
    monkeypatch.setattr(Usuario, "obtener_por_email", lambda _email: None)
    assert Usuario.validar_registro(datos_usuario_validos()) == {}


def test_registro_rechaza_datos_invalidos(monkeypatch):
    monkeypatch.setattr(Usuario, "obtener_por_email", lambda _email: object())
    datos = datos_usuario_validos()
    datos.update(nombre="A", apellido="", email="correo-invalido", password="abc", confirmacion="xyz")
    errores = Usuario.validar_registro(datos)
    assert {"nombre", "apellido", "email", "password", "confirmacion"} <= errores.keys()


def test_registro_rechaza_email_duplicado(monkeypatch):
    monkeypatch.setattr(Usuario, "obtener_por_email", lambda _email: object())
    errores = Usuario.validar_registro(datos_usuario_validos())
    assert "email" in errores


def test_libro_valido_no_genera_errores():
    assert Libro.validar(datos_libro_validos()) == {}


def test_libro_rechaza_campos_vacios():
    errores = Libro.validar({})
    assert {"titulo", "autor", "genero", "fecha_publicacion", "descripcion"} == errores.keys()


def test_libro_rechaza_fecha_futura():
    datos = datos_libro_validos()
    datos["fecha_publicacion"] = (date.today() + timedelta(days=1)).isoformat()
    assert "fecha_publicacion" in Libro.validar(datos)


def test_libro_rechaza_genero_fuera_del_catalogo():
    datos = datos_libro_validos()
    datos["genero"] = "Inventado"
    assert "genero" in Libro.validar(datos)
