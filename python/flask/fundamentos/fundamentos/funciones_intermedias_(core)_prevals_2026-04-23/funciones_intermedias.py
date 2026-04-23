# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]


# Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]


# Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}


# Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]

# Crea la función iterar_diccionario(lista) que reciba una lista de diccionarios (como streamers) y recorra cada uno, imprimiendo sus claves y valores.
# Formatea la salida para que cada diccionario se imprima en una sola línea, con el formato.
# nombre - EliteGamerX, seguidores - 250000


# Obtener valores de un diccionario creando la función obtener_valores(clave, lista) que reciba, por una parte, una cadena con el nombre de una clave, por otra, una lista de diccionarios. La función debe imprimir el valor asociado a esa clave en cada uno de los diccionarios.
# Ejemplo de uso:
# obtener_valores("nombre", streamers)
# obtener_valores("seguidores", streamers)​
# Salida esperada:

# EliteGamerX
# PixelWarrior

# 250000
# 180000



puntajes[1][0] = 600
print(puntajes)


streamers[0]["nombre"] = "EliteGamerX"
print(streamers)

eventos["Estados Unidos"][2] = "San Francisco"
print(eventos)

ubicacion[0]["latitud"] = 40.712776
print(ubicacion)

def iterar_diccionario(lista):
    for elemento in lista:
        print(f"nombre - {elemento['nombre']}, seguidores - {elemento['seguidores']}")

def obtener_valores(clave, lista):
    for elemento in lista:
        print(elemento[clave])


obtener_valores("nombre", streamers)
obtener_valores("seguidores", streamers)


categorias = {
   "juegos_populares": [
      "Fortnite", 
      "Minecraft", 
      "Valorant", 
      "GTA V",
   ],
   "ciudades_eventos": [
      "Nueva York",
      "Madrid",
      "Tokio",
   ]
}

def mostrar_informacion(diccionario):
    for clave, valor in diccionario.items():
        print(f"{len(valor)} - {clave.upper()}")
        for elemento in valor:
            print(elemento)
            
mostrar_informacion(categorias)