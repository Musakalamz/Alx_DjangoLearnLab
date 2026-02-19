Social Media API - Project Setup and Authentication

Overview

This Django project provides the foundation for a social media API built with Django REST Framework. It includes a custom user model and token based authentication.

Project Structure

- social_media_api: Django project configuration
- accounts: App that contains the custom user model and authentication endpoints

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
- profile_picture: URL to the user profile image
- followers: Many to many relationship to other users

Authentication

Authentication is handled using Django REST Framework token authentication.

Installed apps in settings include:

- rest_framework
- rest_framework.authtoken
- accounts

AUTH_USER_MODEL is set to accounts.User and REST_FRAMEWORK is configured to use token authentication by default.

API Endpoints

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
