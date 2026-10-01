# BookHub

Aplicación web MVC para publicar, descubrir y guardar libros. Implementada con Flask, MySQL, PyMySQL, Jinja2, Bootstrap 5 y Flask-Bcrypt a partir del wireframe del examen.

## Funcionalidades

- Registro con validación, correo único y contraseña cifrada con Bcrypt.
- Inicio/cierre de sesión y protección de todas las rutas privadas.
- CRUD completo de libros con validación en backend y mensajes flash.
- Autorización por propietario: editar y eliminar se validan en controlador **y** consulta SQL.
- Comunidad, búsqueda por título/autor, filtro por género y detalle completo.
- Favoritos mediante relación muchos-a-muchos, contador y listado de usuarios.
- Protección CSRF en todas las acciones POST y consultas SQL parametrizadas.
- Vistas Jinja reutilizables, estados vacíos, páginas 404/500 y diseño responsive.

## Estructura MVC

```text
bookhub/
├── run.py
├── requirements.txt
├── flask_app/
│   ├── __init__.py              # Aplicación, Bcrypt y errores
│   ├── config/                  # Conexión PyMySQL
│   ├── controllers/             # Rutas y reglas HTTP
│   ├── models/                  # Usuario, Libro y Favorito (POO)
│   ├── static/                  # CSS y JavaScript
│   └── templates/               # Vistas Jinja2
├── resources/
│   ├── database.sql             # Creación completa de MySQL
│   ├── ERD.png                  # ERD listo para visualizar/entregar
│   ├── ERD.svg                  # ERD visual para la entrega
│   └── ERD.md                   # ERD Mermaid y explicación
└── tests/                       # Validaciones, seguridad y rutas
```

## Instalación

Requisitos: Python 3.11 o superior y MySQL 8.

```powershell
cd python\examen\bookhub
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
mysql -u root -p --execute="source resources/database.sql"
python run.py
```

También puedes abrir `resources/database.sql` desde MySQL Workbench y ejecutar el script completo. Si tu usuario, contraseña o puerto de MySQL son distintos, edita `.env`. La aplicación queda disponible en `http://127.0.0.1:5000`.

## Pruebas

Las pruebas usan dobles de los modelos, por lo que validan rutas y reglas sin modificar una base real:

```powershell
pytest
```

## Flujo recomendado para la demostración

1. Crea una cuenta y publica al menos dos libros.
2. Cierra sesión, crea una segunda cuenta y publica otro libro.
3. Desde la segunda cuenta, abre un libro de la comunidad y agrégalo a favoritos.
4. Comprueba el contador y la lista de personas en el detalle.
5. Abre “Mis favoritos” y luego quita el libro.
6. Intenta abrir manualmente `/libros/editar/ID_AJENO`: la aplicación bloquea la acción.
7. Edita y elimina un libro propio.

## Capturas para la entrega

Guarda las capturas en `resources/capturas/` con estos nombres:

1. `01-registro-login.png`
2. `02-mis-libros-comunidad.png`
3. `03-nuevo-libro.png`
4. `04-detalle-favoritos.png`
5. `05-editar-libro.png`
6. `06-mis-favoritos.png`
7. De forma opcional, agrega `07-pruebas-aprobadas.png` después de ejecutar `pytest` en tu terminal.

## Correspondencia con la rúbrica

| Criterio | Evidencia |
|---|---|
| Base de datos y relaciones | `resources/database.sql`, `resources/ERD.svg` y modelos |
| POO | Clases `Usuario`, `Libro`, `Favorito`, `MySQLConnection` |
| CRUD | Crear, ver, listar, editar y eliminar libros |
| Sesión | Decorador `login_requerido` en rutas privadas |
| Jinja | Herencia de `base.html`, macros y render dinámico |
| Validaciones | Modelos, mensajes por campo, flash y pruebas |
| Login/registro | Controlador de usuarios + Bcrypt + sesión |
| Contraseñas cifradas | `generate_password_hash` y `check_password_hash` |
| MVC | `models/`, `controllers/`, `templates/`, `config/` |
| Calidad | Responsive, accesible, CSRF, búsqueda, filtros y estados vacíos |

## Documentación y modelo editable

- `DOCUMENTACION_CODIGO.md` explica la arquitectura, configuración, rutas, modelos, vistas, seguridad, flujos y pruebas.
- `resources/bookhub.mwb` es el modelo EER editable generado con MySQL Workbench 8.0.
- `resources/database.sql` permite crear o reconstruir `bookhub_db` desde el SQL Editor de Workbench.

## Entrega en GitHub

El examen indica que el repositorio debe ser **privado**. Antes de enviar:

1. Confirma que `.env` no está versionado.
2. Ejecuta `pytest` y toma la captura.
3. Sube las capturas a `resources/capturas/`.
4. Haz el último commit dentro del plazo del examen.
5. Agrega al instructor como colaborador del repositorio privado.

No se incluyen contraseñas reales ni credenciales en el repositorio.
