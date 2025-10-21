"""
Backends
- This file defines custom authentication backends for the application.
- Authentication backends determine how users are authenticated and authorized.

Example:
    from django.contrib.auth.backends import BaseBackend

    class CustomBackend(BaseBackend):
        def authenticate(self, request, username=None, password=None):
            # Custom authentication logic
            pass

        def get_user(self, user_id):
            # Retrieve user by ID
            pass
"""
from django.contrib.auth.backends import ModelBackend

from core.models import GroupHierarchy


class HierarchyPermissionsBackend(ModelBackend):
    def get_all_permissions(self, user_obj, obj=None):
        """Returns all permissions the user has, considering hierarchical groups."""
        permissions = set(self.get_user_permissions(user_obj, obj))
        for group in user_obj.groups.all():  # Get user's groups
            try:
                hierarchy = group.hierarchy
                permissions.update(hierarchy.get_all_permissions(user_obj, obj))  # Inherit permissions
            except GroupHierarchy.DoesNotExist:
                permissions.update(group.permissions.all())  # Standard groups
        return permissions

    def has_perm(self, user_obj, perm, obj=None):
        """Check if user has a specific permission, including inherited ones."""
        if user_obj.is_active:
            if user_obj.is_superuser:
                return True

            return perm in self.get_all_permissions(user_obj, obj)
        else:
            return False
