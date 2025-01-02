# 2. Declare two variables and print that which variable is largest using ternary operators # 

# taking input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Use the ternary operator to determine the largest
largest = a if a > b else b

# Print the result
print(f"The largest number is: {largest}")
