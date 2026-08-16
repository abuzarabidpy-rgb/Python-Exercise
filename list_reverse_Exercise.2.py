
def reverse_list(l):
    reverse = []
    for i in l:
        reverse.append(i[::-1])
    return reverse

words = ['abc', 'tuv', 'xyz']
print(reverse_list(words))