
"""
Una variable es un contenedor de información
que dentro guarda un dato, se pueden crear
muchas variable sy que cada una tenga un dato distinto.
"""

#Creando Variables
texto = "Master En Python"
textoDios = "Un Dios Po Wn"
numero = 123
decimal = 5.5

#Mostrando Variables
print(texto)
print(textoDios)
print(numero)
print(decimal)

#--------------------------#

#Sustituyendo Variables
texto = "Master En Django"
textoDios = "Un Diosito Po Wn"
numero = 321
decimal = 1.1

#Mostrando Variables 
print(texto)
print(textoDios)
print(numero)
print(decimal)

#--------------------------#

#Concatenar
nombre   = "Nicolás"
apellido = "Garcia"
web      = "nicolas.cl"

#Forma de concatenar una por una
print(nombre + " " + apellido + " " + web)

#Forma de concatenar mas formal, !* la mejor de todas *!
print(f"Mi nombre es {nombre}, mi apellido es {apellido} y mi web es {web}")

#Forma de concatnerar con .format
print("Mi nombre es {}, mi apellido es {} y mi web es {}". format(nombre, apellido, web))

#Print llama a las variables, una concatenacion informal, no usar
print(nombre, apellido, web)