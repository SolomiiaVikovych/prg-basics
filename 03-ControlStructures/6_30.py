# Outer loop for rows
for row in range(7):  # There are 7 rows
    for col in range(1, 8):  # Each row has 7 columns
        # Calculate the correct number to print for each row and column
        number = row + 1 + (col - 1) * 7
        print(f'{number:2}', end=' ')  # Print the number with a minimum width of 2
    print()  # Move to the next line after printing all columns in a row



