# **keywarges:
def func(**args):
    for j, v in args.items():
        print(f"{j} : {v}")
    
d = {'name' : 'Abuzar', 'age' : '17'}
print(func(**d))
# func(name = 'Abuzar', age = '17', last_name = 'Abid')