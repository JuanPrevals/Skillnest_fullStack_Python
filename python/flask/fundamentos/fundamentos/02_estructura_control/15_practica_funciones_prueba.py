# Instrucciones generales
# Deberá desarrollar un programa en Python que contenga un menú interactivo utilizando la estructura while, permitiendo al usuario seleccionar distintas opciones para ejecutar funciones previamente definidas.
# Cada opción del menú deberá llamar a una función diferente, la cual resolverá una situación específica utilizando distintos tipos de datos como enteros, decimales, cadenas de texto, listas y diccionarios.
# En aquellos casos donde sea necesario, deberá solicitar información al usuario mediante input(). Además, se deberá trabajar con arreglos (listas) para recorrer información utilizando ciclos for, junto con estructuras condicionales como if, elif y else.

# 1. Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
def calcular_mayor_menor(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El número menor es: {menor}")
    print(f"El número mayor es: {mayor}")
    
def ejercicio_calcular_mayor_menor():
    limit = int(input("Ingrese la cantidad de números que desea ingresar: "))
    numeros = []
    i = 1
    while i <= limit:
        numero = int(input(f"Ingrese el número {i}: "))
        numeros.append(numero)
        i += 1
    calcular_mayor_menor(numeros)
     


# 2. Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def es_vocal(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales


def contar_vocales(texto):
    contador = 0

    for letra in texto:
        if es_vocal(letra):
            contador += 1

    print(f"La cadena contiene {contador} vocales.")


def ejercicio_contar_vocales():
    texto = input("Ingrese una cadena de texto: ")
    contar_vocales(texto)
    


# 3. Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
def tiene_mas_de_cinco_letras(nombre):
    return len(nombre) > 5


def filtrar_nombres(nombres):
    for nombre in nombres:
        if tiene_mas_de_cinco_letras(nombre):
            print(nombre)


def ejercicio_filtrar_nombres():
    nombres = []

    nombre1 = input("Ingrese el primer nombre: ")
    nombre2 = input("Ingrese el segundo nombre: ")
    nombre3 = input("Ingrese el tercer nombre: ")

    nombres.append(nombre1)
    nombres.append(nombre2)
    nombres.append(nombre3)

    filtrar_nombres(nombres)


# 4. Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def calcular_promedio(notas):
    if len(notas) == 0:
        print("Debe ingresar al menos una nota.")
        return

    suma = 0

    for nota in notas:
        suma += nota

    promedio = suma / len(notas)
    print(f"El promedio es: {promedio:.1f}")

    if promedio >= 4.0:
        print("El estudiante aprueba.")
    else:
        print("El estudiante reprueba.")


def ejercicio_calcular_promedio():
    cantidad_notas = int(input("Ingrese la cantidad de notas: "))

    if cantidad_notas <= 0:
        print("La cantidad de notas debe ser mayor a 0.")
        return

    notas = []
    i = 1

    while i <= cantidad_notas:
        nota = float(input(f"Ingrese la nota {i}: ").replace(",", "."))
        notas.append(nota)
        i += 1

    calcular_promedio(notas)

# 5. Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def calcular_precio_con_descuento(precio):
    return precio * 0.90


def aplicar_descuento(precios):
    for precio in precios:
        precio_con_descuento = calcular_precio_con_descuento(precio)
        print(f"Precio original: ${precio:.0f} - Precio con descuento: ${precio_con_descuento:.0f}")


def ejercicio_aplicar_descuento():
    cantidad_precios = int(input("Ingrese la cantidad de precios: "))

    if cantidad_precios <= 0:
        print("La cantidad de precios debe ser mayor a 0.")
        return

    precios = []
    i = 1

    while i <= cantidad_precios:
        precio = float(input(f"Ingrese el precio {i}: "))
        precios.append(precio)
        i += 1

    aplicar_descuento(precios)

# 6. Crear una función que reciba un número entero y determine si es par o impar.
def es_par(numero):
    return numero % 2 == 0


def es_par_impar(numero):
    if es_par(numero):
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")


def ejercicio_es_par_impar():
    numero = int(input("Ingrese un número entero: "))
    es_par_impar(numero)

# 7. Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
def es_mayor_edad(edad):
    return edad >= 18


def contar_mayores_edad(edades):
    contador = 0

    for edad in edades:
        if es_mayor_edad(edad):
            contador += 1

    print(f"Hay {contador} personas mayores de edad.")


def ejercicio_contar_mayores_edad():
    cantidad_edades = int(input("Ingrese la cantidad de edades: "))

    if cantidad_edades <= 0:
        print("La cantidad de edades debe ser mayor a 0.")
        return

    edades = []
    i = 1

    while i <= cantidad_edades:
        edad = int(input(f"Ingrese la edad {i}: "))
        edades.append(edad)
        i += 1

    contar_mayores_edad(edades)

# 8. Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def palabra_coincide(palabra, palabra_buscar):
    return palabra.lower() == palabra_buscar.lower()


def contar_palabra(palabras, palabra_buscar):
    contador = 0

    for palabra in palabras:
        if palabra_coincide(palabra, palabra_buscar):
            contador += 1

    print(f"La palabra '{palabra_buscar}' aparece {contador} veces.")


def ejercicio_contar_palabra():
    cantidad_palabras = int(input("Ingrese la cantidad de palabras: "))

    if cantidad_palabras <= 0:
        print("La cantidad de palabras debe ser mayor a 0.")
        return

    palabras = []
    i = 1

    while i <= cantidad_palabras:
        palabra = input(f"Ingrese la palabra {i}: ")
        palabras.append(palabra)
        i += 1

    palabra_buscar = input("Ingrese la palabra que desea buscar: ")
    contar_palabra(palabras, palabra_buscar)

# 9. Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.
def es_positivo(numero):
    return numero > 0


def filtrar_positivos(numeros):
    positivos = []

    for numero in numeros:
        if es_positivo(numero):
            positivos.append(numero)

    print(f"Los números positivos son: {positivos}")


def ejercicio_filtrar_positivos():
    cantidad_numeros = int(input("Ingrese la cantidad de números: "))

    if cantidad_numeros <= 0:
        print("La cantidad de números debe ser mayor a 0.")
        return

    numeros = []
    i = 1

    while i <= cantidad_numeros:
        numero = int(input(f"Ingrese el número {i}: "))
        numeros.append(numero)
        i += 1

    filtrar_positivos(numeros)

# 10. Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.
def tiene_bajo_stock(producto):
    return producto["stock"] < 5


def productos_bajo_stock(productos):
    print("Productos con bajo stock:")

    hay_bajo_stock = False

    for producto in productos:
        if tiene_bajo_stock(producto):
            print(f"{producto['nombre']} - Stock: {producto['stock']}")
            hay_bajo_stock = True

    if not hay_bajo_stock:
        print("No hay productos con bajo stock.")


def ejercicio_productos_bajo_stock():
    cantidad_productos = int(input("Ingrese la cantidad de productos: "))

    if cantidad_productos <= 0:
        print("La cantidad de productos debe ser mayor a 0.")
        return

    productos = []
    i = 1

    while i <= cantidad_productos:
        nombre = input(f"Ingrese el nombre del producto {i}: ")
        stock = int(input(f"Ingrese el stock de {nombre}: "))
        producto = {
            "nombre": nombre,
            "stock": stock
        }
        productos.append(producto)
        i += 1

    productos_bajo_stock(productos)

#Menu while
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Calcular mayor y menor")
        print("2. Contar vocales")
        print("3. Filtrar nombres con más de 5 letras")
        print("4. Calcular promedio de notas")
        print("5. Aplicar descuento a precios")
        print("6. Determinar si un número es par o impar")
        print("7. Contar personas mayores de edad")
        print("8. Contar ocurrencias de una palabra")
        print("9. Filtrar números positivos")
        print("10. Mostrar productos con bajo stock")
        print("11. Salir")

        opcion = input("Seleccione una opción (1-11): ")

        if opcion == "1":
            ejercicio_calcular_mayor_menor()
        elif opcion == "2":
            ejercicio_contar_vocales()
        elif opcion == "3":
            ejercicio_filtrar_nombres()
        elif opcion == "4":
            ejercicio_calcular_promedio()
        elif opcion == "5":
            ejercicio_aplicar_descuento()
        elif opcion == "6":
            ejercicio_es_par_impar()
        elif opcion == "7":
            ejercicio_contar_mayores_edad()
        elif opcion == "8":
            ejercicio_contar_palabra()
        elif opcion == "9":
            ejercicio_filtrar_positivos()
        elif opcion == "10":
            ejercicio_productos_bajo_stock()
        elif opcion == "11":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    menu()
