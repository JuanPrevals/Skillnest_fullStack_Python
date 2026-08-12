# 🛒 Práctica Integrada - Mercado de Frutas con Flask

> **Curso:** Desarrollo Web con Flask desde Cero  
> **Unidad:** Formularios HTML, Métodos POST y Renderizado de Plantillas  
> **Práctica:** Mercado de Frutas

---

# 📖 Descripción

En esta práctica desarrollarás una pequeña aplicación web utilizando **Flask**, donde un usuario podrá seleccionar distintas frutas, indicar la cantidad que desea comprar y completar un formulario con su información personal para generar una orden de compra.

Esta actividad integra prácticamente todos los conocimientos adquiridos hasta este momento del curso, por lo que representa una excelente instancia para reforzar lo aprendido antes de comenzar a trabajar con sesiones y bases de datos.

Al finalizar obtendrás una aplicación similar a una tienda en línea, con una interfaz moderna y completamente funcional.

---

# 🎯 Objetivos

Al finalizar esta práctica serás capaz de:

- Crear una aplicación Flask organizada.
- Trabajar con múltiples rutas.
- Procesar formularios utilizando el método **POST**.
- Capturar información mediante `request.form`.
- Enviar datos dinámicos hacia una plantilla HTML.
- Recorrer listas utilizando Jinja2.
- Mostrar información enviada por el usuario.
- Realizar cálculos en Python antes de renderizar la vista.
- Utilizar archivos estáticos (CSS e imágenes).
- Integrar Bootstrap para mejorar la apariencia del proyecto.

---

# 🧠 ¿Qué aprenderás?

Durante esta práctica aplicarás conocimientos que has trabajado en las lecciones anteriores.

✅ Rutas Flask

✅ render_template()

✅ request.form

✅ Formularios HTML

✅ Método POST

✅ url_for()

✅ Archivos estáticos

✅ Bootstrap

✅ Jinja2

✅ Variables

✅ Diccionarios

✅ Conversión de tipos con `int()`

✅ Cálculos en Python

---

# 🖥️ Resultado esperado

La aplicación estará compuesta por **tres páginas**.

## 🏠 Página principal

En esta página el usuario podrá:

- visualizar todas las frutas disponibles.
- seleccionar la cantidad deseada.
- completar sus datos personales.
- generar una orden de compra.

La vista tendrá un aspecto similar al siguiente.

- Hero superior.
- Tarjetas con frutas.
- Controles para seleccionar cantidades.
- Formulario de compra.
- Botón **Crear Orden**.

---

## 🍎 Catálogo de frutas

Una segunda página mostrará únicamente las frutas disponibles.

Cada fruta será presentada mediante una tarjeta con:

- Imagen.
- Nombre.
- Precio.

Esta vista permitirá conocer todos los productos disponibles en la tienda.

---

## 🧾 Resumen de la compra

Finalmente se mostrará una página con el resumen del pedido.

Aquí aparecerán:

- Información del cliente.
- Dirección.
- Frutas seleccionadas.
- Cantidad de cada fruta.
- Precio.
- Subtotal.
- Total de frutas compradas.
- Total a pagar.

---

# 📁 Estructura del proyecto

Antes de comenzar, crea la siguiente estructura de carpetas.

```text
mercado_frutas_app/

│

├── app.py

│

├── templates/

│   ├── index.html
│   ├── frutas.html
│   └── checkout.html

│

├── static/

│   ├── css/
│   │
│   └── images/

│       ├── manzana.png
│       ├── platano.png
│       ├── naranja.png
│       ├── fresa.png
│       ├── uva.png
│       ├── pina.png
│       ├── sandia.png
│       └── mango.png

│

└── static/css/

    └── style.css
```

---

# 🖼️ Organización de las imágenes

Todas las imágenes deberán almacenarse dentro de la carpeta:

```text
static/images/
```

Los nombres de los archivos deberán coincidir exactamente con los siguientes.

```text
manzana.png

platano.png

naranja.png

fresa.png

uva.png

pina.png

sandia.png

mango.png
```

Más adelante accederemos a ellas utilizando:

```jinja
{{ url_for('static', filename='images/manzana.png') }}
```

---

# 🏗️ Arquitectura de la aplicación

Nuestra aplicación tendrá tres rutas principales.

```text
                    GET

                     /

                     │

                     ▼

            Página principal

                     │

                     │ POST

                     ▼

               /checkout

                     ▲

                     │

                     │ GET

                     │

                 /frutas
```

Cada ruta tendrá una responsabilidad específica.

