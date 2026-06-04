# Importamos la clase Conexion para reutilizar
# la conexión a la base de datos.
from conexion import Conexion


class Estudiante:
    """
    Clase que representa un estudiante.

    Cada objeto Estudiante almacenará:
    - nombre
    - curso
    - usuario que creó el registro
    """

    # =====================================
    # CONSTRUCTOR
    # =====================================

    def __init__(self, nombre=None, curso=None, created_by="admin"):
        """
        Constructor de la clase.
        Se ejecuta automáticamente cuando
        creamos un objeto Estudiante.

        Ejemplo:

        estudiante = Estudiante(
            "Juan Pérez",
            "3A"
        )
        """
        self.nombre = nombre
        self.curso = curso
        self.created_by = created_by

    # =====================================
    # GUARDAR ESTUDIANTE
    # =====================================

    def guardar(self):
        """
        Inserta un nuevo estudiante en
        la base de datos utilizando los
        atributos almacenados en el objeto.
        """
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO estudiantes
        (
            nombre,
            curso,
            created_by
        )
        VALUES
        (
            %s,
            %s,
            %s
        )
        """

        valores = (
            self.nombre,
            self.curso,
            self.created_by
        )

        cursor.execute(sql, valores)

        # Guarda los cambios realizados
        conexion.commit()
        print("\nEstudiante agregado correctamente.")
        cursor.close()
        conexion.close()

    # =====================================
    # LISTAR ESTUDIANTES
    # =====================================

    @staticmethod
    def listar():
        """
        Muestra todos los estudiantes activos.

        Se utiliza un método estático porque
        no necesitamos crear un objeto para
        realizar una consulta general.
        """
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            id_estudiante,
            nombre,
            curso
        FROM estudiantes
        WHERE deleted = 0
        ORDER BY nombre ASC
        """

        cursor.execute(sql)
        estudiantes = cursor.fetchall()
        print("\n===== ESTUDIANTES =====\n")
        for estudiante in estudiantes:
            print(
                f"ID: {estudiante[0]} | "
                f"Nombre: {estudiante[1]} | "
                f"Curso: {estudiante[2]}"
            )

        cursor.close()
        conexion.close()

    # =====================================
    # BUSCAR ESTUDIANTE
    # =====================================

    @staticmethod
    def buscar():
        """
        Busca estudiantes utilizando LIKE.
        """
        texto = input("Ingrese nombre o parte del nombre: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            id_estudiante,
            nombre,
            curso
        FROM estudiantes
        WHERE nombre LIKE %s
        AND deleted = 0
        ORDER BY nombre ASC
        """

        cursor.execute(sql,('%' + texto + '%',))

        resultados = cursor.fetchall()
        print("\n===== RESULTADOS =====\n")
        if len(resultados) == 0:
            print("No se encontraron registros.")

        else:

            for estudiante in resultados:

                print(
                    f"ID: {estudiante[0]} | "
                    f"Nombre: {estudiante[1]} | "
                    f"Curso: {estudiante[2]}"
                )

        cursor.close()
        conexion.close()

    # =====================================
    # ACTUALIZAR CURSO
    # =====================================

    @staticmethod
    def actualizar():
        """
        Permite modificar el curso
        de un estudiante.
        """

        id_estudiante = input("Ingrese ID del estudiante: ")
        nuevo_curso = input("Ingrese nuevo curso: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE estudiantes
        SET curso = %s
        WHERE id_estudiante = %s
        """

        valores = (nuevo_curso,id_estudiante)
        cursor.execute(sql, valores)
        conexion.commit()
        print("\nCurso actualizado correctamente.")

        cursor.close()
        conexion.close()

    # =====================================
    # ELIMINAR ESTUDIANTE
    # =====================================

    @staticmethod
    def eliminar():
        """
        Realiza un borrado lógico.

        No elimina físicamente el registro.
        Solo cambia el campo deleted a 1.
        """

        id_estudiante = input("Ingrese ID del estudiante: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE estudiantes
        SET deleted = 1
        WHERE id_estudiante = %s
        """

        cursor.execute(sql,(id_estudiante,))
        conexion.commit()

        print(
            "\nEstudiante eliminado correctamente."
        )

        cursor.close()
        conexion.close()