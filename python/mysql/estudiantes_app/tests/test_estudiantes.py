import unittest
from datetime import datetime
from unittest.mock import patch

from server import app
from estudiante import Estudiante


def estudiante_ejemplo():
    return Estudiante({
        "id_estudiante": 2,
        "nombre": "Ana Pérez",
        "email": "ana@email.com",
        "created_at": datetime(2026, 9, 22, 10, 30),
    })


class EstudiantesTest(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    @patch("server.Estudiante.get_all")
    def test_listado_incluye_acciones(self, get_all):
        get_all.return_value = [estudiante_ejemplo()]
        response = self.client.get("/estudiantes")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Ana P\xc3\xa9rez", response.data)
        self.assertIn(b'/estudiantes/ver/2', response.data)
        self.assertIn(b'/estudiantes/editar/2', response.data)
        self.assertIn(b'/eliminar_estudiante/2', response.data)

    @patch("server.Estudiante.get_by_id", return_value=estudiante_ejemplo())
    def test_ver_estudiante(self, get_by_id):
        response = self.client.get("/estudiantes/ver/2")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"ana@email.com", response.data)
        get_by_id.assert_called_once_with(2)

    @patch("server.Estudiante.get_by_id", return_value=None)
    def test_estudiante_inexistente(self, get_by_id):
        self.assertEqual(self.client.get("/estudiantes/ver/99").status_code, 404)
        self.assertEqual(self.client.get("/estudiantes/editar/99").status_code, 404)
        self.assertEqual(self.client.post("/eliminar_estudiante/99").status_code, 404)

    @patch("server.Estudiante.get_by_id", return_value=estudiante_ejemplo())
    def test_formulario_editar_precargado(self, get_by_id):
        response = self.client.get("/estudiantes/editar/2")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'value="Ana P\xc3\xa9rez"', response.data)
        self.assertIn(b'value="ana@email.com"', response.data)

    @patch("server.Estudiante.actualizar", return_value=1)
    @patch("server.Estudiante.get_by_id", return_value=estudiante_ejemplo())
    def test_actualizar_redirige(self, get_by_id, actualizar):
        response = self.client.post("/actualizar_estudiante", data={
            "id_estudiante": "2",
            "nombre": " Ana María ",
            "email": "ana.nueva@email.com",
        })
        actualizar.assert_called_once_with({
            "id_estudiante": 2,
            "nombre": "Ana María",
            "email": "ana.nueva@email.com",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "/estudiantes")

    @patch("server.Estudiante.actualizar")
    @patch("server.Estudiante.get_by_id", return_value=estudiante_ejemplo())
    def test_actualizacion_invalida_no_escribe(self, get_by_id, actualizar):
        response = self.client.post("/actualizar_estudiante", data={
            "id_estudiante": "2", "nombre": "Nuevo nombre", "email": "incorrecto",
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'value="Nuevo nombre"', response.data)
        actualizar.assert_not_called()

    @patch("server.Estudiante.eliminar", return_value=1)
    @patch("server.Estudiante.get_by_id", return_value=estudiante_ejemplo())
    def test_eliminar_por_post(self, get_by_id, eliminar):
        response = self.client.post("/eliminar_estudiante/2")
        eliminar.assert_called_once_with({"id_estudiante": 2})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "/estudiantes")

    def test_eliminar_no_acepta_get(self):
        self.assertEqual(self.client.get("/eliminar_estudiante/2").status_code, 405)


if __name__ == "__main__":
    unittest.main()

