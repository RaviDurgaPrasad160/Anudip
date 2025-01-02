# 1. Write a python program to reverse a number using a while loop. 

number = int(input("Enter a number: "))

reversed_number = 0

while number > 0:
    digit = number % 10 
    reversed_number = reversed_number * 10 + digit 
    number = number // 10 

print(f"The reversed number is: {reversed_number}")