# main.py

import calendar_utils  # Import the module you just created

# Get month number from the user
month_number = int(input("Enter month number: "))

# Call the month function from the imported module
month_name = calendar_utils.month(month_number)

# Print the result
print(f"The name of month {month_number} is {month_name}")
