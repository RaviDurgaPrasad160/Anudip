# 2. Python program to check if the given string is a palindrome 

my_str = input('Enter a string in lowercase: ')

rev_str = ''

for char in my_str:
    rev_str = char + rev_str

if my_str == rev_str:
    print(f'{my_str} is a palindrome string')
else:
    print(f'{my_str} is not a palindrome string')