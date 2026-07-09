# 🧪 Lección 2 - Entornos Virtuales con Pipenv

> **Curso:** Desarrollo Web con Flask desde Cero  
> **Lección 2:** Entornos Virtuales  
> **Requisitos:** Tener Python instalado correctamente y conocer el uso básico de la terminal.

---

# 📖 Descripción General

A medida que desarrollamos aplicaciones, es muy común trabajar en **múltiples proyectos al mismo tiempo**.

Cada proyecto puede utilizar diferentes versiones de Python o distintas versiones de una misma librería. Si todas las librerías se instalaran de forma global en nuestro computador, tarde o temprano comenzarían los conflictos entre proyectos.

Para solucionar este problema existen los **Entornos Virtuales (Virtual Environments)**.

Un entorno virtual es un espacio aislado donde cada proyecto administra sus propias dependencias sin afectar a otros proyectos ni al sistema operativo.

Durante todo este curso utilizaremos **Pipenv**, una herramienta moderna que facilita la creación y administración de entornos virtuales en Python.

---

# 🎯 Objetivos

Al finalizar esta lección serás capaz de:

- Comprender qué es un entorno virtual.
- Entender por qué son indispensables en proyectos reales.
- Instalar Pipenv.
- Crear un entorno virtual para un proyecto Flask.
- Instalar Flask dentro del entorno.
- Activar y desactivar el entorno virtual.
- Comprender la función de los archivos `Pipfile` y `Pipfile.lock`.

---

# 🤔 ¿Qué es un entorno virtual?

Un entorno virtual es una **copia aislada del entorno de Python** utilizada exclusivamente por un proyecto.

Cada entorno posee:

- Sus propias librerías.
- Sus propias versiones.
- Sus propias dependencias.

Esto significa que un proyecto puede utilizar Flask 3.x mientras otro utiliza Flask 2.x sin generar conflictos.

---

# 💼 ¿Por qué es importante?

Imagina que trabajas en una empresa desarrollando tres aplicaciones distintas.

| Proyecto | Framework | Versión |
|----------|-----------|----------|
| Sistema Escolar | Flask | 3.1 |
| Sistema Bancario | Flask | 2.3 |
| API de Inventario | Flask | 3.0 |

Si instalaras todas las librerías de manera global, una actualización podría romper alguno de los proyectos.

Los entornos virtuales evitan exactamente ese problema.

Cada proyecto vive completamente separado de los demás.

---

# 📦 ¿Qué es Pipenv?

**Pipenv** es una herramienta que combina varias funcionalidades:

- Crear entornos virtuales.
- Instalar paquetes.
- Administrar dependencias.
- Mantener versiones compatibles.
- Facilitar el trabajo colaborativo.

En proyectos profesionales es muy común encontrar Pipenv, Poetry o Virtualenv.

Durante este curso utilizaremos **Pipenv** por su simplicidad.

---

# 🖥 Instalación de Pipenv

## Windows

```bash
pip install pipenv
```

---

## macOS

```bash
pip3 install pipenv
```

---

## Verificar la instalación

Podemos comprobar que Pipenv quedó instalado ejecutando:

```bash
pipenv --version
```

Si todo salió correctamente veremos algo similar a:

```text
pipenv, version 2024.x.x
```

---

# 📁 Crear nuestro proyecto

Crearemos la siguiente estructura de carpetas.

```text
python/
│
└── flask/
      │
      └── fundamentos/
              │
              └── hola_flask/
```

La carpeta **hola_flask** será nuestro primer proyecto Flask.

---

# 📂 Abrir el proyecto

1. Abrir Visual Studio Code.
2. Seleccionar **Archivo → Abrir carpeta**.
3. Elegir la carpeta **hola_flask**.
4. Abrir una terminal desde:

```
Terminal → Nueva Terminal
```

---

# 📍 Verificar que estamos en la carpeta correcta

Antes de instalar cualquier dependencia debemos comprobar que estamos dentro del proyecto.

Windows

```bash
dir
```

Mac / Linux

```bash
ls
```

También podemos verificar la ruta actual.

Windows

```bash
cd
```

Mac / Linux

```bash
pwd
```

Deberíamos encontrarnos dentro de:

```text
hola_flask
```

---

# 🚀 Crear el entorno virtual e instalar Flask

Una de las ventajas de Pipenv es que puede crear el entorno virtual e instalar las dependencias al mismo tiempo.

Ejecutamos:

```bash
pipenv install flask
```

Este comando realiza varias tareas automáticamente.

1. Crea un entorno virtual.
2. Descarga Flask.
3. Instala Flask.
4. Registra las dependencias del proyecto.

La primera ejecución puede tardar algunos minutos dependiendo de la velocidad de Internet.

---

# 📁 ¿Qué archivos aparecen?

Después de ejecutar el comando veremos dos nuevos archivos.

```text
hola_flask
│
├── Pipfile
├── Pipfile.lock
```

---

## 📄 Pipfile

Es el archivo que contiene las dependencias principales del proyecto.

Ejemplo:

```toml
[[source]]

url = "https://pypi.org/simple"

[packages]
flask = "*"
```

Aquí podremos ver todas las librerías instaladas.

---

