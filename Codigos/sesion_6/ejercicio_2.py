try:
    numerador = float(input("Numerador: "))
    denominador = float(input("Denominador: "))
    cociente = numerador/denominador
except (ZeroDivisionError, ValueError) as error:
    print(f"Error: {error}")
else:
    print(f"El cociente de la division entre {numerador} y {denominador} es {cociente}")
finally:
    print("Fin del programa.")