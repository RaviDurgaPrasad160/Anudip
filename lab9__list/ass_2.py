# 2. Write a Python program to get the largest and smallest number from a list without builtin functions. 

numbers = [3, 7, 1, 9, 4, -2, 0]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number is:", largest)
print("Smallest number is:", smallest)
