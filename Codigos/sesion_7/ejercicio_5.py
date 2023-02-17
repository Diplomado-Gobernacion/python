vector = list()

while True:
    try:
        numero = int(input("Numero: "))
        if numero < 0:
            break
    except ValueError:
        print("No se ha ingresado un numero valido!")
    else:
       vector.append(numero)

print(vector)
    
    




