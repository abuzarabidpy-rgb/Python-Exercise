# Greater_number:
def greater_num(a,b):
    if a > b:
        return a
    else:
        return b

# Greater three numbers:
def greatest_num(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Function_inside_Function:
def new_greatest_num(a,b,c):
    bigger = greater_num(a,b)
    return greater_num(bigger,c)

print(new_greatest_num(10,20,30))
    

