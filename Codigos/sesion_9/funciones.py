def leerDatos():
    '''Esta funcion valida que el dato de entrada sea int'''
    while True:
        try:
            datos1 = int(input())
        except ValueError:
            print("El dato ingresado no es un numero.")
            print("Ingrese nuevamente el dato: ", end='')
        else:
            break
    return datos1

def suma(a, b=0):
    resultado = a + b
    return resultado

