import mysql.connector


class Conexion:

    @staticmethod
    def conectar():
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="poppy",
            database="tienda_videojuegos"
        )

        return conexion
