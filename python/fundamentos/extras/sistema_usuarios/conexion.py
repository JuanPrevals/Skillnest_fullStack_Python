import pymysql


class Conexion:
    def __init__(self):
        self.conexion = None

    def abrir(self):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="poppy",
            database="usuarios_db",
            cursorclass=pymysql.cursors.DictCursor
        )
        return self.conexion

    def cerrar(self):
        if self.conexion is not None:
            self.conexion.close()

    @staticmethod
    def conectar():
        conexion = Conexion()
        return conexion.abrir()
