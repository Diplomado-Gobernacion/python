def suma(x=0, y=0, z=0):
    resul = x + y + z
    print(z)
    z = z + 1
    return z, resul

a = 3
a, resultado = suma(3,4,a)

print(resultado)
print(a)


