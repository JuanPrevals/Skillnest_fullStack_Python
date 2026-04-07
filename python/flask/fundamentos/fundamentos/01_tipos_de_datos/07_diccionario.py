estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
print(estudiante["nombre"]) #Imprime el diccionario completo
print(estudiante["curso"]) #Imprime el valor asociado a la clave "curso"


estudiante["nombre"] = "Juan"
print(estudiante["nombre"]) #Imprime: Vicente


paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Peru"
paises["ARG"] = "Argentina"
print(paises) #Imprime el diccionario completo


if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
   print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
   paises["CRI"] = "Costa Rica"
   




valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}


pintor = { "nombre": "Frida Kahlo", "pais": "México", "fecha_nacimiento": "6 de julio de 1907"}
pintor = {
   "nombre": "Frida Kahlo",
   "pais": "México",
   "fecha_nacimiento": "6 de julio de 1907"
}




escuela = {
   "nombre": "Coding Dojo LATAM",
   "profesores": [
       {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
       {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
       {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
   ]
}

print(escuela["profesores"][0]["nombre"]) #Imprime: Alfredo 