# 2. Write a Python program to Return a set of elements present in Set A or B, but not both. 
# Input:  
# set1 (10, 20, 30, 40, 50) 
# set2 (30, 40, 50, 60, 70) 
# Output: (20, 70, 10, 60)

# Define the first set with some integer elements
set1 = {10, 20, 30, 40, 50}

# Define the second set with some integer elements
set2 = {30, 40, 50, 60, 70}

# Find the symmetric difference between the two sets
# The symmetric_difference() method returns elements present in either set, but not in both
symmetric_difference = set1.symmetric_difference(set2)

# Print the result
print("Elements in Set A or B, but not both:", symmetric_difference)