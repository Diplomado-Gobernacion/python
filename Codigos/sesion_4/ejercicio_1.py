edad = int(input("Ingrese su edad: "))

if edad < 4 :
    precio = 0
elif edad >= 4 and edad < 18 :
    precio = 20000
else:
    precio = 40000

print(f"El precio del boleto es: {precio}")