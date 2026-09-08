# VoluntaMe: Plataforma de Gestión de Voluntariado

## Sobre el Proyecto
VoluntaMe es una aplicación web diseñada para conectar personas con iniciativas comunitarias. El propósito principal es permitir que cualquier usuario pueda liderar una misión de ayuda o unirse como voluntario a las existentes.

Este proyecto fue desarrollado íntegramente por mí como parte de mi examen de certificación Fullstack, poniendo énfasis en buenas prácticas de programación, seguridad de datos y una arquitectura escalable.

---

## Tecnologías y Arquitectura
El sistema está construido bajo el patrón de diseño MVC (Modelo-Vista-Controlador), lo que garantiza un código ordenado y mantenible.

* **Backend:** Python con Flask (Blueprints).
* **Base de Datos:** MySQL con relaciones.
* **Seguridad:** Encriptación de contraseñas con Bcrypt y manejo seguro de sesiones.
* **Frontend:** Plantillas Jinja2 con diseño responsivo mediante Bootstrap.

---

## Funcionalidades Clave

### 1. Seguridad y Usuarios
Más allá de un registro simple, el sistema cuenta con validaciones estrictas para asegurar que los correos sean únicos y las contraseñas seguras. Protegemos las rutas para que solo usuarios autenticados puedan acceder a la plataforma.

### 2. Gestión Inteligente de Misiones
Los usuarios pueden crear, ver y administrar misiones de voluntariado.
* **Protección de Propiedad:** Implementé una lógica de backend que asegura que solo el creador de una misión pueda editarla o eliminarla, previniendo accesos no autorizados mediante manipulación de URLs.
* **Validaciones de Negocio:** El sistema impide crear eventos en fechas pasadas y controla que los cupos de voluntarios sean lógicos (entre 2 y 20 personas).

### 3. La Funcionalidad "VoluntaMe"
Es el corazón de la aplicación. Permite que los usuarios se inscriban en misiones con un solo clic.
* El sistema detecta automáticamente si el usuario ya participa en la misión.
* Si ya está inscrito, el botón de registro desaparece y confirma su asistencia.
* Se despliega en tiempo real la lista de todos los voluntarios unidos a la causa.

---

## Autor
**Danny**
Desarrollador Fullstack Python
Contacto: dannyahg@gmail.com