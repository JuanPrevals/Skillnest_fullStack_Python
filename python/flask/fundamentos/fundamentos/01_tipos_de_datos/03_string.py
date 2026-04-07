# 🧾 Cadena literal
# Las cadenas son secuencias de caracteres, pueden incluir letras, números, símbolos, y se colocan entre comillas simples o dobles. Por ejemplo:

print("Esta es una cadenas de caracteres.")

# ➕ Concatenar cadenas y variables con la función print
# Existen distintas maneras en las que podemos imprimir una cadena que contenga información de variables. Una de ellas es añadiendo una coma después de la cadena seguido de una variable. Esto ocasiona que la función print() agregue un espacio entre los elementos separados por comas.

nombre = "Marcelo"
print("Me llamo", nombre)

# Otra manera es concatenando el contenido con la ayuda de +.

nombre = "Marcelo"
print("Mi nombre es "+ nombre)

# 🔄 Conversión de tipos (Type Casting) o Conversión de tipo explícito
# Python no tiene manera de unir una cadena con un número, pero sí de juntar dos cadenas. Entonces es necesario convertir el número a cadena para poder “sumar” ambos valores.

print("¿Cuántas vocales hay? " + 5) 
#ERROR: TypeError: can only concatenate str (not "int") to str
print("¿Cuántas vocales hay? " + str(5)) #Imprime: ¿Cuántas vocales hay? 

# Podemos hacer la conversión también de cadena a número, por ejemplo:

tiempo_preparacion = 1
tiempo_horneado = "2"
tiempo_total = tiempo_preparacion + tiempo_horneado 
#ERROR: TypeError: unsupported operand type(s) for +: 'int' and 'str'
tiempo_total = tiempo_preparacion + int(tiempo_horneado) #Imprime: 3


# 🧩 Interpolación de cadenas
# También tenemos la posibilidad de insertar variables en nuestras cadenas, una práctica conocida como interpolación de cadenas. Existen distintas maneras de llevar a cabo esta tarea.

# 🧬 Cadenas »f» (Interpolación de cadenas literal)
# A partir de la versión 3.6 de Python, se pueden utilizar las cadenas “f” para interpolar cadenas. La sintaxis es la siguiente: escribimos una f justo después de la comilla inicial. Después, dentro de la cadena escribimos la variable dentro de llaves.


nombre = "Marcelo"
edad = 29
print(f"Mi nombre es {nombre} y tengo {edad} años de edad.")



# 🛠️ string.format()
# Antes de que se introdujeran las cadenas “f”, esta misma funcionalidad se lograba con el método .format(). Para usar este método, escribimos la cadena completa y colocamos llaves ({}) en los espacios en los que queremos desplegar el valor de la variable. Después invocamos al método format y pasamos las variables como argumentos en el orden que debieran llenarse los parámetros {}. Por ejemplo:

nombre = "Marcelo"
edad = 29
print("Mi nombre es {} y tengo {} años de edad.".format(nombre, edad))

#Imprime: Mi nombre es Marcelo y tengo 29 años de edad.
print("Tengo {} años de edad y mi nombre es {}".format(edad, nombre))

#Imprime: Tengo 29 años de edad y mi nombre es Marcelo


# 🧮 %-formatting
# Quizás en algún código te puedas topar con un método que se utilizaba antes de que existiera las formas vistas antes de interpolación. En lugar de utilizar llaves, se utiliza el símbolo % para indicar un parámetro; %s para indicar una cadena y %d para indicar un número. Una vez establecida la cadena, se coloca de nuevo % para separar el texto de las variables que serán interpoladas. Por ejemplo:

nombre = "Marcelo"
edad = 29
print("Mi nombre es %s y tengo %d años de edad." % (nombre, edad))

#Imprime: Mi nombre es Marcelo y tengo 29 años de edad.