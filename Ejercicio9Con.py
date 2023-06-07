#Ejercicio 4 - condiconales - calculadora aritmetica

#Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritmeticas basicas (suma, resta, multiplicacion y division). El usuario debe especificar la operacion con el primer caracter del nombre de la operacion.
#S,s - Suma
#R,r - Resta
#P,p,M,m - Multiplicacion
#D, d - Division

#pedir al usuario dos numeros
num1 = float(input("Digite un numero: "))
num2 = float(input("Digite un numero"))

#pedir que digite la operacion a realizar
operacion = input("Digite la operacion: ").upper()

#Si digita S, es suma
if operacion=='S': 
    suma = num1+num2
    print(f"\nLa suma es: {suma}")

#Si digita R, es resta
elif operacion == 'R':
    resta = num1-num2
    print(f"\nLa resta es: {resta}")

#Si digita M, es multiplicacion o producto
elif operacion == 'M' or operacion == 'P':
    multi = num1*num2
    print(f"\nLa multiplicacion es: {multi:.2f}")

#Si digita D, es division
elif operacion == 'D':
    div = num1/num2
    print(f"\nLa division es: {div:.2f}") #.2f significa que es para dar solo 2 decimales

#Caso contrario
else:
    print(f"\nSe equivoco de operacion")

