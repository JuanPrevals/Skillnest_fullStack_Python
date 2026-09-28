-- Ejecutar solamente si la tabla usuarios ya fue creada con la versión
-- anterior del proyecto. Los usuarios existentes deberán registrar o definir
-- una contraseña nueva; nunca se debe completar esta columna con texto plano.
ALTER TABLE usuarios
    ADD COLUMN password VARCHAR(255) NULL AFTER email;
