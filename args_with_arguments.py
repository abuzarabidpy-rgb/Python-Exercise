# Multiplication:
def multiply_num(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply

nums = [2, 5, 8]
print(multiply_num(*nums))

# Addition:
def add_num(*args):
    add = 0
    print(args)
    for i in args:
        add += i
        return add

print(add_num(2, 5, 8))
    