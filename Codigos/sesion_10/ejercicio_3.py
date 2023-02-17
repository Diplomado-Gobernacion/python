def indice(lista, valor):
    for indice, x in enumerate(lista):
        if x == valor:
            return indice
    raise ValueError(f"El valor {valor} no se encontro en la lista.")

lista = [1, 4, -3, 6, -8, 9, 10, -45]

try:
    valor = 4
    print(f"El valor {valor} esta en la posicion {indice(lista, valor)}.")
except ValueError as error:
    print(error)

