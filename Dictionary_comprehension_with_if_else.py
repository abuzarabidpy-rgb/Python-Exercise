# Dictionary_comprehension_with_if_else :

# odd_even_numbers:
odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1, 11)}
for j,v in odd_even.items():
    print(f"{j} : {v}")


