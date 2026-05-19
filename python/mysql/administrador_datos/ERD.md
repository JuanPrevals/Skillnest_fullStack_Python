# ERD - Administrador de Datos

ERD simple para MySQL Workbench basado en los datos visibles de la web.

El script principal es `administrador_datos_erd.sql`.

## Tablas

| Tabla | Comentario |
| --- | --- |
| `tipos_usuarios` | Guarda los tipos: administrador o usuario normal |
| `usuarios` | Guarda los usuarios registrados |
| `mensajes` | Guarda mensajes enviados de un usuario a otro |
| `comentarios` | Guarda comentarios sobre los mensajes |

## Campos

### tipos_usuarios

| Campo | Tipo | Comentario |
| --- | --- | --- |
| `id` | INT | Identificador principal |
| `nombre` | VARCHAR(50) | Nombre del tipo de usuario |

### usuarios

| Campo | Tipo | Comentario |
| --- | --- | --- |
| `id` | INT | Identificador principal |
| `tipo_usuario_id` | INT | Tipo de usuario |
| `nombre` | VARCHAR(100) | Nombre del usuario |
| `email` | VARCHAR(255) | Correo del usuario |
| `contrasena` | VARCHAR(255) | Contrasena del usuario |
| `creado_en` | DATETIME | Fecha de creacion |
| `actualizado_en` | DATETIME | Fecha de actualizacion |

### mensajes

| Campo | Tipo | Comentario |
| --- | --- | --- |
| `id` | INT | Identificador principal |
| `usuario_envia_id` | INT | Usuario que envia |
| `usuario_recibe_id` | INT | Usuario que recibe |
| `mensaje` | TEXT | Texto del mensaje |
| `creado_en` | DATETIME | Fecha de creacion |
| `actualizado_en` | DATETIME | Fecha de actualizacion |

### comentarios

| Campo | Tipo | Comentario |
| --- | --- | --- |
| `id` | INT | Identificador principal |
| `mensaje_id` | INT | Mensaje comentado |
| `usuario_id` | INT | Usuario que comenta |
| `comentario` | TEXT | Texto del comentario |
| `creado_en` | DATETIME | Fecha de creacion |
| `actualizado_en` | DATETIME | Fecha de actualizacion |

## Relaciones

| Relacion | Comentario |
| --- | --- |
| `usuarios.tipo_usuario_id` -> `tipos_usuarios.id` | Cada usuario tiene un tipo |
| `mensajes.usuario_envia_id` -> `usuarios.id` | Un usuario envia mensajes |
| `mensajes.usuario_recibe_id` -> `usuarios.id` | Un usuario recibe mensajes |
| `comentarios.mensaje_id` -> `mensajes.id` | Un mensaje tiene comentarios |
| `comentarios.usuario_id` -> `usuarios.id` | Un usuario escribe comentarios |
