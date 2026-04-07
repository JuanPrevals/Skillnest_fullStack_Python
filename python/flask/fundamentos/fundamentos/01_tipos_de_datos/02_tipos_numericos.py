#Tipo de dato numerico

print(type(1.1)) #Imprime: <class 'float'>
print(type(615)) #Imprime: <class 'int'>
print(type(2j)) #Imprime: <class 'complex'>

# 🔄 Conversión
# Todos los objetos en Python tienen métodos que podemos utilizar para convertir de un tipo de número a otro.

entero_a_decimal = float(123)
decimal_a_entero = int(22.5)
entero_a_complejo = complex(35)
print(entero_a_decimal) #Imprime: 123.0
print(decimal_a_entero) #Imprime: 22
print(entero_a_complejo) #Imprime: (35+0j)


# 🎲 Número aleatorio
# Para generar un número aleatorio importamos la librería random. Puedes ver la documentación oficial de la librería aquí.

import random
num_aleatorio = random.randint(5, 10) #Genera un número aleatorio entre 5 y 10
print(num_aleatorio) #Imprime el número aleatorio generad