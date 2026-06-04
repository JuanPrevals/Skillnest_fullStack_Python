from conexion import Conexion
from juego import Juego


class Compra:
    def __init__(self, id_compra=None, id_cliente=None, id_juego=None,
                 cantidad=None, precio_unitario=None, created_by=1):
        self.id_compra = id_compra
        self.id_cliente = id_cliente
        self.id_juego = id_juego
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.created_by = created_by

    def registrar_compra(self):
        return self.guardar()

    def total(self):
        return self.cantidad * self.precio_unitario

    def mostrar_informacion(self):
        return (
            f"ID: {self.id_compra}, Cliente: {self.id_cliente}, "
            f"Juego: {self.id_juego}, Cantidad: {self.cantidad}, "
            f"Total: ${self.total()}"
        )

    def guardar(self):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql_precio = """
        SELECT precio
        FROM juego
        WHERE id_juego = %s AND deleted_at IS NULL
        """

        cursor.execute(sql_precio, (self.id_juego,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("\nEl juego no existe.")
            cursor.close()
            conexion.close()
            return

        self.precio_unitario = resultado[0]
        cursor.close()
        conexion.close()

        if not Juego.vender(self.id_juego, self.cantidad):
            print("\nNo hay stock suficiente.")
            return

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO compra_juego
        (id_cliente, id_juego, cantidad, precio_unitario, created_by)
        VALUES (%s, %s, %s, %s, %s)
        """

        valores = (
            self.id_cliente,
            self.id_juego,
            self.cantidad,
            self.precio_unitario,
            self.created_by
        )

        cursor.execute(sql, valores)
        conexion.commit()
        print("\nCompra registrada correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def listar():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            c.id_compra,
            cl.nombre,
            j.titulo,
            c.cantidad,
            c.precio_unitario,
            (c.cantidad * c.precio_unitario) AS total,
            c.fecha
        FROM compra_juego c
        INNER JOIN cliente cl ON c.id_cliente = cl.id_cliente
        INNER JOIN juego j ON c.id_juego = j.id_juego
        WHERE
            c.deleted_at IS NULL
            AND cl.deleted_at IS NULL
            AND j.deleted_at IS NULL
        ORDER BY c.id_compra ASC
        """

        cursor.execute(sql)
        compras = cursor.fetchall()

        print("\n===== COMPRAS =====\n")
        if not compras:
            print("No hay compras registradas.")

        for compra in compras:
            print(
                f"ID: {compra[0]} | Cliente: {compra[1]} | Juego: {compra[2]} | "
                f"Cantidad: {compra[3]} | Precio: ${compra[4]} | "
                f"Total: ${compra[5]} | Fecha: {compra[6]}"
            )

        cursor.close()
        conexion.close()

    @staticmethod
    def buscar():
        texto = input("Ingrese nombre de cliente o titulo del juego: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            c.id_compra,
            cl.nombre,
            j.titulo,
            c.cantidad,
            c.precio_unitario,
            (c.cantidad * c.precio_unitario) AS total,
            c.fecha
        FROM compra_juego c
        INNER JOIN cliente cl ON c.id_cliente = cl.id_cliente
        INNER JOIN juego j ON c.id_juego = j.id_juego
        WHERE
            c.deleted_at IS NULL
            AND (cl.nombre LIKE %s OR j.titulo LIKE %s)
        ORDER BY c.id_compra ASC
        """

        valor = "%" + texto + "%"
        cursor.execute(sql, (valor, valor))
        compras = cursor.fetchall()

        print("\n===== RESULTADOS =====\n")
        if not compras:
            print("No se encontraron compras.")

        for compra in compras:
            print(
                f"ID: {compra[0]} | Cliente: {compra[1]} | Juego: {compra[2]} | "
                f"Cantidad: {compra[3]} | Precio: ${compra[4]} | "
                f"Total: ${compra[5]} | Fecha: {compra[6]}"
            )

        cursor.close()
        conexion.close()

    @staticmethod
    def actualizar():
        id_compra = input("Ingrese ID de la compra: ")
        cantidad = input("Nueva cantidad: ")

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE compra_juego
        SET cantidad = %s, updated_at = NOW()
        WHERE id_compra = %s AND deleted_at IS NULL
        """

        cursor.execute(sql, (cantidad, id_compra))
        conexion.commit()
        print("\nCompra actualizada correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar():
        id_compra = input("Ingrese ID de la compra: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE compra_juego
        SET deleted_at = NOW()
        WHERE id_compra = %s AND deleted_at IS NULL
        """

        cursor.execute(sql, (id_compra,))
        conexion.commit()
        print("\nCompra eliminada correctamente.")

        cursor.close()
        conexion.close()
