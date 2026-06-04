# 🎓 Sistema Escolar con Python y MySQL

> Proyecto educativo para aprender Programación Orientada a Objetos (POO), Bases de Datos Relacionales y Conexión Python-MySQL.

---

# 📋 Tabla de Contenidos

1. Introducción
2. Objetivos de Aprendizaje
3. Requisitos Previos
4. Instalación de Dependencias
5. Estructura del Proyecto
6. Base de Datos
7. Programación Orientada a Objetos
8. Conexión a MySQL
9. Cursores (Cursor)
10. Ejecución de Consultas SQL
11. Recuperación de Datos
12. Guardado de Cambios (Commit)
13. Importaciones entre Archivos
14. Flujo Completo del Sistema
15. Conceptos SQL Utilizados
16. Errores Comunes
17. Resumen Final

---

# 🚀 Introducción

Este proyecto tiene como objetivo integrar tres áreas fundamentales del desarrollo de software:

* Programación Orientada a Objetos (POO)
* Bases de Datos Relacionales (MySQL)
* Programación con Python

Durante el desarrollo construiremos un sistema escolar capaz de:

✅ Registrar estudiantes

✅ Registrar asignaturas

✅ Registrar calificaciones

✅ Consultar información mediante JOIN

✅ Calcular promedios

✅ Utilizar borrado lógico

✅ Aplicar campos de auditoría

---

# 🎯 Objetivos de Aprendizaje

Al finalizar este proyecto serás capaz de:

* Crear clases y objetos.
* Utilizar constructores.
* Crear métodos.
* Conectarte a MySQL desde Python.
* Ejecutar consultas SQL.
* Utilizar JOIN.
* Utilizar LIKE.
* Utilizar BETWEEN.
* Utilizar GROUP BY.
* Utilizar AVG().
* Organizar código en múltiples archivos.

---

# 📦 Requisitos Previos

Antes de comenzar debes tener instalado:

### Python

Verificar:

```bash
python --version
```

o

```bash
python3 --version
```

---

### MySQL

Verificar:

```bash
mysql --version
```

---

### Visual Studio Code (Recomendado)

Editor recomendado para desarrollar el proyecto.

---

# ⚙️ Instalación de Dependencias

Python no puede comunicarse con MySQL por sí solo.

Necesitamos instalar una librería especial.

Ejecutar:

```bash
pip install mysql-connector-python
```

Verificar instalación:

```bash
pip show mysql-connector-python
```

---

# 🤔 ¿Qué es mysql-connector-python?

Es una librería que permite que Python se comunique con MySQL.

Visualmente:

```text
Python
   │
   ▼
mysql-connector
   │
   ▼
MySQL
```

Sin esta librería:

❌ Python no podría conectarse a la base de datos.

---

# 📁 Estructura del Proyecto

```text
proyecto/

conexion.py
estudiante.py
calificacion.py
main.py
```

---

## conexion.py

Responsable de crear la conexión a MySQL.

```text
Responsabilidad:
Conectarse a la base de datos
```

---

## estudiante.py

Responsable de administrar estudiantes.

```text
Responsabilidad:
CRUD de estudiantes
```

---

## calificacion.py

Responsable de administrar calificaciones.

```text
Responsabilidad:
Notas y consultas JOIN
```

---

## main.py

Responsable de mostrar el menú principal.

```text
Responsabilidad:
Interacción con el usuario
```

---

# 🗄️ Base de Datos

Nuestro modelo se encuentra normalizado hasta Tercera Forma Normal (3FN).

## Diagrama Conceptual

```text
ESTUDIANTES
      │
      │ 1
      │
      │ N
CALIFICACIONES
      │
      │ N
      │
      │ 1
ASIGNATURAS
```

---

# 🧩 Programación Orientada a Objetos

## ¿Qué es una Clase?

Una clase es una plantilla para crear objetos.

Ejemplo:

```python
class Estudiante:
    pass
```

---

## ¿Qué es un Objeto?

Es una instancia de una clase.

```python
estudiante = Estudiante()
```

Visualmente:

```text
Clase
  ↓
Objeto
```

---

## ¿Qué es un Constructor?

Método especial que se ejecuta al crear un objeto.

```python
def __init__(self):
```

Ejemplo:

```python
class Estudiante:

    def __init__(self, nombre):
        self.nombre = nombre
```

---

## ¿Qué es self?

Representa el objeto actual.

```python
self.nombre
```

equivale a:

```python
estudiante.nombre
```

---

# 🔌 Conexión a MySQL

Archivo:

```python
conexion.py
```

Código:

```python
import mysql.connector

class Conexion:

    @staticmethod
    def conectar():

        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="colegio_3fn"
        )
```

---

## ¿Qué hace conectar()?

Retorna una conexión activa.

```python
conexion = Conexion.conectar()
```

Visualmente:

```text
Python
   │
   ▼
Conexion.conectar()
   │
   ▼
MySQL
```

---

# 📡 ¿Qué es un Cursor?

Una vez abierta la conexión:

```python
conexion = Conexion.conectar()
```

debemos crear un cursor.

```python
cursor = conexion.cursor()
```

---

## Analogía

```text
Conexión = Teléfono

Cursor = Persona que habla
```

La conexión abre el canal.

El cursor envía instrucciones.

---

# 📜 Consultas SQL

## Crear una consulta

```python
sql = """
SELECT *
FROM estudiantes
"""
```

La variable `sql` contiene solamente texto.

---

## ¿Qué ocurre si imprimimos la consulta?

```python
print(sql)
```

