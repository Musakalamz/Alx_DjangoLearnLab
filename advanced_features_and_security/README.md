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

## Security Best Practices

### Secure Settings

- **DEBUG**: Set to `False` in production to prevent leakage of sensitive information in error pages.
- **Browser-Side Protections**:
  - `SECURE_BROWSER_XSS_FILTER = True`: Enables the X-XSS-Protection header.
  - `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking attacks by ensuring the site cannot be embedded in an iframe.
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents the browser from sniffing the content type.
- **Secure Cookies**:
  - `CSRF_COOKIE_SECURE = True`: Ensures CSRF cookies are only sent over HTTPS.
  - `SESSION_COOKIE_SECURE = True`: Ensures session cookies are only sent over HTTPS.
- **Content Security Policy (CSP)**:
  - `CSP_DEFAULT_SRC = ("'self'",)`: Restricts content sources to the origin only, mitigating XSS attacks.

### HTTPS and Secure Headers (New in Task 3)

- **HTTPS Enforcement**:
  - `SECURE_SSL_REDIRECT = True`: Redirects all non-HTTPS requests to HTTPS.
  - `SECURE_HSTS_SECONDS = 31536000`: Sets HTTP Strict Transport Security (HSTS) header to 1 year, instructing browsers to strictly use HTTPS.
  - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to all subdomains.
  - `SECURE_HSTS_PRELOAD = True`: Allows the site to be submitted to the HSTS preload list.
- **Secure Cookies (Enhanced)**:
  - `SESSION_COOKIE_SECURE = True`: Prevents session cookies from being transmitted over unencrypted connections.
  - `CSRF_COOKIE_SECURE = True`: Prevents CSRF cookies from being transmitted over unencrypted connections.
- **Secure Headers**:
  - `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-sniffing.
  - `SECURE_BROWSER_XSS_FILTER = True`: Enables XSS filtering in browsers.

### Deployment Configuration

For production deployment, ensure:

1.  **SSL/TLS Certificates**: Obtain and configure valid SSL certificates (e.g., via Let's Encrypt).
2.  **Web Server Config**: Configure Nginx or Apache to listen on port 443 and handle SSL termination.
3.  **Environment Variables**: Set `SECRET_KEY`, `DEBUG=False`, and database credentials via environment variables.

### CSRF Protection

- All forms use the `{% csrf_token %}` template tag to protect against Cross-Site Request Forgery (CSRF) attacks.

### Secure Data Access

- **SQL Injection Prevention**: Django's ORM is used for all database queries, which automatically handles parameterization and escaping of inputs.
- **Input Validation**: `BookForm` (a `ModelForm`) is used in views to validate user input before processing.
