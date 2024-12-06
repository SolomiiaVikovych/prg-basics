def count_file_details(file_name):
    try:
        # Open the file for reading
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        # Calculate the details
        num_lines = len(lines)
        num_characters = sum(len(line) for line in lines)
        num_words = sum(len(line.split()) for line in lines)
        
        # Print the results
        print(f"File: {file_name}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_characters}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    

# User input for the file name
file_name = input("Enter the name of the text file: ")
count_file_details(file_name)
