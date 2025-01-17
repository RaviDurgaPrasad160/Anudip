# 1. Write a Python program to count the occurrences of each word in a given sentence 
# string = “To change the overall look of your document. To change the look available in the gallery” 

string = "To change the overall look of your document. To change the lookavailable in the gallery"

for word in set(string.split()):
    print(word, string.count(word))