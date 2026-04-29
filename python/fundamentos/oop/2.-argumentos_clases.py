# ➡️ Pasar argumentos 
# Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__ y que de esta manera podamos asignarle a los atributos los valores correspondientes.

class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar
       
#Creacion de instancias

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 3000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 3000, 0)
juan = Usuario("Juan", "Prevals", "juanprevals@gmail.com", 3000, 0)

print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel
print(miyagi.email)
print(miyagi.email)
print(miyagi.limite_credito)
print(daniel.limite_credito)
print(miyagi.saldo_pagar)
print(daniel.saldo_pagar)
print(juan.nombre)
print(juan.apellido)
print(juan.email)
print(juan.limite_credito)
print(juan.saldo_pagar)


#Crear una clase estudiante y asignarle los siguientes atriutos: 
#(rut, nombre, apellido, especialidad, fecha_nacimiento)
#Imprimir nombre  y apellido concatenado  + especialidad 


class Estudiantes:
     def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
         self.rut = rut
         self.nombre = nombre
         self.apellido = apellido
         self.especialidad = especialidad
         self.fecha_nac = fecha_nac

marcelo = Estudiantes("23.009.064-5", "Marcelo", "Rios", "Programación", "02/05/2009")     
yoycer = Estudiantes("28.981.454-6", "Yoycer", "Garcia", "Programación", "11/10/2007")
juan = Estudiantes("24.800.174-7", "Juan", "Prevals", "Programación", "04/02/2008")      
print(f"Nombre: {marcelo.nombre}  apellido:  {marcelo.apellido} especialidad:  {marcelo.especialidad}")
print(f"Nombre: {yoycer.nombre}  apellido:  {yoycer.apellido} especialidad:  {yoycer.especialidad}")
print(f"Nombre: {juan.nombre}  apellido:  {juan.apellido} especialidad:  {juan.especialidad}")