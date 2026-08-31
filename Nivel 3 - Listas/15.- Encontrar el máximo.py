#Dada una lista de números, encuentra el mayor.
#Restricción: no uses max()

test = [1, 12, 12, 17, 29, 33, 44,  56, 32, 34, 0, 45, 12, 3, 5, 67, 31, 22, 14, 9, 8, 7, 55, 6]

mayor = test[0]

for i in test:
    if i > mayor:
        mayor = i
        print(mayor)
