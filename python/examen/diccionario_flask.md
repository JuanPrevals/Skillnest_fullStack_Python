# 🧩 Arquitectura de una aplicación Flask con MySQL

> **Guía de comprensión:** cómo organizar un proyecto Flask profesional utilizando Blueprints, Controllers, Models, MySQL, variables de entorno y `request`.

---

# 🎯 Objetivo

Aprender a comprender la estructura de una aplicación Flask que ha crecido más allá de un solo archivo.

En proyectos pequeños podemos tener:

```text
app.py
```

con todas las rutas y lógica.

Pero cuando la aplicación crece aparecen muchas responsabilidades:

- usuarios;
- misiones;
- autenticación;
- base de datos;
- formularios;
- archivos;
- plantillas;
- lógica de negocio.

En ese momento necesitamos separar el proyecto.

La idea central de esta arquitectura es:

```text
Cada archivo tiene una responsabilidad.
```

---

# 1. 🧠 ¿Por qué separar los archivos?

Imagina que todo nuestro proyecto estuviera dentro de:

```text
app.py
```

y tuviéramos:

```python
# Usuarios

@app.route("/usuarios")
def usuarios():
    ...


# Misiones

@app.route("/misiones")
def misiones():
    ...


# Login

@app.route("/login")
def login():
    ...


# Consultas SQL

...


# Conexión MySQL

...


# Validaciones

...


# Procesamiento
```

Al principio puede funcionar.

El problema aparece cuando la aplicación empieza a crecer.

```text
app.py
│
├── Usuarios
├── Misiones
├── Login
├── Registro
├── SQL
├── MySQL
├── Validaciones
├── Formularios
└── ...
```

El archivo termina siendo difícil de:

- leer;
- modificar;
- depurar;
- mantener;
- reutilizar.

Por eso dividimos el proyecto.

---

# 2. 🏗️ La idea de separación de responsabilidades

Una arquitectura organizada puede verse así:

```text
FLASK
│
├── Controllers
│      ↓
│   reciben solicitudes
│
├── Models
│      ↓
│   trabajan con los datos
│
├── Database
│      ↓
│   conecta con MySQL
│
├── Templates
│      ↓
│   muestran información
│
└── Static
       ↓
    CSS / JS / imágenes
```

Podemos imaginarlo como una empresa:

```text
Controllers
    ↓
Recepción

Models
    ↓
Administración de datos

Database
    ↓
Conexión con sistemas externos

Templates
    ↓
Presentación al cliente
```

---

# 3. 📁 Estructura del proyecto

Una estructura habitual podría ser:

```text
flask_app/
│
├── __init__.py
├── app.py
├── .env
├── requirements.txt
│
├── controllers/
│   ├── controlador_usuarios.py
│   └── controlador_misiones.py
│
├── models/
│   ├── usuario.py
│   └── mision.py
│
├── templates/
│
└── static/
    ├── css/
    ├── js/
    └── img/
```

Cada carpeta tiene una función específica.

---

# 4. 🐍 `__init__.py`

Comencemos por el archivo que crea la aplicación Flask.

```text
flask_app/
└── __init__.py
```

## Código

```python
from flask import Flask

# Creamos una única instancia de Flask.
app = Flask(__name__)

# Clave necesaria para utilizar session.
#
# En producción debería almacenarse mediante
# una variable de entorno.
app.secret_key = "clave-de-desarrollo"
```

---

# 🔍 ¿Qué hace este archivo?

La línea:

```python
app = Flask(__name__)
```

crea nuestra aplicación.

Podemos imaginarlo así:

```text
__init__.py
      ↓
crea
      ↓
app
      ↓
aplicación Flask
```

Todos los demás componentes podrán trabajar con esa misma aplicación.

---

# 5. 📦 `requirements.txt`

Este archivo contiene las dependencias necesarias para ejecutar el proyecto.

```text
Flask
PyMySQL
python-dotenv
```

Por ejemplo:

```text
requirements.txt
```

puede contener:

```text
Flask==3.1.2
PyMySQL==1.1.1
python-dotenv==1.1.1
```

