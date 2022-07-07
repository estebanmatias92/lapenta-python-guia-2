print(
    "5. Construye programa en C que, al recibir como dato el precio de un producto importado, "
    + "incremente 35%% el mismo, si es superior a $50,500 y que además escriba el nuevo precio del "
    + "producto. "
)
print("")


price = int(input("Ingresar precio producto: "))

print("")

if price > 50000:
    price = price * 1.35

print(f"Precio del producto: {price}")
