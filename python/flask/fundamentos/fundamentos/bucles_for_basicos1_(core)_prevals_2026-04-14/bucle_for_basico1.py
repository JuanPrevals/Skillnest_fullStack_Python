"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)

def generador_de_niveles():
    for nivel in range(0, 101):
        print(nivel)



# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)

def potenciadores_de_energia():
    for numero in range(2, 501, 2):
        print(numero) 


# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)

def trampa_de_emojis():
    for numero in range(1, 101):
        if numero % 10 == 0:
            print("💣")
        elif numero % 5 == 0:
            print("💥")
        else:
            print(numero)

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)

def suma_colosal():
    suma_total = 0
    for numero in range(0, 500001, 2):
        suma_total += numero
    print(suma_total)


# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)

def retroceso_temporal():
    for año in range(2024, -1, -3):
        print(año)


# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)

def contador_dinamico(inicio, fin, salto):
    for numero in range(inicio + salto, fin + 1, salto):
        print(numero)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10


#Menu de selecion de ejercicios
def menu():
    print("Selecciona un ejercicio:")
    print("1. Generador de niveles")
    print("2. Potenciadores de energía")
    print("3. Trampa de emojis")
    print("4. Suma colosal")
    print("5. Retroceso temporal")
    print("6. Contador dinámico")

    opcion = int(input("Ingresa el número del ejercicio que deseas ejecutar: "))

    if opcion == 1:
        generador_de_niveles()
    elif opcion == 2:
        potenciadores_de_energia()
    elif opcion == 3:
        trampa_de_emojis()
    elif opcion == 4:
        suma_colosal()
    elif opcion == 5:
        retroceso_temporal()
    elif opcion == 6:
        inicio = int(input("Ingresa el valor de inicio: "))
        fin = int(input("Ingresa el valor de fin: "))
        salto = int(input("Ingresa el valor de salto: "))
        contador_dinamico(inicio, fin, salto)
    else:
        print("Opción no válida. Por favor, selecciona un número del 1 al 6.")
if __name__ == "__main__":    menu()
    