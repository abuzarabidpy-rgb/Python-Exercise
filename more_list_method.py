# generate_list_with_range:

numbers = list(range(0,10))
print(numbers)

number = list(range(11,20))
print(number)

number1 = list(range(20,31))
print(number1)

# pop_method():

number2 = list(range(0,11))

print(number2.pop())
number2.pop()
print(number2)

number3 = list(range(1,11))
print(number3.index(2))

number4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 4, 5, 6, 7, 1]
print(number4.index(1,11))

# pass list to a fuction:
number5 = list(range(1,11))

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(number5))