Luego una persona que descargue el proyecto puede instalar todo mediante:

```bash
pip install -r requirements.txt
```

---

# 🧠 ¿Por qué existe este archivo?

Sin `requirements.txt`, otra persona tendría que averiguar:

```text
¿Qué librerías necesita el proyecto?
```

Con él:

```text
requirements.txt
       ↓
pip install -r requirements.txt
       ↓
dependencias instaladas
```

---

# 6. 🔐 `.env`

Las aplicaciones suelen necesitar información que **no debería escribirse directamente en el código**.

Por ejemplo:

```text
MYSQL_HOST
MYSQL_USER
MYSQL_PASSWORD
MYSQL_DATABASE
```

Creamos:

```text
.env
```

con:

```env
# ==========================================
# CONFIGURACIÓN DE BASE DE DATOS
# ==========================================

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=TU_PASSWORD
MYSQL_DATABASE=voluntame_db
```

> **Importante:** nunca publiques contraseñas reales en GitHub. El archivo `.env` normalmente debe incluirse en `.gitignore`.

---

# 7. 🚫 `.gitignore`

Agregamos:

```text
.env
venv/
__pycache__/
*.pyc
```

Por ejemplo:

```text
.gitignore
```

puede contener:

```text
venv/
__pycache__/
*.pyc
.env
```

Así evitamos subir información sensible.

---

# 8. 📥 `load_dotenv()`

Para utilizar `.env`, instalamos:

```text
python-dotenv
```

y luego:

```python
from dotenv import load_dotenv

load_dotenv()
```

Esto carga las variables definidas en `.env`.

Podemos imaginarlo así:

```text
.env
 ↓
load_dotenv()
 ↓
variables de entorno
```

---

# 9. 🧩 `os.environ.get()`

Una vez cargadas las variables:

```python
import os
```

podemos obtenerlas:

```python
host = os.environ.get("MYSQL_HOST")
```

o:

```python
password = os.environ.get("MYSQL_PASSWORD")
```

Por ejemplo:

```env
MYSQL_HOST=localhost
```

permite:

```python
os.environ.get("MYSQL_HOST")
```

obtener:

```text
localhost
```

---

# 10. 🐬 Conexión a MySQL

Ahora necesitamos una pieza que se encargue exclusivamente de hablar con MySQL.

Creamos:

```text
mysqlconnection.py
```

---

# 🔌 `mysqlconnection.py`

```python
import os

import pymysql.cursors

from dotenv import load_dotenv


# ==========================================================
# CARGAR VARIABLES DE ENTORNO
# ==========================================================

load_dotenv()


# ==========================================================
# CONEXIÓN MYSQL
# ==========================================================

class MySQLConnection:

    def __init__(self, db):

        self.connection = pymysql.connect(

            host=os.environ.get("MYSQL_HOST"),

            user=os.environ.get("MYSQL_USER"),

            password=os.environ.get("MYSQL_PASSWORD"),

            database=db,

            charset="utf8mb4",

            cursorclass=pymysql.cursors.DictCursor,

            autocommit=True
        )


    # ======================================================
    # EJECUTAR CONSULTAS
    # ======================================================

    def query_db(self, query, data=None):

        with self.connection.cursor() as cursor:

            try:

                print("Ejecutando consulta:")

                print(query)


                cursor.execute(query, data)


                # --------------------------------------------------
                # SELECT
                # --------------------------------------------------

                if query.strip().lower().startswith("select"):

                    return cursor.fetchall()


                # --------------------------------------------------
                # INSERT
                # --------------------------------------------------

                elif query.strip().lower().startswith("insert"):

                    return cursor.lastrowid


                # --------------------------------------------------
                # UPDATE / DELETE
                # --------------------------------------------------

                else:

                    return None


            except Exception as e:

                print("Error en la Base de Datos:")

                print(e)

                return False


            finally:

                self.connection.close()


# ==========================================================
# FUNCIÓN AUXILIAR
# ==========================================================

def connect_to_mysql(db):

    return MySQLConnection(db)
```

---

