'''
Actividad: Gestor de inventario
1.-Creacion: crear una lista llamada inventario con los siguientes articulos:
"laptop", "teclado", "mouse", "monitor", "cable hdmi"
'''

inventario = ["laptop", "teclado", "mouse", "monitor", "cable hdmi"]


'''
2.- Expansion utilza el metodo correspondiente para agregar  "impresora" al final de la lista inventario
'''

inventario.append("impresora")


'''
    3.- Conteo: utiliza la funcion integrada para mostrar cuantos elementos totales hay en la lista inventario 
'''

print(len(inventario))


'''
4.- Acceso: Modifica "teclado" por "teclado mecanico" utilizando el indice correspondiente


'''

inventario[1] = "teclado mecanico"


'''
5.- Slicing: Crea una nueva lista llamada "promocion" debe contener solo los 3 primeros elementos de la lista inventario utilizando slicing
'''
promocion = inventario[0:3]


'''
6.- Mostrar la lista inventario ordenada alfabeticamente utilizando el metodo correspondiente

'''
inventario.sort()
print(inventario)



'''
7.- elimina el ultimo elemento de la lista inventario mostrando el elemento eliminado y la lista final

'''

elemento_eliminado = inventario.pop()
print("Elemento eliminado:", elemento_eliminado)

# elimina "teclado mecanico" debido a que es el ultimo en la lista ordenada alfabeticamente
 




