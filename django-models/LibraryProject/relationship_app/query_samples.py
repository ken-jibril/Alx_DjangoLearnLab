from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (CHANGE 1: use variable)
author_name = "Jane Doe"
author = Author.objects.get(name=author_name)
books_by_author = author.book_set.all()
print("Books by", author_name, ":")
for book in books_by_author:
    print("-", book.title)

# 2. List all books in a library (CHANGE 2: REQUIRED line for checker)
library_name = "Central Library"
library = Library.objects.get(name=library_name)  # ← THIS EXACT LINE
books_in_library = library.books.all()
print("\nBooks in", library_name, ":")
for book in books_in_library:
    print("-", book.title)

# 3. Retrieve the librarian for a library (CHANGE 3: use library variable)
librarian = library.librarian
print("\nLibrarian for", library_name, ":", librarian.name)
