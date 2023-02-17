
lista = list()
datos = open('datos.txt', 'r')

for linea in datos:
    lista.append([int(x) for x in linea.split()])
datos.close()

print(lista)