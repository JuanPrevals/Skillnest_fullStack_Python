# 🔐 Sesiones y persistencia de datos en Flask

## 🎯 Objetivos

Al finalizar esta lección serás capaz de:

- Comprender qué significa que HTTP sea un protocolo **sin estado**.
- Comprender el concepto de **estado** en una aplicación web.
- Identificar por qué `request.form` no está disponible después de un `redirect()`.
- Comprender qué significa **persistencia de datos**.
- Conocer el concepto de **sesión**.
- Configurar sesiones en Flask.
- Utilizar `session` para conservar información entre solicitudes.
- Recuperar información de una sesión desde una ruta Flask.
- Acceder a información de sesión directamente desde una plantilla Jinja2.
- Comprender la relación entre **sesiones y cookies**.
- Reconocer qué tipo de información debería y no debería almacenarse en una sesión.

---

# 🧠 1. El problema que debemos resolver

En la lección anterior trabajamos con un formulario.

El usuario enviaba información mediante:

```text
POST
```

Flask podía acceder a esos datos utilizando:

```python
request.form
```

Por ejemplo:

```python
nombre = request.form["nombre"]
email = request.form["email"]
```

Después utilizábamos:

```python
redirect("/mostrar_usuario")
```

El problema era que al llegar a:

```text
/mostrar_usuario
```

ya no podíamos acceder a:

```python
request.form
```

¿Por qué?

Porque la redirección genera una **nueva solicitud HTTP**.

---

# 🔄 2. Recordemos el flujo anterior

Nuestro flujo era:

```text
Formulario
     │
     │ POST
     ▼
/crear_usuario
     │
     │ request.form
     │
     │ redirect()
     ▼
/mostrar_usuario
     │
     │ GET
     ▼
mostrar.html
```

La información:

```text
nombre
email
```

pertenecía a la primera solicitud.

Cuando realizamos:

```python
redirect("/mostrar_usuario")
```

el navegador realiza una nueva solicitud.

Por lo tanto:

```python
request.form
```

ya no contiene los datos anteriores.

---

# 🧠 3. ¿Por qué ocurre esto?

HTTP es un protocolo **sin estado (stateless)**.

Esto significa que cada solicitud y respuesta se considera independiente.

Por ejemplo:

```text
Solicitud 1

POST /crear_usuario

nombre = Ana
email = ana@gmail.com
```

y posteriormente:

```text
Solicitud 2

GET /mostrar_usuario
```

La segunda solicitud no conoce automáticamente los datos enviados durante la primera.

Podemos representarlo así:

```text
SOLICITUD 1
────────────────────

POST /crear_usuario

nombre = Ana
email = ana@gmail.com


          ❌


SOLICITUD 2
────────────────────

GET /mostrar_usuario

No conoce automáticamente:

nombre
email
```

---

# 🌐 4. Entonces, ¿cómo funcionan las páginas web reales?

Si HTTP no mantiene información entre solicitudes, podemos preguntarnos:

> ¿Cómo sabe una página web que ya inicié sesión?

> ¿Cómo sabe qué productos tengo en mi carrito?

> ¿Cómo recuerda mis preferencias?

> ¿Cómo puede mostrar mi nombre en diferentes páginas?

La respuesta es que las aplicaciones utilizan mecanismos de **persistencia de datos**.

Uno de estos mecanismos son las:

# 🔐 Sesiones

---

# 📦 5. ¿Qué es una sesión?

Una **sesión** permite mantener determinada información asociada a un usuario entre diferentes solicitudes.

Podemos imaginarla como un pequeño espacio donde nuestra aplicación puede guardar información que necesitaremos posteriormente.

Por ejemplo:

```text
Sesión del usuario

┌──────────────────────────────┐
│ nombre_usuario = "Ana"       │
│ email_usuario = "ana@mail"   │
└──────────────────────────────┘
```

Entonces el flujo puede convertirse en:

```text
Formulario
     │
     │ POST
     ▼
/crear_usuario
     │
     │ request.form
     │
     │ Guardar en session
     ▼
redirect()
     │
     │ GET
     ▼
/mostrar_usuario
     │
     │ Leer session
     ▼
mostrar.html
```

