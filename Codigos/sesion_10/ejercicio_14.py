import json

lista = [[1, 2], [3, 4], [5, 6]]

flujo = open('datasets/lista.json', 'w')
json.dump(lista, flujo)
flujo.close()


diccionario = {1: [{'nombre': 'arroz', 'precio': 34}, {'nombre': 'papa', 'precio': 4}], 2: 'yuca', 3: 'arroz'}
flujo = open('datasets/diccionario.json', 'w')
json.dump(diccionario, flujo)
flujo.close()