def f(dice):
    max_digit = dice[0]  # Store the digit with the longest consecutive run
    max_count = 1        # Track the longest consecutive count for any digit
    current_digit = dice[0]
    current_count = 1
    
    # Loop through the sequence starting from the second character
    for i in range(1, len(dice)):
        if dice[i] == current_digit:
            current_count += 1  # Increase the count if the same digit repeats
        else:
            # Check if the current sequence is the longest
            if current_count > max_count:
                max_count = current_count
                max_digit = current_digit
            # Reset counters for the new digit
            current_digit = dice[i]
            current_count = 1
    
    # Final check for the last sequence
    if current_count > max_count:
        max_digit = current_digit
    
    return int(max_digit)

# Test cases
print(f("5233165554211"))  # Expected output: 5
print(f("2133"))           # Expected output: 3

