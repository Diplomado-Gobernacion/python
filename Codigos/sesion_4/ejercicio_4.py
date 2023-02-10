import random

testigo = False

for i in range(3):
    dado = random.randrange(1,7)
    print(dado)

    if dado == 5:
        testigo = True

if testigo:
    print("Salio un 5")
else:
    print("No salio")
