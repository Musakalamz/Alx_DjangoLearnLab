# Create Operation

Open the Django shell:

```bash
python manage.py shell
```

Run:

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.id, book.title, book.author, book.publication_year
# Expected Output: (1, "1984", "George Orwell", 1949)
```

