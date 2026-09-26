# Sets_comprehension:

square = {k**2 for k in range(1, 11)}
print(square)

name = "Abuzar", "Irfan", "Anas"
first_letter = {names[0] for names in name}
print(first_letter)