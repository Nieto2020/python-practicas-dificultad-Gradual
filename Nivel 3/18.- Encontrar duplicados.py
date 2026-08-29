#Dada una lista, devuelve cuáles elementos aparecen más de una vez.

#Entrada: `[1, 2, 3, 2, 4, 1]`
#Salida: `[1, 2]`

lista = [1, 2, 3, 2, 4, 1]

dic = {}

for i in lista:
    if i not in dic:
        dic[i] =1
    else:
        dic[i] +=1 


out = []

for key, value in dic.items():
    if value > 1:
        out.append(key)

print(out)