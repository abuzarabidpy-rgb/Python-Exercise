# reverse_method_in_list:

numbers = [1, 2, 3, 4]
def reverse_list(l):
    reverse = []
    for i in range(len(l)):
        popped_item = l.pop()
        reverse.append(popped_item)
    return reverse

print(reverse_list(numbers))
