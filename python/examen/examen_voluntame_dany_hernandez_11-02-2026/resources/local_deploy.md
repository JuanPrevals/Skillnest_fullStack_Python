# VoluntaMe

Aplicación web desarrollada con **Python + Flask + MySQL**, utilizando **Pipenv** para la administración del entorno virtual y las dependencias del proyecto.

Este documento explica, paso a paso, cómo configurar VoluntaMe en un computador nuevo y ejecutar la aplicación en un entorno de desarrollo local.

---

## 📋 Tabla de contenidos

* [Requisitos previos](#-requisitos-previos)
* [1. Obtener el proyecto](#1-obtener-el-proyecto)
* [2. Verificar Python](#2-verificar-python)
* [3. Instalar Pipenv](#3-instalar-pipenv)
* [4. Crear el entorno virtual e instalar dependencias](#4-crear-el-entorno-virtual-e-instalar-dependencias)
* [5. Configurar las variables de entorno](#5-configurar-las-variables-de-entorno)
* [6. Configurar MySQL](#6-configurar-mysql)
* [7. Crear la base de datos](#7-crear-la-base-de-datos)
* [8. Ejecutar la aplicación](#8-ejecutar-la-aplicación)
* [9. Verificar que VoluntaMe funciona](#9-verificar-que-voluntame-funciona)
* [10. Solución de problemas](#10-solución-de-problemas)
* [11. Estructura esperada del proyecto](#11-estructura-esperada-del-proyecto)
* [12. Recomendaciones de desarrollo](#12-recomendaciones-de-desarrollo)

---

# 🚀 Requisitos previos

Antes de comenzar, el computador debe tener instalados los siguientes componentes:

| Herramienta                     | Versión recomendada    | Uso                                        |
| ------------------------------- | ---------------------- | ------------------------------------------ |
| Python                          | 3.10 o superior        | Ejecutar la aplicación                     |
| Pipenv                          | Última versión estable | Administrar entorno virtual y dependencias |
| MySQL Server                    | 8.0 o superior         | Base de datos                              |
| MySQL Workbench / DBeaver / CLI | Cualquiera             | Administrar la base de datos               |
| Git                             | Recomendado            | Descargar y administrar el código          |

> **Importante:** MySQL Server debe estar instalado y ejecutándose antes de iniciar la aplicación, ya que VoluntaMe necesita conectarse a la base de datos para funcionar correctamente.

---

# 1. 📥 Obtener el proyecto

Descarga o clona el repositorio de VoluntaMe en tu computador.

Por ejemplo, utilizando Git:

```bash
git clone URL_DEL_REPOSITORIO
```

Luego entra a la carpeta del proyecto:

```bash
cd voluntame
```

También puedes comprobar que estás ubicado correctamente ejecutando:

```bash
ls
```

En Windows puedes utilizar:

```bash
dir
```

Deberías visualizar archivos y carpetas pertenecientes al proyecto, entre ellos `run.py` y `requirements.txt`.

---

# 2. 🐍 Verificar Python

VoluntaMe requiere **Python 3.10 o superior**.

Comprueba la versión instalada:

```bash
python --version
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 --version
```

La salida debería ser similar a:

```text
Python 3.10.x
```

o una versión superior.

## ¿Qué ocurre si Python no está instalado?

Debes instalarlo antes de continuar.

Durante la instalación en Windows, asegúrate de habilitar la opción:

```text
Add Python to PATH
```

Esto permitirá ejecutar Python directamente desde la terminal.

---

# 3. 📦 Instalar Pipenv

VoluntaMe utiliza **Pipenv** para crear y administrar el entorno virtual del proyecto.

Instala Pipenv ejecutando:

```bash
pip install pipenv
```

En algunos sistemas puede ser necesario:

```bash
pip3 install pipenv
```

Una vez instalado, verifica que funciona correctamente:

```bash
pipenv --version
```

Deberías obtener una respuesta similar a:

```text
pipenv, version 202x.x.x
```

---

# 4. 🔧 Crear el entorno virtual e instalar dependencias

Una de las ventajas de Pipenv es que permite mantener las librerías del proyecto aisladas del resto de aplicaciones instaladas en el computador.

Desde la carpeta raíz de VoluntaMe ejecuta:

```bash
pipenv install -r requirements.txt
```

Este comando hará que Pipenv:

1. Cree un entorno virtual para el proyecto.
2. Instale las librerías indicadas en `requirements.txt`.
3. Prepare el entorno necesario para ejecutar VoluntaMe.

Dependiendo de la configuración de Pipenv y del proyecto, también se generarán archivos como:

```text
Pipfile
Pipfile.lock
```

Estos archivos permiten registrar las dependencias utilizadas por el proyecto y facilitar una instalación consistente en otros computadores.

## 🔍 Verificar las dependencias

Puedes revisar las librerías instaladas utilizando:

```bash
pipenv graph
```

También puedes comprobar que el entorno virtual existe ejecutando:

```bash
pipenv --venv
```

La terminal debería mostrar la ruta del entorno virtual creado.

---

# 5. 🔐 Configurar las variables de entorno

VoluntaMe utiliza variables de entorno para almacenar información que **no debería estar escrita directamente dentro del código fuente**, especialmente credenciales y claves de seguridad.

Entre ellas se encuentra:

* La clave secreta de Flask.
* El usuario de MySQL.
* La contraseña de MySQL.
* El nombre de la base de datos.

## 5.1 Crear la clave secreta de Flask

Flask utiliza una clave secreta para operaciones relacionadas con sesiones y otros mecanismos de seguridad de la aplicación.

Genera una clave segura ejecutando:

```bash
python -c "import secrets; print(secrets.token_hex(24))"
```

La terminal mostrará un valor parecido a:

```text
8f4c2e7b9a1d3f6e5c8b2a4d7f9e1c3b5a6d8e0f2c4b6a8
```

> **Importante:** el valor generado es solo un ejemplo. Debes utilizar el valor producido por tu propio computador.

---

## 5.2 Crear el archivo `.env`

En la carpeta raíz del proyecto crea un archivo llamado exactamente:

```text
.env
```

La estructura básica debe ser:

```env
# ==========================================
# CONFIGURACIÓN DE SEGURIDAD
# ==========================================

APP_SECRET="TU_CLAVE_SECRETA_GENERADA"


# ==========================================
# CONFIGURACIÓN DE MYSQL
# ==========================================

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=TU_CONTRASEÑA_DE_MYSQL
MYSQL_DATABASE=voluntame_db
```

### Ejemplo

```env
APP_SECRET="8f4c2e7b9a1d3f6e5c8b2a4d7f9e1c3b5a6d8e0f2c4b6a8"

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=123456
MYSQL_DATABASE=voluntame_db
```

> ⚠️ **No copies este ejemplo literalmente.** Debes reemplazar la contraseña y la clave secreta por los valores correspondientes a tu computador.

---

## 🔒 Importante: no subir `.env` al repositorio

El archivo `.env` contiene información sensible.

Por esta razón, debe estar incluido en `.gitignore`:

```gitignore
.env
```

De esta forma, tus credenciales locales no serán enviadas al repositorio.

---

# 6. 🗄️ Configurar MySQL

VoluntaMe utiliza **MySQL** como sistema de gestión de base de datos.

Antes de iniciar la aplicación, asegúrate de que el servidor MySQL esté activo.

## Comprobar que MySQL está funcionando

Puedes comprobarlo desde MySQL Workbench, DBeaver o mediante la terminal.

Por ejemplo:

```bash
mysql -u root -p
```

El sistema solicitará la contraseña del usuario:

```text
Enter password:
```

Si las credenciales son correctas, deberías acceder a MySQL.

---

# 7. 🏗️ Crear la base de datos

VoluntaMe necesita una estructura de base de datos previamente creada para funcionar.

El proyecto debe incluir un archivo similar a:

```text
voluntame_db_script.sql
```

Este archivo contiene las instrucciones SQL necesarias para crear el esquema y las tablas utilizadas por la aplicación.

---

## 7.1 Utilizando MySQL Workbench

1. Abre **MySQL Workbench**.
2. Conéctate a tu servidor local.
3. Abre el archivo:

```text
voluntame_db_script.sql
```

4. Revisa el contenido del script.
5. Ejecuta el script completo utilizando el botón de ejecución de MySQL Workbench.

El script debería crear la base de datos y sus respectivas tablas.

---

## 7.2 Utilizando la terminal

También puedes ejecutar el script directamente desde la consola:

```bash
mysql -u root -p < voluntame_db_script.sql
```

Luego escribe la contraseña de MySQL cuando sea solicitada.

---

## 🔎 Comprobar que la base de datos fue creada

Ingresa a MySQL:

```bash
mysql -u root -p
```

Después ejecuta:

```sql
SHOW DATABASES;
```

Deberías encontrar:

```text
voluntame_db
```

Luego selecciona la base de datos:

```sql
USE voluntame_db;
```

Y revisa sus tablas:

```sql
SHOW TABLES;
```

La terminal debería mostrar las tablas creadas por el script.

---

# 8. ▶️ Ejecutar la aplicación

Una vez configurados Python, Pipenv, MySQL y las variables de entorno, ya puedes iniciar VoluntaMe.

Desde la carpeta raíz del proyecto ejecuta:

```bash
pipenv run python run.py
```

Este comando es importante porque ejecuta Python **dentro del entorno virtual administrado por Pipenv**.

---

## ¿Por qué utilizar `pipenv run`?

Cuando ejecutas:

```bash
python run.py
```

estás utilizando el Python configurado globalmente en el computador.

En cambio:

```bash
pipenv run python run.py
```

utiliza el Python y las dependencias instaladas específicamente para VoluntaMe.

Esto evita problemas como:

```text
ModuleNotFoundError
```

cuando una librería requerida por el proyecto no está instalada globalmente.

---

# 9. 🌐 Verificar que VoluntaMe funciona

Si el servidor se inicia correctamente, la terminal debería mostrar información indicando que Flask está ejecutándose.

Normalmente aparecerá una dirección similar a:

```text
http://127.0.0.1:5000
```

También puedes utilizar:

```text
http://localhost:5000
```

Abre cualquiera de estas direcciones en tu navegador:

**http://127.0.0.1:5000**

Si todo está correctamente configurado, debería cargarse la interfaz de VoluntaMe.

---

# 🧪 9.1 ¿Cómo saber si todo está correctamente configurado?

Antes de considerar terminada la instalación, comprueba lo siguiente:

* Python responde correctamente.
* Pipenv está instalado.
* El entorno virtual fue creado.
* Las dependencias fueron instaladas.
* Existe el archivo `.env`.
* `APP_SECRET` tiene un valor válido.
* MySQL está ejecutándose.
* Existe la base de datos `voluntame_db`.
* Las tablas fueron creadas.
* El usuario y contraseña de MySQL son correctos.
* Flask puede iniciar `run.py`.
* La aplicación responde en `localhost:5000`.

Si todos estos puntos funcionan, el entorno local está correctamente configurado.

---

# 🛠️ 10. Solución de problemas

## ❌ `ModuleNotFoundError`

### Problema

Puede aparecer un error similar a:

```text
ModuleNotFoundError: No module named 'flask'
```

### Causa

La aplicación está siendo ejecutada fuera del entorno virtual de Pipenv o las dependencias no fueron instaladas correctamente.

### Solución

Ejecuta:

```bash
pipenv install -r requirements.txt
```

Y luego inicia la aplicación mediante:

```bash
pipenv run python run.py
```

También puedes ingresar directamente al entorno virtual:

```bash
pipenv shell
```

Una vez dentro:

```bash
python run.py
```

---

# ❌ `Access denied for user`

Puede aparecer un error similar a:

```text
Access denied for user 'root'@'localhost'
```

### Causa

Las credenciales configuradas en `.env` no coinciden con las de MySQL.

### Revisar

Abre:

```text
.env
```

Y comprueba:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=TU_CONTRASEÑA
MYSQL_DATABASE=voluntame_db
```

La contraseña debe ser exactamente la configurada para el usuario de MySQL.

---

# ❌ La base de datos no existe

Si aparece un error relacionado con:

```text
Unknown database 'voluntame_db'
```

significa que la aplicación está intentando conectarse a una base de datos que todavía no existe.

### Solución

Ejecuta nuevamente:

```text
voluntame_db_script.sql
```

y comprueba posteriormente:

```sql
SHOW DATABASES;
```

---

# ❌ Error de conexión con MySQL

Puede aparecer un error relacionado con:

```text
Can't connect to MySQL server
```

### Posibles causas

* MySQL Server está detenido.
* El puerto configurado no es el esperado.
* El servidor MySQL no está disponible en `localhost`.
* Las credenciales son incorrectas.

Primero verifica que MySQL esté ejecutándose.

Después comprueba que puedes iniciar sesión manualmente:

```bash
mysql -u root -p
```

---

# ❌ Problemas con las sesiones

Si cambias el valor de:

```env
APP_SECRET
```

las sesiones que estaban firmadas con la clave anterior pueden dejar de ser válidas.

Esto puede provocar comportamientos como:

* Cierre de sesión inesperado.
* Redirecciones al formulario de inicio de sesión.
* Sesiones aparentemente inválidas.

### Solución

Después de modificar `APP_SECRET`:

1. Detén el servidor.
2. Inicia nuevamente la aplicación.
3. Elimina las cookies de `localhost`.
4. Vuelve a iniciar sesión.

También puedes probar directamente utilizando una ventana de navegación privada/incógnito.

---

# ❌ El navegador no puede abrir `localhost:5000`

Si el navegador muestra:

```text
ERR_CONNECTION_REFUSED
```

comprueba que la terminal donde ejecutaste:

```bash
pipenv run python run.py
```

continúe abierta y que el servidor no haya finalizado por un error.

La aplicación debe permanecer ejecutándose mientras estés utilizando VoluntaMe.

Para detenerla:

```text
Ctrl + C
```

---

# 📁 11. Estructura esperada del proyecto

La estructura puede variar dependiendo de la versión del proyecto, pero conceptualmente debería existir algo similar a:

```text
voluntame/
│
├── .env
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── requirements.txt
├── run.py
├── voluntame_db_script.sql
│
├── app/
│   ├── ...
│   └── ...
│
├── database/
│   └── ...
│
├── templates/
│   └── ...
│
└── static/
    ├── css/
    ├── js/
    └── img/
```

> La estructura exacta dependerá de cómo esté organizado el código fuente de VoluntaMe.

---

# 💡 12. Recomendaciones de desarrollo

## Mantener separado el código de la configuración

No se recomienda escribir directamente en el código:

```python
MYSQL_PASSWORD = "123456"
```

Las credenciales deben permanecer en `.env`:

```env
MYSQL_PASSWORD=123456
```

---

## No modificar `requirements.txt` sin considerar el entorno

Cuando necesites agregar una librería nueva, procura instalarla mediante Pipenv para mantener sincronizado el entorno del proyecto.

Por ejemplo:

```bash
pipenv install nombre-de-la-libreria
```

Después revisa los archivos:

```text
Pipfile
Pipfile.lock
```

---

## Antes de trabajar en el proyecto

Una rutina recomendada es:

```bash
cd voluntame
```

Luego:

```bash
pipenv install
```

Y finalmente:

```bash
pipenv run python run.py
```

---

# ✅ Instalación rápida

Para una instalación completa, el flujo principal es:

```bash
# 1. Entrar al proyecto
cd voluntame

# 2. Instalar dependencias
pipenv install -r requirements.txt

# 3. Configurar el archivo .env
#    APP_SECRET
#    MYSQL_HOST
#    MYSQL_USER
#    MYSQL_PASSWORD
#    MYSQL_DATABASE

# 4. Crear la base de datos
#    Ejecutar voluntame_db_script.sql

# 5. Iniciar la aplicación
pipenv run python run.py
```

Después abre:

```text
http://127.0.0.1:5000
```

o:

```text
http://localhost:5000
```

---

# 📌 Resumen del flujo

```text
┌──────────────────────┐
│ Descargar proyecto   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Verificar Python     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Instalar Pipenv      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Instalar dependencias│
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Crear archivo .env   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Configurar MySQL     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Crear voluntame_db   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Ejecutar run.py      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ localhost:5000       │
└──────────────────────┘
```

---

# 🎯 Resultado esperado

Al finalizar correctamente la configuración, tendrás:

* Un entorno virtual independiente para VoluntaMe.
* Todas las dependencias necesarias instaladas.
* Una configuración local almacenada en `.env`.
* MySQL funcionando correctamente.
* La base de datos `voluntame_db` creada.
* La aplicación Flask ejecutándose localmente.
* Acceso a VoluntaMe desde:

```text
http://localhost:5000
```

---

## 🔐 Nota de seguridad

Los valores utilizados en `.env`, especialmente `APP_SECRET` y `MYSQL_PASSWORD`, son información sensible.

**Nunca publiques estas credenciales en GitHub, GitLab, documentos públicos ni capturas de pantalla.**

Cada desarrollador debería disponer de su propia configuración local y sus propias credenciales de desarrollo.
