datosUsuario = dict()

while True:
    try:
        numeroUsuarios = int(input("Numero de usuarios a agregar: "))
    except ValueError:
        print("No se ha ingresado un numero de usuarios valdido")
    else:
        break

for i in range(numeroUsuarios):
    datosUsuario[i] = input("Nombre del usuario: ")

print(datosUsuario)


