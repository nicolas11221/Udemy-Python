
#Para crear varibles no se deben poner palabras raras
#no tildes no palabras reservadas no guiones no puntos

#Ejemplos que si sirven
mi_texto1 = "1) Texto 1"
mi_texto2 = "Texto 2"

texto_unido = mi_texto1 + " " + mi_texto2
print(texto_unido)

#Salto de linea o espacio
print(" ")

#Mostrar texto entre comillas
mi_texto1 = "2) 'Dios'"
mi_texto2 = "de \"Python\""

texto_unido = mi_texto1 + " " + mi_texto2 
print(texto_unido)
print("")

#Salto de linea
mi_texto1 = "3) 'Dios'"
mi_texto2 = "de \"Python\" "

texto_unido = mi_texto1 + " \n " + mi_texto2 
print(texto_unido)
print("")

#Tabulacion
mi_texto1 = "4) 'Dios'"
mi_texto2 = "de \"Python\" "

texto_unido = mi_texto1 + " \t " + mi_texto2 
print(texto_unido)
print("")

#Borra todo lo que esta detras de \r
mi_texto1 = "5) 'Dios'"
mi_texto2 = "de \"Python\" "

texto_unido = mi_texto1 + " \r " + mi_texto2 
print(texto_unido)
print("")