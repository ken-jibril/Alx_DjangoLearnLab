from relationship_app.models import Author, Book, Library, Librarian
from django.db import IntegrityError

# Create sample data first (run once)
try:
    author1 = Author.objects.create(name="Jane Doe")
    author2 = Author.objects.create(name="John Smith")
    
    book1 = Book.objects.create(title="Django Basics", author=author1)
    book2 = Book.objects.create(title="Python Advanced", author=author1)
    book3 = Book.objects.create(title="Web Dev", author=author2)
    
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2, book3)
    
    Librarian.objects.create(name="Alice Johnson", library=library)
    print("✅ Sample data created!")
except IntegrityError:
    print("ℹ️ Sample data already exists")

print("\n" + "="*50)
print("1. Query all books by a specific author")
print("="*50)
author = Author.objects.get(name="Jane Doe")
books = author.book_set.all()  # Reverse ForeignKey lookup
for book in books:
    print(f"📚 {book.title} by {book.author.name}")

print("\n" + "="*50)
print("2. List all books in a library")
print("="*50)
library = Library.objects.get(name="Central Library")
books = library.books.all()  # Direct ManyToMany access
for book in books:
    print(f"📚 {book.title}")

print("\n" + "="*50)
print("3. Retrieve the librarian for a library")
print("="*50)
librarian = library.librarian  # Direct OneToOne access
print(f"👩‍💼 {librarian.name} manages {library.name}")
