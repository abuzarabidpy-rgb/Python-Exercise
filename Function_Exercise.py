# # # # # Function no: 01

# statement : (" True / False ") not used 
# Leap_year
def leap_year(year):
    if year % 4 ==0:
        return "Leap_year"
    else:
        return "Not a Leap_year"

print(leap_year(2021))

# #     #    <------------------>

# statement : (" True / False ") not used 
# # # # Function no: 02

# Leap_year
def leap_year(year):
    if year % 4 == 0:
        return "Leap_year"
    return "Not a Leap_year"

print(leap_year(2024))

# #     #    <------------------>

# # # Function no: 03

# statement : (" True / False ") are used
# # # Leap_year
def leap_year(year):
    if year % 4 == 0:
        return True
    return False

print(leap_year(2029))

# #     #    <------------------>

# statement : (" True / False ") are used
# # Function no: 04
# # Leap_year
def leap_year(year):
    return year % 4 == 0

print(leap_year(2031))