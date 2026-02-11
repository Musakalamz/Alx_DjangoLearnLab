# Django Blog Project

A modern, feature-rich Django blog application with user authentication, post management, comment system, tagging, and search functionality.

## Features

### 🔐 User Authentication
- **Registration**: Users can create accounts with email verification.
- **Login/Logout**: Secure session management.
- **Profile Management**: Users can update their profile information.

### 📝 Blog Management (CRUD)
- **Create**: Authenticated users can write and publish posts.
- **Read**: Browse all posts or view detailed content.
- **Update/Delete**: Authors can edit or remove their own posts.

### 💬 Comment System
- **Interactive**: Users can leave comments on posts to foster discussion.
- **Management**: Comment authors can edit or delete their own feedback.

### 🏷️ Tagging & Categorization
- **Organized**: Posts can be tagged with multiple keywords.
- **Discovery**: Click on any tag to find all related posts.
- **django-taggit**: Powered by a robust tagging engine.

### 🔍 Advanced Search
- **Keyword Search**: Find posts by searching through titles, content, or tags.
- **Instant Results**: Dynamic search results page for quick navigation.

## Tech Stack
- **Framework**: [Django](https://www.djangoproject.com/)
- **Database**: SQLite (Development)
- **Tagging**: [django-taggit](https://github.com/jazzband/django-taggit)
- **UI**: Custom CSS with responsive design.

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Musakalamz/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/django_blog
   ```

2. **Install dependencies**:
   ```bash
   pip install django django-taggit
   ```

3. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the app**:
   Open `http://127.0.0.1:8000` in your browser.

## Documentation
- [Comment System Guide](COMMENTS_GUIDE.md)

## License
MIT License
