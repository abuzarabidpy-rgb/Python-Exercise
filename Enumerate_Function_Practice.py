# Enumerate_Function_Practice:
# 1           Even_colors
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
for pos, color in enumerate(colors):
    if pos%2 == 0:
        print(f"{pos} : {color}")
# 2           first_three_names
students = ['Abuzar', 'Irafan', 'Anas', 'David', 'Eve']
for pos, student in enumerate(students, start=1):
    if pos <=3:
        print(f"Postion {pos} : {student}")
# 3           find_position
items = ["Milk", "Bread", "Eggs", "Butter", "Jam"]
for pos, item in enumerate(items):
    if item == "Eggs":
        print(f"Eggs index {pos} per ha")
# 4            seperate_words
words = 'PYTHON'
for pos, letter in enumerate(words, start=1):
    print(f"{pos} : {letter}")
# 5             update_list
marks = [45, 78, 32, 88, 50]
for index, mark in enumerate(marks):
    marks[index] = mark + 5
print(marks)
# 6          cancel_negative
numbers = [10, -5, 20, -15, 30]
for index, number in enumerate(numbers):
    if number < 0:
        numbers[index] = 0
print(numbers)
# 7           capital_letters
names = ["ali", "sara", "bilal", "zoya"]
for index, name in enumerate(names):
    names[index] = name.upper()
print(names)
