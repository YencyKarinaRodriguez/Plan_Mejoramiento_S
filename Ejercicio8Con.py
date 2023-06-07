#Ejercicio 3 - condicionales - comprobar vocales

#Hacer un programa que pida un caracter e indique si es una vocal o no

#Pedir el usuario que digite un caracter
letra = input("Digite un caracter: ").lower()

#determinar si dicho caracter es una vocal o no
if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u': 
    print("Es una vocal")
#caso contrario de digitar otro caracter
else: 
    print("No es una vocal")
