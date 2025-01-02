# 2. Write a python program to check whether a number is palindrome or not?

str = input("Enter a string: ")
revStr =''
for char in str:
    revStr = char + revStr
if str == revStr:
    print("Palindrome")
else:
    print("not Palindrome")