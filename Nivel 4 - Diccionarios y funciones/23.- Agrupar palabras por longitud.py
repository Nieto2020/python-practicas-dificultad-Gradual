"""
- Entrada: ["sol", "python", "casa", "programacion", "pan"]
- Salida (equivalente):

python
{
    3: ["sol","pan"],
    4: ["casa"]
    6: ["python"],
    12: ["programacion"]
}
"""

sq = [
    "sol",
    "mar",
    "cielo",
    "montaña",
    "universo",
    "teclado",
    "programación",
    "dato",
    "algoritmo",
    "nube",
    "electricidad",
    "fuego",
    "río",
    "explorador",
    "astronauta",
    "inteligencia",
    "magia",
    "dragón",
    "ciudad",
    "transparencia",
    "pixel",
    "memoria",
    "computadora",
    "viento",
    "tormenta",
    "galaxia",
    "realidad",
    "fantasía",
    "estructura",
    "minimalismo"
]


dick = {}

for palabra in sq:    
    if len(palabra) not in dick:
        dick[len(palabra)] = []
        dick[len(palabra)].append(palabra)
    else:
        dick[len(palabra)].append(palabra)

res = dict(sorted(dick.items()))

for key, value in res.items():
    print(key, value)