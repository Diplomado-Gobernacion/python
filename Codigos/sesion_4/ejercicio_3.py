lista = ['papa', 'yuca', 'frijol', 'arroz']
testigo = False

for elemento in lista:
    if elemento == "arroz":
        testigo = True

if testigo:
    print("Hay arroz en la lista")
else:
    print("No hay!")