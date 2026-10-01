import os

import pymysql
from pymysql.cursors import DictCursor


class MySQLConnection:
    """Adaptador pequeño para ejecutar consultas parametrizadas en MySQL."""

    def __init__(self, db_name=None):
        host = os.getenv("DB_HOST") or os.getenv("MYSQL_HOST") or "localhost"
        port = os.getenv("DB_PORT") or os.getenv("MYSQL_PORT") or "3306"
        user = os.getenv("DB_USER") or os.getenv("MYSQL_USER") or "root"
        password = os.getenv("DB_PASSWORD")
        if password is None:
            password = os.getenv("MYSQL_PASSWORD", "")

        self.connection = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            database=db_name or os.getenv("DB_NAME", "bookhub_db"),
            charset="utf8mb4",
            cursorclass=DictCursor,
            autocommit=False,
        )

    def query_db(self, query, data=None):
        data = data or {}
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, data)
                if query.lstrip().lower().startswith("select"):
                    return cursor.fetchall()
                self.connection.commit()
                return cursor.lastrowid if cursor.lastrowid else cursor.rowcount
        except Exception:
            self.connection.rollback()
            raise
        finally:
            self.connection.close()


def connect_to_mysql(db_name=None):
    return MySQLConnection(db_name)
