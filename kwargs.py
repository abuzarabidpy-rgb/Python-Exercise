# kwargs:

def func(**kwargs):
    for j,v in kwargs.items():
        print(f"{j} : {v}")

# print(func(name = 'Abuzar', age = 17))
# Dictionary unpacking:
d = {'first_name' : 'Abuzar', 'last_name' : 'Abid', 'age' : 17}
func(**d)