# 🧠 ¿Qué responsabilidad tiene este archivo?

Solamente la conexión y ejecución de consultas.

```text
mysqlconnection.py
       │
       ├── conectar
       ├── ejecutar SQL
       ├── recuperar resultados
       └── cerrar conexión
```

El controlador no necesita saber todos estos detalles.

El modelo tampoco.

Simplemente pueden solicitar:

```python
connect_to_mysql(...)
```

---

# 11. 📊 `DictCursor`

Tenemos:

```python
cursorclass=pymysql.cursors.DictCursor
```

Esto hace que un `SELECT` pueda devolver:

```python
[
    {
        "id": 1,
        "nombre": "Firulais",
        "tipo": "Perro"
    },

    {
        "id": 2,
        "nombre": "Michi",
        "tipo": "Gato"
    }
]
```

Es decir:

```text
SELECT
 ↓
lista
 ↓
diccionarios
```

Esto resulta muy cómodo para trabajar posteriormente con objetos y Jinja2.

---

# 12. 🐕 Models

Ahora tenemos que representar nuestros datos.

Supongamos una tabla:

```text
mascotas
```

crearemos:

```text
models/
└── mascota.py
```

---

# 🐕 `mascota.py`

```python
from mysqlconnection import connect_to_mysql


class Mascota:

    def __init__(self, data):

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.tipo = data["tipo"]

        self.color = data["color"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]


    @classmethod
    def get_all(cls):

        query = """
            SELECT *
            FROM mascotas;
        """


        resultados = connect_to_mysql(
            "voluntame_db"
        ).query_db(query)


        mascotas = []


        for mascota in resultados:

            mascotas.append(
                cls(mascota)
            )


        return mascotas
```

---

# 🧠 ¿Qué hace un Model?

El modelo representa y gestiona los datos.

En este caso:

```text
Mascota
```

representa:

```text
tabla mascotas
```

Por lo tanto:

```text
MySQL
 ↓
mascotas
 ↓
Mascota
 ↓
objetos Python
```

---

# 13. 🔄 `@classmethod`

Observa:

```python
@classmethod
def get_all(cls):
```

Esto permite llamar:

```python
Mascota.get_all()
```

sin crear primero una mascota.

Tiene sentido porque:

```text
get_all()
```

consulta toda la colección de mascotas.

---

# 14. 🔎 Consultar por ID

Podríamos agregar:

```python
@classmethod
def get_by_id(cls, data):

    query = """
        SELECT *
        FROM mascotas
        WHERE id = %(id)s;
    """

    resultado = connect_to_mysql(
        "voluntame_db"
    ).query_db(query, data)

    if not resultado:
        return None

    return cls(resultado[0])
```

Entonces:

```python
data = {
    "id": 5
}
```

y:

```python
Mascota.get_by_id(data)
```

buscará:

```text
mascota #5
```

---

# 15. 📦 ¿Qué es `data`?

`data` suele ser un diccionario que contiene valores que necesita una consulta.

Por ejemplo:

```python
data = {
    "id": 5
}
```

y una consulta:

```sql
SELECT *
FROM mascotas
WHERE id = %(id)s;
```

La clave:

```text
id
```

se relaciona con:

```text
%(id)s
```

---

# 16. 🗑️ `Mision.eliminar(data)`

Una llamada como:

```python
Mision.eliminar(data)
```

significa:

> Ejecutar el método `eliminar()` de la clase `Mision`.

Por ejemplo:

```python
data = {
    "id_mision": id_mision
}

Mision.eliminar(data)
```

Si:

```python
id_mision = 25
```

entonces:

```python
data = {
    "id_mision": 25
}
```

El modelo podría ejecutar:

```sql
DELETE
FROM misiones
WHERE id_mision = %(id_mision)s;
```

---

# 17. 🔗 `Mision.obtener_por_id_con_relaciones(data)`

Esta llamada:

```python
mision = Mision.obtener_por_id_con_relaciones(data)
```

significa:

> Obtener una misión mediante su identificador incluyendo información relacionada.

Por ejemplo:

