from flask import Blueprint, render_template, request, redirect, session, flash
from flask_app.models.modelo_mision import Mision

# Definimos el Blueprint para las rutas de misiones
misiones_bp = Blueprint('misiones', __name__)

# RUTA PRINCIPAL: DASHBOARD ----------------------------------------
@misiones_bp.route('/dashboard')
def dashboard():
    """Muestra todas las misiones futuras ordenadas por fecha."""
    # 1. PROTECCIÓN DE RUTA: Expulsar a quien no tenga sesión activa
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para ver esta página.", "login")
        return redirect('/')
    
    # 2. Obtenemos las misiones (El modelo ya filtra el pasado y ordena por fecha)
    misiones = Mision.obtener_todas_futuras()
    
    return render_template('dashboard.html', misiones=misiones)

# RUTAS DE CREACIÓN ---------------------------------------------
@misiones_bp.route('/nueva')
def nueva_mision():
    """Renderiza el formulario para crear una misión."""
    if 'usuario_id' not in session:
        return redirect('/')
        
    return render_template('nueva_mision.html')

@misiones_bp.route('/crear', methods=['POST'])
def procesar_mision():
    """Valida y guarda una nueva misión en la base de datos."""
    if 'usuario_id' not in session:
        return redirect('/')

    # 1. Ejecutar las validaciones estrictas del modelo
    if not Mision.validar_mision(request.form):
        # Si algo falla, lo devolvemos al formulario de creación
        return redirect('/nueva')

    # 2. Preparar el diccionario inyectando el ID del usuario en sesión
    data = {
        "nombre": request.form['nombre'],
        "fecha": request.form['fecha'],
        "voluntarios_necesarios": request.form['voluntarios_necesarios'],
        "descripcion": request.form['descripcion'],
        "usuario_id": session['usuario_id'] # ¡Vital para que él sea el líder!
    }

    # 3. Guardar en BD
    Mision.guardar(data)
    
    return redirect('/dashboard')

# RUTAS DE VISUALIZACIÓN Y BONUS
@misiones_bp.route('/ver/<int:id_mision>')
def ver_mision(id_mision):
    """Muestra los detalles de una misión y la lista de voluntarios."""
    if 'usuario_id' not in session:
        return redirect('/')

    data = {"id_mision": id_mision}
    mision = Mision.obtener_por_id_con_relaciones(data)

    return render_template('ver_mision.html', mision=mision)

@misiones_bp.route('/unirse/<int:id_mision>')
def unirse_mision(id_mision):
    """BONUS: Conecta al usuario logeado con la misión (Botón VoluntaMe)."""
    if 'usuario_id' not in session:
        return redirect('/')

    data = {
        "usuario_id": session['usuario_id'],
        "id_mision": id_mision
    }
    # Guardamos en la tabla intermedia (Muchos a Muchos)
    Mision.agregar_voluntario(data)
    
    # Recargamos la misma página individual de la misión
    return redirect(f'/ver/{id_mision}')

# RUTAS DE EDICIÓN Y PROTECCIÓN
@misiones_bp.route('/editar/<int:id_mision>')
def editar_mision(id_mision):
    """Renderiza el formulario pre-poblado, solo si el usuario es el creador."""
    if 'usuario_id' not in session:
        return redirect('/')

    data = {"id_mision": id_mision}
    mision = Mision.obtener_por_id_con_relaciones(data)

    # Si el ID de sesión NO es el mismo que el ID del usuario creador de la misión...
    if session['usuario_id'] != mision.usuario_id:
        flash("No tienes permiso para editar misiones de otros usuarios.", "login")
        return redirect('/dashboard')

    return render_template('editar_mision.html', mision=mision)

@misiones_bp.route('/actualizar/<int:id_mision>', methods=['POST'])
def actualizar_mision(id_mision):
    """Valida y actualiza los datos en la BD."""
    if 'usuario_id' not in session:
        return redirect('/')

    # 1. Validamos los campos editados
    if not Mision.validar_mision(request.form):
        return redirect(f'/editar/{id_mision}')

    # 2. Preparamos el diccionario
    data = {
        "id_mision": id_mision,
        "nombre": request.form['nombre'],
        "fecha": request.form['fecha'],
        "voluntarios_necesarios": request.form['voluntarios_necesarios'],
        "descripcion": request.form['descripcion']
    }

    # 3. Guardamos los cambios
    Mision.actualizar(data)

    return redirect('/dashboard')

# RUTAS DE ELIMINACIÓN ------------------------------------------------------
@misiones_bp.route('/borrar/<int:id_mision>')
def borrar_mision(id_mision):
    """Elimina la misión de la BD asegurando que quien borra es el creador."""
    if 'usuario_id' not in session:
        return redirect('/')

    data = {"id_mision": id_mision}
    mision = Mision.obtener_por_id_con_relaciones(data)

    # Doble validación al borrar
    if session['usuario_id'] == mision.usuario_id:
        Mision.eliminar(data)
    else:
        flash("No puedes borrar una misión que no te pertenece.", "login")

    return redirect('/dashboard')