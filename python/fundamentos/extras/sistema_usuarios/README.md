# Sistema de Gestion de Usuarios

Aplicacion de consola en Python que permite iniciar sesion y administrar usuarios con permisos por rol.

## Tecnologias utilizadas

- Python
- Programacion Orientada a Objetos
- MySQL
- PyMySQL

## Estructura

```text
sistema_usuarios/
|-- main.py
|-- conexion.py
|-- usuario.py
|-- README.md
|-- resources/
|   |-- crear_bd.sql
|   |-- poblar_datos.sql
|-- docs/
|   |-- ERD.png
```

## Base de datos

1. Abrir MySQL Workbench.
2. Ejecutar `resources/crear_bd.sql`.
3. Ejecutar `resources/poblar_datos.sql`.

La base de datos se llama `usuarios_db`.

Usuarios iniciales:

| Usuario | Contrasena | Tipo |
| --- | --- | --- |
| admin | admin | ADMIN |
| juan | juan123 | USER |
| camila | camila123 | USER |

## Configuracion

En `conexion.py` se puede modificar el usuario y contrasena de MySQL:

```python
user="root"
password="poppy"
```

## Instalacion

Instalar PyMySQL:

```bash
pip install pymysql
```

## Ejecucion

Desde la carpeta del proyecto:

```bash
python main.py
```

## Funcionalidades

El administrador puede:

- Registrar usuarios.
- Listar usuarios.
- Buscar usuarios por ID.
- Modificar usuarios.
- Eliminar usuarios.

El usuario comun puede:

- Iniciar sesion.
- Ver su tipo de usuario.
- Cerrar sesion.
