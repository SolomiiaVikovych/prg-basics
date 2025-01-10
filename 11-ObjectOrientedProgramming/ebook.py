class EBook:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 1
        self.is_open = False

    def open_book(self):
        self.is_open = True

    def close_book(self):
        self.is_open = False

    def next_page(self):
        if self.is_open:
            if self.current_page < self.total_pages:
                self.current_page += 1
            else:
                print("You are on the last page.")
        else:
            print("The book is closed. Open the book to read.")

    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
            else:
                print("You are on the first page.")
        else:
            print("The book is closed. Open the book to read.")

    def show_status(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Pages: {self.total_pages}")
        print(f"Current Page: {self.current_page}")
        print(f"Book is {'open' if self.is_open else 'closed'}")
