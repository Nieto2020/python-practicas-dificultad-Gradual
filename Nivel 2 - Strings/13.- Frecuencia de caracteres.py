#Cuenta cuántas veces aparece cada carácter.
#Entrada: "banana"
#Salida:

#text
#b: 1
#a: 3
#n: 2

texto = "banana"

dic = {}

for i in texto:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)