```text
Misión
│
├── organización
├── categoría
├── responsable
└── participantes
```

Esto normalmente implica una consulta SQL con `JOIN` o varias consultas coordinadas.

---

# 18. 🧭 Controllers

Ahora llegamos a una de las piezas más importantes.

Los **Controllers** reciben las solicitudes HTTP y deciden qué debe ocurrir.

Por ejemplo:

```text
controllers/
│
├── controlador_usuarios.py
└── controlador_misiones.py
```

Podemos imaginar:

```text
Navegador
    ↓
Controller
    ↓
Model
    ↓
MySQL
```

---

# 19. 🧩 Blueprint

Antes de definir un Controller, aparece:

```python
Blueprint
```

Un Blueprint permite agrupar rutas relacionadas.

Por ejemplo:

```text
usuarios
 ↓
usuarios_bp

misiones
 ↓
misiones_bp
```

---

# 20. Crear un Blueprint

En:

```text
controlador_misiones.py
```

podemos tener:

```python
from flask import Blueprint

misiones_bp = Blueprint(
    "misiones",
    __name__
)
```

Esta línea crea un Blueprint llamado:

```text
misiones
```

---

# 🧠 ¿Qué significa `__name__`?

`__name__` es una variable especial de Python que identifica el módulo actual.

No necesitamos memorizar su funcionamiento interno para utilizar Blueprint.

En términos sencillos:

```python
Blueprint("misiones", __name__)
```

significa:

> Crear un grupo de rutas llamado `misiones` dentro de este módulo.

---

# 21. Rutas dentro del Blueprint

Podemos definir:

```python
@misiones_bp.route("/dashboard")
def dashboard():

    return "Dashboard de misiones"
```

Ahora esta ruta pertenece al Blueprint:

```text
misiones_bp
```

y no directamente a:

```text
app
```

---

# 22. `@app.route()` vs `@misiones_bp.route()`

Sin Blueprint:

```python
@app.route("/dashboard")
def dashboard():
```

Con Blueprint:

```python
@misiones_bp.route("/dashboard")
def dashboard():
```

La diferencia está en quién administra la ruta.

```text
@app.route
    ↓
aplicación principal

@misiones_bp.route
    ↓
Blueprint
```

---

# 23. Registrar un Blueprint

Crear el Blueprint no es suficiente.

Hay que registrarlo.

En nuestro archivo principal:

```python
from flask_app import app

from flask_app.controllers.controlador_usuarios import usuarios_bp

from flask_app.controllers.controlador_misiones import misiones_bp


app.register_blueprint(usuarios_bp)

app.register_blueprint(misiones_bp)
```

---

# 🧠 ¿Qué hace `register_blueprint()`?

Esta línea:

```python
app.register_blueprint(misiones_bp)
```

puede leerse como:

> "Agrega todas las rutas de `misiones_bp` a nuestra aplicación Flask."

Visualmente:

```text
misiones_bp
│
├── /dashboard
├── /crear
├── /editar
└── /eliminar
       │
       ▼
register_blueprint()
       │
       ▼
      app
```

---

# 24. ¿Por qué usar Blueprint?

Supongamos que tenemos:

```text
100 rutas
```

No queremos tener:

```text
app.py
    ↓
100 rutas
```

Podemos dividirlas:

```text
usuarios
    ↓
usuarios_bp
    ↓
20 rutas

misiones
    ↓
misiones_bp
    ↓
30 rutas

organizaciones
    ↓
organizaciones_bp
    ↓
25 rutas

auth
    ↓
auth_bp
    ↓
25 rutas
```

Así cada módulo queda organizado.

---

# 25. 📥 `request`

Ahora necesitamos entender cómo el servidor recibe información del navegador.

Flask proporciona:

```python
request
```

`request` representa la solicitud HTTP actual.

---

# 26. `request.form`

Si tenemos:

```html
<form method="POST">

    <input
        type="text"
        name="nombre"
    >

    <button type="submit">
        Guardar
    </button>

</form>
```

podemos recibir:

```python
from flask import request
```

y:

```python
nombre = request.form["nombre"]
```

