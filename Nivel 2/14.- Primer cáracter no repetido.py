#Dada una cadena, encuentra el primer carácter que aparece solamente una vez.
#Ejemplo: "swiss" → "w"
#Este ya es un **problema de entrevista bastante clásico**.

cadena = "saiwssdfes"

dic = {}

for i in cadena:
    if i not in dic:
        dic[i] = 1
    elif i in dic:
        dic[i] += 1

for j, val in dic.items():
    if val == 1:
        print(f"cadena -> {j}")
        break