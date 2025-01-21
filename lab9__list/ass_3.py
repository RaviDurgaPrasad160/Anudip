# 3. Write a Python program to find duplicate values from a list and display those. 

numbers = [1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 6]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate values are:", list(duplicates))
