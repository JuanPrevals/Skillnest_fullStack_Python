# Recomendaciones para el desarrollo:
# Crea una carpeta en tu computadora para estos ejercicios.
# Abre la carpeta en VS Code.
# Crea un archivo .py para todos los ejercicios.
# Utiliza comentarios (#) para explicar partes clave de tu código.




# Guía de Ejercicios: Lógica Fundamental
# I. Interacción y Condicionales (Básico)
# 1. Números Pares Dinámicos
# Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos.


def numeros_pares():

    n =int(input("¿Cuántos números pares deseas ver? "))
    pares = []
    for i in range(1, ( n * 2 ) + 1):
        if i % 2 == 0:
            pares.append(i)
    print(f"Los primeros {n} números pares son: {pares}")
    
#En este codigo se solicita al usuario que ingrese la cantidad de números pares que desea ver. Luego, se utiliza un bucle for para iterar desde 1 hasta el doble de n (ya que los números pares son cada segundo número). Si el número es par (es decir, si el residuo de la división por 2 es 0), se agrega a la lista de pares. Finalmente, se imprime la lista de números pares solicitados. 

# 2. Verificador de Edad y Acceso
# Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.


def verificardor_edad():
   campo = input("Ingrese su año de nacimiento: ")
   edad = 2026 - int(campo)
   if campo == "":
       print("Error")
   elif edad >= 18:
      print(f"Acceso ya que ustedes tiene {edad}")
   elif edad > 0 and edad < 18:
       print(f"No tiner acceso: te faltan: {18 - edad} años.")   
   else:
       print("No tiene acceso") 

#En este codigo se solicita al usuario que ingrese su año de nacimiento. Luego, se calcula la edad restando el año de nacimiento del año actual (2026). Se verifica si el campo está vacío y se muestra un mensaje de error. Si la edad es mayor o igual a 18, se concede el acceso. Si la edad es menor a 18 pero mayor que 0, se indica cuántos años faltan para alcanzar la mayoría de edad. Si la edad es negativa o no válida, se muestra un mensaje indicando que no tiene acceso.

# 3. Calculadora de Descuentos
# Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.

def calculadora_descuentos():
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    subtotal = precio * cantidad
    if subtotal > 100:
        descuento = subtotal * 0.15
        total = subtotal - descuento
    else:
        total = subtotal
    print(f"Subtotal: ${subtotal:.2f}")
    if subtotal > 100:
        print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Total: ${total:.2f}")

# En este codigo se solicita al usuario que ingrese el precio de un producto y la cantidad comprada. Se calcula el subtotal multiplicando el precio por la cantidad. Si el subtotal supera los $100, se calcula un descuento del 15% y se resta del subtotal para obtener el total final. Se muestra el subtotal, el descuento aplicado (si corresponde) y el total final formateado a dos decimales.

# 4. Clasificador de Números
# Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
# II. Iteraciones y Bucles (Intermedio)

def clasificador_numeros():
    clasificar = int(input("Ingrese un número: "))
    if clasificar > 0:
        if clasificar % 2 == 0:
            print("El número es Positivo-Par.")
        else:
            print("El número es Positivo-Impar.")
    elif clasificar < 0:
        if clasificar % 2 == 0:
            print("El número es Negativo-Par.")
        else:
            print("El número es Negativo-Impar.")
    else:
        print("El número es Cero.")

# En este codigo se solicita al usuario que ingrese un número. Se utiliza una serie de condiciones para clasificar el número como Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero. Se verifica si el número es mayor que 0 para determinar si es positivo, menor que 0 para determinar si es negativo, y se utiliza el operador módulo para verificar si es par o impar. Si el número es igual a 0, se clasifica como Cero.

# 5. Tabla de Multiplicar Personalizada
# Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra los resultados que sean múltiplos de 3.

def tabla_multiplicar():
    tabla_numero = int(input("Ingrese un número entero para mostrar su tabla de multiplicar: "))
    for i in range(1, 13):
        resultado = tabla_numero * i
        if resultado % 3 == 0:
            print(f"{tabla_numero} x {i} = {resultado}")


