def agregueIVA(precioT, iva=21):
    precioT = precioT*(1 + iva/100)
    return precioT


precioT = int(input("Precio Total:"))
iva = int(input("Iva: "))

if iva <= 0:
    total = agregueIVA(precioT)
else:
    total = agregueIVA(precioT, iva)

print(total)