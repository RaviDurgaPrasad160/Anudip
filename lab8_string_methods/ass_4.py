# 4. Write a Python Count vowels in a string 
# input= “Welcome to Python Assignment” 
# Output: Total vowels are: 8

input_string = "Welcome to Python Assignment"

vowels = "aeiouAEIOU"
vowel_count = 0

for char in input_string:
    if char in vowels:
        vowel_count += 1

print("Total vowels are:", vowel_count)
