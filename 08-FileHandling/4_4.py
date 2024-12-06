# Program to read and display 5 lines at a time from a CSV file
def display_file_in_chunks(file_name, chunk_size=5):
    try:
        with open(file_name, 'r') as file:
            while True:
                # Read the next chunk of lines
                lines = [file.readline() for _ in range(chunk_size)]
                
                # Stop if no lines are left to read
                if not any(lines):
                    print("End of file reached.")
                    break
                
                # Print the current chunk
                for line in lines:
                    if line.strip():  # Avoid printing empty lines
                        print(line.strip())
                
                # Wait for the user to press Enter
                input("Press Enter key to continue...")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    

# Usage
file_name = "it_company.csv"
display_file_in_chunks(file_name)

