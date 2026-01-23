from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from .models import Book

class PermissionsTest(TestCase):
    def setUp(self):
        # Create users
        self.viewer_user = get_user_model().objects.create_user(username='viewer', email='viewer@example.com', password='password')
        self.editor_user = get_user_model().objects.create_user(username='editor', email='editor@example.com', password='password')
        self.admin_user = get_user_model().objects.create_user(username='admin_user', email='admin@example.com', password='password')

        # Create groups and assign permissions (mimicking the management command)
        # Note: In tests, we need to ensure permissions exist.
        # Since we use a fresh DB in tests, we rely on migrations creating permissions.
        
        editors_group, _ = Group.objects.get_or_create(name='Editors')
        viewers_group, _ = Group.objects.get_or_create(name='Viewers')
        admins_group, _ = Group.objects.get_or_create(name='Admins')

        from django.contrib.contenttypes.models import ContentType
        content_type = ContentType.objects.get_for_model(Book)
        
        can_view = Permission.objects.get(codename='can_view', content_type=content_type)
        can_create = Permission.objects.get(codename='can_create', content_type=content_type)
        can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
        can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

        viewers_group.permissions.add(can_view)
        editors_group.permissions.add(can_view, can_create, can_edit)
        admins_group.permissions.add(can_view, can_create, can_edit, can_delete)

        self.viewer_user.groups.add(viewers_group)
        self.editor_user.groups.add(editors_group)
        self.admin_user.groups.add(admins_group)
        
        self.client = Client()

    def test_viewer_permissions(self):
        self.assertTrue(self.viewer_user.has_perm('bookshelf.can_view'))
        self.assertFalse(self.viewer_user.has_perm('bookshelf.can_create'))
        self.assertFalse(self.viewer_user.has_perm('bookshelf.can_edit'))
        self.assertFalse(self.viewer_user.has_perm('bookshelf.can_delete'))

    def test_editor_permissions(self):
        self.assertTrue(self.editor_user.has_perm('bookshelf.can_view'))
        self.assertTrue(self.editor_user.has_perm('bookshelf.can_create'))
        self.assertTrue(self.editor_user.has_perm('bookshelf.can_edit'))
        self.assertFalse(self.editor_user.has_perm('bookshelf.can_delete'))

    def test_admin_permissions(self):
        self.assertTrue(self.admin_user.has_perm('bookshelf.can_view'))
        self.assertTrue(self.admin_user.has_perm('bookshelf.can_create'))
        self.assertTrue(self.admin_user.has_perm('bookshelf.can_edit'))
        self.assertTrue(self.admin_user.has_perm('bookshelf.can_delete'))

    def test_view_access(self):
        # Viewer accessing create view (should fail)
        self.client.login(username='viewer', password='password')
        response = self.client.get('/books/create/')
        self.assertEqual(response.status_code, 403)

        # Editor accessing create view (should succeed)
        self.client.login(username='editor', password='password')
        response = self.client.get('/books/create/')
        self.assertEqual(response.status_code, 200)

