from ebook import EBook

def main():
    book = EBook("The Great Gatsby", "F. Scott Fitzgerald", 180)
    book.show_status()
    book.open_book()
    book.show_status()
    book.next_page()
    book.next_page()
    book.show_status()
    book.close_book()
    book.show_status()
    book.next_page()

if __name__ == "__main__":
    main()
