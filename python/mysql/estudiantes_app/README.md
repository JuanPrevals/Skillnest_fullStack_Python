# Estudiantes — UPDATE y DELETE con Flask y MySQL

Aplicación educativa para listar, consultar, actualizar y eliminar estudiantes
guardados en MySQL. Las consultas utilizan parámetros y siempre incluyen una
cláusula `WHERE` en las operaciones `UPDATE` y `DELETE`.

## Preparación

Ejecuta `schema.sql` en MySQL Workbench. El script crea
`esquema_estudiantes`, la tabla `estudiantes` y cuatro registros de ejemplo sin
duplicarlos si vuelves a ejecutarlo.

Desde esta carpeta, instala las dependencias:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

Configura la conexión y ejecuta Flask:

```powershell
$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "tu_clave_mysql"
$env:MYSQL_DATABASE = "esquema_estudiantes"
.venv\Scripts\python server.py
```

Visita http://127.0.0.1:5000/estudiantes.

## Rutas

- `GET /estudiantes`: listado.
- `GET /estudiantes/ver/<id>`: detalle individual.
- `GET /estudiantes/editar/<id>`: formulario precargado.
- `POST /actualizar_estudiante`: validación y actualización.
- `POST /eliminar_estudiante/<id>`: comprobación de existencia y eliminación.

El borrado usa `POST` y una confirmación en el navegador. En una aplicación de
producción también debe añadirse autenticación, autorización y protección CSRF.

## Pruebas

```powershell
python -m unittest discover -s tests -v
```

Las pruebas sustituyen el acceso a MySQL por dobles de prueba, por lo que no
modifican registros reales.

