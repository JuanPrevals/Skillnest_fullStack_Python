# Usuarios CR — Flask y MySQL

Aplicación para crear y listar usuarios del esquema `esquema_usuarios`.
Incluye dos plantillas de acuerdo con el wireframe, modelo `Usuario` y
consultas parametrizadas. Las fechas se guardan con `NOW()` en MySQL.

## Preparación (PowerShell)

Desde esta carpeta:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

Abre `schema.sql` en MySQL Workbench y ejecútalo conectado a tu servidor.
Si ya tienes el esquema del módulo, se conservan sus registros y estructura.
Comprueba que `usuarios.id` sea clave primaria con `AUTO_INCREMENT`:
el formulario no solicita un identificador. El script define esta propiedad
para instalaciones nuevas; no altera una tabla existente automáticamente.

Configura la conexión en la misma terminal que usas para iniciar Flask:

```powershell
$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "tu_clave_mysql"
$env:MYSQL_DATABASE = "esquema_usuarios"
.venv\Scripts\python server.py
```

Los valores predeterminados son los del ejemplo, salvo la contraseña, que
está vacía. No se carga `.env` automáticamente ni se guardan credenciales
en el código.

Visita http://127.0.0.1:5000/usuarios.

## Flujo

- `GET /usuarios`: consulta MySQL y muestra Id, Nombre Completo, E-mail y Fecha Creación.
- `GET /usuarios/nuevo`: muestra el formulario de nombre, apellido y e-mail.
- `POST /usuarios/crear`: valida los campos, inserta el registro y redirige al listado.
- `GET /`: redirige al listado.

Los campos son obligatorios y admiten hasta 45 caracteres. Los errores de
validación conservan los datos del formulario. Si falla MySQL se devuelve
un mensaje con estado HTTP 503 y no se simula un registro exitoso.

## Verificación

```powershell
.venv\Scripts\python -m unittest discover -s tests -v
```

Las pruebas automatizadas aíslan el modelo para verificar rutas, validación,
redirección y presentación sin modificar tu base de datos. Para comprobar la
integración real, crea un usuario desde el navegador y verifica que aparezca
en el listado y en `SELECT * FROM esquema_usuarios.usuarios;`.
