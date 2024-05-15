
print("----------Bienvenido a BANCO PICHINCHA----------")

nombre = input("Ingrese el nombre del cliente: ")
tipoDeTarjeta = input("Ingresa el tipo de tarjeta: 1, 2, 3, otro: ")
credito_Anterior = float (input("Ingrese el credito anterior: "))

if tipoDeTarjeta == '1':
    incremento = 0.25
    nuevo_salario =  credito_Anterior * (1 + incremento)
    porcentaje_incremento = incremento * 100
    print(f"-----Señor/ra {nombre}-----")
    print(f"El incremento salarial fue del {porcentaje_incremento}%")
    print(f"Su credito aprobado es de: ${nuevo_salario: .2f}")
    print("Gracias por confiar en Banco Pichincha")
elif tipoDeTarjeta == '2':
    incremento = 0.35
    nuevo_salario =  credito_Anterior * (1 + incremento)
    porcentaje_incremento = incremento * 100
    print(f"-----Señor/ra {nombre}-----")
    print(f"El incremento salarial fue del {porcentaje_incremento}%")
    print(f"Su credito aprobado es de: ${nuevo_salario: .2f}")
    print("Gracias por confiar en Banco Pichincha")
elif tipoDeTarjeta == '3':
    incremento = 0.40
    nuevo_salario =  credito_Anterior * (1 + incremento)
    porcentaje_incremento = incremento * 100
    print(f"-----Señor/ra {nombre}-----")
    print(f"El incremento salarial fue del {porcentaje_incremento}%")
    print(f"Su credito aprobado es de: ${nuevo_salario: .2f}")
    print("Gracias por confiar en Banco Pichincha")
elif tipoDeTarjeta == 'otro':
    incremento = 0.50
    nuevo_salario =  credito_Anterior * (1 + incremento)
    porcentaje_incremento = incremento * 100
    print(f"-----Señor/ra {nombre}-----")
    print(f"El incremento salarial fue del {porcentaje_incremento}%")
    print(f"Su credito aprobado es de: ${nuevo_salario: .2f}")
    print("Gracias por confiar en Banco Pichincha")
else:
    print("Tipo de tarjeta no valida")