## 🔒 Pipfile.lock

Este archivo guarda información mucho más específica.

Contiene:

- Versiones exactas.
- Dependencias internas.
- Hash de seguridad.
- Compatibilidad.

Este archivo permite que todos los desarrolladores del equipo utilicen exactamente las mismas versiones.

Por esta razón **nunca debemos eliminarlo**.

---

# ⚠ Posible error con Pipenv

En algunos computadores el comando:

```bash
pipenv
```

puede no funcionar.

En ese caso debemos ejecutarlo como un módulo de Python.

---

## Windows

```bash
python -m pipenv install flask
```

---

## macOS

```bash
python3 -m pipenv install flask
```

Lo mismo aplica para cualquier otro comando.

Ejemplo:

```bash
python -m pipenv shell
```

---

# 🟢 Activar el entorno virtual

Una vez instalado Flask debemos ingresar al entorno virtual.

Ejecutamos:

```bash
pipenv shell
```

---

## ¿Cómo saber si está activo?

En la terminal aparecerá algo parecido a:

```text
(hola_flask)
C:\Users\Daniel>
```

o

```text
(hola_flask) daniel@MacBook-Pro
```

El nombre del proyecto aparecerá entre paréntesis.

Eso significa que estamos trabajando dentro del entorno virtual.

---

# 🔍 ¿Qué cambia cuando el entorno está activo?

Cuando el entorno está activo:

- Python utiliza únicamente las librerías del proyecto.
- No afecta otros proyectos.
- Todas las instalaciones quedan aisladas.

En otras palabras, todo lo que instalemos desde este momento pertenecerá únicamente a **hola_flask**.

---

# 🔴 Salir del entorno virtual

Cuando terminemos de trabajar podemos salir escribiendo:

```bash
exit
```

La terminal volverá a la normalidad.

---

# ⚠ Buenas prácticas

## ✅ Un entorno virtual por proyecto

Cada proyecto debe tener su propio entorno virtual.

```
Proyecto A
│
└── Entorno Virtual A

Proyecto B
│
└── Entorno Virtual B

Proyecto C
│
└── Entorno Virtual C
```

---

## ❌ Nunca crear un entorno dentro de otro

Un error muy común es activar un entorno virtual y crear otro encima.

Ejemplo incorrecto:

```text
(entorno1)

pipenv install flask
```

Esto puede provocar problemas difíciles de solucionar.

Siempre verifica que tu terminal no tenga otro entorno activo antes de crear uno nuevo.

---

# 💼 Ejemplo en un proyecto real

Supongamos que desarrollas una aplicación para una clínica.

Hace un año utilizaba:

- Flask 2.2

Hoy comienzas un nuevo proyecto utilizando:

- Flask 3.1

Gracias a Pipenv ambos proyectos pueden coexistir sin inconvenientes.

Cada uno tendrá sus propias librerías y versiones.

---

# 📝 Paso a paso completo

## Paso 1

Crear la carpeta.

```text
hola_flask
```

---

## Paso 2

Abrir la carpeta con VS Code.

---

## Paso 3

Abrir una terminal.

```
Terminal → Nueva Terminal
```

---

## Paso 4

Instalar Flask.

```bash
pipenv install flask
```

---

## Paso 5

Verificar que aparezcan.

```text
Pipfile

Pipfile.lock
```

---

## Paso 6

Activar el entorno.

```bash
pipenv shell
```

---

## Paso 7

Comprobar que el nombre del proyecto aparezca entre paréntesis.

```text
(hola_flask)
```

---

## Paso 8

Salir del entorno.

```bash
exit
```

---

# 🧠 Resumen

En esta lección aprendimos que:

- Un entorno virtual permite aislar las dependencias de cada proyecto.
- Pipenv facilita la creación y administración de estos entornos.
- `pipenv install flask` crea el entorno e instala Flask.
- `Pipfile` almacena las dependencias principales.
- `Pipfile.lock` guarda las versiones exactas utilizadas.
- `pipenv shell` activa el entorno virtual.
- `exit` permite salir del entorno.

Los entornos virtuales son una práctica fundamental en el desarrollo profesional y estarán presentes en prácticamente todos los proyectos que desarrolles con Python.

---

# 📝 Tarea

## Objetivo

Crear correctamente el entorno virtual de tu primer proyecto Flask.

### Instrucciones

1. Crea una carpeta llamada `hola_flask`.
2. Ábrela con Visual Studio Code.
3. Abre una nueva terminal.
4. Instala Flask utilizando Pipenv.
5. Activa el entorno virtual.
6. Verifica que aparezca el nombre del proyecto entre paréntesis.
7. Comprueba que se hayan creado los archivos:
   - `Pipfile`
   - `Pipfile.lock`
8. Sal del entorno utilizando `exit`.

### Evidencia

Realiza una captura de pantalla donde se observe:

- La carpeta `hola_flask`.
- Los archivos `Pipfile` y `Pipfile.lock`.
- La terminal con el entorno virtual activado (`(hola_flask)`).

---

# 🚀 Próxima Lección

En la siguiente clase crearemos nuestra **primera aplicación Flask**, conoceremos la estructura básica de un proyecto y ejecutaremos nuestro primer servidor web local.
