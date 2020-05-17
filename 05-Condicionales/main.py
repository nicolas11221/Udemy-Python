

#Condicional IF

"""
    #Condicional IF

SI se cumple esto:
    Ejecutar grupo de intrucciones
SI NO
    Ejecutar otro grupo de intrucciones


if condicion:
    intrucciones
else:
    otras intrucciones


    #Operadores De Comparacion
    == igual
    != diferente
    <  menor que
    >  mayor que 
    <= menor o igual que
    >= mayor i igual que


    #Operadores Logicos
    and   y
    or    o
    !     negacion
    not   no

"""

print(" Son 8 Ejemplos!!!")

#Ejemplo 1
print("\n####### Ejemplo 1 #######")

color = "rojo"

if color == "rojo":
    print("Wena ql, le achuntaste")
    print("El color es Rojo")
else:
    print("Mala hermano")
    print("El color No es Rojo")

print("")

#Ejemplo 2
print("\n####### Ejemplo 2 #######")

color = "verde"

if color == "rojo":
    print("Wena ql, le achuntaste")
    print("El color es Rojo")
else:
    print("Mala hermano")
    print("El color No es Rojo")

print("")
print("")

#Ejemplo 3
print("\n####### Ejemplo 3 #######")

print("Es Hora De Adivinar El Color Elegido")
print("Entre Rojo Azul y Verde: ")
color = input()

if color == "rojo" or color == "Rojo":
    print("")
    print("Buenardo")
    print("Acertaste, Ya Que El color elegido es Rojo")
else:
    print("")
    print("Malardo")
    print(f"No Acertaste, Ya Que El color elegido no es {color}")


#Ejemplo 4
print("\n####### Ejemplo 4 #######")

print("¿En Que año estamos?")
year = int(input())
resultado = int

if year < 2020:
    resultado= 2020 - year
    print(f"Elegiste {year} como año, y la diferencia de años hasta el 2020 son: {resultado} mas")
elif year > 2020:
    resultado= year - 2020
    print(f"Elegiste {year} como año, y la diferencia de años hasta el 2020 son: {resultado} menos")
elif year == 2020:
        print(f"Elegiste el año {year} y adivina, estamos en el 2020")


#Ejemplo 5
print("\n####### Ejemplo 5 #######")

print("Ingresa Tu Nombre")
nombre = (str(input()))
print("Ingresa Tu Edad")
edad   = (int(input()))
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"Tu edad es {edad},  Eres Mayor De Edad")

    if edad > 17:
    
        print("Se Cuidadoso En Internet")

else:
    print(f"Tu edad es {edad}, No Eres Mayor De Edad")

    if edad < 15:
        print("Ve Internet Con Tus Padres")


#Ejemplo 6
print("\n####### Ejemplo 6 #######")


dia = int(input("Ingresa Un Numero De La Semana Del 1 al 7: "))

while dia <= 0 or dia >= 8:
    print("Debe Ingresar Un Numero Entre 1 y 7")
    dia = int(input("Ingresa Un Numero Del 1 al 7: "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
   print("Es Martes")
elif dia == 3:
   print("Es Miercoles")
elif dia == 4:
   print("Es Jueves")
elif dia == 5:
   print("Es Viernes")
else:
   print("Es Fin De Semana")


#Ejemplo 7
print("\n####### Ejemplo 7, Operadores Logicos #######")

edad_minima = 18
edad_maxima = 65
edad_oficial = 17

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Estas En Edad De Trabajar !!")
else:
    print("No estas En Edad De Trabajar")


#Ejemplo 8
print("\n####### Ejemplo 8 #######")

pais = str(input("Ingresa Tu Pais"))

if pais == "Chile" or pais =="Colombia" or pais == "Ecuador" or pais == "Bolivia" or pais == "Brasi"
    print(f"{pais} Es Un Pais Latinoamericano")
else 
    print(f"{pais} El Pais No Es Latinoamericano")


print("\n####### Ejemplo 8 #######")

pais = str(input("Ingresa Tu Pais"))

if not (pais == "Chile" or pais =="Colombia" or pais == "Ecuador" or pais == "Bolivia" or pais == "Brasi")
    print(f"{pais} No Un Pais Latinoamericano")
else 
    print(f"{pais} El Pais Es Latinoamericano")