# shopping list file name
shopping_list = 'shopping_list.txt'

# Adds product name at the end of the shopping list
def add_product(file_name, product_name):
    # Open the file in append mode
    with open(file_name, 'a') as file:
        file.write(product_name + '\n')  # Write the product name and add a newline

# Takes product names from the keyboard
product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == "0":
        print("Shopping list complete.")
        break  # Exit the loop if the user enters '0'
    else:
        add_product(shopping_list, product)  # Add the product to the file
        print(f'"{product}" added to the shopping list.')

