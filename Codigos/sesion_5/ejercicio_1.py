palabra = input("Introduzca palabra: ")

# HOLA -> 4 elementos
# len() -> 4
# range(4-1, -1, -1) -> range(3, -1, -1) -> 3, 2, 1, 0

for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])

print()

# HOLA -> 4 elementos
# len() -> 4
# range(-1, (4+1)*(-1), -1) -> range(-1, -5, -1) -> -1, -2, -3, -4


for i in range(-1, (len(palabra)+1) * (-1), -1):
    print(palabra[i])