Ahora sí podemos conservar información entre solicitudes.

---

# 🧠 6. `request.form` vs `session`

Es importante distinguir estos dos conceptos.

## `request.form`

Contiene información enviada **en la solicitud actual**.

```python
request.form["nombre"]
```

Por ejemplo:

```text
POST
 ↓
request.form
 ↓
nombre
```

---

## `session`

Permite almacenar información para utilizarla **en solicitudes posteriores**.

```python
session["nombre_usuario"]
```

Por ejemplo:

```text
POST
 ↓
request.form
 ↓
session
 ↓
redirect
 ↓
GET
 ↓
session
```

---

# 📊 Comparación

| Característica | `request.form` | `session` |
|---|---|---|
| Proviene de | Formulario | Datos almacenados en sesión |
| Disponible después de redirect | ❌ | ✅ |
| Persiste entre solicitudes | ❌ | ✅ |
| Se utiliza para | Recibir datos | Mantener estado |
| Ejemplo | `request.form["nombre"]` | `session["nombre"]` |

---

# 🛠️ 7. Configurar sesiones en Flask

Volveremos a trabajar con nuestro proyecto:

```text
formulario_prueba/
```

La estructura será:

```text
formulario_prueba/

│
├── server.py
│
└── templates/
    │
    ├── index.html
    │
    └── mostrar.html
```

---

# 🐍 8. Importar `session`

En `server.py` debemos agregar `session` a nuestras importaciones.

```python
from flask import Flask, render_template, request, redirect, session
```

Ahora Flask conoce el objeto:

```python
session
```

que utilizaremos para almacenar información.

---

# 🔑 9. Configurar `SECRET_KEY`

Flask necesita una clave secreta para proteger la información de la sesión.

Agregaremos:

```python
app.secret_key = "una-clave-secreta"
```

Nuestro inicio de aplicación quedará:

```python
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "una-clave-secreta"
```

---

# ⚠️ Importante sobre `SECRET_KEY`

En un ejercicio educativo podemos utilizar:

```python
app.secret_key = "una-clave-secreta"
```

Pero en una aplicación real **no debemos publicar una clave secreta en GitHub ni compartirla públicamente**.

Una aplicación profesional debería utilizar una clave aleatoria y almacenarla mediante una variable de entorno.

Por ahora utilizaremos una clave sencilla porque el objetivo de esta lección es comprender el funcionamiento de `session`.

---

# 📝 10. Guardar información en una sesión

La ruta que recibe el formulario es:

```python
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
```

Aquí tenemos acceso a:

```python
request.form
```

Por lo tanto, este es el lugar adecuado para guardar la información en la sesión.

```python
session["nombre_usuario"] = request.form["nombre"]

session["email_usuario"] = request.form["email"]
```

Estamos creando dos propiedades:

```text
nombre_usuario
email_usuario
```

---

# 🧩 11. Código completo de `server.py`

Reemplaza el contenido de `server.py` por el siguiente código:

