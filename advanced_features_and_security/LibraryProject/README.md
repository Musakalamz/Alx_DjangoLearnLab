# Advanced Features and Security

## Permissions and Groups Setup

### Permissions
The `Book` model in `bookshelf` app has the following custom permissions:
- `can_view`: Allows user to view the list of books.
- `can_create`: Allows user to create new books.
- `can_edit`: Allows user to edit existing books.
- `can_delete`: Allows user to delete books.

### Groups
Three groups are configured with specific permissions:

1. **Viewers**
   - Permissions: `can_view`
   - Access: Can only view the book list.

2. **Editors**
   - Permissions: `can_view`, `can_create`, `can_edit`
   - Access: Can view, create, and edit books, but cannot delete them.

3. **Admins**
   - Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`
   - Access: Full access to all book operations.

### Configuration
Groups are created and configured using the management command:
```bash
python manage.py create_groups
```
This command ensures that the groups exist and have the correct permissions assigned.

### Implementation Details
- **Models**: Permissions are defined in the `Meta` class of the `Book` model.
- **Views**: Views are protected using the `@permission_required` decorator.
  - `book_list` requires `bookshelf.can_view`
  - `book_create` requires `bookshelf.can_create`
  - `book_edit` requires `bookshelf.can_edit`
  - `book_delete` requires `bookshelf.can_delete`
