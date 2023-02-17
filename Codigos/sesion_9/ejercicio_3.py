import funciones

datos = dict()

datos['nombre'] = input("Nombre: ")
datos['dirreccion'] = input("Dirreccion: ") 
print("Ingrese su numero de telerfono: ", end='')
datos['telefono'] = funciones.leerDatos() 
print("Ingrese su edad: ", end='')
datos['edad'] = funciones.leerDatos()

print(funciones.suma(4))

print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['dirreccion']} y su numero de telefono es {datos['telefono']}")
