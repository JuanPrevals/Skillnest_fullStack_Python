from conexion import Conexion


class Plataforma:
    def __init__(self, id_plataforma=None, nombre=None, created_by=1):
        self.id_plataforma = id_plataforma
        self.nombre = nombre
        self.created_by = created_by

    def mostrar_informacion(self):
        return f"ID: {self.id_plataforma}, Plataforma: {self.nombre}"

    def guardar(self):
        guardar_catalogo(
            "plataforma",
            "id_plataforma",
            self.nombre,
            self.created_by,
            "Plataforma"
        )

    @staticmethod
    def listar():
        listar_catalogo("plataforma", "id_plataforma", "Plataformas")

    @staticmethod
    def buscar():
        buscar_catalogo("plataforma", "id_plataforma", "Plataformas")

    @staticmethod
    def actualizar():
        actualizar_catalogo("plataforma", "id_plataforma", "Plataforma")

    @staticmethod
    def eliminar():
        eliminar_catalogo("plataforma", "id_plataforma", "Plataforma")


class Genero:
    def __init__(self, id_genero=None, nombre=None, created_by=1):
        self.id_genero = id_genero
        self.nombre = nombre
        self.created_by = created_by

    def mostrar_informacion(self):
        return f"ID: {self.id_genero}, Genero: {self.nombre}"

    def guardar(self):
        guardar_catalogo(
            "genero",
            "id_genero",
            self.nombre,
            self.created_by,
            "Genero"
        )

    @staticmethod
    def listar():
        listar_catalogo("genero", "id_genero", "Generos")

    @staticmethod
    def buscar():
        buscar_catalogo("genero", "id_genero", "Generos")

    @staticmethod
    def actualizar():
        actualizar_catalogo("genero", "id_genero", "Genero")

    @staticmethod
    def eliminar():
        eliminar_catalogo("genero", "id_genero", "Genero")


class Formato:
    def __init__(self, id_formato=None, nombre=None, created_by=1):
        self.id_formato = id_formato
        self.nombre = nombre
        self.created_by = created_by

    def mostrar_informacion(self):
        return f"ID: {self.id_formato}, Formato: {self.nombre}"

    def guardar(self):
        guardar_catalogo(
            "formato",
            "id_formato",
            self.nombre,
            self.created_by,
            "Formato"
        )

    @staticmethod
    def listar():
        listar_catalogo("formato", "id_formato", "Formatos")

    @staticmethod
    def buscar():
        buscar_catalogo("formato", "id_formato", "Formatos")

    @staticmethod
    def actualizar():
        actualizar_catalogo("formato", "id_formato", "Formato")

    @staticmethod
    def eliminar():
        eliminar_catalogo("formato", "id_formato", "Formato")


def guardar_catalogo(tabla, id_columna, nombre, created_by, etiqueta):
    conexion = Conexion.conectar()
    cursor = conexion.cursor()

    sql = f"""
    INSERT INTO {tabla} (nombre, created_by)
    VALUES (%s, %s)
    """

    cursor.execute(sql, (nombre, created_by))
    conexion.commit()
    print(f"\n{etiqueta} creado correctamente.")

    cursor.close()
    conexion.close()


def listar_catalogo(tabla, id_columna, titulo):
    conexion = Conexion.conectar()
    cursor = conexion.cursor()

    sql = f"""
    SELECT {id_columna}, nombre
    FROM {tabla}
    WHERE deleted_at IS NULL
    ORDER BY {id_columna} ASC
    """

    cursor.execute(sql)
    resultados = cursor.fetchall()

    print(f"\n===== {titulo.upper()} =====\n")
    if not resultados:
        print("No hay registros.")

    for fila in resultados:
        print(f"ID: {fila[0]} | Nombre: {fila[1]}")

    cursor.close()
    conexion.close()


def buscar_catalogo(tabla, id_columna, titulo):
    texto = input("Ingrese nombre a buscar: ")
    conexion = Conexion.conectar()
    cursor = conexion.cursor()

    sql = f"""
    SELECT {id_columna}, nombre
    FROM {tabla}
    WHERE deleted_at IS NULL
    AND nombre LIKE %s
    ORDER BY {id_columna} ASC
    """

    cursor.execute(sql, ("%" + texto + "%",))
    resultados = cursor.fetchall()

    print(f"\n===== RESULTADOS {titulo.upper()} =====\n")
    if not resultados:
        print("No se encontraron registros.")

    for fila in resultados:
        print(f"ID: {fila[0]} | Nombre: {fila[1]}")

    cursor.close()
    conexion.close()


def actualizar_catalogo(tabla, id_columna, etiqueta):
    id_registro = input(f"Ingrese ID de {etiqueta.lower()}: ")
    nombre = input("Nuevo nombre: ")

    conexion = Conexion.conectar()
    cursor = conexion.cursor()

    sql = f"""
    UPDATE {tabla}
    SET nombre = %s, updated_at = NOW()
    WHERE {id_columna} = %s AND deleted_at IS NULL
    """

    cursor.execute(sql, (nombre, id_registro))
    conexion.commit()
    print(f"\n{etiqueta} actualizado correctamente.")

    cursor.close()
    conexion.close()


def eliminar_catalogo(tabla, id_columna, etiqueta):
    id_registro = input(f"Ingrese ID de {etiqueta.lower()}: ")

    conexion = Conexion.conectar()
    cursor = conexion.cursor()

    sql = f"""
    UPDATE {tabla}
    SET deleted_at = NOW()
    WHERE {id_columna} = %s AND deleted_at IS NULL
    """

    cursor.execute(sql, (id_registro,))
    conexion.commit()
    print(f"\n{etiqueta} eliminado correctamente.")

    cursor.close()
    conexion.close()


def obtener_id_catalogo(tabla, id_columna, valor):
    conexion = Conexion.conectar()
    cursor = conexion.cursor()

    valor = str(valor).strip()

    if valor.isdigit():
        sql = f"""
        SELECT {id_columna}
        FROM {tabla}
        WHERE {id_columna} = %s AND deleted_at IS NULL
        """
    else:
        sql = f"""
        SELECT {id_columna}
        FROM {tabla}
        WHERE nombre = %s AND deleted_at IS NULL
        """

    cursor.execute(sql, (valor,))
    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if resultado is None:
        return None

    return resultado[0]


def pedir_id_catalogo(tabla, id_columna, etiqueta):
    while True:
        valor = input(f"\nID o nombre de {etiqueta.lower()}: ")
        id_registro = obtener_id_catalogo(tabla, id_columna, valor)

        if id_registro is not None:
            return id_registro

        print(f"{etiqueta} no existe. Ingrese un ID o nombre valido.")
