def greater_num(a,b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("enter a number :"))
num2 = int(input("enter a number :"))
bigger = greater_num(num1,num2)

print(f"{bigger} is greater")

        # <------------------->

# # smaller number
def smaller_num(a,b):
    if a < b:
        return a
    else:
        return b

num1 = int(input("enter a number :"))
num2 = int(input("enter a number :"))
smaller = smaller_num(num1,num2)
print(f"{smaller} is smaller")

      # <------------------->

# Equal number
def equal_num(a,b):
    return a == b

num1 = int(input("enter a number :"))
num2 = int(input("enter a number :"))

if equal_num(num1,num2):
    print(f"{num1} and {num2} are equal")
else:
    print(f"{num1} and {num2} are not equal")