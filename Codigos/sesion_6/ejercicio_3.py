cadena = "Hola mundo!"

for i in range(15):
    try:
        print(f"Letra: {cadena[i]}")
    except IndexError:
        print("Indice excedido")
        break
        