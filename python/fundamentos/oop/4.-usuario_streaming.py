# 🗂️ Define la clase UsuarioStreaming, que debe incluir:

# Atributos:
# nombre
# email
# suscripcion (Gratis, Estándar o Premium)
# lista_reproduccion (lista de títulos agregados por el usuario).
# Métodos:
# agregar_a_lista(self, titulo) agrega un contenido a la lista de reproducción.
# ver_contenido(self, titulo) simula que el usuario reproduce un contenido.
# cambiar_suscripcion(self, nueva_suscripcion) modifica el tipo de suscripción del usuario.
# mostrar_info_usuario(self) muestra los datos del usuario y su lista de reproducción.
# 🧪 Realizar las siguientes pruebas con instancias:

# Crea 3 usuarios de la plataforma de streaming.
# Haz que el primer usuario agregue dos títulos a su lista y los vea.
# Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
# Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces.


class UsuarioStreaming:
   def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []


   def agregar_a_lista(self, titulo):
       """Agrega un contenido a la lista de reproducción del usuario."""
       self.lista_reproduccion.append(titulo)
       print(f"{titulo} ha sido agregado a la lista de reproducción de {self.nombre}.")
      


   def ver_contenido(self, titulo):
       """Simula que el usuario reproduce un contenido."""
       if titulo in self.lista_reproduccion:
           print(f"{titulo} agregado a la lista.")
       else:
           print("Este contenido no esta disponible en la lista")
       


   def cambiar_suscripcion(self, nueva_suscripcion):
       suscripciones_validas = ["Gratis", "Estándar", "Premium"]

       if nueva_suscripcion in suscripciones_validas:
           susAntigua = self.suscripcion
           self.suscripcion = nueva_suscripcion
           print(f"{self.nombre} ha cambiado su suscripción de {susAntigua} a {nueva_suscripcion}.")
       else:
           print("Tipo de suscripción no válido. Por favor, elija entre Gratis, Estándar o Premium.")
       


   def mostrar_info_usuario(self):
       """Muestra la información del usuario y su lista de reproducción."""
       print(f"Nombre: {self.nombre}")
       print(f"Email: {self.email}")
       print(f"Suscripción: {self.suscripcion}")
       print("Lista de reproducción:")
       if len(self.lista_reproduccion) == 0:
           print("La lista de reproducción está vacía.")
       else:
              for titulo in self.lista_reproduccion:
                print(f"Nombres de la lista: {titulo}")
   
# Todos los valores que se deban mostrar deben ser con input 
# Añadir un menu while para llamar a los metodos 
#(Menu de seleción)


usuario1 = UsuarioStreaming("Usuario 1", "usuario@gmail.com" "Premiun")
usuario2 = UsuarioStreaming("Usuario 2", "usuario@gmail.com" "Estandar")
usuario3 = UsuarioStreaming("Usuario 3", "usuario@gmail.com" "Gratis")

def menu():
    while True:
         print("Seleccione una opción:")
         print("1. Agregar a lista")
         print("2. Ver contenido")
         print("3. Cambiar suscripción")
         print("4. Mostrar información del usuario")
         print("5. Salir")
    
         opcion = input("Ingrese el número de la opción: ")
    
         if opcion == "1":
              titulo = input("Ingrese el título a agregar: ")
              usuario1.agregar_a_lista(titulo)
         elif opcion == "2":
              titulo = input("Ingrese el título a ver: ")
              usuario1.ver_contenido(titulo)
         elif opcion == "3":
              nueva_suscripcion = input("Ingrese la nueva suscripción (Gratis, Estándar, Premium): ")
              usuario1.cambiar_suscripcion(nueva_suscripcion)
         elif opcion == "4":
              usuario1.mostrar_info_usuario = input("Ingrese el número del usuario para mostrar su información (1, 2, 3): ")
              if usuario1.mostrar_info_usuario == "1":
                     usuario1.mostrar_info_usuario()
         elif opcion == "5":
              print("Saliendo del programa.")
              break
         else:
              print("Opción no válida. Por favor, intente de nuevo.")
              
              
menu()
