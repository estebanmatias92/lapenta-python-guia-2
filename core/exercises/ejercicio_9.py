print(
    "9. Realizar una aplicación que realice la siguiente figura: "
    + "\n\t0 B N B N B N B"
    + "\n\tB 0 B N B N B N"
    + "\n\tN B 0 B N B N B"
    + "\n\tB N B 0 B N B N"
    + "\n\tN B N B 0 B N B"
    + "\n\tB N B N B 0 B N"
    + "\n\tN B N B N B 0 B"
    + "\n\tB N B N B N B 0"
)
print("")


secuence = ["0", "B", "N", "B", "N", "B", "N", "B"]

# Rotates a list one time, (n) amount of positions
def rotate(my_list, n):
    return my_list[-n:] + my_list[:-n]


# Rotate the secuencia 8 times
for i in range(0, 8):
    print(rotate(secuence, i))
