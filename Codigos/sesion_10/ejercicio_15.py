import json

flujo = open('datasets/lista.json', 'r')
lista = json.load(flujo)
print(lista)
flujo.close()

flujo = open('datasets/diccionario.json', 'r')
dicc = json.load(flujo)
print(dicc['1'][0]['nombre'])
flujo.close()