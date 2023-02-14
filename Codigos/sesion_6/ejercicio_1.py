try:
    numerador = float(input("Numerador: "))
    denominador = float(input("Denominador: "))
    cociente = numerador/denominador
except ZeroDivisionError:
    print("Error: el denominador es nulo")
except ValueError:
    print("Error: valor ingresado no es numero")
else:
    print(f"El cociente de la division entre {numerador} y {denominador} es {cociente}")
finally:
    print("Fin del programa.")