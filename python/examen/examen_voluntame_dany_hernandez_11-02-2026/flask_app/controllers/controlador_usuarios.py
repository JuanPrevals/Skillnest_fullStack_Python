from flask import Blueprint, render_template, request, redirect, session, flash
from flask_app.models.modelo_usuario import Usuario
from flask_bcrypt import Bcrypt

# CONFIGURACIÓN DEL BLUEPRINT Y BCRYPT
usuarios_bp = Blueprint('usuarios', __name__)
bcrypt = Bcrypt()

# RUTA PRINCIPAL: MOSTRAR LOGIN/REGISTRO ----------------------------------------
@usuarios_bp.route('/')
def index():
    """Muestra la página de inicio. Si hay sesión activa, redirige al dashboard."""
    if 'usuario_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

# RUTA: PROCESAR EL REGISTRO -----------------------------------------------------
@usuarios_bp.route('/registro', methods=['POST'])
def procesar_registro():
    """Valida, encripta y guarda el nuevo usuario."""
    # 1. Validar campos
    if not Usuario.validar_registro(request.form):
        return redirect('/')
        
    # 2. Encriptar contraseña
    password_hash = bcrypt.generate_password_hash(request.form['contrasena']).decode('utf-8')
    
    # 3. Preparar datos para el modelo
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "contrasena": password_hash
    }
    
    # 4. Guardar usuario y recuperar el ID generado
    id_usuario = Usuario.guardar(data)
    
    # 5. Guardar datos en sesión para mantenerlo logeado
    session['usuario_id'] = id_usuario
    session['usuario_nombre'] = request.form['nombre']
    
    return redirect('/dashboard')

# RUTA: PROCESAR EL LOGIN ------------------------------------------------------------
@usuarios_bp.route('/login', methods=['POST'])
def procesar_login():
    """Verifica credenciales e inicia la sesión."""
    # 1. Buscar al usuario por el email proporcionado
    data = {"email": request.form['email']}
    usuario_encontrado = Usuario.obtener_por_email(data)
    
    # 2. Validar si el correo existe
    if not usuario_encontrado:
        flash("Email o contraseña inválidos.", "login")
        return redirect('/')
        
    # 3. Validar si la contraseña encriptada coincide
    if not bcrypt.check_password_hash(usuario_encontrado.contrasena, request.form['contrasena']):
        flash("Email o contraseña inválidos.", "login")
        return redirect('/')
        
    # 4. Iniciar sesión exitosa
    session['usuario_id'] = usuario_encontrado.id_usuario
    session['usuario_nombre'] = usuario_encontrado.nombre
    
    return redirect('/dashboard')

# RUTA: CERRAR SESIÓN (LOGOUT) --------------------------------------------------------
@usuarios_bp.route('/logout')
def logout():
    """Limpia el diccionario de sesión y redirige al inicio."""
    session.clear()
    return redirect('/')