```python
# ==========================================
# IMPORTACIONES
# ==========================================

from flask import Flask, render_template, request, redirect, session


# ==========================================
# CREAR APLICACIÓN
# ==========================================

app = Flask(__name__)


# ==========================================
# CLAVE SECRETA
# ==========================================

# Flask utiliza esta clave para proteger
# la información asociada a la sesión.
#
# En proyectos reales NO debemos publicar
# esta clave en GitHub.

app.secret_key = "una-clave-secreta"


# ==========================================
# RUTA PRINCIPAL
# ==========================================

@app.route("/")
def index():
    """
    Muestra el formulario de creación
    de usuario.
    """

    return render_template("index.html")


# ==========================================
# PROCESAR FORMULARIO
# ==========================================

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    """
    Recibe los datos enviados mediante POST
    y los almacena en la sesión.
    """

    # --------------------------------------
    # Obtener datos del formulario
    # --------------------------------------

    nombre = request.form["nombre"]

    email = request.form["email"]


    # --------------------------------------
    # Mostrar información en la terminal
    # --------------------------------------

    print("===================================")

    print("Información recibida")

    print(f"Nombre: {nombre}")

    print(f"Email: {email}")

    print("===================================")


    # --------------------------------------
    # Guardar información en la sesión
    # --------------------------------------

    session["nombre_usuario"] = nombre

    session["email_usuario"] = email


    # --------------------------------------
    # Redireccionar
    # --------------------------------------

    return redirect("/mostrar_usuario")


# ==========================================
# MOSTRAR USUARIO
# ==========================================

@app.route("/mostrar_usuario")
def mostrar_usuario():
    """
    Recupera la información almacenada
    en la sesión.
    """

    # --------------------------------------
    # Leer información desde session
    # --------------------------------------

    nombre = session["nombre_usuario"]

    email = session["email_usuario"]


    # --------------------------------------
    # Mostrar información en terminal
    # --------------------------------------

    print("===================================")

    print("Usuario redirigido")

    print(f"Nombre: {nombre}")

    print(f"Email: {email}")

    print("===================================")


    # --------------------------------------
    # Renderizar plantilla
    # --------------------------------------

    return render_template("mostrar.html")


# ==========================================
# EJECUTAR SERVIDOR
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)
```

---

# 🔍 12. Analicemos la parte más importante

Tenemos:

```python
session["nombre_usuario"] = nombre
```

Esto significa:

> Guarda el valor de `nombre` en la sesión utilizando `nombre_usuario` como clave.

Por ejemplo, si:

```text
nombre = "Ana"
```

la sesión tendrá conceptualmente:

```text
nombre_usuario → Ana
```

Lo mismo hacemos con:

```python
session["email_usuario"] = email
```

La sesión tendrá:

```text
nombre_usuario → Ana

email_usuario → ana@gmail.com
```

---

# 🔄 13. ¿Qué ocurre después del `redirect()`?

Ahora nuestro flujo es:

```text
Formulario

     │

     │ POST

     ▼

/crear_usuario

     │

     ├── request.form
     │
     ├── session["nombre_usuario"]
     │
     └── session["email_usuario"]

     │

     ▼

redirect()

     │

     │ GET

     ▼

/mostrar_usuario

     │

     ├── session["nombre_usuario"]
     │
     └── session["email_usuario"]

     │

     ▼

mostrar.html
```

La diferencia fundamental es que ahora **la información no depende de `request.form`**.

La información fue almacenada en:

```python
session
```

---

# 📝 14. Recuperar información desde la sesión

En:

```python
/mostrar_usuario
```

podemos hacer:

```python
nombre = session["nombre_usuario"]

email = session["email_usuario"]
```

Y ahora podemos utilizar esos datos aunque la solicitud actual sea:

```text
GET
```

Esto resuelve el problema que teníamos en la lección anterior.

---

# 🌐 15. Acceder a la sesión desde Jinja2

Una característica muy útil de Flask es que las plantillas también pueden acceder directamente a:

```python
session
```

Por ejemplo:

```jinja
{{ session["nombre_usuario"] }}
```

y:

```jinja
{{ session["email_usuario"] }}
```

No necesitamos necesariamente enviar estas variables mediante:

```python
render_template(
    "mostrar.html",
    nombre=nombre,
    email=email
)
```

porque Flask pone `session` disponible para las plantillas.

---

# 📝 16. Crear `mostrar.html`

Reemplaza el contenido de:

```text
templates/mostrar.html
```

por:

```html
<!DOCTYPE html>

<html lang="es">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0">

    <title>Usuario</title>

</head>

<body>

    <h1>Usuario registrado</h1>

    <hr>

    <!--
        Podemos acceder directamente
        a la sesión desde Jinja2.
    -->

    <h3>

        Nombre:

        {{ session["nombre_usuario"] }}

    </h3>


    <h3>

        E-mail:

        {{ session["email_usuario"] }}

    </h3>


    <hr>

    <a href="{{ url_for('index') }}">

        Volver al formulario

    </a>

</body>

</html>
```

---

# 📝 17. Crear `index.html`

Nuestro formulario será:

