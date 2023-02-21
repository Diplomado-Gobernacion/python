def leerArchivo(ruta):
    try:
        datos = open(ruta, 'r')
        datos.readline()

        productos = dict()

        for linea in datos:
            palabras = linea.split()
            productos[palabras[0]] = float(palabras[1])

    except FileNotFoundError as error:
        raise FileNotFoundError(error)
    else:
        return productos
    finally:
        try:
            datos.close()
        except UnboundLocalError as error:
            print(error)


try:
    productoLista = leerArchivo('datasets/datos1.txt')
except FileNotFoundError:
    print("No se encontro el archivo.")
else:
    print(productoLista)
