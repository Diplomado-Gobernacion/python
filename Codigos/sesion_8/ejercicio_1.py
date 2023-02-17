departamento = [[10, 20, 30, 20, 10, 10], 
                [20, 20, 20, 20, 20, 10], 
                [10, 10, 10, 10, 10, 10],
                [30, 30, 15, 30, 30, 10],
                [40, 40, 40, 40, 40, 10]]

nombresDepartamentos = ("Marketing","Contabilidad","RH","Distribucion","Ingenieria", "Aseo") 
nombresConceptos = ("Salarios","Suministros","Mobiliario","Equipamento","Otros")

sumaGastosDepartamento = [0, 0, 0, 0, 0, 0]

for fila in range(len(departamento)):
    sumaGastosConcepto = 0
    for columna in range(len(departamento[fila])):
        sumaGastosConcepto += departamento[fila][columna]
        sumaGastosDepartamento[columna] += departamento[fila][columna]

    print(f"La suma del concepto {nombresConceptos[fila]} es: {sumaGastosConcepto}")


#for fila in range(len(departamento)):
#    for columna in range(len(departamento[fila])):
#        sumaGastosDepartamento[columna] += departamento[fila][columna]
       
for i in range(len(nombresDepartamentos)):
    print(f"La suma del departamento de {nombresDepartamentos[i]} es: {sumaGastosDepartamento[i]}")

# primera vuelta
        #sumaGastosConcepto[0] += departamento[0][0]
        #sumaGastosConcepto[1] += departamento[0][1]
        #sumaGastosConcepto[2] += departamento[0][2]
        #sumaGastosConcepto[3] += departamento[0][3]
        #sumaGastosConcepto[4] += departamento[0][4]

        # segunda vuelta
        #sumaGastosConcepto[0] += departamento[1][0]
        #sumaGastosConcepto[1] += departamento[1][1]
        #sumaGastosConcepto[2] += departamento[1][2].
        # ...