```html
<!DOCTYPE html>

<html lang="es">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0">

    <title>Crear Usuario</title>

</head>

<body>

    <h1>Crear Usuario</h1>

    <form
        action="{{ url_for('crear_usuario') }}"
        method="POST">

        <label for="nombre">

            Nombre:

        </label>

        <input
            type="text"
            id="nombre"
            name="nombre"
            required>

        <br><br>


        <label for="email">

            E-mail:

        </label>

        <input
            type="email"
            id="email"
            name="email"
            required>

        <br><br>


        <button type="submit">

            Crear Usuario

        </button>

    </form>

</body>

</html>
```

---

# ▶️ 18. Probar la aplicación

Ejecuta:

```bash
python server.py
```

Abre:

```text
http://127.0.0.1:5000/
```

Completa:

```text
Nombre:

Ana
```

y:

```text
E-mail:

ana@gmail.com
```

Presiona:

```text
Crear Usuario
```

Flask realizará:

```text
POST /crear_usuario
```

guardará los datos:

```python
session["nombre_usuario"] = "Ana"

session["email_usuario"] = "ana@gmail.com"
```

y después:

```python
redirect("/mostrar_usuario")
```

Finalmente se realizará:

```text
GET /mostrar_usuario
```

La página mostrará:

```text
Usuario registrado

Nombre: Ana

E-mail: ana@gmail.com
```

---

# 🧠 19. Lo importante: la información sobrevivió al redirect

Este es el concepto central de esta lección.

Antes:

```text
POST
 ↓
request.form
 ↓
redirect
 ↓
GET
 ↓
❌ request.form vacío
```

Ahora:

```text
POST
 ↓
request.form
 ↓
session
 ↓
redirect
 ↓
GET
 ↓
session
 ↓
✅ información disponible
```

---

# 🍪 20. ¿Qué relación tienen las cookies?

Las sesiones de Flask utilizan mecanismos asociados al cliente para mantener la información de sesión.

En la configuración predeterminada de Flask, la sesión se implementa mediante una **cookie firmada**.

Esto significa que el navegador recibe información relacionada con la sesión y la devuelve en solicitudes posteriores.

Conceptualmente:

```text
Servidor
   │
   │ Información de sesión
   ▼
Navegador
   │
   │ Cookie
   ▼
Servidor
```

Flask utiliza la `SECRET_KEY` para proteger la integridad de esa información.

---

# ⚠️ 21. ¿Puedo guardar cualquier cosa en `session`?

No.

Aunque podemos almacenar información en una sesión, debemos utilizarla de manera responsable.

Por ejemplo, podemos guardar:

```python
session["nombre_usuario"] = "Ana"

session["idioma"] = "es"

session["tema"] = "oscuro"
```

Pero no deberíamos utilizar la sesión como si fuera una base de datos.

Evita almacenar grandes cantidades de información.

Tampoco debemos guardar información extremadamente sensible directamente en una sesión sin comprender las implicaciones de seguridad y privacidad.

---

# 🗄️ 22. Sesión vs Base de Datos

Es importante comenzar a distinguir ambos conceptos.

### Sesión

Adecuada para información temporal relacionada con la interacción del usuario.

Ejemplos:

```text
Usuario autenticado

Preferencias

Carrito temporal

Mensajes

Identificadores
```

### Base de datos

Adecuada para información que debe almacenarse de manera estructurada y persistente.

Ejemplos:

```text
Usuarios

Productos

Pedidos

Clientes

Historial de compras
```

Podemos visualizarlo así:

```text
                 APLICACIÓN FLASK
                       │
          ┌────────────┴────────────┐
          │                         │
       SESSION                  BASE DE DATOS
          │                         │
     Estado temporal          Datos persistentes
          │                         │
    Usuario actual              Usuarios
    Preferencias                Productos
    Carrito                     Pedidos
    Mensajes                    Historial
```

---

# 🧪 23. Ejercicio práctico

## Desafío: Perfil de usuario

Ahora modifica el proyecto para almacenar **tres datos** en la sesión.

El formulario deberá solicitar:

```text
Nombre

Email

Ciudad
```

---

## Requisitos

### 1. Modificar el formulario

Agrega un nuevo campo:

```html
<input
    type="text"
    name="ciudad">
```

