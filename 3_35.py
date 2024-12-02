def transpose_matrix(m):
    # Transpose the matrix using list comprehension
    transposed = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return transposed

# Function to print a 2D array in rows and columns
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print() 