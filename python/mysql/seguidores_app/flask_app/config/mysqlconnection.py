"""Conexión reutilizable con MySQL mediante PyMySQL."""

import os

import pymysql.cursors


class MySQLConnection:
    def __init__(self, database):
        self.connection = pymysql.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            port=int(os.getenv("MYSQL_PORT", "3306")),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", ""),
            database=database,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False,
        )

    def query_db(self, query, data=None):
        """Ejecuta una sentencia preparada y administra la transacción."""

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, data or {})
                if cursor.description is not None:
                    return cursor.fetchall()

                self.connection.commit()
                return cursor.lastrowid or cursor.rowcount
        except pymysql.MySQLError:
            self.connection.rollback()
            raise
        finally:
            self.connection.close()


def connectToMySQL(database):
    return MySQLConnection(database)
