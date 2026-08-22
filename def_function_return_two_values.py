def func(num1,num2):
    add = num1 + num2
    multiply = num1*num2
    subtract = num1 - num2
    return add, multiply, subtract

print(func(549,5))
add, multiply, subtract = func(549,5)
print(add)
print(multiply)
print(subtract)
