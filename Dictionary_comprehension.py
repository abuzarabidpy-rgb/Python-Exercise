# dictionary_comprehension :
square = {f"square of {num} is":num**2 for num in range(1, 11)}
for j,v in square.items():
    print(f"{j} : {v}")
    
# character_count:
name = "Abuzar"
word_count = {char:name.count(char) for char in name}
for j,v in word_count.items():
    print(f"{j} : {v}")
    