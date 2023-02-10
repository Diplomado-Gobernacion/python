numero = int(input("Ingrese el numero: "))

for i in range(1, numero+1):
    if i%2 != 0:
        print(f"{i},", end="")
