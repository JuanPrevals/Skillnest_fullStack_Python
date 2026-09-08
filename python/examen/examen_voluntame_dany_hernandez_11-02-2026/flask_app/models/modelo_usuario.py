from flask_app.config.mysql_connection import connect_to_mysql
from flask import flash
import re

# Validación formato de Email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#CLASE DE USUARIO
class Usuario:
    def __init__(self, data):
        # Mapeamos las columnas tabla 'usuarios'
        self.id_usuario = data.get('id_usuario')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.contrasena = data.get('contrasena')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    # MÉTODOS CRUD BD
    
    @classmethod
    def guardar(cls, formulario):
        """Inserta un nuevo usuario en la base de datos."""
        query = """
            INSERT INTO usuarios (nombre, apellido, email, contrasena)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(contrasena)s);
        """
        return connect_to_mysql('voluntame_db').query_db(query, formulario)

    @classmethod
    def obtener_por_email(cls, formulario):
        """Busca un usuario por su email. Vital para el Login y para evitar duplicados."""
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultado = connect_to_mysql('voluntame_db').query_db(query, formulario)
        
        if len(resultado) < 1:
            return False
            
        return cls(resultado[0])
        
    @classmethod
    def obtener_por_id(cls, formulario):
        """Obtiene un usuario por su ID para validar sesiones."""
        query = "SELECT * FROM usuarios WHERE id_usuario = %(id_usuario)s;"
        resultado = connect_to_mysql('voluntame_db').query_db(query, formulario)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])


    # VALIDACIONES
    @staticmethod
    def validar_registro(formulario):
        """Valida que los datos cumplan las reglas antes de guardarlos."""
        es_valido = True
        
        # Validaciones de longitud
        if len(formulario['nombre']) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            es_valido = False
            
        if len(formulario['apellido']) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            es_valido = False
            
        # Validación de formato de email
        if not EMAIL_REGEX.match(formulario['email']):
            flash("El formato del email es inválido.", "registro")
            es_valido = False
        else:
            # Validación de email único en BD
            usuario_existente = Usuario.obtener_por_email({'email': formulario['email']})
            if usuario_existente:
                flash("Este email ya se encuentra registrado.", "registro")
                es_valido = False
                
        # Validación de contraseñas
        if len(formulario['contrasena']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            es_valido = False
            
        if formulario['contrasena'] != formulario['confirmar_contrasena']:
            flash("Las contraseñas no coinciden.", "registro")
            es_valido = False
            
        return es_valido