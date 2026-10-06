def power_to(num, *args):
    if args:
        return [num**i for i in args]
    else:
        return "You didn't pass any list of powers"

nums = [2, 3, 6]
print(power_to(2, *nums))






    