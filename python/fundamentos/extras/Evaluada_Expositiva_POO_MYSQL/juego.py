from conexion import Conexion
from catalogo import Plataforma, Genero, Formato


class Juego:
    def __init__(
        self,
        id_juego=None,
        titulo=None,
        precio=None,
        stock=None,
        id_plataforma=None,
        id_genero=None,
        id_formato=None,
        created_by=1
    ):
        self.id_juego = id_juego
        self.titulo = titulo
        self.precio = precio
        self.stock = stock
        self.id_plataforma = id_plataforma
        self.id_genero = id_genero
        self.id_formato = id_formato
        self.created_by = created_by

    def mostrar_informacion(self):
        return (
            f"ID: {self.id_juego}, Titulo: {self.titulo}, Precio: ${self.precio}, "
            f"Stock: {self.stock}, Plataforma: {self.id_plataforma}, "
            f"Genero: {self.id_genero}, Formato: {self.id_formato}"
        )

    def guardar(self):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO juego
        (titulo, precio, stock, id_plataforma, id_genero, id_formato, created_by)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            self.titulo,
            self.precio,
            self.stock,
            self.id_plataforma,
            self.id_genero,
            self.id_formato,
            self.created_by
        )

        cursor.execute(sql, valores)
        conexion.commit()
        print("\nJuego creado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def pedir_entero(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Debe ingresar un numero entero.")

    @staticmethod
    def pedir_decimal(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Debe ingresar un numero valido.")

    @staticmethod
    def listar():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            j.id_juego,
            j.titulo,
            j.precio,
            j.stock,
            p.nombre,
            g.nombre,
            f.nombre
        FROM juego j
        INNER JOIN plataforma p ON j.id_plataforma = p.id_plataforma
        INNER JOIN genero g ON j.id_genero = g.id_genero
        INNER JOIN formato f ON j.id_formato = f.id_formato
        WHERE
            j.deleted_at IS NULL
            AND p.deleted_at IS NULL
            AND g.deleted_at IS NULL
            AND f.deleted_at IS NULL
        ORDER BY j.id_juego ASC
        """

        cursor.execute(sql)
        juegos = cursor.fetchall()

        print("\n===== JUEGOS =====\n")
        if not juegos:
            print("No hay juegos registrados.")

        for juego in juegos:
            print(
                f"ID: {juego[0]} | Titulo: {juego[1]} | Precio: ${juego[2]} | "
                f"Stock: {juego[3]} | Plataforma: {juego[4]} | "
                f"Genero: {juego[5]} | Formato: {juego[6]}"
            )

        cursor.close()
        conexion.close()

    @staticmethod
    def buscar():
        texto = input("Ingrese titulo del juego: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            j.id_juego,
            j.titulo,
            j.precio,
            j.stock,
            p.nombre,
            g.nombre,
            f.nombre
        FROM juego j
        INNER JOIN plataforma p ON j.id_plataforma = p.id_plataforma
        INNER JOIN genero g ON j.id_genero = g.id_genero
        INNER JOIN formato f ON j.id_formato = f.id_formato
        WHERE
            j.deleted_at IS NULL
            AND j.titulo LIKE %s
        ORDER BY j.id_juego ASC
        """

        cursor.execute(sql, ("%" + texto + "%",))
        juegos = cursor.fetchall()

        print("\n===== RESULTADOS =====\n")
        if not juegos:
            print("No se encontraron juegos.")

        for juego in juegos:
            print(
                f"ID: {juego[0]} | Titulo: {juego[1]} | Precio: ${juego[2]} | "
                f"Stock: {juego[3]} | Plataforma: {juego[4]} | "
                f"Genero: {juego[5]} | Formato: {juego[6]}"
            )

        cursor.close()
        conexion.close()

    @staticmethod
    def actualizar():
        id_juego = Juego.pedir_entero("Ingrese ID del juego: ")
        titulo = input("Nuevo titulo: ")
        precio = Juego.pedir_decimal("Nuevo precio: ")
        stock = Juego.pedir_entero("Nuevo stock: ")

        print("\nPLATAFORMAS DISPONIBLES")
        Plataforma.listar()
        id_plataforma = Juego.pedir_entero("\nNuevo ID plataforma: ")

        print("\nGENEROS DISPONIBLES")
        Genero.listar()
        id_genero = Juego.pedir_entero("\nNuevo ID genero: ")

        print("\nFORMATOS DISPONIBLES")
        Formato.listar()
        id_formato = Juego.pedir_entero("\nNuevo ID formato: ")

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE juego
        SET
            titulo = %s,
            precio = %s,
            stock = %s,
            id_plataforma = %s,
            id_genero = %s,
            id_formato = %s,
            updated_at = NOW()
        WHERE id_juego = %s AND deleted_at IS NULL
        """

        valores = (
            titulo,
            precio,
            stock,
            id_plataforma,
            id_genero,
            id_formato,
            id_juego
        )
        cursor.execute(sql, valores)
        conexion.commit()
        print("\nJuego actualizado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar():
        id_juego = Juego.pedir_entero("Ingrese ID del juego: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE juego
        SET deleted_at = NOW()
        WHERE id_juego = %s AND deleted_at IS NULL
        """

        cursor.execute(sql, (id_juego,))
        conexion.commit()
        print("\nJuego eliminado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def vender(id_juego, cantidad):
        if cantidad <= 0:
            return False

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql_stock = """
        SELECT stock
        FROM juego
        WHERE id_juego = %s AND deleted_at IS NULL
        """

        cursor.execute(sql_stock, (id_juego,))
        resultado = cursor.fetchone()

        if resultado is None or resultado[0] < cantidad:
            cursor.close()
            conexion.close()
            return False

        sql_update = """
        UPDATE juego
        SET stock = stock - %s, updated_at = NOW()
        WHERE id_juego = %s
        """

        cursor.execute(sql_update, (cantidad, id_juego))
        conexion.commit()

        cursor.close()
        conexion.close()
        return True
