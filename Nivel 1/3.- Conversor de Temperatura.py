# Convierte Celsius a Fahrenheit y viceversa.

f = 0
c = 0
mesure = 0
dic={
    1 : "Celsius",
    2 : "Fatrenheit"
}

while True:
    print("Bienvenido al convertidor de Unidades")

    mesure = int(input("""
========================================
Selecciona la Medida que ingresaras:
========================================

            |1| --Celsius--
            |2| --Farenheit--
            |3| --SALIR--
            : """))

    if mesure in [1,2]:

        x = float(input(f"Ingresa la cantidad exacta de {dic[mesure]} : \n"))
        print(f"{x} {dic[mesure]}")

        print("""
========================================
Calculando......:3
========================================""")

        #Formula -> °F = (°C × 9/5) + 32.
        if mesure == 1:
            f = (x * (9/5) + 32)
            respuesta = f"{f} Grados Farenheit\n"

        #Formula -> °C = (°F - 32) × 5/9.
        else:
            c = ((x - 32) * (5/9))
            respuesta = f"{c} Grados Celsius \n"

        print(respuesta)
        

    else:
        print("Elegiste Salir, bye.bye...")
        break
    