# Update Operation

Open the Django shell:

```bash
python manage.py shell
```

Run:

```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
book.id, book.title, book.author, book.publication_year
# Expected Output: (1, "Nineteen Eighty-Four", "George Orwell", 1949)
```

