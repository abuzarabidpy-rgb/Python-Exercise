numbers = [6,60,2]

# Min_method:
print(min(numbers))
# output: 2
print(max(numbers))
# output: 60

# function:

def greatest_diff(l):
    return max(l) - min(l)

print(greatest_diff(numbers))
# output: 58

def smallest_num(l):
    return min(l)

print(smallest_num(numbers))
# output: 2

def greatest_num(l):
    return max(l)

print(greatest_num(numbers))
# output: 60