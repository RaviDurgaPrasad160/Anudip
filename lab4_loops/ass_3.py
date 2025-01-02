# 3. Write a python program finding the factorial of a given number using a while loop.

number = int(input("Enter a number: "))

factorial = 1
current = number

while current > 0:
    factorial *= current  
    current -= 1          

print(f"The factorial of {number} is: {factorial}")