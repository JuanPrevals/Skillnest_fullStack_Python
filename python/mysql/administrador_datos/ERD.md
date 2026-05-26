# ERD - Administrador de Datos

ERD simple para MySQL Workbench basado en los datos visibles de la web.

El script principal es `resources/database.sql`.

## Tablas

| Tabla | Comentario |
| --- | --- |
| `roles` | Guarda los roles disponibles para los usuarios |
| `usuarios` | Guarda los usuarios registrados |
| `mensajes` | Guarda mensajes enviados de un usuario a otro |
| `comentarios` | Guarda comentarios sobre los mensajes |

## Campos

### roles

| Campo | Tipo | Comentario |
| --- | --- | --- |
| `id_rol` | INT | Identificador principal |
| `nombre` | VARCHAR(50) | Nombre del rol |
| `descripcion_rol` | VARCHAR(75) | Descripcion del rol |
| `created` | DATETIME | Fecha de creacion |
| `updated` | DATETIME | Fecha de actualizacion |
| `deleted` | TINYINT(1) | Borrado logico |

### usuarios

| Campo | Tipo | Comentario |
| --- | --- | --- |
| `id_usuario` | INT | Identificador principal |
| `rol_id` | INT | Rol del usuario |
| `nombre` | VARCHAR(100) | Nombre del usuario |
| `email` | VARCHAR(255) | Correo del usuario |
| `contrasena` | VARCHAR(255) | Contrasena del usuario |
| `created` | DATETIME | Fecha de creacion |
| `updated` | DATETIME | Fecha de actualizacion |
| `deleted` | TINYINT(1) | Borrado logico |

### mensajes

| Campo | Tipo | Comentario |
| --- | --- | --- |
| `id` | INT | Identificador principal |
| `user_sent_id` | INT | Usuario que envia |
| `user_recibe_id` | INT | Usuario que recibe |
| `mensaje` | TEXT | Texto del mensaje |
| `created` | DATETIME | Fecha de creacion |
| `updated` | DATETIME | Fecha de actualizacion |
| `deleted` | TINYINT(1) | Borrado logico |

### comentarios

| Campo | Tipo | Comentario |
| --- | --- | --- |
| `id_comentario` | INT | Identificador principal |
| `mensaje_id` | INT | Mensaje comentado |
| `usuario_id` | INT | Usuario que comenta |
| `comentario` | TEXT | Texto del comentario |
| `created` | DATETIME | Fecha de creacion |
| `updated` | DATETIME | Fecha de actualizacion |

## Relaciones

| Relacion | Comentario |
| --- | --- |
| `usuarios.rol_id` -> `roles.id_rol` | Cada usuario tiene un rol |
| `mensajes.user_sent_id` -> `usuarios.id_usuario` | Un usuario envia mensajes |
| `mensajes.user_recibe_id` -> `usuarios.id_usuario` | Un usuario recibe mensajes |
| `comentarios.mensaje_id` -> `mensajes.id` | Un mensaje tiene comentarios |
| `comentarios.usuario_id` -> `usuarios.id_usuario` | Un usuario escribe comentarios |
