lista = [3,4,6,1,8]

menor = 0

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        print(f"lista[i]: {lista[i]} < lista[j]: {lista[j]}")
        if lista[i] < lista[j]:
            menor = lista[i]

print(menor)
