import os
from usuario import Usuario
from cliente import Cliente
from catalogo import Plataforma, Genero, Formato
from juego import Juego
from compra import Compra


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input("\nPresione Enter para continuar...")


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero entero.")


def pedir_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero valido.")


def iniciar_sesion():
    while True:
        limpiar_consola()
        print("\n===================================")
        print("     INICIO DE SESION")
        print("===================================")
        Usuario.listar()
        id_usuario = pedir_entero("\nID del usuario que usara el sistema: ")
        usuario = Usuario.obtener_por_id(id_usuario)

        if usuario is None:
            print("\nUsuario no encontrado.")
            pausar()
            continue

        if usuario["tipo_usuario"] == "Administrador":
            password = input("Password de administrador: ")
            if not Usuario.validar_password(usuario, password):
                print("\nPassword incorrecta.")
                pausar()
                continue

        print(f"\nSesion iniciada como {usuario['nombre_usuario']} ({usuario['tipo_usuario']}).")
        pausar()
        return usuario


def mostrar_usuario_actual(usuario_actual):
    print(f"Usuario actual: {usuario_actual['nombre_usuario']} | Rol: {usuario_actual['tipo_usuario']}")


def sin_permiso():
    print("\nNo tiene permiso para realizar esta operacion.")


def crear_usuario(usuario_actual):
    print("\n===== NUEVO USUARIO =====")
    nombre_usuario = input("Nombre de usuario: ")
    correo = input("Correo: ")

    Usuario.listar_tipos()
    id_tipo_usuario = pedir_entero("\nID del rol que tendra el usuario: ")

    password = None
    if id_tipo_usuario == 1:
        while not password:
            password = input("Password para el administrador: ")
            if not password:
                print("El rol Administrador requiere password.")

    usuario = Usuario(
        nombre_usuario=nombre_usuario,
        correo=correo,
        id_tipo_usuario=id_tipo_usuario,
        password=password,
        created_by=usuario_actual["id_usuario"]
    )
    usuario.guardar()


def crear_cliente(usuario_actual):
    print("\n===== NUEVO CLIENTE =====")
    rut = input("RUT: ")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    correo = input("Correo: ")
    created_by = usuario_actual["id_usuario"]
    cliente = Cliente(rut=rut, nombre=nombre, telefono=telefono, correo=correo, created_by=created_by)
    cliente.guardar()


def crear_plataforma(usuario_actual):
    print("\n===== NUEVA PLATAFORMA =====")
    nombre = input("Nombre: ")
    created_by = usuario_actual["id_usuario"]
    plataforma = Plataforma(nombre=nombre, created_by=created_by)
    plataforma.guardar()


def crear_genero(usuario_actual):
    print("\n===== NUEVO GENERO =====")
    nombre = input("Nombre: ")
    created_by = usuario_actual["id_usuario"]
    genero = Genero(nombre=nombre, created_by=created_by)
    genero.guardar()


def crear_formato(usuario_actual):
    print("\n===== NUEVO FORMATO =====")
    nombre = input("Nombre: ")
    created_by = usuario_actual["id_usuario"]
    formato = Formato(nombre=nombre, created_by=created_by)
    formato.guardar()


def crear_juego(usuario_actual):
    print("\n===== NUEVO JUEGO =====")
    titulo = input("Titulo: ")
    precio = pedir_decimal("Precio: ")
    stock = pedir_entero("Stock: ")

    print("\nPLATAFORMAS DISPONIBLES")
    Plataforma.listar()
    id_plataforma = pedir_entero("\nID plataforma: ")

    print("\nGENEROS DISPONIBLES")
    Genero.listar()
    id_genero = pedir_entero("\nID genero: ")

    print("\nFORMATOS DISPONIBLES")
    Formato.listar()
    id_formato = pedir_entero("\nID formato: ")

    created_by = usuario_actual["id_usuario"]

    juego = Juego(
        titulo=titulo,
        precio=precio,
        stock=stock,
        id_plataforma=id_plataforma,
        id_genero=id_genero,
        id_formato=id_formato,
        created_by=created_by
    )
    juego.guardar()


