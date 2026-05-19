# Skillnest FullStack Python

Repositorio de ejercicios de Python, Flask y MySQL.

## Proyecto MySQL

El proyecto principal de base de datos esta en:

`python/mysql/administrador_datos`

| Archivo | Comentario |
| --- | --- |
| `administrador_datos_erd.sql` | Script simple para crear el ERD en MySQL Workbench |
| `ERD.md` | Resumen de tablas y relaciones |
| `index.html` | Pantalla de login y registro |
| `pages/` | Pantallas de usuarios, admin, mensajes y formularios |

## Tablas del ERD

| Tabla | Comentario |
| --- | --- |
| `tipos_usuarios` | Guarda si un usuario es administrador o usuario normal |
| `usuarios` | Guarda nombre, email, contrasena y tipo de usuario |
| `mensajes` | Guarda mensajes enviados entre usuarios |
| `comentarios` | Guarda comentarios hechos sobre un mensaje |

## Relaciones

| Relacion | Comentario |
| --- | --- |
| `usuarios.tipo_usuario_id` | Conecta cada usuario con su tipo |
| `mensajes.usuario_envia_id` | Usuario que envia el mensaje |
| `mensajes.usuario_recibe_id` | Usuario que recibe el mensaje |
| `comentarios.mensaje_id` | Mensaje al que pertenece el comentario |
| `comentarios.usuario_id` | Usuario que escribe el comentario |
