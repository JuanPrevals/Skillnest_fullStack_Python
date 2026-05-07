#Atributos, métodos de clase, métodos estáticos

#DEFINICION DE LA CLASE
class Estudiante:
    #Atributo de clase
    colegio = "Liceo Vate Vicente Huidobro"
    #Lista en donde esten todos los estudiantes
    estudiantes = []

    #Método CONSTRUCTOR
    def __init__(self, nombre, nota):
        #Atributos de instancias
        self.nombre = nombre
        self.nota = nota
        
        #Agregar elementos a la lista Estudiante (objeto)
        Estudiante.estudiantes.append(self)
        
    #Método de instancia
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
        
    #Método de CLASE
    # Usa "CLS" porque trabaja con la información de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre
        
    @classmethod #Contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)

    #Método estático
    #Este no usa CLS ni SELF, solo parámetros.
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False
        
#Creación de objetos (Instancias)
e1 = Estudiante("Daniel", 4.0)
e2 = Estudiante("Randy", 6.7)

#Uso de métodos de instancia
print("== MÉTODO DE INSTANCIA==")
#Mostrar datos de estudiantes
e1.mostrar_info()
print()
e2.mostrar_info()
print()

#Usar Atributo de clase
print("== MÉTODO DE INSTANCIA==")
print(e1.colegio)
print(e2.colegio)
print()

#Uso de método de clase
print("== MÉTODO DE CLASE ==")

Estudiante.cambiar_colegio("Purkuyen")
e1.colegio = "VVH" ##Modifica el atributo de la instancia en la clase
print(e1.coleio)
print(e2.colegio)
print

#Contar Estudiantes
print("== CONTAR ESTUDIANTES ==")
print(f"Total estudiantes: {Estudiante.cantidad_estudiantes()}")

#Método estático 
print("=== MÉTODO ESTÁTICO ===")

## Función repaso.
## Crear una función que valide usuario y contraseña

def validador(user, password):
    if user == "matias123" and password == "matias321":
        print(f"Bienvenido, {user}!")
        return True
    else:
        print("Acceso Denegado")
        return False

def enviarDatos():
    username = input("Ingrese su nombre usuario: ")
    password = input("Ingrese su contraseña: ")
    validador(username, password)
    
enviarDatos()