| Ruta      | Función                                  |
| --------- | ---------------------------------------- |
| /         | Mostrar el formulario principal.         |
| /frutas   | Mostrar el catálogo de frutas.           |
| /checkout | Procesar la compra y mostrar el resumen. |

---

# 🐍 Paso 1 - Crear el servidor Flask

Dentro del proyecto crea el archivo:

```text
app.py
```

En este archivo construiremos toda la lógica del servidor.

Durante esta práctica utilizaremos una pequeña base de datos ficticia compuesta por una lista de diccionarios, donde cada fruta tendrá información como:

- nombre
- precio
- imagen
- descripción

Más adelante esta información será enviada dinámicamente hacia nuestras plantillas HTML.

En la siguiente parte construiremos completamente el archivo **app.py**, definiendo todas las rutas necesarias y comentando cada sección para comprender cómo funciona la aplicación.

# 🐍 Paso 2 - Crear el servidor Flask (`app.py`)

En esta sección construiremos el servidor Flask encargado de:

- Mostrar la página principal.
- Mostrar el catálogo de frutas.
- Procesar el formulario enviado por el usuario.
- Calcular el total de frutas compradas.
- Calcular el total a pagar.
- Enviar toda la información al resumen de compra.

---

# 📄 Código completo de `app.py`

```python
# ==========================================
# Importaciones
# ==========================================

from flask import Flask, render_template, request

# ==========================================
# Crear aplicación Flask
# ==========================================

app = Flask(__name__)

# ==========================================
# Base de datos ficticia
# ==========================================

frutas = [

    {
        "nombre": "Manzana",
        "precio": 2.5,
        "imagen": "manzana.png",
        "descripcion": "Fruta dulce y crujiente, rica en fibra y vitamina C."
    },

    {
        "nombre": "Plátano",
        "precio": 1.8,
        "imagen": "platano.png",
        "descripcion": "Fruta energética rica en potasio, perfecta para deportistas."
    },

    {
        "nombre": "Naranja",
        "precio": 3.0,
        "imagen": "naranja.png",
        "descripcion": "Cítrico jugoso con alto contenido de vitamina C y antioxidantes."
    },

    {
        "nombre": "Fresa",
        "precio": 4.5,
        "imagen": "fresa.png",
        "descripcion": "Baya dulce y aromática, rica en antioxidantes y vitamina C."
    },

    {
        "nombre": "Uva",
        "precio": 3.8,
        "imagen": "uva.png",
        "descripcion": "Fruta pequeña y dulce, ideal para snacks y postres."
    },

    {
        "nombre": "Piña",
        "precio": 5.0,
        "imagen": "pina.png",
        "descripcion": "Fruta tropical dulce y ácida, con propiedades antiinflamatorias."
    },

    {
        "nombre": "Sandía",
        "precio": 4.2,
        "imagen": "sandia.png",
        "descripcion": "Fruta refrescante, compuesta en un 90% de agua, ideal para el verano."
    },

    {
        "nombre": "Mango",
        "precio": 3.5,
        "imagen": "mango.png",
        "descripcion": "Fruta tropical dulce y aromática, rica en vitaminas A y C."
    }

]

# ==========================================
# Ruta principal
# ==========================================

@app.route("/")
def index():
    """
    Muestra la página principal del mercado.
    """

    return render_template(
        "index.html",
        frutas=frutas
    )


# ==========================================
# Catálogo de frutas
# ==========================================

@app.route("/frutas")
def catalogo():

    return render_template(
        "frutas.html",
        frutas=frutas
    )


# ==========================================
# Procesar compra
# ==========================================

@app.route("/checkout", methods=["POST"])
def checkout():

    # ----------------------------
    # Información del cliente
    # ----------------------------

    nombre = request.form["nombre"]

    email = request.form["email"]

    direccion = request.form["direccion"]


    # ----------------------------
    # Variables auxiliares
    # ----------------------------

    pedido = []

    total = 0

    total_frutas = 0


    # ----------------------------
    # Recorrer todas las frutas
    # ----------------------------

    for fruta in frutas:

        cantidad = int(request.form[fruta["nombre"]])

        if cantidad > 0:

            subtotal = cantidad * fruta["precio"]

            pedido.append({

                "nombre": fruta["nombre"],

                "precio": fruta["precio"],

                "cantidad": cantidad,

                "subtotal": subtotal,

                "imagen": fruta["imagen"]

            })

            total += subtotal

            total_frutas += cantidad


    # ----------------------------
    # Mostrar resumen
    # ----------------------------

    return render_template(

        "checkout.html",

        nombre=nombre,

        email=email,

        direccion=direccion,

        pedido=pedido,

        total=total,

        total_frutas=total_frutas

    )


# ==========================================
# Ejecutar servidor
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)
```

