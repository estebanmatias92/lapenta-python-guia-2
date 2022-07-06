
print("1. Convertir kilómetros a millas " 
    + "Escribir un programa para convertir una distancia en kilómetros en una distancia en millas. "
    + "Ingrese una distancia en Km usando la función input(). Convierta el valor devuelto por la "
    + "función input() a un entero. Realice la conversión dividiendo los kilómetros por 0.6214. Imprima "
    + "un mensaje diciéndole al usuario cuáles son las millas correspondientes."
)
print("")


km = int(input("Ingresar kilometros: "))
miles = int(km/0.6214)

print("")

print(f"Kilometros: {km}")
print(f"Millas: {miles}")