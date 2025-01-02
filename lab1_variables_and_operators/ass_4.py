# 4. Python program to find the area of a triangle whose sides are given

# Input the sides of the triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Display the result
print(f"The area of the triangle with sides {a}, {b}, {c} is: {area}")