#Entrada: [10, 5, 8, 20, 15]
#Salida: 15
#Restricción: no uses sort().

test = [10, 5, 8, 20, 15]
n = len(test)
segundo_mayor = test[n-1]

for i in range(0, n-1): #0123
    for j in range(0, n-1-i): #0123 - 012 -01 - 0
        if test[j] > test[j+1]:
            test[j], test[j+1] = test[j+1], test[j]

print(test)
print(segundo_mayor)