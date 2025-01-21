# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 
# Output: 
# UpperCase : 5 
# LowerCase : 18 
# NumberCase : 5 
# SpecialCase : 11 

def count_elements(input_string):
    uppercase = lowercase = numbers = special = 0

    for char in input_string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            numbers += 1
        else:
            special += 1  

    return uppercase, lowercase, numbers, special

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

uppercase, lowercase, numbers, special = count_elements(input_string)

print("UpperCase:", uppercase)
print("LowerCase:", lowercase)
print("NumberCase:", numbers)
print("SpecialCase:", special)