Si el usuario escribió:

```text
Dany
```

obtendremos:

```text
Dany
```

---

# 27. `request.args`

Si tenemos:

```text
/buscar?nombre=Dany
```

podemos obtener:

```python
nombre = request.args.get("nombre")
```

Entonces:

```text
URL
 ↓
request.args
 ↓
nombre
```

---

# 28. Diferencia entre `request.form` y `request.args`

| Elemento | Uso |
|---|---|
| `request.form` | Datos enviados mediante formularios, normalmente POST |
| `request.args` | Parámetros incluidos en la URL, normalmente GET |

Ejemplo POST:

```python
request.form["nombre"]
```

Ejemplo GET:

```python
request.args.get("nombre")
```

---

# 29. `request.method`

También podemos consultar el método HTTP:

```python
request.method
```

Puede entregar:

```text
GET
```

o:

```text
POST
```

Por ejemplo:

```python
if request.method == "POST":
    ...
```

---

# 30. Controller completo

Ahora podemos unir Blueprint + request + Model.

```python
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from flask_app.models.mision import Mision


# ==========================================================
# BLUEPRINT
# ==========================================================

misiones_bp = Blueprint(
    "misiones",
    __name__
)


# ==========================================================
# DASHBOARD
# ==========================================================

@misiones_bp.route("/dashboard")
def dashboard():

    misiones = Mision.obtener_todas()

    return render_template(
        "misiones/dashboard.html",
        misiones=misiones
    )


# ==========================================================
# ELIMINAR MISIÓN
# ==========================================================

@misiones_bp.route(
    "/eliminar/<int:id_mision>",
    methods=["POST"]
)
def eliminar(id_mision):

    data = {
        "id_mision": id_mision
    }

    Mision.eliminar(data)

    return redirect(
        url_for("misiones.dashboard")
    )
```

---

# 🔍 Analizando el flujo

Cuando el usuario visita:

```text
/misiones/dashboard
```

el recorrido puede ser:

```text
Navegador
    ↓
Flask
    ↓
misiones_bp
    ↓
dashboard()
    ↓
Mision.obtener_todas()
    ↓
mysqlconnection.py
    ↓
MySQL
    ↓
datos
    ↓
Jinja2
    ↓
HTML
    ↓
Navegador
```

---

# 31. ¿Qué ocurre al eliminar?

Supongamos:

```text
POST /eliminar/25
```

Flask recibe:

```python
id_mision = 25
```

Luego:

```python
data = {
    "id_mision": 25
}
```

Después:

```python
Mision.eliminar(data)
```

El modelo puede ejecutar:

```sql
DELETE
FROM misiones
WHERE id_mision = %(id_mision)s;
```

Finalmente:

```python
return redirect(
    url_for("misiones.dashboard")
)
```

---

# 32. `url_for()` con Blueprints

Aquí aparece una diferencia importante.

Sin Blueprint podemos tener:

```python
url_for("index")
```

Pero si la función pertenece a un Blueprint llamado:

```text
misiones
```

podemos utilizar:

```python
url_for("misiones.dashboard")
```

La estructura es:

```text
nombre_blueprint.nombre_funcion
```

Por ejemplo:

```python
url_for("misiones.dashboard")
```

busca:

```python
def dashboard():
```

dentro del Blueprint:

```text
misiones
```

---

# 33. Flujo completo de una aplicación profesional

Ahora podemos unir todas las piezas.

```text
                         NAVEGADOR
                              │
                              │ HTTP
                              ▼
                           FLASK
                              │
                 register_blueprint()
                              │
              ┌───────────────┴───────────────┐
              │                               │
              ▼                               ▼
        usuarios_bp                    misiones_bp
              │                               │
              ▼                               ▼
         Controller                       Controller
              │                               │
              │                               │
              └───────────────┬───────────────┘
                              ▼
                            Model
                              │
                              ▼
                     MySQLConnection
                              │
                              ▼
                           PyMySQL
                              │
                              ▼
                            MySQL
                              │
                              ▼
                             Datos
                              │
                              ▼
                          Jinja2
                              │
                              ▼
                            HTML
                              │
                              ▼
                         NAVEGADOR
```

