# Tacos MVC: relación muchos a muchos

Aplicación Flask y MySQL para practicar una relación M:N:

```text
tacos ──< complementos_en_tacos >── complementos
```

Un taco puede incluir varios complementos y un complemento puede aparecer en
varios tacos. La tabla intermedia usa una clave primaria compuesta para impedir
que una misma relación se registre dos veces.

## Puesta en marcha

1. Crea las tablas ejecutando `resources/esquema_tacos.sql` en MySQL.
2. Opcionalmente carga `resources/datos_demo.sql` sobre una base vacía.
3. Configura las variables de entorno que aparecen en `.env.example`.
4. Instala las dependencias con `pipenv install --dev`.
5. Inicia la aplicación con `pipenv run python server.py`.

## Recorrido de la relación

- `/tacos`: lista el CRUD existente.
- `/complementos`: crea y lista complementos.
- `/complementos/<id>`: ejecuta el `LEFT JOIN`, construye un objeto
  `Complemento` y llena `complemento.en_tacos` con objetos `Taco`.
- Desde el detalle se pueden crear y eliminar filas de
  `complementos_en_tacos`.

Para ejecutar las pruebas sin una base de datos activa:

```bash
pipenv run pytest
```
