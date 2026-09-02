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

def eliminar(db: dict, producto: str) -> None:
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
        print(f"Saliendo...")
        break
    elif opt == 1:
        pd = str(input("Ingresa el producto a agregar: "))
        val = int(input("Ingresa la cantidad: "))
        agregar(inventario, pd, val)
    elif opt == 2:
        for k in inventario:
            print(k)
        pd = str(input("Ingresa el Producto a elminar: "))
        confirmation = str(input(f"¿Seguro que quieres eliminar '{pd}'? \n |S|N|: ")).lower
        if confirmation != "n":
            eliminar(inventario, pd)
        else:
            print("Regresando al menu")
    elif opt == 3:
        