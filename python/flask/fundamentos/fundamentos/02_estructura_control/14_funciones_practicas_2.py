import os

# Ejercicio 1
def multiplica_por_2(n):
    return [i * 2 for i in range(n + 1)]

print(multiplica_por_2(5))

# Ejercicio 2
def suma_y_resta(lista):
    suma = lista[0] + lista[1]
    resta = lista[0] - lista[1]
    print(f"suma: {suma}")
    return resta

def ejercicio2():
    resultado = suma_y_resta([120, 115])
    print(f"retorno / resta: {resultado}")

# Ejercicio 3
def sumatoria_menos_longitud(sumatoria):
    total = sum(sumatoria)
    longitud = len(sumatoria)
    resultado = total - longitud
    print(f"Total = {total}, longitud = {longitud}")
    return resultado

def ejercicio3():
    retornar = sumatoria_menos_longitud([10, 5, 3, 7])
    print(f"El resultado del retorno es {retornar}")

# Ejercicio 4
def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
        return []
    else:
        segEle = lista[1]
        nuevaLista = []
        for i in lista:
            nuevaLista.append(i * segEle)
        long = len(nuevaLista)
        print(long)
        return nuevaLista

def ejercicio4():
    result1 = valores_multiplicados_segundo([100, 3, 50, 200])
    print(result1)

valores_multiplicados_segundo([100])

# Ejercicio 5
def valor_multiplicado_longitud(a, b):
    multlista = []
    for i in range(0, b):
        multlista.append(a * b)
    return multlista

def ejercicio5():
    result = valor_multiplicado_longitud(5, 2)
    print(f"El resultado del retorno es {result}")
    result2 = valor_multiplicado_longitud(7, 5)
    print(f"El resultado del retorno es {result2}")

# Menú
def limpiarConsola():
    os.system('cls')

def menu():                          # <-- extraído a su propia función
    continuar = True
    while continuar:
        print("\n --- ejercicios ---")
        print("--- ejercicio 1 ---")
        print(" --- ejercicio 2 ---")
        print(" --- ejercicio 3 ---")
        print(" --- ejercicio 4 ---")
        print(" --- ejercicio 5 ---")
        opcion = input("\n --- Elige una opción (1-5) o '(0 para salir)': ")
        if opcion == "1":
            limpiarConsola()
            print("\nEjecutando ejercicio 1: ")
            multiplica_por_2(5) 
        elif opcion == "2":
            print("\nEjecutando ejercicio 2: ")
            ejercicio2()
        elif opcion == "3":
            print("\nEjecutando ejercicio 3: ")
            ejercicio3()
        elif opcion == "4":
            print("\nEjecutando ejercicio 4: ")
            ejercicio4()               
        elif opcion == "5":
            print("\nEjecutando ejercicio 5: ")
            ejercicio5()
        elif opcion == "0":
            limpiarConsola()
            print("Saliendo...")
            continuar = False
        else:
            print("Opción no válida, intenta otra vez")

menu()                              