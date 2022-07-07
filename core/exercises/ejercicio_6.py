print(
    "6. Elabore un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente."
)
print("")

week = {
    1: "Domingo",
    2: "Lunes",
    3: "Martes",
    4: "Miercoles",
    5: "Jueves",
    6: "Viernes",
    7: "Sabado",
}

num = int(input("Ingresar numero de la semana: "))

print("")

if num < 1 or num > 7:
    print("El número no pertenece a un día de la semana")
else:
    print(f"Día: {week[num]}")
