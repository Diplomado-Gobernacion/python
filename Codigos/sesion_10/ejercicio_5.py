def agregueIVA(precioT, iva=21):
    precioT = precioT*(1 + iva/100)
    return precioT


precioT = int(input("Precio Total:"))

try:
    iva = int(input("Iva: "))
except ValueError:
    total = agregueIVA(precioT)
else:
    if iva >= 0:
        total = agregueIVA(precioT, iva)
    else:
        print("IVA no puede ser negativo!")



print(total)