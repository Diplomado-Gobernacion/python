import numpy as np

# A lo viejo
lista = list(range(10))
suma = 0
for i in range(len(lista)):
    suma += lista[i]

promedio = suma/len(lista)
print(promedio)

# Usando numpy
lista_numpy = np.array(lista)
print(f"El promedio es: {lista_numpy.mean()}")
