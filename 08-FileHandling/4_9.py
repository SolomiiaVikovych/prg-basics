import csv

def extract_graphic_designers(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            
            print("GRAPHIC DESIGNERS")
            print("=================")
            
            # Iterate through rows to find 'Graphic Designer'
            for row in reader:
                if row.get('Job Title') == 'Graphic Designer':
                    first_name = row.get('First Name')
                    last_name = row.get('Last Name')
                    email = row.get('Email')
                    
                    # Print the desired information
                    if first_name and last_name and email:
                        print(f"{first_name} {last_name},{email}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

file_name = 'it_company.csv'
extract_graphic_designers(file_name)