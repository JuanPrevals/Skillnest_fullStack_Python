num = 15
if num > 20:
   print("Número mayor a 20")
else:
   print("Número menor a 20")
'''
La variable num es menor a 20, por lo que el bloque de código de else será ejecutado.
Es decir que vamos a imprimir "Número menor a 20"
'''

#Estructura if-elif-else

num = 101
if num > 50:
   print("Número mayor a 50")
elif num > 100:
   print("Número mayor a 100")
else:
   print("Número menor a 10")
'''
A pesar de que num es mayor que 50 y 100, la primera condicional que se cumpla es la única que se ejecutará.
Es por eso que solo imprimirá: "Número mayor a 50"
'''
if num < 60:
   print("Número menor a 50")

#No se cumple con la condicional, por lo que no se ejecuta el bloque de 

#Desafio
#Ingresar 3 numeros por consola, luego indentificar cual es el mayor y cual es el menor, e imprimir ambos resultados.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercero número: "))

if num1 > num2 and num1 > num3:
   print(num1, "Es mayor y los numeros menores son", num2, "y", num3)
elif num2 > num1 and num2 > num3:
   print(num2, "Es mayor y los numeros menores son", num1, "y", num3)   
else:   print(num3, "Es mayor y los numeros menores son", num2, "y", num1)


