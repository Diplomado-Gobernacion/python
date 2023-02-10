password = "PepeGrillo123#"

while True:
    passUser = input("Ingrese su contraseña: ")
    if passUser == password:
        break
    else:
        print("Contraseña incorrecta")

while True:
    print("Bienvenido al programa!")
    print("1. Sumar")
    print("2.")
    print("3.")
    print("4. Salir")
    opcion = int(input("Opcion: "))

    if opcion == 1:
        print("Realizar sumas")
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de b: "))
        print(f"La suma entre {a} y {b} es {a+b}")

    if opcion == 4:
        print("Finalizando programa...")
        break

