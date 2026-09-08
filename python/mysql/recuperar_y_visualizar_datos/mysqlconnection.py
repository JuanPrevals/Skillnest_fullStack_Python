import os

import pymysql
from pymysql.cursors import DictCursor


class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host=os.environ.get("MYSQL_HOST", "localhost"),
            port=int(os.environ.get("MYSQL_PORT", "3306")),
            user=os.environ.get("MYSQL_USER", "root"),
            password=os.environ.get("MYSQL_PASSWORD", ""),
            database=db,
            charset="utf8mb4",
            cursorclass=DictCursor,
        )

    def query_db(self, query, data=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, data)
                if cursor.description:
                    return cursor.fetchall()
                self.connection.commit()
                return cursor.lastrowid
        except Exception:
            self.connection.rollback()
            raise
        finally:
            self.connection.close()


def connect_to_mysql(db):
    return MySQLConnection(db)
