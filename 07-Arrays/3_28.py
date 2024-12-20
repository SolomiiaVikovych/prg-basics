# Define the 2D array
array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

# Initialize a variable to store the sum of the last column
sum_last_column = 0

# Iterate through each row and add the last column value to the sum
for row in array:
    sum_last_column += row[-1]

# Print the result
print("Sum of values in the last column:", sum_last_column)
