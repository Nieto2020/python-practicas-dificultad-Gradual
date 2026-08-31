#Determina si un número es primo.

#Ejemplos:
#7 → True
#10 → False

n = int(input("Ingresa el Numero: "))

if n % 2 == 1 and n != 1:
    print("PRIMO")
else:
    print("NOT PRIMO")