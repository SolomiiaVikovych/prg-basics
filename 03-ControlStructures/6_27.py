i = 6
while i >= 0:  # Continue the loop while i is greater than or equal to 0
    j = 1
    while j <= 3:  # Inner loop replaces the for loop to iterate j from 1 to 3
        print(f'{i+j}', end=' ')  # Print i+j for each value of j
        j += 1
    print()  # Move to the next line after inner loop completes
    i -= 3  # Decrease i by 3 to move to the next row (6 -> 3 -> 0)