---

# 🔍 Analizando el código

## Importaciones

```python
from flask import Flask, render_template, request
```

Importamos tres elementos fundamentales.

| Elemento        | Función                                                     |
| --------------- | ----------------------------------------------------------- |
| Flask           | Crea la aplicación web.                                     |
| render_template | Envía información a las plantillas HTML.                    |
| request         | Permite acceder a la información enviada por el formulario. |

---

## Nuestra "base de datos"

Para simplificar la práctica utilizaremos una lista de diccionarios.

```python
frutas = [

    {
        "nombre":"Manzana",
        "precio":2.5,
        "imagen":"manzana.png"
    }

]
```

Cada fruta posee distintas propiedades.

| Propiedad   | Descripción          |
| ----------- | -------------------- |
| nombre      | Nombre de la fruta.  |
| precio      | Precio unitario.     |
| imagen      | Nombre de la imagen. |
| descripcion | Texto descriptivo.   |

Más adelante esta información será enviada al HTML mediante Jinja2.

---

## Ruta principal

```python
@app.route("/")
```

Esta ruta mostrará la página principal del mercado.

Además enviará toda la lista de frutas.

```python
return render_template(

    "index.html",

    frutas=frutas

)
```

De esta forma el HTML podrá construir automáticamente todas las tarjetas utilizando un bucle `for`.

---

## Ruta del catálogo

```python
@app.route("/frutas")
```

Esta página reutiliza exactamente la misma lista.

No es necesario volver a escribir los datos.

Simplemente enviamos nuevamente la colección.

```python
render_template(

    "frutas.html",

    frutas=frutas

)
```

Una de las ventajas de trabajar con listas y Jinja2 es que una misma información puede reutilizarse en distintas vistas.

---

## Ruta `/checkout`

Esta es la ruta más importante de toda la práctica.

¿Por qué?

Porque será la encargada de:

- recibir el formulario.
- leer todas las cantidades.
- calcular subtotales.
- calcular el total de la compra.
- contar el número total de frutas.
- enviar toda la información al resumen final.

En la siguiente parte construiremos el archivo **index.html**, donde el usuario podrá seleccionar las frutas, completar sus datos personales y enviar la orden utilizando un formulario **POST**.

# 📝 Paso 3 - Crear la página principal (`index.html`)

En esta sección construiremos la página principal del Mercado de Frutas.

Esta será la vista más importante de toda la aplicación, ya que permitirá al usuario:

- Visualizar todas las frutas disponibles.
- Seleccionar la cantidad que desea comprar.
- Completar su información personal.
- Enviar una orden al servidor mediante un formulario **POST**.

Al finalizar este paso obtendrás una página similar a la siguiente:

- Banner superior.
- Tarjetas de frutas.
- Formulario de compra.
- Botón **Crear Orden**.

---

# 📄 Código completo de `index.html`

```html
<!DOCTYPE html>
<html lang="es">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Mercado de Frutas</title>

    <!-- Bootstrap CSS -->

    <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css"
    rel="stylesheet">

    <!-- Bootstrap Icons -->

    <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css">

    <!-- Hoja de estilos -->

    <link
    rel="stylesheet"
    href="{{ url_for('static', filename='css/style.css') }}">

</head>

<body>

<!-- ===================================== -->
<!-- Barra de navegación                   -->
<!-- ===================================== -->

<nav class="navbar navbar-expand-lg navbar-dark bg-success">

    <div class="container">

        <a class="navbar-brand fw-bold"
           href="{{ url_for('index') }}">

            <i class="bi bi-apple"></i>

            Mercado de Frutas

        </a>

        <div>

            <a class="nav-link text-white d-inline"

               href="{{ url_for('index') }}">

                Inicio

            </a>

            <a class="nav-link text-white d-inline"

               href="{{ url_for('catalogo') }}">

                Catálogo

            </a>

        </div>

    </div>

</nav>

<!-- ===================================== -->
<!-- Encabezado                            -->
<!-- ===================================== -->

<header class="hero text-center text-white">

    <div class="container">

        <h1>

            Frutas Frescas a Tu Puerta

        </h1>

        <p>

            Selecciona tus frutas favoritas y realiza tu pedido.

        </p>

    </div>

</header>

<!-- ===================================== -->
<!-- Formulario                            -->
<!-- ===================================== -->

<form

action="{{ url_for('checkout') }}"

method="POST">

<div class="container mt-5">

<div class="row">

<!-- ===================================== -->
<!-- Lista de frutas                       -->
<!-- ===================================== -->

<div class="col-lg-8">

<div class="card shadow">

<div class="card-header">

<h3>

Selecciona tus frutas

</h3>

</div>

<div class="card-body">

<div class="row">

{% for fruta in frutas %}
```

