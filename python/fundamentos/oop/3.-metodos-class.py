class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0
   def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
       self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido 

#Instancias de la clase

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
segundaCompra = 300
miyagi.hacer_compra(300)
print(f"Segunda compra: {miyagi.saldo_pagar}")
#Imprimir cunato saldo le queda a miyagi
print(f"Credito disponible {miyagi.limite_credito - miyagi.saldo_pagar}")

#Cmpras de daniel
daniel.hacer_compra(45)
print(miyagi.saldo_pagar) #Imprime: 350
print(daniel.saldo_pagar) #Imprime: 45  


#Tarea

'''
1.- Crear un nuevo método que permita aumentar el límite de crédito.
Imprimir el nuevo límite de crédito

2.- Crear un método de que permita cambiar el correo de la instancia.
Mostrar el nuevo correo.

'''
miyagi.aumentarCredito(2000)
print(f"El nuevo límite de crédito es: {miyagi.limite_credito}")

miyagi.cambiarCorreo("miyagisacamela@gmail.com")
miyagi.cambiarCorreo("El nuevo correo establecido es: {miyagi.email}")