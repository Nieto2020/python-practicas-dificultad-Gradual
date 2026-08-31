#Entrada: `[1, 2, 3, 4, 5]` con `k = 2`
#Salida: `[4, 5, 1, 2, 3]`

lista = [1, 2, 3, 4, 5]
n = len(lista)
k = 2
k = k % n # Si k > n, k % n = valido

a = lista[n-k:]
b = lista[:n-k]

a.extend(b)
print(a)