lista_enteros = list()

try:
    datos = open('datasets/datos.txt', 'r')
except FileNotFoundError:
    print("No se encontro el archivo.")
else:
    lista_enteros = datos.read()
    print(lista_enteros)
finally:
    datos.close()