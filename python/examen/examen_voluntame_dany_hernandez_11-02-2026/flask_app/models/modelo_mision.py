from flask_app.config.mysql_connection import connect_to_mysql
from flask import flash
from datetime import datetime, date
from flask_app.models.modelo_usuario import Usuario # Importamos para atar el creador a la misión

# CLASE MISIÓN
class Mision:
    def __init__(self, data):
        # Mapeamos las columnas de la tabla 'misiones'
        self.id_mision = data.get('id_mision')
        self.nombre = data.get('nombre')
        self.fecha = data.get('fecha')
        self.voluntarios_necesarios = data.get('voluntarios_necesarios')
        self.descripcion = data.get('descripcion')
        self.usuario_id = data.get('usuario_id')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        
        self.lider = None       # Guardará el objeto Usuario del creador
        self.voluntarios = []   # Guardará una lista de Usuarios que dieron clic en "Voluntarme"


    # CRUD 
    @classmethod
    def guardar(cls, formulario):
        """Inserta una nueva misión en la base de datos."""
        query = """
            INSERT INTO misiones (nombre, fecha, voluntarios_necesarios, descripcion, usuario_id)
            VALUES (%(nombre)s, %(fecha)s, %(voluntarios_necesarios)s, %(descripcion)s, %(usuario_id)s);
        """
        return connect_to_mysql('voluntame_db').query_db(query, formulario)

    @classmethod
    def actualizar(cls, formulario):
        """Actualiza los datos de una misión existente."""
        query = """
            UPDATE misiones 
            SET nombre = %(nombre)s, fecha = %(fecha)s, 
                voluntarios_necesarios = %(voluntarios_necesarios)s, descripcion = %(descripcion)s
            WHERE id_mision = %(id_mision)s;
        """
        return connect_to_mysql('voluntame_db').query_db(query, formulario)

    @classmethod
    def eliminar(cls, formulario):
        """Elimina una misión por su ID."""
        query = "DELETE FROM misiones WHERE id_mision = %(id_mision)s;"
        return connect_to_mysql('voluntame_db').query_db(query, formulario)

    # MÉTODOS AVANZADOS
    @classmethod
    def obtener_todas_futuras(cls):
        """
        Petición de Bonus: 
        Filtra fechas pasadas (>= CURRENT_DATE) y ordena por fecha más cercana (ASC).
        """
        query = """
            SELECT * FROM misiones
            JOIN usuarios ON misiones.usuario_id = usuarios.id_usuario
            WHERE fecha >= CURRENT_DATE
            ORDER BY fecha ASC;
        """
        resultados = connect_to_mysql('voluntame_db').query_db(query)
        misiones = []
        
        if not resultados:
            return misiones
            
        for fila in resultados:
            mision_actual = cls(fila)
            
            # Preparamos los datos del líder usando .get() por seguridad
            datos_lider = {
                "id_usuario": fila['id_usuario'],
                "nombre": fila['nombre'],
                "apellido": fila['apellido'],
                "email": fila['email'],
                "contrasena": fila['contrasena'],
                "created_at": fila.get('usuarios.created_at'),
                "updated_at": fila.get('usuarios.updated_at')
            }
            mision_actual.lider = Usuario(datos_lider)
            misiones.append(mision_actual)
            
        return misiones

    @classmethod
    def obtener_por_id_con_relaciones(cls, formulario):
        """Obtiene una misión específica, adjunta a su líder y a la lista de voluntarios."""
        # 1. Traer la misión y el líder
        query_mision = """
            SELECT * FROM misiones
            JOIN usuarios ON misiones.usuario_id = usuarios.id_usuario
            WHERE id_mision = %(id_mision)s;
        """
        resultado = connect_to_mysql('voluntame_db').query_db(query_mision, formulario)
        
        if not resultado:
            return False
            
        fila = resultado[0]
        mision_encontrada = cls(fila)
        
        datos_lider = {
            "id_usuario": fila['id_usuario'],
            "nombre": fila['nombre'],
            "apellido": fila['apellido'],
            "email": fila['email'],
            "contrasena": fila['contrasena'],
            "created_at": fila.get('usuarios.created_at'),
            "updated_at": fila.get('usuarios.updated_at')
        }
        mision_encontrada.lider = Usuario(datos_lider)
        
        # 2. Traer a los voluntarios (BONUS ORO)
        query_voluntarios = """
            SELECT usuarios.* FROM usuarios
            JOIN voluntarios_misiones ON usuarios.id_usuario = voluntarios_misiones.usuario_id
            WHERE voluntarios_misiones.mision_id = %(id_mision)s;
        """
        resultados_voluntarios = connect_to_mysql('voluntame_db').query_db(query_voluntarios, formulario)
        
        # Si hay voluntarios, los convertimos en objetos Usuario y los guardamos en la lista
        if resultados_voluntarios:
            for vol in resultados_voluntarios:
                mision_encontrada.voluntarios.append(Usuario(vol))
                
        return mision_encontrada

    # MÉTODOS PARA LA RELACIÓN N:M --> El voluntario queda registrado para la misión
    @classmethod
    def agregar_voluntario(cls, formulario):
        """Inserta el registro en la tabla intermedia cuando alguien hace clic en 'Voluntarme'."""
        query = """
            INSERT INTO voluntarios_misiones (usuario_id, mision_id)
            VALUES (%(usuario_id)s, %(id_mision)s);
        """
        return connect_to_mysql('voluntame_db').query_db(query, formulario)

    # VALIDACIONES
    @staticmethod
    def validar_mision(formulario):
        """Valida campos vacíos, rango de voluntarios y fechas futuras."""
        es_valido = True
        
        if len(formulario['nombre']) < 3:
            flash("El nombre de la misión debe tener al menos 3 caracteres.", "mision")
            es_valido = False
            
        if len(formulario['descripcion']) < 3:
            flash("La descripción no puede estar vacía y debe ser clara.", "mision")
            es_valido = False

        # Validación estricta de rango de voluntariados
        try:
            voluntarios = int(formulario['voluntarios_necesarios'])
            if voluntarios < 2 or voluntarios > 20:
                flash("Los voluntarios necesarios deben ser un número entre 2 y 20.", "mision")
                es_valido = False
        except ValueError:
            flash("Debes ingresar un número válido de voluntarios.", "mision")
            es_valido = False

        # Validación estricta de fecha para el pasado
        if not formulario['fecha']:
            flash("Debes ingresar una fecha.", "mision")
            es_valido = False
        else:
            fecha_ingresada = datetime.strptime(formulario['fecha'], '%Y-%m-%d').date()
            if fecha_ingresada < date.today():
                flash("No puedes crear una misión con fecha en el pasado.", "mision")
                es_valido = False

        return es_valido