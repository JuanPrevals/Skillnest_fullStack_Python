import hashlib

import pymysql

from conexion import Conexion


class Usuario:
    def __init__(self, id=None, usuario=None, password=None, tipo=None):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo = tipo

    @staticmethod
    def generar_hash(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    @staticmethod
    def obtener_id_tipo(tipo):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT id
        FROM tipos_usuario
        WHERE nombre = %s
        """

        cursor.execute(sql, (tipo.upper(),))
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado is None:
            return None

        return resultado["id"]

    def crear_usuario(self):
        id_tipo = Usuario.obtener_id_tipo(self.tipo)

        if id_tipo is None:
            print("\nTipo de usuario invalido. Use ADMIN o USER.")
            return

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO usuarios (usuario, password, tipo_usuario)
        VALUES (%s, %s, %s)
        """

        password_hash = Usuario.generar_hash(self.password)

        try:
            cursor.execute(sql, (self.usuario, password_hash, id_tipo))
            conexion.commit()
            print("\nUsuario registrado correctamente.")
        except pymysql.err.IntegrityError:
            print("\nEl nombre de usuario ya existe.")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def listar_usuarios():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT u.id, u.usuario, t.nombre AS tipo
        FROM usuarios u
        INNER JOIN tipos_usuario t ON u.tipo_usuario = t.id
        WHERE u.deleted_at IS NULL
        ORDER BY u.id ASC
        """

        cursor.execute(sql)
        usuarios = cursor.fetchall()

        print("\nID   Usuario              Tipo")
        print("--------------------------------")

        if not usuarios:
            print("No hay usuarios registrados.")

        for usuario in usuarios:
            print(f"{usuario['id']:<4} {usuario['usuario']:<20} {usuario['tipo']}")

        print(f"\nTotal de usuarios registrados: {len(usuarios)}")

        cursor.close()
        conexion.close()

    @staticmethod
    def buscar_por_id(id_usuario):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            u.id,
            u.usuario,
            t.nombre AS tipo,
            u.created_at,
            u.updated_at
        FROM usuarios u
        INNER JOIN tipos_usuario t ON u.tipo_usuario = t.id
        WHERE u.id = %s AND u.deleted_at IS NULL
        """

        cursor.execute(sql, (id_usuario,))
        usuario = cursor.fetchone()

        cursor.close()
        conexion.close()

        return usuario

    @staticmethod
    def mostrar_usuario(usuario):
        if usuario is None:
            print("\nUsuario no encontrado.")
            return

        print("\n===== DATOS DEL USUARIO =====")
        print(f"ID: {usuario['id']}")
        print(f"Usuario: {usuario['usuario']}")
        print(f"Tipo: {usuario['tipo']}")
        print(f"Creado: {usuario['created_at']}")
        print(f"Actualizado: {usuario['updated_at']}")

    @staticmethod
    def modificar_usuario(id_usuario, nuevo_usuario, nueva_password, nuevo_tipo):
        id_tipo = Usuario.obtener_id_tipo(nuevo_tipo)

        if id_tipo is None:
            print("\nTipo de usuario invalido. Use ADMIN o USER.")
            return

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuarios
        SET usuario = %s,
            password = %s,
            tipo_usuario = %s,
            updated_at = NOW()
        WHERE id = %s AND deleted_at IS NULL
        """

        password_hash = Usuario.generar_hash(nueva_password)

        try:
            cursor.execute(sql, (nuevo_usuario, password_hash, id_tipo, id_usuario))
            conexion.commit()

            if cursor.rowcount == 0:
                print("\nUsuario no encontrado.")
            else:
                print("\nUsuario modificado correctamente.")
        except pymysql.err.IntegrityError:
            print("\nEl nombre de usuario ya existe.")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar_usuario(id_usuario):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuarios
        SET deleted_at = NOW()
        WHERE id = %s AND deleted_at IS NULL
        """

        cursor.execute(sql, (id_usuario,))
        conexion.commit()

        if cursor.rowcount == 0:
            print("\nUsuario no encontrado.")
        else:
            print("\nUsuario eliminado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def validar_login(nombre_usuario, password):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT u.id, u.usuario, t.nombre AS tipo
        FROM usuarios u
        INNER JOIN tipos_usuario t ON u.tipo_usuario = t.id
        WHERE u.usuario = %s
        AND u.password = %s
        AND u.deleted_at IS NULL
        """

        password_hash = Usuario.generar_hash(password)
        cursor.execute(sql, (nombre_usuario, password_hash))
        usuario = cursor.fetchone()

        cursor.close()
        conexion.close()

        return usuario
