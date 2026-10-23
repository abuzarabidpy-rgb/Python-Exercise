# Function_with_all_parameters:
# 1- Parameters
# 2- *args:
# 3- Default_parameters:
# 4- **kwargs:

# ----->  PADK
def func2(name = 'unknown', age = 17 ):
    print(name)
    print(age)

print(func2('Abuzar',18))

def func(name, *args, age = 17, **kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)

print(func('Abuzar', 1, 2, 3, age = 17, a = 1, b = 2, c = 3 ))
