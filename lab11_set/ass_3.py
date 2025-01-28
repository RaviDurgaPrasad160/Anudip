# 3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements.  
# Input: 
# set1 (10, 20, 30, 40, 50) 
# set2 (60, 70, 80, 90, 10)  
# Output: {10}  

# Define the first set with some integer elements
set1 = {10, 20, 30, 40, 50}

# Define the second set with some integer elements
set2 = {60, 70, 80, 90, 10}

# Find the common elements between the two sets using the intersection() method
common_elements = set1.intersection(set2)

# Check if there are any common elements
if common_elements:
    # If common elements exist, print them
    print("Common elements:", common_elements)
else:
    # If no common elements exist, display a message
    print("No common elements.")