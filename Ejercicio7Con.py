#Ejercicio 2 - condicionales - mayor de 3 numeros

#Hacer un programa que pida 3 numeros y determine cual es el mayor

#pedir al usuarios los 3 numeros

num1 = int(input("Digite un numero: ")) 
num2 = int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))

#comprobar cual es mayor, en este caso el numero 1 es mayor
if num1>=num2 and num1>=num3:
    print(f"El numero mayor es: {num1}")
#En caso del numero 2 sea el mayor
elif num2>=num1 and num2>=num3:
    print(f"El numero mayor es: {num2}")
#En caso del numero 3 sea el mayor
elif num3>=num1 and num3>=num2:
    print(f"El numero mayor es: {num3}")
