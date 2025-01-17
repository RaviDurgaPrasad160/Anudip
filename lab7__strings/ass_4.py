# 4. Write a Python program to count and display the vowels of a given text 
# String=”Welcome to python Training”

string = 'Welcome to python Training'

vowels = 'aeiou'
vowel_cnt = {}
for char in string:
    if char.lower() in vowel_cnt:
        vowel_cnt[char.lower()] += 1
    elif char.lower() in vowels:
        vowel_cnt[char.lower()] = 1

print(vowel_cnt)