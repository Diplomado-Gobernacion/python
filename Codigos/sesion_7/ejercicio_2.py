numeroFrutas = int(input("Numero de frutas a agregar: "))

frutas = list()

for i in range(numeroFrutas):
    fruta = input(f"Fruta {i+1}:")
    frutas.append(fruta)

print(frutas)
