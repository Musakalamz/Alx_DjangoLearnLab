# Delete Operation

Open the Django shell:

```bash
python manage.py shell
```

Run:

```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
Book.objects.count()
# Expected Output: 0
```

