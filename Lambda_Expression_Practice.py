# Lambda_Expression_Practice:
def is_even(a):
    return a%2 == 0
print(is_even(4))

# lambda_Expression:
is_even = lambda a : a%2 == 0
print(is_even(5))

    #last_char()
def last_char(a):
    return a[-1]
print(last_char("Abuzar"))

last_char = lambda a: a[-1]
print(last_char("Irfan"))

# lambda with if , else:
def func(s):
    if len(s) > 5:
        return True
    return False
print(func("Abuzar"))

lenght = lambda s: True if len(s) > 5 else False
print(lenght("Abuzar Abid"))

def func2(a):
    return len(a) > 5
print(func2("Irfan"))

len2 = lambda a: len(a) > 5
print(len2("Abuzar"))
