
print("4. Escribir un programa para calcular los números primos desde 1 hasta el valor ingresado por el usuario."
    + "\n\t • Si el usuario ingresa un número inferior a 2, imprima un mensaje de error."
    + "\n\t • Para cualquier número mayor de 2, realizar ciclos para determinar cuáles son esos números primos."
)
print("")


range_limit = int(input("Ingresar valor numerico: "))

print("")

if range_limit < 2:
    print("No se puede encontrar un numero primo menor a 2")
else:
    print("Correcto!!!")