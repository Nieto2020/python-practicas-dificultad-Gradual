lista = []

while True:

    print("Ingresa tres numeros enteros validos...")

    for i in range(3):

        x = int(input(": "))
        lista.append(x)

    print("Listo Calculando Valores.....")
    #PROHIBIDO USAR 'MAX()'
    mayor = lista[0]

    for j in lista:
        if j > mayor:
            mayor = j

    print(f"El numero mayor es: {mayor}")
    romper = input("Deseas calcular nuevos numeros?\n|y|n|\n: ")
    if romper != "y":
        print("Cerrando correctamente. bye bye")
        break
    else:
        lista = []