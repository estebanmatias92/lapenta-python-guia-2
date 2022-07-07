print(
    "8. Calcule y muestre el sueldo en pesos, de los empleados de la empresa P50.S.A, al consultar "
    + "\nsegún su puesto de trabajo."
    + "\nLos haberes se calculan de acuerdo a una unidad de valor (u.v),la misma tiene una valor, a la"
    + "\nfecha, de u$s 55.-"
    + "\nTenga en cuenta que:"
    + "\n\tEl presidente de la empresa cobra 50 u.v"
    + "\n\tUn gerente cobra: 30 u.v"
    + "\n\tUn jefe de sector: 20 u.v"
    + "\n\tUn empleado administrativo: 10 u.v"
    + "\n\tUn empleado de maestranza: 7 u.v"
    + "\nConsidere el valor del dólar :$220"
)
print("")


# Create the data
unit_value = 55
dolar_conversion = 220
unit_value_peso = dolar_conversion * unit_value

ranks = {
    "presidente": 50,
    "gerente": 30,
    "jefe": 20,
    "administrativo": 10,
    "maestranza": 7,
}


# Show the options
print("Las opciones son: ")
for option in ranks.keys():
    print("\t" + option)

print("")

rank = input("Ingresar categoria a consultar: ")

print("")

if not rank in ranks:
    print("El escalafon no es correcto")
else:
    print(
        f"El salario de {rank} es: U$D{ranks[rank] * unit_value} (${ranks[rank] * unit_value_peso})"
    )
