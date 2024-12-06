import csv

# Function to read books from CSV file
def read_books_from_csv(file_name):
    books = []
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    return books

# Function to write books to a text file based on genre
def write_books_to_file(genre, books):
    # Define a mapping of genre to filenames
    genre_file_map = {
        'Fiction': 'books_fiction.txt',
        'Dystopian': 'books_dystopian.txt',
        'Classic': 'books_classic.txt',
        'Romance': 'books_romance.txt',
        'Adventure': 'books_adventure.txt',
        'Historical': 'books_historical.txt',
        'Modernist': 'books_modernist.txt',
        'Epic': 'books_epic.txt',
        'Gothic': 'books_gothic.txt',
        'Psychological': 'books_psychological.txt',
        'Philosophical': 'books_philosophical.txt',
        'Fantasy': 'books_fantasy.txt',
        'Literary': 'books_literary.txt',
        'Southern Gothic': 'books_southern_gothic.txt',
        'Magic Realism': 'books_magic_realism.txt',
        'Gothic Horror': 'books_gothic_horror.txt',
        'Novella': 'books_novella.txt',
        'Satire': 'books_satire.txt',
        'Science Fiction': 'books_science_fiction.txt',
        'Post-apocalyptic': 'books_post_apocalyptic.txt',
        'Horror': 'books_horror.txt'
    }

    # Determine the filename for the genre
    file_name = genre_file_map.get(genre)
    if not file_name:
        print(f"Error: No file mapping found for genre '{genre}'.")
        return

    # Write the books of the specified genre to the corresponding file
    with open(file_name, 'w') as file:
        for book in books:
            if book['Genre'] == genre:
                file.write(f"{book['Title']},{book['Author']},{book['Year']},{book['Genre']}\n")
    print(f"Books in the genre '{genre}' have been written to {file_name}.")

# Main function to process books and organize them by genre
def organize_books_by_genre(input_file):
    # Read books from the input CSV file
    books = read_books_from_csv(input_file)
    
    if not books:
        print("No books found in the file.")
        return
    
    # Process and write books to their corresponding genre files
    genres = set(book['Genre'] for book in books)  # Get all unique genres
    for genre in genres:
        write_books_to_file(genre, books)

# Run the program with the books.csv file
input_file = 'books.csv'
organize_books_by_genre(input_file)
