print(
    "7. Calcule el precio del corte de cabello de una peluquería sabiendo que al precio de lista ($500), "
    + "\nque ese valor que se considera para caballero, se le incrementa $100 para dama y se reduce a "
    + "\nla mitad el corte de niño. "
)
print("")

# Create the data
cut_man = 500
cut_woman = cut_man + 100
cut_kids = cut_man / 2
cost_table = {"mujer": cut_woman, "caballero": cut_man, "niño": cut_kids}

# Show the options
print("Las opciones son: ")
for option in cost_table.keys():
    print("\t" + option)

print("")

person = input("Ingresar sujeto para corte de cabello: ")

print("")

if not person in cost_table:
    print("El sujeto no se encuentra estimado en la tabla de costos")
else:
    print(f"El costo para {person} es: ${cost_table[person]}")
