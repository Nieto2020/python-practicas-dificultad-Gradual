#Determina si una palabra se lee igual al derecho y al revés.

#Ejemplos:
#"reconocer" → Tru
#"python" → False

palabra1 = "reconocer"
palabra2 = "Python"

def palindromo(word):  #Hize una funcion xq si xd
    if word == word[::-1]:
        print("Palindromo")
    else:
        print("Not Palindromo")

palindromo(palabra1)
palindromo(palabra2)