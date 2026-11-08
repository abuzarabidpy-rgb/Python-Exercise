# Enumerate_Function:

#  without using enumerate function:
names = ['Abuzar', 'Irfan', 'Anas']
# pos = 0
# for name in names:
#     print(f"{pos} -----> {name}")
#     pos += 1

# with Enumerate function:

for pos, name in enumerate(names):
     print(f"{pos} -----> {name}")

# find position with for loop:
def find_pos(l, target):
     for pos, name in enumerate(l):
          if name == target:
               return pos
     return -1

print(find_pos(names, 'Anass'))