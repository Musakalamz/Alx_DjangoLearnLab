from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class ExampleForm(forms.Form):
    """
    This is an example form for demonstration purposes.
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