# En este codigo se solicita al usuario que ingrese un número entero para mostrar su tabla de multiplicar. Se utiliza un bucle for para iterar del 1 al 12 y calcular el resultado de multiplicar el número ingresado por cada iteración. Si el resultado es un múltiplo de 3 (es decir, si el residuo de la división por 3 es 0), se imprime la operación y su resultado.

# 6. Sumatoria con Centinela
# Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).

def sumatoria_centinela():
    sumatoria = 0
    while True:
        numero = int(input("Ingrese un número (negativo para terminar): "))
        if numero < 0:
            break
        sumatoria += numero
    print(f"La suma total es: {sumatoria}")


# En este codigo se inicializa una variable sumatoria en 0. Se utiliza un bucle while para solicitar al usuario que ingrese números continuamente. Si el número ingresado es negativo, el bucle se rompe y se termina la entrada de números. Si el número es positivo o cero, se suma a la variable sumatoria. Al finalizar, se muestra la suma total de los números ingresados (sin incluir el número negativo que terminó el ciclo).

# 7. Contador de Vocales
# Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.

def contador_vocales():
    contarVocales = input("Ingrese una frase o palabra: ")
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in contarVocales:
        if letra in vocales:
            contador += 1
    print(f"La cantidad total de vocales es: {contador}")
    
# En este codigo se solicita al usuario que ingrese una frase o palabra. Se define una cadena de vocales (tanto mayúsculas como minúsculas) y se inicializa un contador en 0. Se utiliza un bucle for para recorrer cada letra de la cadena ingresada por el usuario. Si la letra es una vocal (es decir, si está presente en la cadena de vocales), se incrementa el contador. Al finalizar el bucle, se muestra la cantidad total de vocales encontradas en la frase o palabra ingresada.

# 8. Validación de Contraseña
# Define una contraseña en una variable. Pide al usuario que la intente adivinar. Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
# III. Manejo de Arreglos / Listas (Avanzado)

def validacion_contrasena():
    password = "segura123"
    intentos = 3
    while intentos > 0:
        intento_usuario = input("Intenta adivinar la contraseña: ")
        if intento_usuario == password:
            print("¡Contraseña correcta! Acceso concedido.")
            break
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
    if intentos == 0:
        print("Acceso bloqueado. Has agotado tus intentos.")

# En este codigo se define una contraseña en la variable password. Se inicializa un contador de intentos en 3. Se utiliza un bucle while para permitir al usuario intentar adivinar la contraseña. Si el intento del usuario coincide con la contraseña, se muestra un mensaje de éxito y se rompe el bucle. Si el intento es incorrecto, se decrementa el contador de intentos y se muestra un mensaje indicando cuántos intentos quedan. Si el usuario agota los 3 intentos sin adivinar la contraseña, se muestra un mensaje indicando que el acceso ha sido bloqueado.

# 9. Registro de Nombres
# Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.

def registro_nombres():
    registro_nombres_lista = []
    for i in range(5):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        registro_nombres_lista.append(nombre)
    print("Nombres en orden inverso:")
    for nombre in reversed(registro_nombres_lista):
        print(nombre)


# En este codigo se inicializa una lista vacía llamada registro_nombres_lista. Se utiliza un bucle for para solicitar al usuario que ingrese 5 nombres, los cuales se agregan a la lista. Al finalizar la entrada de nombres, se imprime un mensaje indicando que los nombres se mostrarán en orden inverso. Se utiliza la función reversed() para recorrer la lista en orden inverso y se imprime cada nombre.

# 10. Promedio de Notas
# Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.

def promedio_notas():
    promedio_notas_lista = []
    cantidad_notas = int(input("¿Cuántas notas deseas ingresar? "))
    for i in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        promedio_notas_lista.append(nota)
    if promedio_notas_lista:                  
        promedio = sum(promedio_notas_lista) / len(promedio_notas_lista)
        nota_maxima = max(promedio_notas_lista)
        nota_minima = min(promedio_notas_lista)
        print(f"Promedio: {promedio:.2f}")
        print(f"Nota más alta: {nota_maxima}")
        print(f"Nota más baja: {nota_minima}")
      
