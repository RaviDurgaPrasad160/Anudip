# 3. Write a Python program to get the key, value and item in a dictionary. 
# input:dict_num = (1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6:60) 
# Output: 
# key   value  
# 1        10 
# 2        20
# 3        30
# 5        40
# 6        50

# Define the dictionary with key-value pairs
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Print table header
print("key   value")

# Loop through key-value pairs in the dictionary
for key, value in dict_num.items():
    # Print each key and value
    print(f"{key}       {value}")