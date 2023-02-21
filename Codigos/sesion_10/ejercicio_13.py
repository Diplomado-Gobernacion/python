def salvarArchivo(ruta, cabecera, datos):
    try:
        flujo = open(ruta, 'a')
    except FileNotFoundError as error:
        raise FileNotFoundError(error)
    else:
        for valor in lista:
            flujo.write(f'{valor[0]},{valor[1],valor[2]}\n')
    finally:
        flujo.close()


cabecera = 'Nombre  Precio  UnidadesDisponibles'
lista = [('arveja', 23, 300), ('yuca', 10, 100), ('arroz', 30, 242)]

try:
    salvarArchivo('datasets/datos4.txt', cabecera, lista)
except FileNotFoundError:
    print("No existe el archivo.")
