#Ejercicio 3 - intercambiar el valor de 2 variables

#Hacer un programa para intercambiar el valor de 2 variables 
#a = 10     a = 5
#b = 5      b = 10

#Pedimos los datos al usuario
a = input("a => ")
b = input("b =>")

#Intercambiar valores
a , b = b , a

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")