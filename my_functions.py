import json
from book import Book

# making a load books func before save func

# loading books function
def load_books():
    try:
        file = open("books.dat", "r")
        books_dict = json.loads(file.read())
        books = []
        # id, name, description, isbn, page_count, issued, author, year
        for book in books_dict:
            book_obj = Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
            books.append(book_obj)
        return books
    except:
        return []

# save books function
def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    with open("books.dat", "w") as file:
        file.write(json.dumps(json_books, indent=4))

# add book function
def add_book(book):
    books = load_books()
    new_book = Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
    save_books([*books, assign_valid_id(books, new_book)])

# valid id method
def assign_valid_id(books, new_book):
    book_ids = []
    for book in books:
        book_ids.append(int(book.id))
    if list(filter(lambda id: id == int(new_book.id), book_ids)) == []:
        return new_book
    else:
        new_book.id = int(max(book_ids) + 1)
        return new_book
    
def get_issued_books():
    books = load_books()
    return list(filter(lambda book: book.issued == True, books))

def get_unissued_books():
    books = load_books()
    return list(filter(lambda book: book.issued == False, books))

def find_book(book_id):
    books = load_books()
    for book in books:
        if int(book.id) == int(book_id):
            return book
    return None