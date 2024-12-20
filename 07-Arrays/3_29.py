# Function to create a 2D array of size x by y filled with zeros
def create_2d_arr(x, y):
    # Creating a 2D array with dimensions x by y, filled with zeros
    return [[0 for _ in range(y)] for _ in range(x)]

# Create a 3 by 5 2D array using the function
array = create_2d_arr(3, 5)

# Print the created 2D array
for row in array:
    print(row)
