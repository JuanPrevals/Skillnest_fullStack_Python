"""Modelo de la relación muchos-a-muchos entre usuarios y canciones."""

import os

from flask_app.config.mysqlconnection import connectToMySQL


class Favorito:
    @staticmethod
    def _database():
        return os.getenv("MYSQL_DATABASE", "esquema_canciones")

    @classmethod
    def existe(cls, datos):
        query = """
            SELECT usuario_id, cancion_id
            FROM favoritos
            WHERE usuario_id = %(usuario_id)s
              AND cancion_id = %(cancion_id)s;
        """
        resultado = connectToMySQL(cls._database()).query_db(query, datos)
        return bool(resultado)

    @classmethod
    def agregar(cls, datos):
        query = """
            INSERT INTO favoritos (usuario_id, cancion_id)
            VALUES (%(usuario_id)s, %(cancion_id)s);
        """
        return connectToMySQL(cls._database()).query_db(query, datos)
