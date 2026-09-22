import os

import pymysql
from pymysql.cursors import DictCursor


class MySQLConnection:
    def __init__(self, database):
        self.connection = pymysql.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            port=int(os.getenv("MYSQL_PORT", "3306")),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", ""),
            database=database,
            charset="utf8mb4",
            cursorclass=DictCursor,
            connect_timeout=5,
        )

    def query_db(self, query, data=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, data)
                if cursor.description:
                    return cursor.fetchall()
                self.connection.commit()
                if query.lstrip().lower().startswith("insert"):
                    return cursor.lastrowid
                return cursor.rowcount
        except Exception:
            self.connection.rollback()
            raise
        finally:
            self.connection.close()


def connect_to_mysql(database):
    return MySQLConnection(database)

