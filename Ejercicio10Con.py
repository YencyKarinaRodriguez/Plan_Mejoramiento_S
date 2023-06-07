#Ejercicio 5 - condicionales - cajero automatico

#Hacer un programa que simule un cajero automatico con un saldo incial de $1000 y tendra el siguiente menu de opciones
#Ingresar dinero en la cuenta
#Retirar dinero de la cuenta
#Mostrar dinero disponible
#Salir

#creamos una variable para definir el saldo
saldo = 1000

print("\t.:MENU:.") #\t nos dara 4 espacios al mostrar el mensaje

#creamos el menu
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponnible")
print("4. Salir")

opcion = int(input("Digite una opcion de menu: "))

print() #para crear un salto de linea entre el menu de opciones y todo lo demas

#menu de opciones 
#Si la opcion es 1 es para ingresar dinero
if opcion==1:
    extra = float(input("Cuanto dinero desea ingresar => "))
    #Sumamos la variable extra con la variable saldo 
    saldo += extra
    print(f"Dinero en la cuenta: {saldo}")

#opcion #2 retirar dinero
elif opcion==2:
    retirar = float(input("Cuanto dinero desea retirar => "))
    #creamos una condicional donde si el usuario desea retirar un monto mayor a 1000, eso significa que no tiene esa acantidad de dinero
    if retirar>saldo:
        print("No tiene esa cantidad de dinero")
    #si el monto a retirar es menor a 1000 o igual, se le descontamos la cantidad que el usuario desea retirar
    else:
        saldo -= retirar
        print(f"Dinero en la cuenta: {saldo}")

#opcion 3, dinero disponible
elif opcion==3:
    print(f"Dinero en la cuenta: {saldo}")

#si la opcion es 4, salir
elif opcion==4:
    print("Gracias por utilizar su cajero automatico")
#si digita una opcion que no exisste
else:
    print("Error, se equivoco de opcion de menu")
