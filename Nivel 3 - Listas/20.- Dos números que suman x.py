#Entrada: `[2, 7, 11, 15]` y `target = 9`
#Salida: los dos números cuya suma sea `9`.

lista = [2, 7, 11, 15]
salida = []


for i in lista:

    for j in lista:

        if i+j == 9:
            salida.append(i)

print(salida)