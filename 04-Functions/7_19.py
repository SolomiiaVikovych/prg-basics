def f(number):
    num_str = str(number)  # Convert the number to a string
    sum_repeats = 0
    
    # Loop through each unique digit in the number
    for digit in set(num_str):
        count = num_str.count(digit)  # Count occurrences of the digit
        if count > 1:  # Only if the digit repeats
            sum_repeats += int(digit) * (count - 1)  # Add the repeated values
    
    return sum_repeats
