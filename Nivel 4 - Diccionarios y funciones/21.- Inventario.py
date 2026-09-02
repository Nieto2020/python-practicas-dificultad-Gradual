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

def agregar(db: dict) -> None:
    pd = str(input("Ingresa el producto a agregar: "))
    val = int(input("Ingresa la cantidad: "))
    db[pd] = val
    print(f"Producto: {pd}\nCantidad agregada:{val} ")

def eliminar(db: dict) -> None:
    for k in inventario:
        print(k)
    pd = str(input("Ingresa el Producto a elminar: "))
    confirmation = str(input(f"¿Seguro que quieres eliminar '{pd}'? \n |S|N|: ")).lower
    if confirmation != "n":
        print(f"Producto '{pd}' ELIMINADO...")
        del db[pd]
    else:
        print("Regresando al menu")

def modificar(db: dict) -> None:
    for k in db:
        print(k)
    pd = str(input("Ingresa el producto a modificar: "))
    trans = int(input("Presiona |1| para sumar // Presiona |2| Para restar.\n: "))
    val = int(input("¿Cuanto? :"))
    if trans != 1:
        db[pd] -= val
    else:
        db[pd] += val
    print("Modificiación LISTA")

def consultar(db: dict) -> None:
    for k in db:
        print(k)
    pd = str(input("Ingresa el producto a consultar: "))
    print(f" Cantidad de '{pd}': {db.get(pd)}")

def calcular(db: dict) -> None:
    print("\n|PRODUCTO|CANTIDAD|")
    for key, value in db.items():
        print(f" {key} -> {value} ")


while continuar:
    print("\nQue deseas realizar?......\n")
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
    elif opt == 1:
        agregar(inventario)
    elif opt == 2:
        eliminar(inventario)
    elif opt == 3:
        modificar(inventario)
    elif opt == 4:
        consultar(inventario)
    elif opt == 5:
        calcular(inventario)