# 2. Using input function take two number and then swap the number 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Swaping
temp = num1
num1 = num2
num2 = temp

print(f"After swapping: num1 = {num1}, num2 = {num2}")