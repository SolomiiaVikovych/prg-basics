

import text_utils  # Import the module with the counting function

# Define the text to analyze
text = "You never get a second chance to make a first impression"
letter_to_count = 'e'

# Call the count_letter function and store the result
count = text_utils.count_letter(text, letter_to_count)

# Display the result
print(f"The number of letter '{letter_to_count}': {count}")
