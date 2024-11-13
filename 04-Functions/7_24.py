def f(expression):
    # Initialize result to 0 and set default operator to '+'
    result = 0
    current_operator = '+'
    
    for char in expression:
        if char.isdigit():  # Check if the character is a digit
            number = int(char)
            # Apply the current operator to the number
            if current_operator == '+':
                result += number
            elif current_operator == '-':
                result -= number
        else:
            # Update the operator when a '+' or '-' is encountered
            current_operator = char

    return result

# Example usage:
print(f("2+3"))       # Output: 5
print(f("3+8+1"))     # Output: 12
print(f("2+3-4+5-0")) # Output: 6
