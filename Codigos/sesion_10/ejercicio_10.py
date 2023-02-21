try:
    datos = open('datasets/datos1.txt', 'r')
    datos.readline()

    productos = list()
    precios = list()

    for linea in datos:
        palabras = linea.split()
        productos.append(palabras[0])
        precios.append(float(palabras[1]))
except FileNotFoundError:
    print('No se encontro el archivo.')
else:
    print(productos)
    print(precios)
finally:
    datos.close()