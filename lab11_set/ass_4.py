# 4.Write a Python program to Remove items from set1 that are not common to both set1 and set2. 
# Input: 
# set1 (10, 20, 30, 40, 50) 
# set2 (30, 40, 50, 60, 70) 
# Output: (40, 50, 30)

# Define the first set with some integer elements
set1 = {10, 20, 30, 40, 50}

# Define the second set with some integer elements
set2 = {30, 40, 50, 60, 70}

# Update set1 to contain only the items that are common to both sets
# Using set comprehension to filter elements present in both sets
set1 = {item for item in set1 if item in set2}

# Print the resulting set with common elements
print("Items common to both sets:", set1)