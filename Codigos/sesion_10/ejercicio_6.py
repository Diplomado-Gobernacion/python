def agregueIVA(precioTsinIVA, iva=21):
    precioTconIVA = precioTsinIVA*(1 + iva/100)
    return precioTconIVA

factura = list()

# desc     cantidad    precioU     precioTP
# ...       ...         ...         ...
# ...       ...         ...         ...
#                                   precioTsinIVA
#                                       IVA
#                                   precioTconIVA

print("Introduzca 0 en nombre de producto para terminar.")
while True:
    desc = input("Nombre producto: ")
    if desc == "0":
        break
    cantidad = int(input("Cantidad de producto: "))
    precioU = float(input("Precio unitario: "))
    precioTP = cantidad * precioU
    factura.append([desc, cantidad, precioU, precioTP])

precioTsinIVA = 0

for i in range(len(factura)):
    precioTsinIVA += factura[i][3]

while True:
    try:
        iva = int(input("Iva: "))
    except ValueError:
        precioTconIVA = agregueIVA(precioTsinIVA)
    else:
        if iva > 0:
            precioTconIVA = agregueIVA(precioTsinIVA, iva)
            break
        else:
            print("IVA no puede ser negativo!")

print(precioTconIVA)

if len(factura) > 0:
    print(factura)