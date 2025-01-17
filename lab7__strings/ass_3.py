# 3. Write a Python program to reverse words in a string 
# String = “Deeptech Python Training” 

string = 'Deeptech Python Training'

def rev_word(word):
    return word[ : : -1]

rev_word_str = ''

for word in string.split():
    rev_word_str += rev_word(word) + ' '

print(rev_word_str)