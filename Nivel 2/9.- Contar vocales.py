#Dada una cadena, cuenta cuántas vocales contiene.
#Ejemplos:
#"python" → 1
#"hola mundo" → 4

voc = ["a", "e", "i", "o", "u"] #VOCALES

cadena = str(input("Ingresa el texto: ")).lower() #Normalizacion de texto
words = cadena.split() #Separar str en palabras

dic = {}


for palabra in words:
    dic[palabra] = 0
    for letra in palabra:
        if letra in voc:
            dic[palabra] += 1

            
print(dic)