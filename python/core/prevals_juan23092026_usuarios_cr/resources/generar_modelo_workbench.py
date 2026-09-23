"""Genera esquema_usuarios.mwb desde el shell de scripts de MySQL Workbench."""

import os

import grt


SQL = """
CREATE DATABASE IF NOT EXISTS esquema_usuarios
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
USE esquema_usuarios;
CREATE TABLE IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"""


try:
    grt.log_info("GENERADOR_MWB", "Creando documento")
    grt.modules.Workbench.newDocument()
    documento = grt.root.wb.doc
    modelo = documento.physicalModels[0]
    catalogo = modelo.catalog

    # El documento nuevo incluye el esquema de ejemplo "mydb".
    while catalogo.schemata:
        catalogo.schemata.remove(catalogo.schemata[0])

    grt.log_info("GENERADOR_MWB", "Interpretando DDL")
    contexto = grt.modules.MySQLParserServices.createNewParserContext(
        catalogo.characterSets,
        catalogo.version,
        "STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION",
        1,
    )
    grt.modules.MySQLParserServices.parseSQLIntoCatalogSql(
        contexto, catalogo, SQL, {}
    )

    grt.log_info("GENERADOR_MWB", "Creando diagrama")
    grt.modules.WbModel.createDiagramWithCatalog(modelo, catalogo)
    modelo.diagrams[0].name = "ERD esquema_usuarios"

    destino = os.environ["USUARIOS_MWB_DESTINO"]
    grt.modules.Workbench.saveModelAs(destino)
    grt.log_info("GENERADOR_MWB", f"Modelo guardado en {destino}")
except Exception as error:
    grt.log_error("GENERADOR_MWB", repr(error))
    raise
