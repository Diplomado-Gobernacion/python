try:
    datos = open('datasets/datos1.txt', 'r')
    datos.readline()

    productos = dict()

    for linea in datos:
        palabras = linea.split()
        productos[palabras[0]] = float(palabras[1])

except FileNotFoundError:
    print('No se encontro el archivo.')
else:
    print(productos)
finally:
    datos.close()