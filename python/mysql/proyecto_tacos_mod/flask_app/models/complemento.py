"""Modelo de complementos y su relación muchos-a-muchos con los tacos."""

import os

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import taco


class Complemento:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre_complemento = data["nombre_complemento"]
        self.en_tacos = []
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def _database():
        return os.getenv("MYSQL_DATABASE", "esquema_tacos")

    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO complementos (nombre_complemento)
            VALUES (%(nombre_complemento)s);
        """
        return connectToMySQL(cls._database()).query_db(query, datos)

    @classmethod
    def get_all(cls):
        query = """
            SELECT id, nombre_complemento, created_at, updated_at
            FROM complementos
            ORDER BY nombre_complemento;
        """
        resultados = connectToMySQL(cls._database()).query_db(query)
        return [cls(registro) for registro in resultados]

    @classmethod
    def get_complementos_y_tacos(cls, datos):
        """Recupera un complemento y crea los objetos Taco asociados."""

        query = """
            SELECT
                complementos.id AS complemento_id,
                complementos.nombre_complemento,
                complementos.created_at AS complemento_created_at,
                complementos.updated_at AS complemento_updated_at,
                tacos.id AS taco_id,
                tacos.tortilla,
                tacos.guiso,
                tacos.salsa,
                tacos.created_at AS taco_created_at,
                tacos.updated_at AS taco_updated_at
            FROM complementos
            LEFT JOIN complementos_en_tacos
                ON complementos_en_tacos.complemento_id = complementos.id
            LEFT JOIN tacos
                ON complementos_en_tacos.taco_id = tacos.id
            WHERE complementos.id = %(id)s
            ORDER BY tacos.id;
        """
        resultados = connectToMySQL(cls._database()).query_db(query, datos)

        if not resultados:
            return None

        complemento = cls(
            {
                "id": resultados[0]["complemento_id"],
                "nombre_complemento": resultados[0]["nombre_complemento"],
                "created_at": resultados[0]["complemento_created_at"],
                "updated_at": resultados[0]["complemento_updated_at"],
            }
        )

        for fila_en_db in resultados:
            # Un LEFT JOIN devuelve una fila con taco_id NULL si no hay relaciones.
            if fila_en_db["taco_id"] is None:
                continue

            datos_taco = {
                "id": fila_en_db["taco_id"],
                "tortilla": fila_en_db["tortilla"],
                "guiso": fila_en_db["guiso"],
                "salsa": fila_en_db["salsa"],
                "created_at": fila_en_db["taco_created_at"],
                "updated_at": fila_en_db["taco_updated_at"],
            }
            complemento.en_tacos.append(taco.Taco(datos_taco))

        return complemento

    @classmethod
    def asociar_taco(cls, datos):
        """Crea la relación sin duplicarla si ya existe."""

        query = """
            INSERT IGNORE INTO complementos_en_tacos (complemento_id, taco_id)
            VALUES (%(complemento_id)s, %(taco_id)s);
        """
        return connectToMySQL(cls._database()).query_db(query, datos)

    @classmethod
    def desasociar_taco(cls, datos):
        query = """
            DELETE FROM complementos_en_tacos
            WHERE complemento_id = %(complemento_id)s
              AND taco_id = %(taco_id)s;
        """
        return connectToMySQL(cls._database()).query_db(query, datos)
