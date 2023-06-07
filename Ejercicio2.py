#Ejercicio 2 - Operacion con 3 tipos de operaciones

#Determinar la solucion logica de la siguiente operacion ((3+5x8)<3 and ((-6/3 x4)+2<2)) or (a>b)

# Pedir al usuario que dijite el valor de a y b
a = float(input("a => "))
b = float(input("b => "))

#creamos variable para almacenar el valor
resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)

#Mostar el resultado, aca nos va a mostrar si es falso o verdadero
print(f"El resultado es: {resultado}")