#Ejercicio 5 - Descuento del 15% en una tienda

#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra

#creamos la variable para definir el precio
precio = float(input("Digite el precio: "))

#calculamos el descuento
descuento = precio * 0.15

#sacamos el precio final de la compra
precio_final = precio - descuento

#resultado
print(f"El precio total a pagar es de $: {precio_final}")