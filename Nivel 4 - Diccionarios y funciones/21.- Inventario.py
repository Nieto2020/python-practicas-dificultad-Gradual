"""Tienes:

inventario = {
    "manzanas": 10,
    "peras": 5,
    "naranjas": 8
}

Crea funciones para:

- agregar productos
- eliminar productos
- modificar cantidades
- consultar cantidad
- calcular productos totales"""

########################################

inventario = {
    "manzanas": 10,
    "peras": 5,
    "naranjas": 8
}

continuar = True

def agregar(db: dict, producto: str, valor: int) -> None:
    db[producto] = valor

def eliminar(db: dict, producto) -> None:
    del db[producto]

def modificar(db: dict, producto: str, valor: int) -> None:
    db[producto] += valor

def consultar(db: dict, producto: str) -> int:
    return db.get(producto)

def calcular(db: dict) -> int:
    count = 0
    for value in db.values():
        count += value
    return count


while continuar:
    print(f"{inventario}\nQue deseas realizar?......\n")
    opt = int(input("""
    ----------------------------------
        Opciones de Inventario
    ----------------------------------
            |1|Agregar Producto
            |2|Eliminar Producto
            |3|Modificar
            |4|Consultar
            |5|Calcular Total
            |0|XxSALIRxX
    ----------------------------------
    Opcion |1|2|3|4|5|0|: """))

    if opt == 0:
        continuar = False
    elif opt ==1:
        agregar()