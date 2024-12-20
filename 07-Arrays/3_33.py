arr = [[1,3,4,2,6],[5,4,3,2,1],[6,7,8,9,0] ]

def print_array(array, message):
    print(message)
    for row in array:
        print(row)
    print()

# Print the original array
print_array(arr, "Original Array:")

# Swap the first and last columns
for row in arr:
    row[0], row[-1] = row[-1], row[0]  # Swap first and last column

# Print the modified array
print_array(arr, "Array After Swapping First and Last Columns:")