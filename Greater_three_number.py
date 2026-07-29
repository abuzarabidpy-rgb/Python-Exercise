# Greatest_three_number:

def greater_three(a,b,c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c

num1 = int(input("enter a first number :"))
num2 = int(input("enter a second number :"))
num3 = int(input("enter a third number :"))
greater = greater_three(num1,num2,num3)
print(f"{greater} is greater")
