numbers = [1, 2, 3, 4, 5, 6, 7]

def even_odd_filter(l):
    even = []
    odd = []
    for i in l:
        if i % 2 ==0:
            even.append(i)
        else:
            odd.append(i)
    output = [even, odd]
    return output

print(even_odd_filter(numbers))

       
