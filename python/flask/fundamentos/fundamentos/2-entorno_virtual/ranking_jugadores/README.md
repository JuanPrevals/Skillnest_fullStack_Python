# 🎮 Ranking de jugadores (Práctica)

> **Curso:** Desarrollo web con Flask desde cero  
> **Unidad:** Motores de plantilla con Jinja2  
> **Duración estimada:** 60-90 minutos

---

## 🎯 Objetivo

Aprender a enviar información desde el servidor a una plantilla HTML en Flask y utilizar bucles `for` y condicionales `if` de Jinja2 para mostrar un ranking de jugadores.

---

## ❓ ¿Por qué es importante?

Las aplicaciones web suelen trabajar con listas de información que se presentan dinámicamente en la interfaz. Es el caso de las tablas de puntuaciones, los comentarios en redes sociales o las listas de reproducción en plataformas de *streaming*.

Flask permite estructurar estos datos en el servidor y enviarlos a plantillas HTML. Después, Jinja2 los presenta de forma ordenada y atractiva para el usuario.

---

## 📝 Instrucciones

### 1. Crea la estructura del proyecto

Crea una carpeta llamada `ranking_game` con la siguiente estructura:

```text
ranking_game/
├── app.py
└── templates/
    └── ranking.html
```

- `app.py` contendrá el servidor Flask.
- `templates/` almacenará las plantillas HTML.
- `templates/ranking.html` mostrará el ranking de jugadores.

### 2. Configura el servidor

Crea el archivo `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)


# Datos de jugadores con sus puntajes
jugadores = [
    {"nombre": "AlexGamer", "puntaje": 5000},
    {"nombre": "PixelMaster", "puntaje": 7500},
    {"nombre": "ShadowNinja", "puntaje": 8200},
    {"nombre": "CyberWarrior", "puntaje": 9100},
    {"nombre": "UltraNoob", "puntaje": 3000},
]


# Ruta para mostrar el ranking completo


# Ruta para mostrar un número limitado de jugadores


# Ruta para personalizar el color de fondo del ranking


if __name__ == "__main__":
    app.run(debug=True)
```

> [!IMPORTANT]
> Completa las tres rutas indicadas en los comentarios. Antes de enviar los datos a la plantilla, ordena a los jugadores de mayor a menor puntaje.

### 3. Crea la plantilla HTML

Crea el archivo `templates/ranking.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ranking de Jugadores</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: {% if color %}{{ color }}{% else %}#f4f4f4{% endif %};
            text-align: center;
        }

        h1 {
            color: #333;
        }

        .ranking {
            display: inline-block;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        ul {
            list-style: none;
            padding: 0;
        }

        li {
            min-width: 350px;
            margin: 10px 0;
            padding: 8px;
            border-bottom: 1px solid #ddd;
            font-size: 18px;
        }

        .top {
            color: gold;
            font-weight: bold;
        }
    </style>
</head>

<body>
    <h1>🎮 Ranking de Jugadores 🎮</h1>

    <div class="ranking">
        <ul>
            {% for jugador in jugadores %}
                <li {% if loop.index == 1 %}class="top"{% endif %}>
                    {{ loop.index }}. {{ jugador.nombre }} - {{ jugador.puntaje }} puntos
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

### 4. Implementa las rutas

La aplicación debe responder a las siguientes rutas dinámicas:

| Ruta | Descripción | Ejemplo | Resultado esperado |
| --- | --- | --- | --- |
| `/ranking` | Muestra el ranking completo. | `http://127.0.0.1:5000/ranking` | Aparecen todos los jugadores. |
| `/ranking/<int:cantidad>` | Limita la cantidad de jugadores. | `http://127.0.0.1:5000/ranking/3` | Aparecen los tres primeros. |
| `/ranking/<int:cantidad>/<color>` | Limita los jugadores y cambia el fondo. | `http://127.0.0.1:5000/ranking/3/lightblue` | Aparecen tres jugadores sobre un fondo celeste. |

> [!TIP]
> Puedes utilizar *slicing* (`lista[:cantidad]`) para limitar el ranking y `sorted()` para ordenar los puntajes.

### 5. Ejecuta la aplicación

Abre una terminal dentro de `ranking_game` y ejecuta:

```bash
python app.py
```

En macOS o Linux también puede ser necesario utilizar:

```bash
python3 app.py
```

Después, abre `http://127.0.0.1:5000/ranking` en el navegador y prueba las diferentes rutas.

---

## 💡 Tips

- Usa `@app.route("/ruta")` para definir una ruta en Flask.
- Envía variables al HTML mediante `render_template()`.
- Jinja2 permite utilizar bucles `for` y condicionales `if` dentro de las plantillas.
- Prueba distintos fondos con rutas como `/ranking/5/red`, `/ranking/3/black` o `/ranking/3/lightblue`.
- Valida la cantidad solicitada para evitar resultados inesperados con números negativos.

---

## 📚 Contenidos que estás aplicando

- 🌐 Creación de un servidor Flask y configuración de rutas.
- 📨 Uso de `render_template()` para enviar información al HTML.
- 🔁 Uso de bucles `for` para presentar listas de datos.
- ⚖️ Uso de condicionales `if` para modificar la apariencia.
- 🛣️ Manejo de rutas dinámicas con parámetros en Flask.
- 📊 Ordenamiento y segmentación de listas en Python.

---

## 💬 Pregunta guía y reflexión

> Si quisieras actualizar este ranking dinámicamente con jugadores reales, ¿cómo integrarías una base de datos en la aplicación Flask?

---

## 🏁 Resultado esperado

Al finalizar esta práctica habrás construido un sistema de ranking dinámico con Flask. La aplicación enviará información desde el servidor a una plantilla HTML y personalizará el contenido mediante CSS, Jinja2 y rutas dinámicas.

Comprueba estos tres casos:

1. **Ranking completo:** `/ranking`
2. **Ranking limitado:** `/ranking/3`
3. **Ranking limitado con fondo personalizado:** `/ranking/3/lightblue`

### Lista de comprobación

- [ ] Los jugadores aparecen ordenados de mayor a menor puntaje.
- [ ] El primer jugador se distingue visualmente.
- [ ] La ruta con cantidad muestra únicamente el número solicitado.
- [ ] La ruta con color modifica el fondo de la página.
- [ ] Las tres rutas cargan sin errores en el navegador.

---

> **Recuerda:** Python procesa los datos y Jinja2 los presenta.
