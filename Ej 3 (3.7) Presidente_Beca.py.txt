
print("ASIGNACION DE BECAS POR PARTE DE LA PRESIDENCIA DE LA REPUBLICA")

Edad = int(input(" Ingrese la edad del estudiante: "))
Promedio = float(input("Ingrese el promedio del estudiante: "))
Beca = float()
if Edad > 18: 
    if Promedio >= 9: 
        Beca = 2000.00 
    elif Promedio>=7.5:
        Beca = 1000.00 
    elif Promedio<7.5 and Promedio>=6: 
        Beca = 500.00 
    else: 
        print("Por favor, estudiar más para el proximo ciclo escolar.")
else: 
    if Promedio >= 9: 
        Beca = 3000.00 
    elif Promedio<9 and Promedio>=8: 
        B = 2000.00 
    elif Promedio<8 and Promedio>=6: 
        Beca = 100.00 
    else:
        print("Por favor, estudiar más para el proximo ciclo escolar.")
if Beca > 0: 
    print("El monto de la Beca del estudiante es de: $",Beca)