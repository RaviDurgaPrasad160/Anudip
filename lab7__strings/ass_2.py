# 2. Write a Python program to remove a newline in Python 
# String = "\nBest \nDeeptech \nPython \nTraining\n"

string = "\nBest \nDeeptech \nPython \nTraining\n"
new_str = ''

for char in string:
    if char not in '\n':
        new_str += char

print(new_str)