import pymysql.cursors
import os
from dotenv import load_dotenv

# Variables de entorno
load_dotenv()

# CLASE DE CONEXIÓN MYSQL

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host=os.environ.get('MYSQL_HOST'),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    # MÉTODO PARA REALIZAR LAS CONSULTAS
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print(f"Ejecutando Consulta: {query}")
                cursor.execute(query, data)
                
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print(f"Error en la Base de Datos: {e}")
                return False
            finally:
                self.connection.close()


# INSTANCIACIÓN
def connect_to_mysql(db):
    return MySQLConnection(db)