---

### 2. Recibir el dato en Flask

En:

```python
crear_usuario()
```

obtén:

```python
ciudad = request.form["ciudad"]
```

---

### 3. Guardarlo en la sesión

Utiliza:

```python
session["ciudad_usuario"] = ciudad
```

---

### 4. Mostrarlo en `/mostrar_usuario`

Agrega:

```python
ciudad = session["ciudad_usuario"]
```

---

### 5. Mostrarlo en HTML

Utiliza:

```jinja
{{ session["ciudad_usuario"] }}
```

El resultado debería ser:

```text
Usuario registrado

Nombre: Ana

E-mail: ana@gmail.com

Ciudad: Santiago
```

---

# ⭐ 24. Desafío adicional

Agrega una ruta:

```text
/perfil
```

Esta ruta deberá mostrar un pequeño perfil utilizando exclusivamente información almacenada en `session`.

Por ejemplo:

```text
============================

Perfil de usuario

Nombre: Ana

Email: ana@gmail.com

Ciudad: Santiago

============================

[Volver]
```

La ruta deberá utilizar:

```python
@app.route("/perfil")
```

y obtener los datos desde:

```python
session
```

---

# 🧠 25. Preguntas de reflexión

Responde antes de continuar.

### 1.

¿Qué significa que HTTP sea un protocolo **sin estado**?

---

### 2.

¿Por qué `request.form` no está disponible después de un `redirect()`?

---

### 3.

¿Cuál es la diferencia entre:

```python
request.form["nombre"]
```

y:

```python
session["nombre_usuario"]
```

---

### 4.

¿Por qué necesitamos configurar:

```python
app.secret_key
```

?

---

### 5.

¿Por qué no deberíamos utilizar `session` como sustituto de una base de datos?

---

### 6.

¿Qué tipo de información tendría sentido almacenar temporalmente en una sesión?

---

# 📚 26. Conceptos fundamentales

| Concepto | Descripción |
|---|---|
| Estado | Información que una aplicación conserva para utilizarla posteriormente. |
| Stateless | Característica de HTTP por la cual cada solicitud es independiente. |
| Persistencia | Capacidad de conservar información más allá de una solicitud. |
| Sesión | Mecanismo que permite mantener información asociada a un usuario entre solicitudes. |
| `session` | Objeto de Flask utilizado para almacenar y recuperar información de sesión. |
| `SECRET_KEY` | Clave utilizada por Flask para proteger la información de sesión. |
| Cookie | Pequeño dato almacenado en el navegador que puede participar en el mantenimiento de una sesión. |
| `request.form` | Datos recibidos desde un formulario en la solicitud actual. |
| `redirect()` | Genera una redirección hacia otra URL. |

---

# 🔄 27. Flujo completo aprendido

Ahora podemos comprender el flujo completo:

```text
                    USUARIO
                       │
                       ▼
                  index.html
                       │
                       │ POST
                       ▼
                /crear_usuario
                       │
                       │
                request.form
                       │
                       ▼
                    session
                       │
                       │
                   redirect()
                       │
                       ▼
               /mostrar_usuario
                       │
                       │ GET
                       ▼
                    session
                       │
                       ▼
                 mostrar.html
```

---

# 🏁 Resultado esperado

Al finalizar esta lección deberás comprender que:

> **HTTP no mantiene automáticamente el estado entre solicitudes.**

Por eso:

```python
request.form
```

pertenece a una solicitud concreta.

Cuando necesitamos conservar información para solicitudes posteriores podemos utilizar:

```python
session
```

El patrón aprendido será:

```python
request.form
        ↓
     session
        ↓
    redirect()
        ↓
       GET
        ↓
     session
        ↓
    HTML
```

Este concepto será fundamental para desarrollar funcionalidades como:

- Inicio de sesión.
- Cierre de sesión.
- Carritos de compra.
- Preferencias de usuario.
- Mensajes temporales.
- Datos asociados a una navegación.

Más adelante, las **bases de datos** permitirán llevar este concepto mucho más lejos, almacenando información estructurada que debe sobrevivir a las sesiones y mantenerse disponible de forma permanente.