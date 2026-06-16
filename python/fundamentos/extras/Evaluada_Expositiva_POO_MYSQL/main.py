import os
from usuario import Usuario
from cliente import Cliente
from catalogo import Plataforma, Genero, Formato, pedir_id_catalogo
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


def pedir_usuario_responsable():
    while True:
        Usuario.listar()
        id_usuario = pedir_entero("\nID del usuario que realiza la accion: ")
        usuario = Usuario.obtener_por_id(id_usuario)

        if usuario is None:
            print("\nUsuario no encontrado.")
            continue

        return id_usuario


def crear_usuario(created_by):
    print("\n===== NUEVO USUARIO =====")
    nombre_usuario = input("Nombre de usuario: ")
    correo = input("Correo: ")
    password = ""
    while not password:
        password = input("Password: ")
        if not password:
            print("La password es obligatoria.")

    usuario = Usuario(
        nombre_usuario=nombre_usuario,
        correo=correo,
        password=password,
        created_by=created_by
    )
    usuario.guardar()


def crear_cliente(created_by):
    print("\n===== NUEVO CLIENTE =====")
    rut = input("RUT: ")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    correo = input("Correo: ")

    cliente = Cliente(
        rut=rut,
        nombre=nombre,
        telefono=telefono,
        correo=correo,
        created_by=created_by
    )
    cliente.guardar()


def crear_plataforma(created_by):
    print("\n===== NUEVA PLATAFORMA =====")
    nombre = input("Nombre: ")
    plataforma = Plataforma(nombre=nombre, created_by=created_by)
    plataforma.guardar()


def crear_genero(created_by):
    print("\n===== NUEVO GENERO =====")
    nombre = input("Nombre: ")
    genero = Genero(nombre=nombre, created_by=created_by)
    genero.guardar()


def crear_formato(created_by):
    print("\n===== NUEVO FORMATO =====")
    nombre = input("Nombre: ")
    formato = Formato(nombre=nombre, created_by=created_by)
    formato.guardar()


def crear_juego(created_by):
    print("\n===== NUEVO JUEGO =====")
    titulo = input("Titulo: ")
    precio = pedir_decimal("Precio: ")
    stock = pedir_entero("Stock: ")

    print("\nPLATAFORMAS DISPONIBLES")
    Plataforma.listar()
    id_plataforma = pedir_id_catalogo("plataforma", "id_plataforma", "Plataforma")

    print("\nGENEROS DISPONIBLES")
    Genero.listar()
    id_genero = pedir_id_catalogo("genero", "id_genero", "Genero")

    print("\nFORMATOS DISPONIBLES")
    Formato.listar()
    id_formato = pedir_id_catalogo("formato", "id_formato", "Formato")

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


def crear_compra(created_by):
    print("\n===== NUEVA COMPRA =====")

    print("\nCLIENTES DISPONIBLES")
    Cliente.listar()
    id_cliente = pedir_entero("\nID cliente: ")

    print("\nJUEGOS DISPONIBLES")
    Juego.listar()
    id_juego = pedir_entero("\nID juego: ")

    cantidad = pedir_entero("Cantidad: ")

    compra = Compra(
        id_cliente=id_cliente,
        id_juego=id_juego,
        cantidad=cantidad,
        created_by=created_by
    )
    compra.guardar()


def menu_crud(titulo, listar, buscar, crear, actualizar, eliminar):
    while True:
        limpiar_consola()
        print("\n===================================")
        print(f"     C.R.U.D {titulo.upper()}")
        print("===================================")
        print("1. Listar")
        print("2. Buscar")
        print("3. Crear")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Volver")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            listar()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            created_by = pedir_usuario_responsable()
            crear(created_by)
        elif opcion == "4":
            pedir_usuario_responsable()
            actualizar()
        elif opcion == "5":
            pedir_usuario_responsable()
            eliminar()
        elif opcion == "6":
            break
        else:
            print("\nOpcion invalida.")

        pausar()


def main():
    while True:
        limpiar_consola()
        print("\n===================================")
        print("     TIENDA DE VIDEOJUEGOS")
        print("===================================")
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
            menu_crud(
                "usuarios",
                Usuario.listar,
                Usuario.buscar,
                crear_usuario,
                Usuario.actualizar,
                Usuario.eliminar
            )
        elif opcion == "2":
            menu_crud(
                "clientes",
                Cliente.listar,
                Cliente.buscar,
                crear_cliente,
                Cliente.actualizar,
                Cliente.eliminar
            )
        elif opcion == "3":
            menu_crud(
                "plataformas",
                Plataforma.listar,
                Plataforma.buscar,
                crear_plataforma,
                Plataforma.actualizar,
                Plataforma.eliminar
            )
        elif opcion == "4":
            menu_crud(
                "generos",
                Genero.listar,
                Genero.buscar,
                crear_genero,
                Genero.actualizar,
                Genero.eliminar
            )
        elif opcion == "5":
            menu_crud(
                "formatos",
                Formato.listar,
                Formato.buscar,
                crear_formato,
                Formato.actualizar,
                Formato.eliminar
            )
        elif opcion == "6":
            menu_crud(
                "juegos",
                Juego.listar,
                Juego.buscar,
                crear_juego,
                Juego.actualizar,
                Juego.eliminar
            )
        elif opcion == "7":
            menu_crud(
                "compras",
                Compra.listar,
                Compra.buscar,
                crear_compra,
                Compra.actualizar,
                Compra.eliminar
            )
        elif opcion == "8":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpcion invalida.")
            pausar()


if __name__ == "__main__":
    main()
