"""Controlador del CRUD de tacos."""

from flask import flash, redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.complemento import Complemento
from flask_app.models.taco import Taco


def _datos_formulario():
    return {
        "tortilla": request.form.get("tortilla", "").strip(),
        "guiso": request.form.get("guiso", "").strip(),
        "salsa": request.form.get("salsa", "").strip(),
    }


def _formulario_valido(datos):
    return all(0 < len(valor) <= 45 for valor in datos.values())


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/crear", methods=["POST"])
def crear():
    datos = _datos_formulario()
    if not _formulario_valido(datos):
        flash("Completa los tres campos (máximo 45 caracteres).", "danger")
        return redirect(url_for("index"))

    Taco.save(datos)
    flash("Taco creado correctamente.", "success")
    return redirect(url_for("tacos"))


@app.route("/tacos")
def tacos():
    return render_template("resultados.html", todos_tacos=Taco.get_all())


@app.route("/complementos")
def complementos():
    return render_template(
        "complementos.html",
        todos_complementos=Complemento.get_all(),
    )


@app.route("/complementos/crear", methods=["POST"])
def crear_complemento():
    nombre = request.form.get("nombre_complemento", "").strip()
    if not 0 < len(nombre) <= 45:
        flash("Escribe un complemento (máximo 45 caracteres).", "danger")
        return redirect(url_for("complementos"))

    Complemento.save({"nombre_complemento": nombre})
    flash("Complemento creado correctamente.", "success")
    return redirect(url_for("complementos"))


@app.route("/complementos/<int:complemento_id>")
def detalle_complemento(complemento_id):
    complemento = Complemento.get_complementos_y_tacos({"id": complemento_id})
    if complemento is None:
        return render_template("404.html"), 404
    return render_template(
        "complemento_detalle.html",
        complemento=complemento,
        todos_tacos=Taco.get_all(),
    )


@app.route("/complementos/<int:complemento_id>/tacos", methods=["POST"])
def asociar_taco(complemento_id):
    taco_id = request.form.get("taco_id", type=int)
    if taco_id is None or Taco.get_one({"id": taco_id}) is None:
        flash("Selecciona un taco válido.", "danger")
    else:
        Complemento.asociar_taco(
            {"complemento_id": complemento_id, "taco_id": taco_id}
        )
        flash("Taco asociado al complemento.", "success")
    return redirect(url_for("detalle_complemento", complemento_id=complemento_id))


@app.route(
    "/complementos/<int:complemento_id>/tacos/<int:taco_id>/quitar",
    methods=["POST"],
)
def desasociar_taco(complemento_id, taco_id):
    Complemento.desasociar_taco(
        {"complemento_id": complemento_id, "taco_id": taco_id}
    )
    flash("Relación eliminada.", "success")
    return redirect(url_for("detalle_complemento", complemento_id=complemento_id))


@app.route("/mostrar/<int:taco_id>")
def detalle(taco_id):
    taco = Taco.get_one({"id": taco_id})
    if taco is None:
        return render_template("404.html"), 404
    return render_template("detalle.html", taco=taco)


@app.route("/editar/<int:taco_id>")
def editar(taco_id):
    taco = Taco.get_one({"id": taco_id})
    if taco is None:
        return render_template("404.html"), 404
    return render_template("editar.html", taco=taco)


@app.route("/actualizar/<int:taco_id>", methods=["POST"])
def actualizar(taco_id):
    datos = _datos_formulario()
    if not _formulario_valido(datos):
        flash("Completa los tres campos (máximo 45 caracteres).", "danger")
        return redirect(url_for("editar", taco_id=taco_id))

    datos["id"] = taco_id
    Taco.update(datos)
    flash("Taco actualizado correctamente.", "success")
    return redirect(url_for("detalle", taco_id=taco_id))


@app.route("/borrar/<int:taco_id>", methods=["POST"])
def borrar(taco_id):
    Taco.delete({"id": taco_id})
    flash("Taco eliminado correctamente.", "success")
    return redirect(url_for("tacos"))

