from conexion import Conexion


class Usuario:
    def __init__(self, id_usuario=None, nombre_usuario=None, correo=None):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.correo = correo

    def mostrar_datos(self):
        return f"ID: {self.id_usuario}, Usuario: {self.nombre_usuario}, Correo: {self.correo}"

    def guardar(self):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO usuario (nombre_usuario, correo)
        VALUES (%s, %s)
        """

        cursor.execute(sql, (self.nombre_usuario, self.correo))
        conexion.commit()
        print("\nUsuario creado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def listar():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT id_usuario, nombre_usuario, correo
        FROM usuario
        WHERE deleted_at IS NULL
        ORDER BY id_usuario ASC
        """

        cursor.execute(sql)
        usuarios = cursor.fetchall()

        print("\n===== USUARIOS =====\n")
        if not usuarios:
            print("No hay usuarios registrados.")

        for usuario in usuarios:
            print(f"ID: {usuario[0]} | Usuario: {usuario[1]} | Correo: {usuario[2]}")

        cursor.close()
        conexion.close()

    @staticmethod
    def buscar():
        texto = input("Ingrese nombre o correo: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT id_usuario, nombre_usuario, correo
        FROM usuario
        WHERE deleted_at IS NULL
        AND (nombre_usuario LIKE %s OR correo LIKE %s)
        ORDER BY id_usuario ASC
        """

        valor = "%" + texto + "%"
        cursor.execute(sql, (valor, valor))
        usuarios = cursor.fetchall()

        print("\n===== RESULTADOS =====\n")
        if not usuarios:
            print("No se encontraron usuarios.")

        for usuario in usuarios:
            print(f"ID: {usuario[0]} | Usuario: {usuario[1]} | Correo: {usuario[2]}")

        cursor.close()
        conexion.close()

    @staticmethod
    def actualizar():
        id_usuario = input("Ingrese ID del usuario: ")
        nombre_usuario = input("Nuevo nombre de usuario: ")
        correo = input("Nuevo correo: ")

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuario
        SET nombre_usuario = %s, correo = %s, updated_at = NOW()
        WHERE id_usuario = %s AND deleted_at IS NULL
        """

        cursor.execute(sql, (nombre_usuario, correo, id_usuario))
        conexion.commit()
        print("\nUsuario actualizado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar():
        id_usuario = input("Ingrese ID del usuario: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuario
        SET deleted_at = NOW()
        WHERE id_usuario = %s AND deleted_at IS NULL
        """

        cursor.execute(sql, (id_usuario,))
        conexion.commit()
        print("\nUsuario eliminado correctamente.")

        cursor.close()
        conexion.close()
