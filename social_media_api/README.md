Social Media API - Project Setup and Authentication

Overview

This Django project provides the foundation for a social media API built with Django REST Framework. It includes a custom user model and token based authentication.

Project Structure

- social_media_api: Django project configuration
- accounts: App that contains the custom user model and authentication endpoints
- posts: App that contains post and comment models and API endpoints
- notifications: App that contains notification model, serializers, and API endpoint

Requirements

- Python 3
- Django
- Django REST Framework

Installation

1. Navigate to the project directory:

   cd social_media_api

2. Apply migrations:

   python manage.py migrate

3. Create a superuser (optional but recommended for admin access):

   python manage.py createsuperuser

4. Run the development server:

   python manage.py runserver

Custom User Model

The project uses a custom user model defined in the accounts app.

- bio: Text field for user biography
- profile_picture: Image field stored under media/profile_pictures
- followers: Many to many relationship to other users

Authentication

Authentication is handled using Django REST Framework token authentication.

Installed apps in settings include:

- rest_framework
- rest_framework.authtoken
- accounts
- posts
- notifications

AUTH_USER_MODEL is set to accounts.User and REST_FRAMEWORK is configured to use token authentication by default.

Authentication API Endpoints

Base path for authentication endpoints:

- /accounts/

Available endpoints:

- POST /accounts/register/
  - Registers a new user and returns a token
  - Request body fields: username, email, password, bio, profile_picture

- POST /accounts/login/
  - Authenticates a user and returns a token
  - Request body fields: username, password

- GET /accounts/profile/
  - Returns the authenticated user profile
  - Requires Authorization header with token

- PUT or PATCH /accounts/profile/
  - Updates the authenticated user profile
  - Requires Authorization header with token

Follow management endpoints:

- POST /accounts/follow/{user_id}/
  - Follow the user with the given ID
  - Requires Authorization header with token

- POST /accounts/unfollow/{user_id}/
  - Unfollow the user with the given ID
  - Requires Authorization header with token

Posts and Comments API Endpoints

Base path for posts and comments endpoints:

- /api/

Post endpoints:

- GET /api/posts/
  - List posts with pagination
  - Supports search by title or content using ?search= query parameter

- POST /api/posts/
  - Create a new post for the authenticated user
  - Request body fields: title, content

- GET /api/posts/{id}/
  - Retrieve a single post with its comments

- PUT or PATCH /api/posts/{id}/
  - Update a post (only the author can update)

- DELETE /api/posts/{id}/
  - Delete a post (only the author can delete)

Comment endpoints:

- GET /api/comments/
  - List comments with pagination

- POST /api/comments/
  - Create a new comment for a post
  - Request body fields: post, content

- GET /api/comments/{id}/
  - Retrieve a single comment

- PUT or PATCH /api/comments/{id}/
  - Update a comment (only the author can update)

- DELETE /api/comments/{id}/
  - Delete a comment (only the author can delete)

Feed endpoint:

- GET /api/feed/
  - Returns paginated posts from users the authenticated user follows
  - Ordered by creation date (most recent first)

Like endpoints:

- POST /api/posts/{id}/like/
  - Like the specified post
  - Requires Authorization header with token

- POST /api/posts/{id}/unlike/
  - Unlike the specified post
  - Requires Authorization header with token

Notifications API Endpoints

Base path for notifications:

- /notifications/

Notification endpoint:

- GET /notifications/
  - Returns notifications for the authenticated user
  - Unread notifications are listed first

Authentication Header

Include the token in the Authorization header for protected endpoints:

Authorization: Token your_token_here

Testing with HTTP client

You can use tools like Postman or curl to test the endpoints.

Example curl requests:

- Register:

  curl -X POST http://127.0.0.1:8000/accounts/register/ -H "Content-Type: application/json" -d "{\"username\": \"user1\", \"email\": \"user1@example.com\", \"password\": \"StrongPass123\"}"

- Login:

  curl -X POST http://127.0.0.1:8000/accounts/login/ -H "Content-Type: application/json" -d "{\"username\": \"user1\", \"password\": \"StrongPass123\"}"

- Get profile:

  curl -X GET http://127.0.0.1:8000/accounts/profile/ -H "Authorization: Token your_token_here"

- List posts:

  curl -X GET http://127.0.0.1:8000/api/posts/

- Search posts:

  curl -X GET "http://127.0.0.1:8000/api/posts/?search=hello"

- Create post:

  curl -X POST http://127.0.0.1:8000/api/posts/ -H "Authorization: Token your_token_here" -H "Content-Type: application/json" -d "{\"title\": \"My first post\", \"content\": \"Post content\"}"

- Create comment:

  curl -X POST http://127.0.0.1:8000/api/comments/ -H "Authorization: Token your_token_here" -H "Content-Type: application/json" -d "{\"post\": 1, \"content\": \"Nice post\"}"

- Follow user:

  curl -X POST http://127.0.0.1:8000/accounts/follow/2/ -H "Authorization: Token your_token_here"

- Unfollow user:

  curl -X POST http://127.0.0.1:8000/accounts/unfollow/2/ -H "Authorization: Token your_token_here"

- Get feed:

  curl -X GET http://127.0.0.1:8000/api/feed/ -H "Authorization: Token your_token_here"

- Like post:

  curl -X POST http://127.0.0.1:8000/api/posts/1/like/ -H "Authorization: Token your_token_here"

- Unlike post:

  curl -X POST http://127.0.0.1:8000/api/posts/1/unlike/ -H "Authorization: Token your_token_here"

- Get notifications:

  curl -X GET http://127.0.0.1:8000/notifications/ -H "Authorization: Token your_token_here"

Production Configuration and Deployment

The project is configured for production-ready deployment:

- DEBUG is set to False in settings.py for production safety.
- ALLOWED_HOSTS is read from the DJANGO_ALLOWED_HOSTS environment variable (comma separated), defaulting to localhost and 127.0.0.1.
- DATABASES can be configured via environment variables for a PostgreSQL database:
  - DB_ENGINE (default: django.db.backends.postgresql)
  - DB_NAME
  - DB_USER
  - DB_PASSWORD
  - DB_HOST (default: localhost)
  - DB_PORT (default: 5432)
- If DB_NAME is not set, the project falls back to SQLite for local development.
- Static files:
  - STATIC_URL is set to /static/
  - STATIC_ROOT is set to staticfiles/ for use with collectstatic
- Media files:
  - MEDIA_URL is set to /media/
  - MEDIA_ROOT is set to media/
- Optional AWS S3 storage:
  - When AWS_STORAGE_BUCKET_NAME is provided, DEFAULT_FILE_STORAGE uses S3 via django-storages.
  - Related AWS environment variables are read for credentials and region.
- Security settings:
  - SECURE_BROWSER_XSS_FILTER and SECURE_CONTENT_TYPE_NOSNIFF are enabled when DEBUG is False.
  - X_FRAME_OPTIONS is set to DENY.
  - SECURE_SSL_REDIRECT can be enabled via DJANGO_SECURE_SSL_REDIRECT.
  - SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE are enabled when DEBUG is False.

To deploy:

1. Configure environment variables for SECRET_KEY, database, allowed hosts, and security options.
2. Run migrations: python manage.py migrate
3. Collect static files: python manage.py collectstatic --noinput
4. Start the application using a WSGI server such as Gunicorn, and place a reverse proxy like Nginx in front if needed.
