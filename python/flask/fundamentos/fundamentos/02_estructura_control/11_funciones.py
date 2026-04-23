def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
   resultado = num1 * num2     #instrucciones dentro de la función
   return resultado            #regresamos valor de resultado


a = int (input("Ingrese el primer número: ")) #pedimos al usuario que ingrese el primer número y lo convertimos a entero
b = int (input("Ingrese el segundo número: ")) #pedimos al usuario que ingrese el segundo número y lo convertimos a entero
print("El resultado de la multiplicación es: ", multiplicacion(a, b)) #imprimimos el resultado de la función multiplicación con los argumentos a y b
print("El resultado de la multiplicación es: ", multiplicacion(5, 10)) #imprimimos el resultado de la función multiplicación con los argumentos 5 y 10


#🧮 Parámetros y argumentos

def buenos_dias(nombre):
   print("Buenos días "+nombre)
   
   
#Una vez definida la función, podemos invocarla llamándola por su nombre y enviando la cantidad de argumentos requeridos:

buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")


def buenos_dias(nombre):
   return "Buenos días "+nombre

#El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi variable frase será ese

frase = buenos_dias("Python")
print(frase) #Imprime: Buenos días Python   


#Ejercicio retorno de valor
#Crear una funcion que reciba una frase + un parametro
#Devolver el valor de la frase completa e imprimirlo
def frase_completa(frase, palabra):
   return f"{frase} {palabra}"

def recibirFrase():
   frase = input("Ingrese una frase")
   palabra = input("Ingrese una palabra")
   resultradoFrease = frase_completa(frase, palabra)