# 2. Write a Python script to concatenate the following dictionaries to create a new one. Sample Dictionary: 
# dic1={1:10, 2:20} 
# dic2={3:30, 4:40}
# dic3={5:50,6:60} 
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Define the first dictionary
dic1 = {1: 10, 2: 20}

# Define the second dictionary
dic2 = {3: 30, 4: 40}

# Define the third dictionary
dic3 = {5: 50, 6: 60}

# Initialize an empty dictionary to store the result
result = {}

# Use the update() method to merge dic1 into the result dictionary
result.update(dic1)

# Use the update() method to merge dic2 into the result dictionary
result.update(dic2)

# Use the update() method to merge dic3 into the result dictionary
result.update(dic3)

# Print the final concatenated dictionary
print("Concatenated dictionary:", result)