# En este codigo se solicita al usuario que ingrese la cantidad de notas que desea ingresar. Se utiliza un bucle for para solicitar cada nota, la cual se almacena en una lista llamada promedio_notas_lista. Al finalizar la entrada de notas, se verifica si la lista no está vacía para evitar errores. Se calcula el promedio sumando todas las notas y dividiendo por la cantidad de notas. Se utiliza la función max() para encontrar la nota más alta y min() para encontrar la nota más baja. Finalmente, se muestran el promedio, la nota más alta y la nota más baja formateados a dos decimales.

# 11. Filtro de Arreglos
# Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los números que sean mayores a 50. Muestra ambos arreglos.

def filtro_arreglos():
    numeros = []
    cantidad_numeros = int(input("¿Cuántos números deseas ingresar? "))
    for i in range(cantidad_numeros):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)
    numeros_mayores_50 = [num for num in numeros if num > 50]
    print("Números ingresados:", numeros)
    print("Números mayores a 50:", numeros_mayores_50)

# En este codigo se solicita al usuario que ingrese la cantidad de números que desea ingresar. Se utiliza un bucle for para solicitar cada número, el cual se almacena en una lista llamada numeros. Luego, se crea una nueva lista llamada numeros_mayores_50 utilizando una comprensión de listas, que incluye solo los números que son mayores a 50. Finalmente, se muestran ambos arreglos: el arreglo original de números ingresados y el nuevo arreglo con los números mayores a 50.

# 12. Buscador de Elementos
# Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.
# IV. Retos de Lógica Combinada

def buscador_elementos():
    elementos = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Málaga", "Murcia", "Palma", "Las Palmas", "Bilbao"]
    ciudad_buscar = input("Ingrese el nombre de una ciudad: ")
    if ciudad_buscar in elementos:
        indice = elementos.index(ciudad_buscar)
        print(f"La ciudad '{ciudad_buscar}' se encuentra en la lista en el índice {indice}.")
    else:
        print(f"La ciudad '{ciudad_buscar}' no se encuentra en la lista.")
    

# 13. Simulación de Inventario
# Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].

def simulacion_inventario():
    inventario_productos = []
    inventario_precios = []
    for i in range(3):
        nombre_producto = input(f"Ingrese el nombre del producto {i + 1}: ")
        precio_producto = float(input(f"Ingrese el precio del producto {i + 1}: "))
        inventario_productos.append(nombre_producto)
        inventario_precios.append(precio_producto)
    print("\nInventario de Productos:")
    for nombre, precio in zip(inventario_productos, inventario_precios):
        print(f"Producto: {nombre} - Precio: ${precio:.2f}")
        
# En este codigo se crean dos listas vacías: inventario_productos para almacenar los nombres de los productos e inventario_precios para almacenar sus precios. Se utiliza un bucle for para solicitar al usuario que ingrese el nombre y el precio de 3 productos, los cuales se agregan a las respectivas listas. Al finalizar la entrada de productos, se muestra una lista formateada utilizando la función zip() para combinar los nombres y precios, imprimiendo cada producto con su precio formateado a dos decimales.


# 14. Generador de Lista de Compras
# Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.

def generador_lista_compras():
    lista_compras = []
    while True:
        articulo = input("Agrega un artículo a la lista de compras (escribe 'terminar' para finalizar): ")
        if articulo.lower() == "terminar":
            break
        lista_compras.append(articulo)
    lista_compras.sort()
    print("\nLista de Compras Ordenada:")
    for articulo in lista_compras:
        print(articulo)
        
# En este codigo se inicializa una lista vacía llamada lista_compras. Se utiliza un bucle while para permitir al usuario agregar artículos a la lista de compras. El proceso continúa hasta que el usuario escribe "terminar". Cada artículo ingresado se agrega a la lista. Al finalizar, se ordena la lista alfabéticamente utilizando el método sort() y se muestra la lista ordenada al usuario.
    

# 15. Análisis de Temperaturas
# Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
# El promedio semanal.
# Cuántos días la temperatura fue superior a 25 grados.
# El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).

