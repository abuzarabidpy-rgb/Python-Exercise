# intro *args:

def all_numbers(*args):
    total = 0 
    for num in args:
        total += num
    return total

print(all_numbers(5, 10, 15))


def multiply_num(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply_num(2, 3))


def subtract_num(*args):
    subtract = args[0]
    for i in args[1:]:
        subtract -= i
    return subtract

print(subtract_num(10, 5))