Resultado:

```sql
SELECT *
FROM estudiantes
```

⚠️ La consulta NO se ejecuta.

Solo se muestra en pantalla.

---

## ¿Cuándo se ejecuta realmente?

Cuando utilizamos:

```python
cursor.execute(sql)
```

---

Visualmente:

```text
Variable SQL
       │
       ▼
cursor.execute(sql)
       │
       ▼
MySQL ejecuta la consulta
```

---

# 📥 Recuperación de Datos

Después de ejecutar una consulta SELECT:

```python
cursor.execute(sql)
```

debemos recuperar resultados.

---

## fetchall()

```python
datos = cursor.fetchall()
```

Retorna una lista de registros.

Ejemplo:

```python
[
    (1, 'Juan', '3A'),
    (2, 'María', '3B')
]
```

---

## Recorrer resultados

```python
for fila in datos:

    print(fila)
```

Resultado:

```text
(1, 'Juan', '3A')
(2, 'María', '3B')
```

---

# 💾 Guardado de Cambios

Cuando realizamos:

```sql
INSERT
UPDATE
DELETE
```

debemos confirmar los cambios.

---

## commit()

```python
conexion.commit()
```

---

## Sin commit()

```python
cursor.execute(sql)
```

⚠️ El cambio podría perderse.

---

## Con commit()

```python
cursor.execute(sql)
conexion.commit()
```

✅ El cambio queda guardado permanentemente.

---

# 📦 Importaciones

## ¿Qué es import?

Permite utilizar código definido en otro archivo.

Ejemplo:

Archivo:

```python
# saludo.py

def saludar():
    print("Hola")
```

Otro archivo:

```python
from saludo import saludar

saludar()
```

Resultado:

```text
Hola
```

---

# 🔄 Importaciones del Proyecto

## Desde estudiante.py

```python
from conexion import Conexion
```

Significa:

> Utilizar la clase Conexion definida en conexion.py

---

## Desde main.py

```python
from estudiante import Estudiante
```

Significa:

> Utilizar la clase Estudiante definida en estudiante.py

---

## Desde main.py

```python
from calificacion import Calificacion
```

Significa:

> Utilizar la clase Calificacion definida en calificacion.py

---

# 🔁 Flujo Completo del Sistema

Cuando agregamos un estudiante:

```python
estudiante = Estudiante(
    "Juan Pérez",
    "3A"
)

estudiante.guardar()
```

Ocurre lo siguiente:

```text
Usuario
   │
   ▼
main.py
   │
   ▼
Objeto Estudiante
   │
   ▼
guardar()
   │
   ▼
Conexion.conectar()
   │
   ▼
cursor.execute()
   │
   ▼
MySQL
   │
   ▼
commit()
   │
   ▼
Datos guardados
```

---

# 🔍 Conceptos SQL Utilizados

## SELECT

Obtiene registros.

```sql
SELECT *
FROM estudiantes;
```

---

## INSERT

Inserta registros.

```sql
INSERT INTO estudiantes
(nombre)
VALUES
('Juan');
```

---

## UPDATE

Actualiza registros.

```sql
UPDATE estudiantes
SET curso = '4A'
WHERE id_estudiante = 1;
```

---

## LIKE

Búsqueda parcial.

```sql
WHERE nombre LIKE '%Juan%'
```

---

## BETWEEN

Buscar rangos.

```sql
WHERE nota BETWEEN 5.0 AND 7.0
```

---

## INNER JOIN

Relaciona tablas.

```sql
SELECT
    e.nombre,
    a.nombre_asignatura,
    c.nota
FROM calificaciones c
INNER JOIN estudiantes e
    ON c.id_estudiante = e.id_estudiante
INNER JOIN asignaturas a
    ON c.id_asignatura = a.id_asignatura;
```

---

## GROUP BY

Agrupa registros.

```sql
GROUP BY e.nombre
```

---

## AVG()

Calcula promedios.

```sql
AVG(c.nota)
```

---

# ⚠️ Errores Comunes

## Error 1

```text
ModuleNotFoundError:
No module named 'mysql'
```

Solución:

```bash
pip install mysql-connector-python
```

---

## Error 2

```text
Access denied for user
```

Solución:

Verificar:

* Usuario
* Contraseña
* Host

---

## Error 3

```text
Unknown database
```

Solución:

Crear la base de datos antes de ejecutar el proyecto.

---

## Error 4

```text
Can't connect to MySQL server
```

Solución:

Verificar que el servicio MySQL esté iniciado.

---

# 🧠 Resumen Final

## Programación Orientada a Objetos

```text
Clase
 │
 ├── Constructor
 ├── Atributos
 ├── Métodos
 └── Objetos
```

---

## Python + MySQL

```text
Conexion
 │
 ├── cursor()
 ├── execute()
 ├── fetchall()
 ├── commit()
 └── close()
```

---

## SQL

```text
SELECT
INSERT
UPDATE
LIKE
BETWEEN
JOIN
GROUP BY
AVG
```

---

# 🚀 Próximos Pasos

Una vez dominado este proyecto podrás avanzar a:

* Flask
* Bootstrap
* CRUD Web
* Autenticación de Usuarios
* Formularios HTML
* APIs REST
* SQLAlchemy
* Arquitectura MVC

---

## ✅ Proyecto Completado

Si logras comprender cada sección de este README, habrás adquirido una base sólida en:

**Python + POO + MySQL + SQL Relacional**, competencias fundamentales para el desarrollo de aplicaciones de escritorio y aplicaciones web.
