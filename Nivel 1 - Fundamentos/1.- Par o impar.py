#Recibe un número entero y determina si es par o impar.

num = 0
option = "y"

while True:
    num = int(input("Ingrese el numero del 1 al Infinito: "))
    if num % 2 == 0:
        print("Numero Par")
    else:
        print("Impar")
    option = input("Continuar? yes = y | no = n")
    if option != "y":
        print("ok, by bye")
        break