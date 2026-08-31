
#Dada una frase, determina cuántas palabras contiene.

#Ejemplo: "Python es muy interesante" → 4

frase = "Python es muy interesante"
count = 0

for i in frase.split():
    count += 1
print(f"'{frase}' -> {count}")