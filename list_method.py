# list_method
# count()
# sort()
# sorted_function()
# clear()
# copy()

fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
# count_method  -------> it count the number of values
print(fruits.count("banana"))
print(fruits.count("apple"))
print(fruits.count("kiwi"))

# sort_method
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
# fruits.sort()  ------> sequence of Alphabets
print(fruits)

numbers = [5, 3, 1, 6, 10, 8]
# numbers.sort()
print(numbers)

# sorted_function
numbers = [5, 3, 1, 6, 10, 8]
# print(sorted(numbers))  ------> it is also a sequence of Alphabets

# clear_method
numbers = [5, 3, 1, 6, 10, 8]
# numbers.clear() -------> it can empty the list
print(numbers)
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
# fruits.clear()
print(fruits)

# copy_method
numbers_copy = numbers.copy()   
# this method can copy the list
print(numbers_copy)
