# Function to read a string from the keyboard
def input_string(message):
    user_input = input(message)  # Simply takes the input as a string
    return user_input

# Function to read an integer from the keyboard
def input_integer(message):
    while True:
        try:
            user_input = int(input(message))  # Converts input to integer
            return user_input
        except ValueError:
            print("Please enter a valid integer.")

# Function to read a real (float) number from the keyboard
def input_real(message):
    while True:
        try:
            user_input = float(input(message))  # Converts input to float
            return user_input
        except ValueError:
            print("Please enter a valid real number.")

# Function to read a boolean value from the keyboard
def input_boolean(message):
    while True:
        user_input = input(message + " (y/n): ")
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print("Please enter 'y' for Yes or 'n' for No.")


            
