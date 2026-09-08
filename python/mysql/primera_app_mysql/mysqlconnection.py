import os

import pymysql.cursors


class MySQLConnection:
    """Administra la conexión y las consultas a MySQL."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password=os.environ.get("MYSQL_PASSWORD", "root"),
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )

    def query_db(self, query, data=None):
        try:
            with self.connection.cursor() as cursor:
                print("Running Query:")
                print(query)
                cursor.execute(query, data)
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                elif query.strip().lower().startswith("insert"):
                    return cursor.lastrowid
                return None
        except Exception as error:
            print("Something went wrong:")
            print(error)
            return False
        finally:
            self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)
