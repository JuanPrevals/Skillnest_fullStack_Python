"""Juego del destino: formulario, sesiones y resultados aleatorios con Flask."""

import random
import unicodedata

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "clave_secreta"

DESTINOS = {
    "positivo": (
        "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
        "Una gran oportunidad laboral está a punto de tocar tu puerta. Prepárate para aprovecharla.",
        "Tus esfuerzos darán frutos muy pronto. La abundancia se acerca a tu vida.",
        "Un viaje inesperado traerá aventuras y aprendizajes que recordarás para siempre.",
        "Recibirás buenas noticias de una persona que hace tiempo no ves.",
    ),
    "advertencia": (
        "Debes tener cuidado con las decisiones financieras en las próximas semanas.",
        "Una amistad pondrá a prueba tu paciencia, pero saldrás fortalecido.",
        "Se avecina un periodo de cambios inesperados; mantén la calma y la mente clara.",
        "Podrías enfrentar un pequeño obstáculo, pero tu perseverancia lo superará.",
        "Alguien cercano podría decepcionarte; confía en tu propio criterio.",
    ),
}

COLORES = {
    "rojo": ("pasión y energía", "#dc2626"),
    "azul": ("calma y sabiduría", "#2563eb"),
    "verde": ("misterio y descubrimiento", "#16a34a"),
    "amarillo": ("alegría y creatividad", "#eab308"),
    "morado": ("intuición y espiritualidad", "#9333ea"),
    "naranja": ("entusiasmo y aventura", "#f97316"),
    "negro": ("poder y elegancia", "#111827"),
    "blanco": ("pureza y nuevos comienzos", "#f9fafb"),
    "rosa": ("ternura y compasión", "#ec4899"),
    "gris": ("equilibrio y neutralidad", "#6b7280"),
}

ANIMALES = {
    "gato": "independencia y misterio",
    "perro": "lealtad y protección",
    "aguila": "visión y libertad",
    "leon": "coraje y liderazgo",
    "delfin": "inteligencia e intuición",
    "lobo": "instinto y comunidad",
    "buho": "sabiduría y conocimiento oculto",
    "tigre": "fuerza y determinación",
    "mariposa": "transformación y renovación",
}


def texto_normalizado(valor):
    """Prepara el texto para encontrar valores escritos con o sin tilde."""
    texto = unicodedata.normalize("NFD", valor.strip().lower())
    return "".join(letra for letra in texto if unicodedata.category(letra) != "Mn")


def crear_resultado(datos):
    """Construye la predicción completa de una consulta."""
    categoria = random.choice(tuple(DESTINOS))
    significado_color, color_hex = COLORES.get(
        texto_normalizado(datos["color"]),
        ("originalidad y sorpresa", "#7c3aed"),
    )

    return {
        **datos,
        "mensaje": random.choice(DESTINOS[categoria]),
        "es_positivo": categoria == "positivo",
        "significado_color": significado_color,
        "significado_animal": ANIMALES.get(
            texto_normalizado(datos["animal"]), "curiosidad y aventura"
        ),
        "color_hex": color_hex,
        "numero_suerte": random.randint(1, 99),
    }


@app.route("/")
def index():
    """Presenta el formulario de consulta."""
    return render_template("index.html")


@app.route("/enviar", methods=["POST"])
def enviar():
    """Procesa el formulario y conserva el resultado en la sesión."""
    datos_usuario = {
        "nombre": request.form.get("nombre", "").strip() or "Viajero",
        "edad": request.form.get("edad", "").strip() or "?",
        "color": request.form.get("color", "").strip().lower() or "morado",
        "animal": request.form.get("animal", "").strip().lower() or "gato",
    }
    session["consulta_destino"] = crear_resultado(datos_usuario)
    return redirect(url_for("futuro"))


@app.route("/futuro")
def futuro():
    """Muestra el resultado o regresa al formulario cuando no existe."""
    resultado = session.get("consulta_destino")
    if resultado is None:
        return redirect(url_for("index"))
    return render_template("futuro.html", **resultado)


if __name__ == "__main__":
    app.run(debug=True)
