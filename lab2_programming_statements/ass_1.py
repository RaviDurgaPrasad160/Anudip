# 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

# Take input from the user
number = int(input("Enter a number: "))

# to check number is even or odd
result = "Even" if number % 2 == 0 else "Odd"

print(f"The number {number} is {result}.")