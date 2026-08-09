# # list no : 01
# # insert method
fruits = ["grapes", "apples"]
fruits.insert(1, "mango")
print(fruits)

# # list no : 02
fruits = [ "mango", "grapes"]
fruits.insert(0, "cherry")
print(fruits)

# # list no : 03
# extend method
fruits1 = ["grapes", "apples"]
fruits2 = ["mango", "cherry"]
print(fruits1 + fruits2)

# list no : 04
fruits1 = ["apples", "grapes"]
fruits2 = ["mango", "cherry"]
fruits1.extend(fruits2)
print(fruits1)

# list no : 05
fruits1 = ["apples", "grapes"]
fruits2 = ["mango", "cherry"]
fruits1.append(fruits2)
print(fruits1)
