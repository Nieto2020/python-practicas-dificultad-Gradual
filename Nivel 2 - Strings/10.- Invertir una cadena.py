#Invierte un string.

#Ejemplo: `"python" → "nohtyp"`
#Restricción: intenta primero sin `[::-1]`

texto = "Python"
invertido = ""

for i in range(len(texto) -1, -1, -1):
    invertido += texto[i]

print(invertido)