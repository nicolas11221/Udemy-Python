
nada = None
cadena = "Hola Me Llamo Nicolas"
cadena = "Desarrollador Web"
entero = 99
float = 4.2
booleano = True
#ArrayList
lista = [10, 20, 30, 40, 50]
#Tipos De Datos Que No Cambian
tuplaNoCambia = ("Master", "En", "Python")
#Diccionario
diccionario = {
    "nombre"  : "Nicolás",
    "apellido": "García",
    "edad"    : "21"
}

rango = range(9)

dato_byte = b"Probando"

#Aqui da error ya que estoy concatenando un String con un Int
#Solo se deben concatenar string con string e int con int
"""
texto = "Hola soy un Texto"
numero = 555
print(texto + " " + numero)
"""
#aqui solucionamos el error de arriba, con la funcion STR
#se mete la variable que uno desea cambiar por ejemplo aqui
texto = "Hola soy un Texto"
numero = str(555)
print(texto + " " + numero)
print(type(texto))

#aqui convertiremos un entero
numero = int(555)
print(type(numero))

#aqui convertiremos en un float (Me da error jaja nose que es)
"""
numero = float(505)
print(numero)
"""

#Imprimir Variable
print(cadena)

#Mostrar Tipo De Dato
print(type(cadena))

#Imprimir Variable
print(entero)

#Mostrar Tipo De Dato
print(type(entero))

#Imprimir Variable
print(float)

#Mostrar Tipo De Dato
print(type(float))

#Imprimir Variable
print(booleano)

#Mostrar Tipo De Dato
print(type(booleano))

#Imprimir Variable
print(lista)

#Mostrar Tipo De Dato
print(type(lista))

#Imprimir Variable
print(tuplaNoCambia)

#Mostrar Tipo De Dato
print(type(tuplaNoCambia))

#Imprimir Variable
print(diccionario)

#Mostrar Tipo De Dato
print(type(diccionario))

#Imprimir Variable
print(rango)

#Mostrar Tipo De Dato
print(type(rango))

#Imprimir Variable
print(dato_byte)

#Mostrar Tipo De Dato
print(type(dato_byte))