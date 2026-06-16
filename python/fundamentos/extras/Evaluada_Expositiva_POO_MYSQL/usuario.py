import hashlib

from conexion import Conexion


class Usuario:
    def __init__(
        self,
        id_usuario=None,
        nombre_usuario=None,
        correo=None,
        id_tipo_usuario=2,
        password=None,
        created_by=None
    ):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.id_tipo_usuario = id_tipo_usuario
        self.password = password
        self.created_by = created_by

    def mostrar_datos(self):
        return f"ID: {self.id_usuario}, Usuario: {self.nombre_usuario}, Correo: {self.correo}"

    @staticmethod
    def generar_hash(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def guardar(self):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO usuario (id_tipo_usuario, nombre_usuario, correo, password_hash, created_by)
        VALUES (%s, %s, %s, %s, %s)
        """

        password_hash = None
        if self.password:
            password_hash = Usuario.generar_hash(self.password)

        cursor.execute(
            sql,
            (
                self.id_tipo_usuario,
                self.nombre_usuario,
                self.correo,
                password_hash,
                self.created_by
            )
        )
        conexion.commit()
        print("\nUsuario creado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def listar():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT u.id_usuario, u.nombre_usuario, u.correo, t.nombre
        FROM usuario u
        INNER JOIN tipo_usuario t ON u.id_tipo_usuario = t.id_tipo_usuario
        WHERE u.deleted_at IS NULL
        ORDER BY u.id_usuario ASC
        """

        cursor.execute(sql)
        usuarios = cursor.fetchall()

        print("\n===== USUARIOS =====\n")
        if not usuarios:
            print("No hay usuarios registrados.")

        for usuario in usuarios:
            print(f"ID: {usuario[0]} | Usuario: {usuario[1]} | Correo: {usuario[2]} | Rol: {usuario[3]}")

        cursor.close()
        conexion.close()

    @staticmethod
    def buscar():
        texto = input("Ingrese nombre o correo: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT u.id_usuario, u.nombre_usuario, u.correo, t.nombre
        FROM usuario u
        INNER JOIN tipo_usuario t ON u.id_tipo_usuario = t.id_tipo_usuario
        WHERE u.deleted_at IS NULL
        AND (u.nombre_usuario LIKE %s OR u.correo LIKE %s)
        ORDER BY u.id_usuario ASC
        """

        valor = "%" + texto + "%"
        cursor.execute(sql, (valor, valor))
        usuarios = cursor.fetchall()

        print("\n===== RESULTADOS =====\n")
        if not usuarios:
            print("No se encontraron usuarios.")

        for usuario in usuarios:
            print(f"ID: {usuario[0]} | Usuario: {usuario[1]} | Correo: {usuario[2]} | Rol: {usuario[3]}")

        cursor.close()
        conexion.close()

    @staticmethod
    def actualizar():
        id_usuario = input("Ingrese ID del usuario: ")
        nombre_usuario = input("Nuevo nombre de usuario: ")
        correo = input("Nuevo correo: ")
        Usuario.listar_tipos()
        id_tipo_usuario = input("Nuevo ID de rol: ")
        password = input("Nueva password si sera administrador, Enter para mantener: ")

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        if password:
            sql = """
            UPDATE usuario
            SET id_tipo_usuario = %s, nombre_usuario = %s, correo = %s,
                password_hash = %s, updated_at = NOW()
            WHERE id_usuario = %s AND deleted_at IS NULL
            """
            valores = (
                id_tipo_usuario,
                nombre_usuario,
                correo,
                Usuario.generar_hash(password),
                id_usuario
            )
        else:
            sql = """
            UPDATE usuario
            SET id_tipo_usuario = %s, nombre_usuario = %s, correo = %s, updated_at = NOW()
            WHERE id_usuario = %s AND deleted_at IS NULL
            """
            valores = (id_tipo_usuario, nombre_usuario, correo, id_usuario)

        cursor.execute(sql, valores)
        conexion.commit()
        print("\nUsuario actualizado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def listar_tipos():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            id_tipo_usuario,
            nombre,
            descripcion,
            puede_crear,
            puede_leer,
            puede_actualizar,
            puede_eliminar,
            puede_gestionar_usuarios
        FROM tipo_usuario
        ORDER BY id_tipo_usuario ASC
        """

        cursor.execute(sql)
        tipos = cursor.fetchall()

        print("\n===== ROLES DISPONIBLES =====\n")
        for tipo in tipos:
            permisos = []
            if tipo[3]:
                permisos.append("crear")
            if tipo[4]:
                permisos.append("leer")
            if tipo[5]:
                permisos.append("actualizar")
            if tipo[6]:
                permisos.append("eliminar")
            if tipo[7]:
                permisos.append("usuarios")
            print(f"ID: {tipo[0]} | Rol: {tipo[1]} | Permisos: {', '.join(permisos)}")

        cursor.close()
        conexion.close()

    @staticmethod
    def obtener_por_id(id_usuario):
        conexion = Conexion.conectar()
        cursor = conexion.cursor(dictionary=True)

        sql = """
        SELECT
            u.id_usuario,
            u.nombre_usuario,
            u.correo,
            u.password_hash,
            t.id_tipo_usuario,
            t.nombre AS tipo_usuario,
            t.puede_crear,
            t.puede_leer,
            t.puede_actualizar,
            t.puede_eliminar,
            t.puede_gestionar_usuarios
        FROM usuario u
        INNER JOIN tipo_usuario t ON u.id_tipo_usuario = t.id_tipo_usuario
        WHERE u.id_usuario = %s AND u.deleted_at IS NULL
        """

        cursor.execute(sql, (id_usuario,))
        usuario = cursor.fetchone()

        cursor.close()
        conexion.close()
        return usuario

    @staticmethod
    def validar_password(usuario, password):
        if not usuario["password_hash"]:
            return False

        return usuario["password_hash"] == Usuario.generar_hash(password)

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
