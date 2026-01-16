from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView

from .models import Book, Library


def list_books(request):
    books = Book.objects.all()
    lines = [f"{book.title} by {book.author.name}" for book in books]
    if not lines:
        lines.append("No books available.")
    return HttpResponse("\n".join(lines))


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm(request)
    return render(request, 'relationship_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
