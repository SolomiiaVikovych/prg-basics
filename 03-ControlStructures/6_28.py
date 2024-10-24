# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Print the first 20 Fibonacci numbers
print(a, b, end=' ')  # Print the first two numbers: 0 and 1

for i in range(18):  # We already printed the first two numbers, so we need 18 more
    next_term = a + b  # Each subsequent term is the sum of the previous two
    print(next_term, end=' ')
    a, b = b, next_term  # Update a and b for the next iteration
