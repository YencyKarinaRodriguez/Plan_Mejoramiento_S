#Ejercicio 1 - condicionesles - numeros pares e impares

#Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son

#crear variable para pedir los numeros
num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

#comprobacion si ambos numeros son pares o no
#se divide el numero uno entre 2 y sacando el residuo de la division
if num1%2==0 and num2%2==0:
    print("Los numeros son pares")

#comprobar si uno no es par
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par")
else:
    print("Ambos numeros son impares")