def analisis_temperaturas():
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del {dias_semana[i]}: "))
        temperaturas.append(temp)
    promedio_semanal = sum(temperaturas) / len(temperaturas)
    dias_sobre_25 = sum(1 for t in temperaturas if t > 25)
    indice_minima = temperaturas.index(min(temperaturas))
    print(f"Promedio semanal: {promedio_semanal:.2f}°")
    print(f"Días con temperatura superior a 25°: {dias_sobre_25}")
    print(f"Día con temperatura más baja: {dias_semana[indice_minima]} ({min(temperaturas)}°)")
    
# En este codigo se solicita al usuario que ingrese las temperaturas de los 7 días de la semana, almacenándolas en una lista llamada temperaturas. Se calcula el promedio semanal sumando todas las temperaturas y dividiendo por la cantidad de días. Se cuenta cuántos días tuvieron una temperatura superior a 25 grados utilizando una comprensión de listas. Se encuentra el índice de la temperatura más baja para determinar qué día corresponde a esa temperatura. Finalmente, se muestra el promedio semanal, la cantidad de días con temperatura superior a 25 grados y el día con la temperatura más baja junto con su valor.


continuar = True

while continuar:
    print("\n--- Menú de Ejercicios ---")
    print("1. Números Pares Dinámicos")
    print("2. Verificador de Edad y Acceso")
    print("3. Calculadora de Descuentos")
    print("4. Clasificador de Números")
    print("5. Tabla de Multiplicar Personalizada")
    print("6. Sumatoria con Centinela")
    print("7. Contador de Vocales")
    print("8. Validación de Contraseña")
    print("9. Registro de Nombres")
    print("10. Promedio de Notas")
    print("11. Filtro de Arreglos")
    print("12. Buscador de Elementos")
    print("13. Simulación de Inventario")
    print("14. Generador de Lista de Compras")
    print("15. Análisis de Temperaturas")
    print("0. Salir")
    opcion = input("Selecciona un ejercicio (0 para salir): ")
    if opcion == "1":
        print("\nEjecutando: ejercicio 1 - Números Pares Dinámicos")
        numeros_pares()
    elif opcion == "2":
        print("\nEjecutando: ejercicio 2 - Verificador de Edad y Acceso")
        verificardor_edad()
    elif opcion == "3":
        print("\nEjecutando: ejercicio 3 - Calculadora de Descuentos")
        calculadora_descuentos()
    elif opcion == "4":
        print("\nEjecutando: ejercicio 4 - Clasificador de Números")
        clasificador_numeros()
    elif opcion == "5":
        print("\nEjecutando: ejercicio 5 - Tabla de Multiplicar Personalizada")
        tabla_multiplicar()
    elif opcion == "6":
        print("\nEjecutando: ejercicio 6 - Sumatoria con Centinela")
        sumatoria_centinela()
    elif opcion == "7":
        print("\nEjecutando: ejercicio 7 - Contador de Vocales")
        contador_vocales()
    elif opcion == "8":
        print("\nEjecutando: ejercicio 8 - Validación de Contraseña")
        validacion_contrasena()
    elif opcion == "9":
        print("\nEjecutando: ejercicio 9 - Registro de Nombres")
        registro_nombres()
    elif opcion == "10":
        print("\nEjecutando: ejercicio 10 - Promedio de Notas")
        promedio_notas()
    elif opcion == "11":
        print("\nEjecutando: ejercicio 11 - Filtro de Arreglos")
        filtro_arreglos()
    elif opcion == "12":
        print("\nEjecutando: ejercicio 12 - Buscador de Elementos")
        buscador_elementos()
    elif opcion == "13":
        print("\nEjecutando: ejercicio 13 - Simulación de Inventario")
        simulacion_inventario()
    elif opcion == "14":
        print("\nEjecutando: ejercicio 14 - Generador de Lista de Compras")
        generador_lista_compras()
    elif opcion == "15":
        print("\nEjecutando: ejercicio 15 - Análisis de Temperaturas")
        analisis_temperaturas()
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        continuar = False
    else:
        print("Opción no válida. Por favor selecciona un número del 0 al 15.")