---

# 🔍 Analizando el código

Hasta este momento hemos construido la estructura principal de la página.

Observa que todo el contenido está contenido dentro de un único formulario.

```html
<form

action="{{ url_for('checkout') }}"

method="POST">
```

Esto significa que **todos los datos del formulario viajarán juntos** hacia la ruta:

```
/checkout
```

---

# 📤 El atributo `action`

Observa la siguiente línea.

```html
action="{{ url_for('checkout') }}"
```

Flask generará automáticamente la URL correspondiente a la función:

```python
@app.route("/checkout")
def checkout():
```

El resultado será:

```
/checkout
```

Utilizar `url_for()` es una buena práctica porque evita escribir las rutas manualmente.

---

# 🔄 Método POST

También utilizamos:

```html
method="POST"
```

¿Por qué?

Porque el usuario está enviando información al servidor.

En este caso viajarán:

- Nombre.
- Correo.
- Dirección.
- Cantidad de cada fruta.

---

# 🧠 ¿Por qué el formulario rodea toda la página?

Observa dónde comienza el formulario.

```html
<form>

...

Todas las frutas

...

Información del cliente

...

Botón Crear Orden

</form>
```

Todo lo que esté dentro del formulario será enviado al servidor cuando el usuario haga clic en **Crear Orden**.

---

# 📦 El sistema de columnas

Bootstrap divide la pantalla utilizando un sistema de 12 columnas.

En esta práctica utilizaremos:

```html
<div class="row">

    <div class="col-lg-8">

    ...

    </div>

    <div class="col-lg-4">

    ...

    </div>

</div>
```

Visualmente tendremos.

```text
┌──────────────────────┬──────────────┐

│                      │              │

│     Frutas           │ Formulario   │

│                      │              │

└──────────────────────┴──────────────┘
```

Esta distribución es exactamente la que observamos en la captura de referencia.

---

# 🍎 Mostrar las frutas dinámicamente

Dentro de la tarjeta principal utilizaremos un bucle de Jinja2.

```jinja
{% for fruta in frutas %}
```

Recordemos que la variable **frutas** proviene desde Flask.

```python
return render_template(

    "index.html",

    frutas=frutas

)
```

Esto significa que **no escribiremos ocho tarjetas manualmente**.

El servidor generará automáticamente una tarjeta por cada fruta existente en la lista.

---

# 💡 En la siguiente parte...

Continuaremos completando el interior del ciclo `for`, donde construiremos cada tarjeta de fruta con:

- Imagen.
- Nombre.
- Precio.
- Descripción.
- Selector de cantidad.
- Campo oculto que enviará la información al servidor.

Después construiremos el formulario de datos del cliente y el botón **Crear Orden**, dejando completamente terminada la página principal.

{% for fruta in frutas %}

<div class="col-md-6 mb-4">

    <div class="card fruta-card h-100 shadow-sm">

        <!-- Imagen de la fruta -->

        <img

        src="{{ url_for('static', filename='images/' + fruta.imagen) }}"

        class="card-img-top"

        alt="{{ fruta.nombre }}">

        <div class="card-body">

            <!-- Nombre -->

            <h5 class="card-title">

                {{ fruta.nombre }}

            </h5>

            <!-- Precio -->

            <h6 class="text-success fw-bold">

                ${{ fruta.precio }}

            </h6>

            <!-- Descripción -->

            <p class="card-text">

                {{ fruta.descripcion }}

            </p>

        </div>

        <!-- Selector de cantidad -->

        <div class="card-footer bg-white">

            <input

            type="number"

            class="form-control"

            min="0"

            value="0"

            name="{{ fruta.nombre }}">

        </div>

    </div>

</div>

{% endfor %}

</div>

</div>

</div>

<!-- ===================================== -->
<!-- Información del cliente               -->
<!-- ===================================== -->

<div class="col-lg-4">

<div class="card shadow">

<div class="card-header">

<h3>

Información de Contacto

</h3>

</div>

<div class="card-body">

<!-- Nombre -->

