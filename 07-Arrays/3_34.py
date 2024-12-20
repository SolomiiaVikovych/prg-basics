# Function to create an identity matrix of size n
def identity_matrix(n):
    # Initialize a 2D array with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    # Set 1s along the diagonal
    for i in range(n):
        matrix[i][i] = 1
    return matrix

# Function to print a 2D array in rows and columns
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()  # Add a blank line between matrices

# Program to print identity matrices with dimensions 3, 5, and 8
print("Identity Matrix (3x3):")
print_matrix(identity_matrix(3))

print("Identity Matrix (5x5):")
print_matrix(identity_matrix(5))

print("Identity Matrix (8x8):")
print_matrix(identity_matrix(8))
