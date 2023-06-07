#Ejercicio 1 - Operacion aritmetica

#Escribir la siguiente expresion en forma de expresion algoritmica a^3 x (b^2 - 2ac) / 2b

# Pedimos al usuario que dijite el valor de a, b y c
a = float(input("a => "))
b = float(input("b => "))
c = float(input("c => "))

#creamos una variable para el resultado
resultado = (a**3 * (b**2 - 2*a*c))/(2*b)

print (f"El resultado es: {resultado}")