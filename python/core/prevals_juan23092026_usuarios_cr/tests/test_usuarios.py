import unittest
from datetime import datetime
from unittest.mock import patch

from pymysql import OperationalError

from python.core.usuarios_cr.flask_app.models.usuario import Usuario
from python.core.usuarios_cr.server import app


MODELO = "flask_app.controllers.usuarios.Usuario"


class UsuariosTest(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    @patch(f"{MODELO}.get_all")
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
        self.assertIn(b'href="/usuarios/1"', response.data)
        self.assertIn(b'href="/usuarios/editar/1"', response.data)
        self.assertIn(b'href="/usuarios/borrar/1"', response.data)

    def test_formulario_y_ruta_inicial(self):
        self.assertEqual(self.client.get("/").location, "/usuarios")
        response = self.client.get("/usuarios/nuevo")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'/usuarios/crear', response.data)
        self.assertEqual(self.client.get("/usuarios/crear").status_code, 405)

    @patch(f"{MODELO}.get_all", return_value=[])
    def test_listado_vacio(self, get_all):
        self.assertIn("Aún no hay usuarios", self.client.get("/usuarios").text)

    @patch(f"{MODELO}.save", return_value=5)
    def test_creacion_redirige(self, save):
        response = self.client.post("/usuarios/crear", data={
            "nombre": " Ana ", "apellido": "Pérez", "email": "ana@example.com",
        })
        save.assert_called_once_with(dict(nombre="Ana", apellido="Pérez", email="ana@example.com"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "/usuarios")

    @patch(f"{MODELO}.save")
    def test_datos_invalidos_no_insertan(self, save):
        casos = (
            {},
            dict(nombre="A" * 46, apellido="Pérez", email="ana@example.com"),
            dict(nombre="Ana", apellido="Pérez", email="invalido"),
        )
        for datos in casos:
            with self.subTest(datos=datos):
                self.assertEqual(self.client.post("/usuarios/crear", data=datos).status_code, 400)
        save.assert_not_called()

    @patch(f"{MODELO}.save", side_effect=OperationalError(2003, "Sin conexión"))
    def test_error_mysql_conserva_formulario(self, save):
        with self.assertLogs(app.logger, level="ERROR"):
            response = self.client.post("/usuarios/crear", data=dict(
                nombre="Ana", apellido="Pérez", email="ana@example.com"))
        self.assertEqual(response.status_code, 503)
        self.assertIn(b'value="Ana"', response.data)

    @patch(f"{MODELO}.get_by_id")
    def test_ver_usuario(self, get_by_id):
        get_by_id.return_value = Usuario(dict(
            id=3, nombre="Celia", apellido="Cruz", email="celia@example.com",
            created_at=datetime(2026, 9, 20, 10, 30),
            updated_at=datetime(2026, 9, 21, 11, 45),
        ))
        response = self.client.get("/usuarios/3")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Celia Cruz", response.data)
        self.assertIn(b"2026-09-21 11:45:00", response.data)
        get_by_id.assert_called_once_with(3)

    @patch(f"{MODELO}.get_by_id", return_value=None)
    def test_usuario_inexistente_devuelve_404(self, get_by_id):
        self.assertEqual(self.client.get("/usuarios/99").status_code, 404)
        self.assertEqual(self.client.get("/usuarios/editar/99").status_code, 404)

    @patch(f"{MODELO}.get_by_id")
    def test_formulario_editar_precargado(self, get_by_id):
        get_by_id.return_value = Usuario(dict(
            id=3, nombre="Celia", apellido="Cruz", email="celia@example.com",
            created_at=None, updated_at=None,
        ))
        response = self.client.get("/usuarios/editar/3")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'action="/usuarios/3/actualizar"', response.data)
        self.assertIn(b'value="Celia"', response.data)
        self.assertIn(b'value="Cruz"', response.data)
        self.assertIn(b'value="celia@example.com"', response.data)

    @patch(f"{MODELO}.update", return_value=0)
    @patch(f"{MODELO}.get_by_id")
    def test_actualizacion_redirige(self, get_by_id, update):
        get_by_id.return_value = Usuario(dict(
            id=3, nombre="Celia", apellido="Cruz", email="celia@example.com",
            created_at=None, updated_at=None,
        ))
        response = self.client.post("/usuarios/3/actualizar", data={
            "nombre": " Celia María ", "apellido": "Cruz", "email": "celia@nueva.cl",
        })
        update.assert_called_once_with(dict(
            id=3, nombre="Celia María", apellido="Cruz", email="celia@nueva.cl",
        ))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "/usuarios")

    @patch(f"{MODELO}.update")
    @patch(f"{MODELO}.get_by_id")
    def test_actualizacion_invalida_conserva_datos(self, get_by_id, update):
        get_by_id.return_value = Usuario(dict(
            id=3, nombre="Celia", apellido="Cruz", email="celia@example.com",
            created_at=None, updated_at=None,
        ))
        response = self.client.post("/usuarios/3/actualizar", data={
            "nombre": "Nuevo", "apellido": "", "email": "incorrecto",
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'value="Nuevo"', response.data)
        update.assert_not_called()

    @patch(f"{MODELO}.delete", return_value=0)
    def test_borrado_redirige(self, delete):
        response = self.client.get("/usuarios/borrar/3")
        delete.assert_called_once_with(3)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "/usuarios")


if __name__ == "__main__":
    unittest.main()
