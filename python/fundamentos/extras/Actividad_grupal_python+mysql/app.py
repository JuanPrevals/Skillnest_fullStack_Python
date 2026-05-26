class Usuario:
    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self):
        return f"ID: {self.id_usuario}, Nombre: {self.nombre}, Correo: {self.correo}"

    def actualizar_correo(self, nuevo_correo):
        self.correo = nuevo_correo
        return f"Correo actualizado: {self.correo}"


class Libro:
    def __init__(self, id_libro, titulo, autor, disponible=True):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"ID: {self.id_libro}, Titulo: {self.titulo}, Autor: {self.autor}, Estado: {estado}"

    def cambiar_disponibilidad(self):
        self.disponible = not self.disponible
        return "El libro ahora esta disponible." if self.disponible else "El libro ahora esta prestado."

    
class Prestamo:
    def __init__(self, id_prestamo, usuario, libro):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.libro = libro
        self.devuelto = False

    def registrar_prestamo(self):
        if self.libro.disponible:
            self.libro.cambiar_disponibilidad()
            return f"Prestamo registrado: {self.usuario.nombre} pidio '{self.libro.titulo}'."

        return f"No se puede prestar '{self.libro.titulo}' porque no esta disponible."

    def devolver_libro(self):
        if not self.devuelto:
            self.libro.cambiar_disponibilidad()
            self.devuelto = True
            return f"Libro devuelto: {self.usuario.nombre} devolvio '{self.libro.titulo}'."

        return f"El libro '{self.libro.titulo}' ya fue devuelto."


def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario.mostrar_datos())


if __name__ == "__main__":
    usuarios = [
        Usuario(1, "Camila Torres", "camila@correo.com"),
        Usuario(2, "Claudia Pina", "claudia@correo.com")
    ]

    libros = [
        Libro(1, "Python desde cero", "Ana Perez"),
        Libro(2, "humpty dumpty", "joshua cortejo")
    ]

    prestamos = [
        Prestamo(1, usuarios[0], libros[0]),
        Prestamo(2, usuarios[1], libros[1])
    ]

    while True:
        print("\nMenu de Biblioteca")
        print("1. Mostrar datos de usuarios")
        print("2. Mostrar informacion de libros")
        print("3. Registrar prestamos")
        print("4. Devolver libros")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_usuarios(usuarios)

        elif opcion == "2":
            for libro in libros:
                print(libro.mostrar_informacion())

        elif opcion == "3":
            for prestamo in prestamos:
                print(prestamo.registrar_prestamo())

        elif opcion == "4":
            for prestamo in prestamos:
                print(prestamo.devolver_libro())

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida, por favor intente de nuevo.")
