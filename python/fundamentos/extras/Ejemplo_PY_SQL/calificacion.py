# Importamos la clase Conexion para reutilizar
# la conexión a la base de datos.
from conexion import Conexion


class Calificacion:
    """
    Representa una calificación asociada
    a un estudiante y una asignatura.
    """

    def __init__(self,id_estudiante=None,id_asignatura=None,nota=None,fecha_evaluacion=None,created_by="profesor"):
        """
        Constructor de la clase.

        Se ejecuta automáticamente cuando
        creamos un objeto Calificacion.
        """
        self.id_estudiante = id_estudiante
        self.id_asignatura = id_asignatura
        self.nota = nota
        self.fecha_evaluacion = fecha_evaluacion
        self.created_by = created_by

    # =====================================
    # GUARDAR CALIFICACIÓN
    # =====================================

    def guardar(self):
        """
        Inserta una nueva calificación
        en la base de datos.
        """

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO calificaciones
        (
            id_estudiante,
            id_asignatura,
            nota,
            fecha_evaluacion,
            created_by
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """

        valores = (
            self.id_estudiante,
            self.id_asignatura,
            self.nota,
            self.fecha_evaluacion,
            self.created_by
        )

        cursor.execute(sql, valores)

        # Guarda los cambios en MySQL
        conexion.commit()
        print("\nCalificación registrada correctamente.")
        cursor.close()
        conexion.close()

    # =====================================
    # LISTAR ASIGNATURAS
    # =====================================

    @staticmethod
    def listar_asignaturas():
        """
        Muestra todas las asignaturas activas.
        """
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            id_asignatura,
            nombre_asignatura
        FROM asignaturas
        WHERE deleted = 0
        ORDER BY nombre_asignatura ASC
        """

        cursor.execute(sql)
        asignaturas = cursor.fetchall()
        print("\n===== ASIGNATURAS =====\n")

        for asignatura in asignaturas:
            print(
                f"ID: {asignatura[0]} | "
                f"{asignatura[1]}"
            )

        cursor.close()
        conexion.close()

    # =====================================
    # VER TODAS LAS CALIFICACIONES
    # =====================================

    @staticmethod
    def ver_calificaciones():
        """
        Muestra todas las calificaciones
        utilizando INNER JOIN.
        """

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            e.id_estudiante,
            e.nombre,
            e.curso,
            a.nombre_asignatura,
            c.nota,
            c.fecha_evaluacion
        FROM calificaciones c
        INNER JOIN estudiantes e
            ON c.id_estudiante = e.id_estudiante
        INNER JOIN asignaturas a
            ON c.id_asignatura = a.id_asignatura
        WHERE
            c.deleted = 0
            AND e.deleted = 0
            AND a.deleted = 0
        ORDER BY
            e.nombre ASC,
            a.nombre_asignatura ASC
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        print("\n===== CALIFICACIONES =====\n")

        for fila in resultados:
            print(
                f"ID: {fila[0]} | "
                f"Alumno: {fila[1]} | "
                f"Curso: {fila[2]} | "
                f"Asignatura: {fila[3]} | "
                f"Nota: {fila[4]} | "
                f"Fecha: {fila[5]}"
            )

        cursor.close()
        conexion.close()

    # =====================================
    # VER NOTAS DE UN ESTUDIANTE
    # =====================================

    @staticmethod
    def ver_notas_estudiante():
        """
        Muestra todas las notas de un
        estudiante específico.
        """
        id_estudiante = input("\nIngrese ID del estudiante: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            e.nombre,
            a.nombre_asignatura,
            c.nota,
            c.fecha_evaluacion

        FROM calificaciones c

        INNER JOIN estudiantes e
            ON c.id_estudiante = e.id_estudiante

        INNER JOIN asignaturas a
            ON c.id_asignatura = a.id_asignatura

        WHERE
            e.id_estudiante = %s
            AND c.deleted = 0
            AND e.deleted = 0
            AND a.deleted = 0

        ORDER BY
            a.nombre_asignatura
        """

        cursor.execute(sql,(id_estudiante,))

        resultados = cursor.fetchall()

        print("\n===== NOTAS DEL ESTUDIANTE =====\n")

        for fila in resultados:

            print(
                f"Alumno: {fila[0]} | "
                f"Asignatura: {fila[1]} | "
                f"Nota: {fila[2]} | "
                f"Fecha: {fila[3]}"
            )

        cursor.close()
        conexion.close()

    # =====================================
    # BUSCAR NOTAS ENTRE RANGOS
    # =====================================

    @staticmethod
    def buscar_por_rango():
        """
        Utiliza BETWEEN para buscar
        notas dentro de un rango.
        """
        nota_minima = float(input("Nota mínima: "))
        nota_maxima = float(input("Nota máxima: "))

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT

            e.nombre,
            a.nombre_asignatura,
            c.nota

        FROM calificaciones c

        INNER JOIN estudiantes e
            ON c.id_estudiante = e.id_estudiante

        INNER JOIN asignaturas a
            ON c.id_asignatura = a.id_asignatura

        WHERE

            c.nota BETWEEN %s AND %s

            AND c.deleted = 0
            AND e.deleted = 0
            AND a.deleted = 0

        ORDER BY
            c.nota DESC
        """

        cursor.execute(
            sql,
            (
                nota_minima,
                nota_maxima
            )
        )

        resultados = cursor.fetchall()

        print("\n===== RESULTADOS =====\n")

        for fila in resultados:

            print(
                f"{fila[0]} | "
                f"{fila[1]} | "
                f"Nota: {fila[2]}"
            )

        cursor.close()
        conexion.close()

    # =====================================
    # VER PROMEDIOS
    # =====================================

    @staticmethod
    def ver_promedios():
        """
        Calcula el promedio de cada estudiante
        utilizando AVG y GROUP BY.
        """

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT

            e.nombre,

            ROUND(
                AVG(c.nota),
                2
            ) AS promedio

        FROM calificaciones c

        INNER JOIN estudiantes e
            ON c.id_estudiante = e.id_estudiante

        WHERE
            c.deleted = 0
            AND e.deleted = 0

        GROUP BY
            e.id_estudiante,
            e.nombre

        ORDER BY
            promedio DESC
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        print("\n===== PROMEDIOS =====\n")

        for fila in resultados:

            print(
                f"{fila[0]} "
                f"→ Promedio: {fila[1]}"
            )

        cursor.close()
        conexion.close()