# 🎯 MINI DESAFÍO (nivel core)
datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el puntaje de Pedro a 75
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores

datos[2]["puntaje"] = 75
print(datos)

def mostrar_puntos(lista):
    for elemento in lista:
        print(f"{elemento['nombre']} Obvtuvo {elemento['puntaje']} puntos")
        
mostrar_puntos(datos)



def obtener_valores(clave, lista):
    for elemento in lista:
        print(elemento[clave])


obtener_valores("nombre", datos)
obtener_valores("puntaje", datos)
