#Crear clase usuario
class Usuario:
   def __init__(self):
       self.nombre = "Nariyoshi"
       self.apellido = "Miyagi"
       self.email = "miyagi@codingdojo.la"
       self.limite_credito = 30000
       self.saldo_pagar = 0
#Instancias
miyagi = Usuario()
prevals = Usuario()
daniel = Usuario()


#Acceder

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)
print(daniel.nombre) #Imprime: Nariyoshi


#Nuevos valores
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "danielsinho@gmail.com"
daniel.limite_credito = 10000
daniel.saldo_pagar = 29990
print(daniel.nombre) #Imprime: Daniel

#Valores a nueva instancia

prevals.nombre = "Juan"
prevals.apellido = "Prevals"
prevals.email = "juanprevals@gmail.com"
prevals.limite_credito = 1000000
prevals.saldo_pagar = 0

#imprmir el nombre de cada instancia
print(prevals.nombre)
print(prevals.apellido)
print(prevals.email)
print(prevals.limite_credito)
print(prevals.saldo_pagar)
