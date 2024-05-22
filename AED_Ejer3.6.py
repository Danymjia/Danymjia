
precio_articulo = float(input("Ingrese el precio del articulo: "))

if precio_articulo >= 200:
    descuento = 0.15
elif 100 < precio_articulo < 200:
    descuento = 0.12
else:
    descuento = 0.10

descuento_final = precio_articulo * descuento
precio_final = precio_articulo - descuento_final

print(f"-------------------------------")
print(f"Precio original: ${precio_articulo:.2f}")
print(f"Descuento de: ${descuento_final:.2f}")
print(f"Precio final: ${precio_final:.2f}")
print(f"-------------------------------")


