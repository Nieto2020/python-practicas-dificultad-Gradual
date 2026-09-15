#Determina si un número es primo.

#Ejemplos:
#7 → True
#10 → False

PRIMOS = [2, 3, 5, 7, 11, 13]
n = [2, 3, 5, 7, 11, 13, 4, 6, 9]

for i in n:
    es_primo = True
    raiz = int(i ** 0.5)

    if i in PRIMOS:
        es_primo = True
    else:

        for p in PRIMOS:
            if p <= raiz:
                if i % p == 0:
                    es_primo = False
                    break  

    if es_primo:
        print(f"{i}: Primo")
    else:
        print(f"{i}: Not primo")