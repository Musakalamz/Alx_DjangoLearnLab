# Comment System Documentation

## Overview
The comment system allows users to engage with blog posts by leaving feedback, starting discussions, and interacting with other readers.

## Functionality

### 1. Viewing Comments
- All users (authenticated or not) can view comments on a blog post.
- Comments are displayed at the bottom of the [Post Detail](file:///c:/Users/USER/OneDrive/Desktop/Alx_DjangoLearnLab/django_blog/blog/templates/blog/post_detail.html) page.

### 2. Adding a Comment
- Only authenticated users can post comments.
- A comment form is provided at the bottom of each blog post detail page.
- Once submitted, the comment is linked to the post and the user who wrote it.

### 3. Editing a Comment
- Only the author of a comment can edit it.
- An "Edit" link appears next to comments owned by the logged-in user.
- Editing is handled via a dedicated form that preserves the original content for modification.

### 4. Deleting a Comment
- Only the author of a comment can delete it.
- A "Delete" link appears next to comments owned by the logged-in user.
- A confirmation page is shown before the comment is permanently removed.

## Technical Details

### Model: `Comment`
- `post`: Link to the [Post](file:///c:/Users/USER/OneDrive/Desktop/Alx_DjangoLearnLab/django_blog/blog/models.py) model.
- `author`: Link to the Django `User` model.
- `content`: The text of the comment.
- `created_at`: Timestamp of when the comment was created.
- `updated_at`: Timestamp of the last update.

### URLs
- Add Comment: `/post/<int:pk>/comments/new/`
- Update Comment: `/comment/<int:pk>/update/`
- Delete Comment: `/comment/<int:pk>/delete/`

## Permissions
- **Add**: `LoginRequiredMixin` ensures only logged-in users can comment.
- **Edit/Delete**: `UserPassesTestMixin` ensures only the original author of the comment can modify or remove it.
