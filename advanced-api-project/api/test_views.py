from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Book, Author

class BookAPITests(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        """
        Set up the test environment.
        Create a user, an author, and some books.
        """
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")
        
        # Create books
        self.book1 = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            publication_year=1998,
            author=self.author
        )
        
        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        # Detail, update, delete URLs require pk, will be generated in tests

    def test_list_books(self):
        """
        Test retrieving the list of books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get(self.list_url, {'publication_year': 1997})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Philosopher's Stone")

    def test_search_books(self):
        """
        Test searching books by title or author name.
        """
        response = self.client.get(self.list_url, {'search': 'Chamber'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Chamber of Secrets")

    def test_order_books(self):
        """
        Test ordering books.
        """
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Harry Potter and the Chamber of Secrets")

    def test_create_book_authenticated(self):
        """
        Test creating a book with an authenticated user.
        """
        self.client.login(username='testuser', password='password123')
        data = {
            'title': 'Harry Potter and the Prisoner of Azkaban',
            'publication_year': 1999,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'Harry Potter and the Prisoner of Azkaban')

    def test_create_book_unauthenticated(self):
        """
        Test that unauthenticated users cannot create books.
        """
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """
        Test updating a book with an authenticated user.
        """
        self.client.login(username='testuser', password='password123')
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {
            'title': 'Updated Title',
            'publication_year': 1997,
            'author': self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book_authenticated(self):
        """
        Test deleting a book with an authenticated user.
        """
        self.client.login(username='testuser', password='password123')
        url = reverse('book-delete', kwargs={'pk': self.book1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_permissions_update_delete(self):
        """
        Test permissions for update and delete endpoints.
        Unauthenticated users should be denied.
        """
        update_url = reverse('book-update', kwargs={'pk': self.book1.id})
        delete_url = reverse('book-delete', kwargs={'pk': self.book1.id})

        # Try update without login
        response = self.client.put(update_url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Try delete without login
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
