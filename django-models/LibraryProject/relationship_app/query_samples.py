from relationship_app.models import Author, Book, Library, Librarian
from django.db import IntegrityError

# Create sample data
try:
    author1 = Author.objects.create(name="Jane Doe")
    author2 = Author.objects.create(name="John Smith")
    
    book1 = Book.objects.create(title="Django Basics", author=author1)
    book2 = Book.objects.create(title="Python Advanced", author=author1)
    book3 = Book.objects.create(title="Web Dev", author=author2)
    
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2, book3)
    
    Librarian.objects.create(name="Alice Johnson", library=library)
except IntegrityError:
    pass

# 1. Query all books by a specific author - REQUIRED .filter()
author_name = "Jane Doe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by", author_name, ":")
for book in books_by_author:
    print("-", book.title)

# 2. List all books in a library - REQUIRED .get()
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("\nBooks in", library_name, ":")
for book in books_in_library:
    print("-", book.title)

# 3. Retrieve the librarian - REQUIRED Librarian.objects.get()
librarian = Librarian.objects.get(library=library)
print("\nLibrarian for", library_name, ":", librarian.name)
