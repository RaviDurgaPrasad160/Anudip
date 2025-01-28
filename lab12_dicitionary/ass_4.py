# 4.Write a Python program to get the key, value and item in a dictionary. 
# Input: input_dict = (1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60) 

# Output: 
# Dictionary with Empty Items Dropped: 
# {1: 10, 2: 20, 4: 40, 6: 60}

# Define the dictionary with some keys having None as values
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

# Initialize an empty dictionary to store filtered key-value pairs
filtered_dict = {}

# Loop through key-value pairs in the dictionary
for key, value in input_dict.items():
    # Add key-value pairs to filtered_dict if value is not None
    if value is not None:
        filtered_dict.update({key: value})

# Print the filtered dictionary without None values
print("Dictionary with Empty Items Dropped:")
print(filtered_dict)