---

# 34. 🧠 ¿Qué hace cada pieza?

## `__init__.py`

```text
Crea la aplicación Flask.
```

---

## `Blueprint`

```text
Agrupa rutas relacionadas.
```

---

## Controller

```text
Recibe solicitudes y coordina qué debe ocurrir.
```

---

## `request`

```text
Permite acceder a la información enviada por el navegador.
```

---

## Model

```text
Representa y consulta los datos.
```

---

## `MySQLConnection`

```text
Administra la conexión y ejecución de SQL.
```

---

## `.env`

```text
Contiene configuración sensible o específica del entorno.
```

---

## `requirements.txt`

```text
Define las dependencias Python del proyecto.
```

---

## `templates`

```text
Presentan la información al usuario.
```

---

# 35. 📚 Diccionario rápido

| Elemento | Significado |
|---|---|
| `Flask()` | Crea la aplicación |
| `Blueprint()` | Crea un grupo de rutas |
| `route()` | Define una URL |
| `register_blueprint()` | Registra un Blueprint |
| `request` | Solicitud HTTP actual |
| `request.form` | Datos enviados por formulario |
| `request.args` | Parámetros enviados por URL |
| `request.method` | Método HTTP utilizado |
| `session` | Información mantenida entre solicitudes |
| `render_template()` | Renderiza HTML |
| `redirect()` | Envía al navegador a otra ruta |
| `url_for()` | Genera URLs de Flask |
| `@classmethod` | Permite ejecutar métodos desde la clase |
| `data` | Diccionario de parámetros |
| `DictCursor` | Devuelve registros SQL como diccionarios |
| `fetchall()` | Obtiene todos los registros |
| `lastrowid` | Obtiene el ID generado por INSERT |
| `commit()` | Confirma modificaciones |
| `load_dotenv()` | Carga variables desde `.env` |
| `os.environ.get()` | Obtiene una variable de entorno |
| `requirements.txt` | Dependencias |
| `.env` | Configuración sensible |
| `__init__.py` | Inicialización del paquete/aplicación |

---

# 🎯 La idea más importante

No memorices la arquitectura como una colección de archivos independientes.

Piensa en **responsabilidades**.

```text
¿Quién recibe la solicitud?
        ↓
    Controller

¿Quién contiene los datos?
        ↓
      Model

¿Quién habla con MySQL?
        ↓
MySQLConnection

¿Quién muestra la información?
        ↓
     Jinja2

¿Quién organiza las rutas?
        ↓
    Blueprint

¿Dónde están las credenciales?
        ↓
       .env

¿Dónde están las dependencias?
        ↓
requirements.txt
```

---

# 🏁 Resumen final

Una aplicación Flask grande puede organizarse así:

```text
flask_app/
│
├── __init__.py
│       ↓
│   crea Flask
│
├── controllers/
│       ↓
│   reciben solicitudes
│
├── models/
│       ↓
│   trabajan con datos
│
├── mysqlconnection.py
│       ↓
│   conecta con MySQL
│
├── templates/
│       ↓
│   muestran HTML
│
├── static/
│       ↓
│   CSS / JS / imágenes
│
├── .env
│       ↓
│   configuración
│
└── requirements.txt
        ↓
    dependencias
```

El flujo fundamental es:

```text
NAVEGADOR
    ↓
FLASK
    ↓
BLUEPRINT
    ↓
CONTROLLER
    ↓
MODEL
    ↓
MYSQLCONNECTION
    ↓
MYSQL
    ↓
MODEL
    ↓
CONTROLLER
    ↓
JINJA2
    ↓
HTML
    ↓
NAVEGADOR
```

Una vez entendido este flujo, conceptos como:

```python
Mision.eliminar(data)

Mision.obtener_por_id_con_relaciones(data)

request.form

misiones_bp.route()

app.register_blueprint()

load_dotenv()

os.environ.get()
```

dejan de parecer instrucciones aisladas y empiezan a tener sentido dentro de una arquitectura completa.