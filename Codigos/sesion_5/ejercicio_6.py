correcto = False

while not correcto:
    try:
        valor = int(input("Digite un numero: "))
    except ValueError:
        print("La embarro!")
    else:
        correcto = True



    
