print(
    "4. Mostrar en forma ascendente y descendente los números naturales existentes en un "
    + "determinado rango \n"
    + "Ejemplo: A=5 y B=12 \n"
    + "Salida ascendente: 5 - 6 - 7 - 8 - 9 - 10 - 11 - 12 \n"
    + "Salida descendente: 12 - 11 - 10 - 9 - 8 - 7 - 6"
)
print("")


MIN = int(input("Ingresar mínimo: "))
MAX = int(input("Ingresar máximo: "))

print("")

if MIN == MAX:
    print("El mínimo y el máximo son iguales")
elif MIN > MAX:
    print("El mínimo es superior al máximo")
else:
    print("Secuencia ascendente: ", [elem for elem in range(MIN, MAX + 1)])
    print("Secuencia descendente: ", [elem for elem in range(MAX, MIN - 1, -1)])
