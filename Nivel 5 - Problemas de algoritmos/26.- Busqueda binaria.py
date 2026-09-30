"""Dada una lista ordenada:
[1, 3, 5, 7, 9, 11, 13, 15]

encuentra un número utilizando búsqueda binaria.

-Restricción: no puedes utilizar `in` ni `index()`; debes implementar el algoritmo."""

x = [1, 3, 5, 7, 9, 11, 13, 15]
numero = 5

def busqueda_binaria(lista, n) -> int:

    inicio = 0
    fin = len(lista) -1

    while inicio <= fin:

        medio = (inicio + fin) // 2

        if lista[medio] == n:
            return medio
        
        if lista[medio] > n:
            fin = medio -1

        else:
            inicio = medio +1

    return -1 

indice_encontrado = busqueda_binaria(x, numero)

if indice_encontrado != -1:
    print(f"Exito el número enontrado |{numero}| en el indice -> |{indice_encontrado}|")
else:
    print(f"El numero |{numero}| no se encuentra en la lista")