# Stack implementation using a list
stack = []

# Input the natural number
number = int(input("Enter a natural number: "))

# Handle special case for zero
if number == 0:
    print("Binary representation: 0")
else:
    # Convert to binary
    while number > 0:
        remainder = number % 2
        stack.append(remainder)  # Push the remainder onto the stack
        number //= 2  # Integer division by 2

    # Pop and display values from the stack
    print("Binary representation: ", end="")
    while stack:
        print(stack.pop(), end="")  # Pop and print each bit
    print()  # Add a newline after the binary number

