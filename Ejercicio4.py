#Ejercicio 4 - area y longitua de un circulo

#Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circunferencia
#area = π* r^2
#longitud = 2 * π * r

#importar el modulo math xq ahi esta el valor de π
import math

radio = float(input("radio => "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

#mostrar resultado 
#:.2f significa la cantidad de desimales que quieras que tenga
print(f"El area es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")