# Filter_Function:
def is_even(a):
    return a%2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(is_even, numbers))
print(evens)
evens2 = tuple(filter(is_even, numbers))
print(evens2)

for num in filter(is_even, numbers):
    print(num)

# lambda_function:
new_evens = list(filter(lambda a: a%2 == 0, numbers))
print(new_evens)

# list_comprehension:
new_evens2 = [i for i in numbers if i%2 == 0]
print(new_evens2)