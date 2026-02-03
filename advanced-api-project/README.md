# Advanced API Project

## Overview
This project implements an advanced API for managing Books and Authors using Django REST Framework. It includes comprehensive CRUD operations, filtering, searching, ordering, and permission handling.

## Testing Strategy
The project uses Django's built-in testing framework (`APITestCase`) to ensure the reliability and security of the API endpoints. The tests are located in `api/test_views.py`.

### Key Areas Tested
1.  **CRUD Operations**:
    *   **Create**: Verifies that authenticated users can create books and unauthenticated users cannot.
    *   **Read**: Verifies retrieval of book lists and details.
    *   **Update**: Verifies that only authenticated users can update books.
    *   **Delete**: Verifies that only authenticated users can delete books.

2.  **Filtering, Searching, and Ordering**:
    *   **Filtering**: Tests filtering books by `publication_year`.
    *   **Searching**: Tests searching books by title or author name.
    *   **Ordering**: Tests ordering books by fields like `publication_year`.

3.  **Permissions**:
    *   Ensures `IsAuthenticatedOrReadOnly` is enforced for list/detail views.
    *   Ensures `IsAuthenticated` is enforced for create/update/delete views.

### Running Tests
To run the test suite, execute the following command from the project root directory:

```bash
python manage.py test api
```

### Test Cases Breakdown
*   `test_list_books`: Checks if the list endpoint returns status 200 and the correct number of books.
*   `test_filter_books_by_publication_year`: Verifies filtering functionality.
*   `test_search_books`: Verifies search functionality.
*   `test_order_books`: Verifies ordering functionality.
*   `test_create_book_authenticated`: Ensures authenticated users can create books (Status 201).
*   `test_create_book_unauthenticated`: Ensures unauthenticated users are forbidden (Status 403).
*   `test_update_book_authenticated`: Verifies successful updates by authenticated users.
*   `test_delete_book_authenticated`: Verifies successful deletion by authenticated users.
*   `test_permissions_update_delete`: explicitly checks that unauthenticated requests to update/delete endpoints are rejected.
