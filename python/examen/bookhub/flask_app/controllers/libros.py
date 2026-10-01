from flask import abort, flash, redirect, render_template, request, session, url_for
from pymysql import MySQLError

from flask_app import app
from flask_app.controllers.helpers import exigir_csrf, login_requerido
from flask_app.models.favorito import Favorito
from flask_app.models.libro import Libro


def _datos_libro_formulario():
    return {
        "titulo": request.form.get("titulo", "").strip(),
        "autor": request.form.get("autor", "").strip(),
        "genero": request.form.get("genero", "").strip(),
        "fecha_publicacion": request.form.get("fecha_publicacion", "").strip(),
        "descripcion": request.form.get("descripcion", "").strip(),
    }


def _obtener_libro_o_404(libro_id):
    libro = Libro.obtener_por_id(libro_id, session["usuario_id"])
    if not libro:
        abort(404)
    return libro


@app.get("/libros")
@login_requerido
def mis_libros():
    propios = Libro.obtener_del_usuario(session["usuario_id"])
    comunidad = Libro.obtener_comunidad(session["usuario_id"], limite=6)
    return render_template("libros/dashboard.html", propios=propios, comunidad=comunidad)


@app.get("/explorar")
@login_requerido
def explorar():
    termino = request.args.get("q", "").strip()
    genero = request.args.get("genero", "").strip()
    libros = Libro.explorar(session["usuario_id"], termino, genero)
    return render_template(
        "libros/explorar.html",
        libros=libros,
        generos=Libro.GENEROS,
        termino=termino,
        genero_actual=genero,
    )


@app.get("/libros/nuevo")
@login_requerido
def nuevo_libro():
    return render_template("libros/formulario.html", libro={}, errores={}, generos=Libro.GENEROS)


@app.post("/libros/crear")
@login_requerido
def crear_libro():
    if not exigir_csrf():
        return redirect(url_for("nuevo_libro"))
    datos = _datos_libro_formulario()
    errores = Libro.validar(datos)
    if errores:
        return render_template(
            "libros/formulario.html", libro=datos, errores=errores, generos=Libro.GENEROS
        ), 422
    datos["usuario_id"] = session["usuario_id"]
    Libro.crear(datos)
    flash(f'El libro “{datos["titulo"]}” fue publicado.', "success")
    return redirect(url_for("mis_libros"))


@app.get("/libros/<int:libro_id>")
@login_requerido
def detalle_libro(libro_id):
    libro = _obtener_libro_o_404(libro_id)
    usuarios_favoritos = Favorito.usuarios_del_libro(libro_id)
    return render_template(
        "libros/detalle.html", libro=libro, usuarios_favoritos=usuarios_favoritos
    )


@app.get("/libros/editar/<int:libro_id>")
@login_requerido
def editar_libro(libro_id):
    libro = _obtener_libro_o_404(libro_id)
    if libro.usuario_id != session["usuario_id"]:
        flash("Solo puedes editar los libros que publicaste.", "danger")
        return redirect(url_for("detalle_libro", libro_id=libro_id))
    return render_template(
        "libros/formulario.html", libro=libro, errores={}, generos=Libro.GENEROS
    )


@app.post("/libros/actualizar/<int:libro_id>")
@login_requerido
def actualizar_libro(libro_id):
    if not exigir_csrf():
        return redirect(url_for("editar_libro", libro_id=libro_id))
    libro = _obtener_libro_o_404(libro_id)
    if libro.usuario_id != session["usuario_id"]:
        flash("No tienes permiso para modificar ese libro.", "danger")
        return redirect(url_for("detalle_libro", libro_id=libro_id))
    datos = _datos_libro_formulario()
    errores = Libro.validar(datos)
    if errores:
        datos["id"] = libro_id
        datos["usuario_id"] = libro.usuario_id
        return render_template(
            "libros/formulario.html", libro=datos, errores=errores, generos=Libro.GENEROS
        ), 422
    Libro.actualizar(libro_id, session["usuario_id"], datos)
    flash(f'Los cambios en “{datos["titulo"]}” se guardaron.', "success")
    return redirect(url_for("detalle_libro", libro_id=libro_id))


@app.post("/libros/eliminar/<int:libro_id>")
@login_requerido
def eliminar_libro(libro_id):
    if not exigir_csrf():
        return redirect(url_for("mis_libros"))
    libro = _obtener_libro_o_404(libro_id)
    if libro.usuario_id != session["usuario_id"]:
        flash("No tienes permiso para eliminar ese libro.", "danger")
        return redirect(url_for("detalle_libro", libro_id=libro_id))
    Libro.eliminar(libro_id, session["usuario_id"])
    flash(f'“{libro.titulo}” fue eliminado de tu biblioteca.', "success")
    return redirect(url_for("mis_libros"))


@app.post("/libros/<int:libro_id>/favorito")
@login_requerido
def alternar_favorito(libro_id):
    if not exigir_csrf():
        return redirect(url_for("detalle_libro", libro_id=libro_id))
    libro = _obtener_libro_o_404(libro_id)
    if libro.es_favorito:
        Favorito.quitar(session["usuario_id"], libro_id)
        flash(f'“{libro.titulo}” se quitó de tus favoritos.', "info")
    else:
        Favorito.agregar(session["usuario_id"], libro_id)
        flash(f'“{libro.titulo}” se agregó a tus favoritos.', "success")
    destino = request.form.get("siguiente", "")
    if destino == "favoritos":
        return redirect(url_for("mis_favoritos"))
    return redirect(url_for("detalle_libro", libro_id=libro_id))


@app.get("/favoritos")
@login_requerido
def mis_favoritos():
    libros = Favorito.del_usuario(session["usuario_id"])
    return render_template("libros/favoritos.html", libros=libros)
