print(
    "2. Modifique el ejercicio anterior y verifique que el usuario haya ingresado una distancia positiva "
    + "(es decir, no puede ingresar un número negativo), además verificar que la entrada sea un "
    + "número, si no es un número no debe hacer nada, de lo contrario, convierta la distancia a millas.\n"
    + "(Utilizar funcion isnumeric() solo es para enteros)."
)
print("")


km = input("Ingresar kilometros: ")

print("")

if km.isnumeric() and int(km) > 0:
    miles = int(int(km) / 0.6214)

    print(f"Kilometros: {km}")
    print(f"Millas: {miles}")
else:
    print("El valor ingresado es invalido")
