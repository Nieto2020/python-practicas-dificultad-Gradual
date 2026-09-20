"""Dadas:
python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
"""
#encuentra los elementos que aparecen en ambas.

#Salida: [3, 4]

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

lista = []
for i in a:
    for j in b:
        if i == j:
            lista.append(i)

print(lista)