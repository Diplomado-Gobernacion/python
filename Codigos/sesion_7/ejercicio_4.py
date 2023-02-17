lista = [[1,2,3], [4,5,6], [7,8,10]]

testigo = False

for row in lista:
    for elem in row:
        if elem == 10:
            print("El 10 existe!")
            testigo = True
            break

if not testigo:
    print("No se encontro el 10")
            