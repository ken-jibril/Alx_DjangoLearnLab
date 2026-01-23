## Retrieve Book

### Command
```python
book = Book.objects.get(title="1984")
book.id, book.title, book.author, book.published_date
