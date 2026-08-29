#Entrada: `[1, 2, 2, 3, 4, 4, 5]`
#Salida: `[1, 2, 3, 4, 5]`
#Restriccion no uses "set()"

l = [1, 2, 2, 3, 4, 4, 5]

lgg = []

for i in l:
    if i not in lgg:
        lgg.append(i)

print(lgg)