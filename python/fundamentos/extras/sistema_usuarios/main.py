import os
from getpass import getpass

from usuario import Usuario


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresione Enter para continuar...")


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero entero.")


def pedir_tipo_usuario():
    while True:
        tipo = input("Tipo (ADMIN o USER): ").upper()

        if tipo == "ADMIN" or tipo == "USER":
            return tipo

        print("Tipo invalido. Debe ingresar ADMIN o USER.")


def registrar_usuario():
    print("\n===== REGISTRAR USUARIO =====")
    nombre_usuario = input("Usuario: ")
    password = getpass("Contrasena: ")
    tipo = pedir_tipo_usuario()

    usuario = Usuario(
        usuario=nombre_usuario,
        password=password,
        tipo=tipo
    )
    usuario.crear_usuario()


def listar_usuarios():
    print("\n===== LISTADO DE USUARIOS =====")
    Usuario.listar_usuarios()


def buscar_usuario():
    print("\n===== BUSCAR USUARIO =====")
    id_usuario = pedir_entero("Ingrese ID: ")
    usuario = Usuario.buscar_por_id(id_usuario)
    Usuario.mostrar_usuario(usuario)


def modificar_usuario():
    print("\n===== MODIFICAR USUARIO =====")
    id_usuario = pedir_entero("Ingrese ID: ")

    usuario = Usuario.buscar_por_id(id_usuario)
    if usuario is None:
        print("\nUsuario no encontrado.")
        return

    print(f"Usuario actual: {usuario['usuario']}")
    nuevo_usuario = input("Nuevo usuario: ")
    nueva_password = getpass("Nueva contrasena: ")
    nuevo_tipo = pedir_tipo_usuario()

    Usuario.modificar_usuario(
        id_usuario,
        nuevo_usuario,
        nueva_password,
        nuevo_tipo
    )


def eliminar_usuario():
    print("\n===== ELIMINAR USUARIO =====")
    id_usuario = pedir_entero("Ingrese ID: ")

    usuario = Usuario.buscar_por_id(id_usuario)
    if usuario is None:
        print("\nUsuario no encontrado.")
        return

    print(f"Usuario encontrado: {usuario['usuario']} ({usuario['tipo']})")
    confirmacion = input("Seguro que desea eliminarlo? (s/n): ").lower()

    if confirmacion == "s":
        Usuario.eliminar_usuario(id_usuario)
    else:
        print("\nEliminacion cancelada.")


def menu_administrador(usuario_logueado):
    while True:
        limpiar_consola()
        print("==============================")
        print("Bienvenido Administrador:")
        print(usuario_logueado["usuario"])
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("6. Cerrar sesion")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            modificar_usuario()
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == "6":
            break
        else:
            print("\nOpcion invalida.")

        pausar()


def menu_usuario(usuario_logueado):
    while True:
        limpiar_consola()
        print("==============================")
        print("Bienvenido")
        print(usuario_logueado["usuario"])
        print("Tipo de usuario:")
        print(usuario_logueado["tipo"])
        print("1. Cerrar sesion")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            break
        else:
            print("\nOpcion invalida.")
            pausar()


def iniciar_sesion():
    print("\n===== INICIAR SESION =====")
    nombre_usuario = input("Usuario: ")
    password = getpass("Contrasena: ")

    usuario = Usuario.validar_login(nombre_usuario, password)

    if usuario is None:
        print("\nUsuario o contrasena incorrectos.")
        return

    if usuario["tipo"] == "ADMIN":
        menu_administrador(usuario)
    else:
        menu_usuario(usuario)


def main():
    while True:
        limpiar_consola()
        print("==============================")
        print("  SISTEMA DE USUARIOS")
        print("==============================")
        print("1. Iniciar sesion")
        print("2. Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            iniciar_sesion()
            pausar()
        elif opcion == "2":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpcion invalida.")
            pausar()


if __name__ == "__main__":
    main()
