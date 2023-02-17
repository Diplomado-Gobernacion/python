datos = dict()

datos['nombre'] = input("Nombre: ")
datos['dirreccion'] = input("Dirreccion: ") 

while True:
    try:
        datos['telefono'] = int(input("Telefono: "))
    except ValueError:
        print("El datos ingresado no es un numero.")
    else:
        break

while True:
    try:
        datos['edad'] = int(input("Edad: ")) 
    except ValueError:
        print("El datos ingresado no es un numero.")
    else:
        break

print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['dirreccion']} y su numero de telefono es {datos['telefono']}")
