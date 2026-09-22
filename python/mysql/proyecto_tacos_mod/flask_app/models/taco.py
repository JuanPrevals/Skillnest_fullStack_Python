"""Modelo orientado a objetos para la tabla ``tacos``."""

import os

from flask_app.config.mysqlconnection import connectToMySQL


class Taco:
    def __init__(self, data):
        self.id = data["id"]
        self.tortilla = data["tortilla"]
        self.guiso = data["guiso"]
        self.salsa = data["salsa"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def _database():
        return os.getenv("MYSQL_DATABASE", "esquema_tacos")

    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO tacos (tortilla, guiso, salsa)
            VALUES (%(tortilla)s, %(guiso)s, %(salsa)s);
        """
        return connectToMySQL(cls._database()).query_db(query, datos)

    @classmethod
    def get_all(cls):
        query = """
            SELECT id, tortilla, guiso, salsa, created_at, updated_at
            FROM tacos
            ORDER BY id;
        """
        resultados = connectToMySQL(cls._database()).query_db(query)
        return [cls(registro) for registro in resultados]

    @classmethod
    def get_one(cls, datos):
        query = """
            SELECT id, tortilla, guiso, salsa, created_at, updated_at
            FROM tacos
            WHERE id = %(id)s;
        """
        resultados = connectToMySQL(cls._database()).query_db(query, datos)
        return cls(resultados[0]) if resultados else None

    @classmethod
    def update(cls, datos):
        query = """
            UPDATE tacos
            SET tortilla = %(tortilla)s,
                guiso = %(guiso)s,
                salsa = %(salsa)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls._database()).query_db(query, datos)

    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM tacos WHERE id = %(id)s;"
        return connectToMySQL(cls._database()).query_db(query, datos)

