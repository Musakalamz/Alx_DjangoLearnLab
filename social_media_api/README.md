Social Media API - Project Setup and Authentication

Overview

This Django project provides the foundation for a social media API built with Django REST Framework. It includes a custom user model and token based authentication.

Project Structure

- social_media_api: Django project configuration
- accounts: App that contains the custom user model and authentication endpoints
- posts: App that contains post and comment models and API endpoints

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
