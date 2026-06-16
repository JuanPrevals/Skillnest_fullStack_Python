from conexion import Conexion


class Cliente:
    def __init__(
        self,
        id_cliente=None,
        rut=None,
        nombre=None,
        telefono=None,
        correo=None,
        created_by=1
    ):
        self.id_cliente = id_cliente
        self.rut = rut
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.created_by = created_by

    def mostrar_datos(self):
        return (
            f"ID: {self.id_cliente}, RUT: {self.rut}, Nombre: {self.nombre}, "
            f"Telefono: {self.telefono}, Correo: {self.correo}"
        )

    def guardar(self):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO cliente (rut, nombre, telefono, correo, created_by)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (
                self.rut,
                self.nombre,
                self.telefono,
                self.correo,
                self.created_by
            )
        )
        conexion.commit()
        print("\nCliente creado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def listar():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT id_cliente, rut, nombre, telefono, correo
        FROM cliente
        WHERE deleted_at IS NULL
        ORDER BY id_cliente ASC
        """

        cursor.execute(sql)
        clientes = cursor.fetchall()

        print("\n===== CLIENTES =====\n")
        if not clientes:
            print("No hay clientes registrados.")

        for cliente in clientes:
            print(
                f"ID: {cliente[0]} | RUT: {cliente[1]} | Nombre: {cliente[2]} | "
                f"Telefono: {cliente[3]} | Correo: {cliente[4]}"
            )

        cursor.close()
        conexion.close()

    @staticmethod
    def buscar():
        texto = input("Ingrese nombre, RUT o correo: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT id_cliente, rut, nombre, telefono, correo
        FROM cliente
        WHERE deleted_at IS NULL
        AND (rut LIKE %s OR nombre LIKE %s OR correo LIKE %s)
        ORDER BY id_cliente ASC
        """

        valor = "%" + texto + "%"
        cursor.execute(sql, (valor, valor, valor))
        clientes = cursor.fetchall()

        print("\n===== RESULTADOS =====\n")
        if not clientes:
            print("No se encontraron clientes.")

        for cliente in clientes:
            print(
                f"ID: {cliente[0]} | RUT: {cliente[1]} | Nombre: {cliente[2]} | "
                f"Telefono: {cliente[3]} | Correo: {cliente[4]}"
            )

        cursor.close()
        conexion.close()

    @staticmethod
    def actualizar():
        id_cliente = input("Ingrese ID del cliente: ")
        rut = input("Nuevo RUT: ")
        nombre = input("Nuevo nombre: ")
        telefono = input("Nuevo telefono: ")
        correo = input("Nuevo correo: ")

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE cliente
        SET rut = %s, nombre = %s, telefono = %s, correo = %s, updated_at = NOW()
        WHERE id_cliente = %s AND deleted_at IS NULL
        """

        cursor.execute(
            sql,
            (
                rut,
                nombre,
                telefono,
                correo,
                id_cliente
            )
        )
        conexion.commit()
        print("\nCliente actualizado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar():
        id_cliente = input("Ingrese ID del cliente: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE cliente
        SET deleted_at = NOW()
        WHERE id_cliente = %s AND deleted_at IS NULL
        """

        cursor.execute(sql, (id_cliente,))
        conexion.commit()
        print("\nCliente eliminado correctamente.")

        cursor.close()
        conexion.close()
