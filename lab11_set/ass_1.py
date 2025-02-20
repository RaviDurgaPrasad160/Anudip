# 1. Write a Python program to Get Only unique items from two sets. 
# Input: 
# set1 (10, 20, 30, 40, 50) 
# set2 (30, 40, 50, 60, 70) 
# Output: (70, 40, 10, 50, 20, 60, 30) 

# Define the first set with some integer elements
set1 = {10, 20, 30, 40, 50}

# Define the second set with some integer elements
set2 = {30, 40, 50, 60, 70}

# Combine the two sets using the union() method, which gives all unique items from both sets
unique_items = set1.union(set2)

# Print the result
print("Unique items from both sets:", unique_items)