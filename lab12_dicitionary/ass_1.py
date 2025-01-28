# Write a Python program and calculate the mean of the below dictionary. 
# test_dict={"A": 6, "B": 9, "C": 5, "D": 7, "E":4} 
# Output: 6.2 

# Define the dictionary with key-value pairs
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Initialize a variable to store the sum of all values
sum = 0

# Get the number of observations (i.e., the number of items in the dictionary)
no_of_observations = len(test_dict)

# Loop through the values of the dictionary and calculate the total sum
for value in test_dict.values():
    sum += value

# Calculate the mean by dividing the total sum by the number of observations
mean = sum / no_of_observations

# Print the calculated mean
print("Mean of the dictionary values:", mean)
