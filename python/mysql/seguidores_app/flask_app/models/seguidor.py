"""Modelo de la auto-relación entre usuarios."""

import os

from flask_app.config.mysqlconnection import connectToMySQL


class Seguidor:
    @staticmethod
    def _database():
        return os.getenv("MYSQL_DATABASE", "esquema_seguidores")

    @classmethod
    def get_all(cls):
        query = """
            SELECT
                f.id,
                u.id AS usuario_id,
                CONCAT(u.nombre, ' ', u.apellido) AS usuario_nombre,
                s.id AS seguidor_id,
                CONCAT(s.nombre, ' ', s.apellido) AS seguidor_nombre,
                f.created_at
            FROM seguidores AS f
            INNER JOIN usuarios AS u ON f.usuario_id = u.id
            INNER JOIN usuarios AS s ON f.seguidor_id = s.id
            ORDER BY u.nombre, u.apellido, s.nombre, s.apellido;
        """
        return connectToMySQL(cls._database()).query_db(query)

    @classmethod
    def existe(cls, datos):
        query = """
            SELECT id
            FROM seguidores
            WHERE usuario_id = %(usuario_id)s
              AND seguidor_id = %(seguidor_id)s;
        """
        resultado = connectToMySQL(cls._database()).query_db(query, datos)
        return bool(resultado)

    @classmethod
    def seguir(cls, datos):
        query = """
            INSERT INTO seguidores (usuario_id, seguidor_id)
            VALUES (%(usuario_id)s, %(seguidor_id)s);
        """
        return connectToMySQL(cls._database()).query_db(query, datos)
