from flask import redirect, render_template, request, url_for

from flask_app import app
from flask_app.models.pedido import Pedido


@app.get("/")
def inicio():
    return redirect(url_for("listar_pedidos"))


@app.get("/arepas")
def listar_pedidos():
    return render_template("pedidos.html", pedidos=Pedido.get_all())


@app.get("/pedido")
def nuevo_pedido():
    return render_template("nuevo_pedido.html")


@app.post("/pedido")
def crear_pedido():
    data = {
        "nombre": request.form.get("nombre", "").strip(),
        "cantidad": request.form.get("cantidad", "").strip(),
        "relleno": request.form.get("relleno", "").strip(),
    }

    if not Pedido.validar_pedido(data):
        return redirect(url_for("nuevo_pedido"))

    data["cantidad"] = int(data["cantidad"])
    Pedido.save(data)
    return redirect(url_for("listar_pedidos"))