<div class="mb-3">

<label class="form-label">

Nombre

</label>

<input

type="text"

class="form-control"

name="nombre"

required>

</div>

<!-- Correo -->

<div class="mb-3">

<label class="form-label">

Email

</label>

<input

type="email"

class="form-control"

name="email"

required>

</div>

<!-- Dirección -->

<div class="mb-3">

<label class="form-label">

Dirección de entrega

</label>

<textarea

class="form-control"

rows="3"

name="direccion"

required>

</textarea>

</div>

<hr>

<button

type="submit"

class="btn btn-primary w-100">

<i class="bi bi-cart-fill"></i>

Crear Orden

</button>

</div>

</div>

</div>

</div>

</div>

</form>

</body>

</html>
```

---

# 🔍 Analizando el código

## 🖼️ Mostrar la imagen

Cada tarjeta obtiene su imagen dinámicamente.

```jinja
<img

src="{{ url_for('static', filename='images/' + fruta.imagen) }}"

>
```

Si la fruta corresponde a:

```python
{
    "imagen":"manzana.png"
}
```

Flask generará automáticamente.

```text
/static/images/manzana.png
```

---

## 🏷️ Mostrar el nombre

```jinja
{{ fruta.nombre }}
```

Resultado.

```
Manzana
```

---

## 💲 Mostrar el precio

```jinja
{{ fruta.precio }}
```

Resultado.

```
$2.5
```

---

## 📝 Mostrar la descripción

```jinja
{{ fruta.descripcion }}
```

Cada tarjeta tendrá su propia descripción.

No es necesario escribir ocho tarjetas distintas.

Todo se genera automáticamente utilizando el ciclo `for`.

---

# 🔢 Selector de cantidad

Cada fruta posee un campo numérico.

```html
<input

type="number"

name="{{ fruta.nombre }}"

value="0"

min="0">
```

Este campo es muy importante.

Cuando el formulario se envía, Flask recibirá algo como:

```text
Manzana = 2

Plátano = 3

Fresa = 1
```

Observa que el atributo

```html
name="{{ fruta.nombre }}"
```

coincide exactamente con el nombre de cada fruta.

Gracias a esto podremos recuperar la información utilizando.

```python
request.form["Manzana"]

request.form["Plátano"]

request.form["Fresa"]
```

---

# 👤 Datos del cliente

Después de las frutas agregamos un segundo panel.

Aquí el usuario deberá ingresar.

- Nombre.
- Correo electrónico.
- Dirección.

Estos datos también viajarán junto con el formulario.

---

# 📨 Botón "Crear Orden"

Finalmente encontramos el botón.

```html
<button

type="submit">

Crear Orden

</button>
```

Al presionarlo ocurre el siguiente flujo.

```text
Usuario

↓

Completa sus datos

↓

Selecciona frutas

↓

Presiona

Crear Orden

↓

POST

↓

/checkout

↓

Servidor Flask
```

En este momento Flask recibirá toda la información utilizando:

```python
request.form
```

---

# 📌 ¿Qué datos recibirá Flask?

Si el usuario selecciona.

| Fruta   | Cantidad |
| ------- | -------: |
| Manzana |        2 |
| Plátano |        3 |
| Fresa   |        1 |

y completa el formulario.

```
Nombre

Juan Pérez

Correo

juan@gmail.com

Dirección

Av. Siempre Viva 123
```

El servidor recibirá un diccionario similar a este.

```python
{

    "nombre":"Juan Pérez",

    "email":"juan@gmail.com",

    "direccion":"Av. Siempre Viva 123",

    "Manzana":"2",

    "Plátano":"3",

    "Naranja":"0",

    "Fresa":"1",

    "Uva":"0",

    "Piña":"0",

    "Sandía":"0",

    "Mango":"0"

}
```

Observa que **todos los valores llegan como cadenas de texto (`str`)**.

Por este motivo, en `app.py` utilizamos la función:

```python
int()
```

para convertir las cantidades a números enteros antes de realizar cálculos.

---

# 🏁 Resultado esperado

Al finalizar esta parte tendrás completamente construida la página principal del Mercado de Frutas.

Esta página permitirá:

- Mostrar dinámicamente todas las frutas.
- Seleccionar cantidades.
- Capturar la información del cliente.
- Enviar el formulario mediante **POST**.

En la siguiente parte construiremos la página **checkout.html**, donde Flask mostrará el resumen completo de la compra, incluyendo las frutas seleccionadas, subtotales, total de frutas y el monto final a pagar.