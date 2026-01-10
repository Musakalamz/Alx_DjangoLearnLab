# CRUD Operations Summary

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.id, book.title, book.author, book.publication_year
# Output: (1, "1984", "George Orwell", 1949)
```

## Retrieve
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.id, book.title, book.author, book.publication_year
# Output: (1, "1984", "George Orwell", 1949)
```

## Update
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
book.id, book.title, book.author, book.publication_year
# Output: (1, "Nineteen Eighty-Four", "George Orwell", 1949)
```

## Delete
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
Book.objects.count()
# Output: 0
```

