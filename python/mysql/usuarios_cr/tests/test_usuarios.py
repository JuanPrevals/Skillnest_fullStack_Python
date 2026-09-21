import unittest
from datetime import datetime
from unittest.mock import patch

from pymysql import OperationalError

from server import app
from usuario import Usuario


class UsuariosTest(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    @patch("server.Usuario.get_all")
    def test_listado_y_escape_html(self, get_all):
        get_all.return_value = [Usuario(dict(
            id=1, nombre="<script>alert(1)</script>", apellido="Pérez",
            email="ana@example.com", created_at=datetime(2026, 9, 21), updated_at=None,
        ))]
        response = self.client.get("/usuarios")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"2026-09-21", response.data)
        self.assertIn(b"&lt;script&gt;", response.data)
        self.assertNotIn(b"<script>", response.data)

    def test_formulario_y_ruta_inicial(self):
        self.assertEqual(self.client.get("/").location, "/usuarios")
        response = self.client.get("/usuarios/nuevo")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'/usuarios/crear', response.data)
        self.assertEqual(self.client.get("/usuarios/crear").status_code, 405)

    @patch("server.Usuario.get_all", return_value=[])
    def test_listado_vacio(self, get_all):
        self.assertIn("Aún no hay usuarios", self.client.get("/usuarios").text)

    @patch("server.Usuario.save", return_value=5)
    def test_creacion_redirige(self, save):
        response = self.client.post("/usuarios/crear", data={
            "nombre": " Ana ", "apellido": "Pérez", "email": "ana@example.com",
        })
        save.assert_called_once_with(dict(nombre="Ana", apellido="Pérez", email="ana@example.com"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "/usuarios")

    @patch("server.Usuario.save")
    def test_datos_invalidos_no_insertan(self, save):
        for datos in ({}, dict(nombre="A" * 46, apellido="Pérez", email="ana@example.com"),
                      dict(nombre="Ana", apellido="Pérez", email="invalido")):
            with self.subTest(datos=datos):
                self.assertEqual(self.client.post("/usuarios/crear", data=datos).status_code, 400)
        save.assert_not_called()

    @patch("server.Usuario.save", side_effect=OperationalError(2003, "Sin conexión"))
    def test_error_mysql_conserva_formulario(self, save):
        with self.assertLogs(app.logger, level="ERROR"):
            response = self.client.post("/usuarios/crear", data=dict(
                nombre="Ana", apellido="Pérez", email="ana@example.com"))
        self.assertEqual(response.status_code, 503)
        self.assertIn(b'value="Ana"', response.data)


if __name__ == "__main__":
    unittest.main()