def crear_compra(usuario_actual):
    print("\n===== NUEVA COMPRA =====")

    print("\nCLIENTES DISPONIBLES")
    Cliente.listar()
    id_cliente = pedir_entero("\nID cliente: ")

    print("\nJUEGOS DISPONIBLES")
    Juego.listar()
    id_juego = pedir_entero("\nID juego: ")

    cantidad = pedir_entero("Cantidad: ")
    created_by = usuario_actual["id_usuario"]

    compra = Compra(
        id_cliente=id_cliente,
        id_juego=id_juego,
        cantidad=cantidad,
        created_by=created_by
    )
    compra.guardar()


def menu_crud(titulo, listar, buscar, crear, actualizar, eliminar, usuario_actual):
    while True:
        limpiar_consola()
        print("\n===================================")
        print(f"     C.R.U.D {titulo.upper()}")
        print("===================================")
        mostrar_usuario_actual(usuario_actual)
        print("1. Listar")
        print("2. Buscar")
        print("3. Crear" if usuario_actual["puede_crear"] else "3. Crear (sin permiso)")
        print("4. Actualizar" if usuario_actual["puede_actualizar"] else "4. Actualizar (sin permiso)")
        print("5. Eliminar" if usuario_actual["puede_eliminar"] else "5. Eliminar (sin permiso)")
        print("6. Volver")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            if usuario_actual["puede_leer"]:
                listar()
            else:
                sin_permiso()
        elif opcion == "2":
            if usuario_actual["puede_leer"]:
                buscar()
            else:
                sin_permiso()
        elif opcion == "3":
            if usuario_actual["puede_crear"]:
                crear(usuario_actual)
            else:
                sin_permiso()
        elif opcion == "4":
            if usuario_actual["puede_actualizar"]:
                actualizar()
            else:
                sin_permiso()
        elif opcion == "5":
            if usuario_actual["puede_eliminar"]:
                eliminar()
            else:
                sin_permiso()
        elif opcion == "6":
            break
        else:
            print("\nOpcion invalida.")

        pausar()


def main():
    usuario_actual = iniciar_sesion()

    while True:
        limpiar_consola()
        print("\n===================================")
        print("     TIENDA DE VIDEOJUEGOS")
        print("===================================")
        mostrar_usuario_actual(usuario_actual)
        print("1. CRUD usuarios")
        print("2. CRUD clientes")
        print("3. CRUD plataformas")
        print("4. CRUD generos")
        print("5. CRUD formatos")
        print("6. CRUD juegos")
        print("7. CRUD compras")
        print("8. Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            if usuario_actual["puede_gestionar_usuarios"]:
                menu_crud(
                    "usuarios",
                    Usuario.listar,
                    Usuario.buscar,
                    crear_usuario,
                    Usuario.actualizar,
                    Usuario.eliminar,
                    usuario_actual
                )
            else:
                sin_permiso()
                pausar()
        elif opcion == "2":
            menu_crud(
                "clientes",
                Cliente.listar,
                Cliente.buscar,
                crear_cliente,
                Cliente.actualizar,
                Cliente.eliminar,
                usuario_actual
            )
        elif opcion == "3":
            menu_crud(
                "plataformas",
                Plataforma.listar,
                Plataforma.buscar,
                crear_plataforma,
                Plataforma.actualizar,
                Plataforma.eliminar,
                usuario_actual
            )
        elif opcion == "4":
            menu_crud(
                "generos",
                Genero.listar,
                Genero.buscar,
                crear_genero,
                Genero.actualizar,
                Genero.eliminar,
                usuario_actual
            )
        elif opcion == "5":
            menu_crud(
                "formatos",
                Formato.listar,
                Formato.buscar,
                crear_formato,
                Formato.actualizar,
                Formato.eliminar,
                usuario_actual
            )
        elif opcion == "6":
            menu_crud(
                "juegos",
                Juego.listar,
                Juego.buscar,
                crear_juego,
                Juego.actualizar,
                Juego.eliminar,
                usuario_actual
            )
        elif opcion == "7":
            menu_crud(
                "compras",
                Compra.listar,
                Compra.buscar,
                crear_compra,
                Compra.actualizar,
                Compra.eliminar,
                usuario_actual
            )
        elif opcion == "8":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpcion invalida.")
            pausar()


if __name__ == "__main__":
    main()
