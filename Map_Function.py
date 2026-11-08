# Map_Function:
numbers = [1, 2, 3, 4]
def square(num):
    return num**2

squared_number = list(map(square, numbers))
print(squared_number)

# Lambda_Function:
squared_numbers = list(map(lambda num: num**2, numbers))
print(squared_numbers)

# list_Comprehension:
squared_number = [num**2 for num in numbers]
print(squared_number)

# simple:
square = []
for num in numbers:
    square.append(num**2)
print(square)

# Find_Length:
names = ['Abuzar', 'Irfan', 'Anas']
length = list(map(len, names))
print(length)




