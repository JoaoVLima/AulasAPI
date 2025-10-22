"""
Models
- This file contains the definitions of the data models for the application.
- Each model corresponds to a database table and defines the structure of the
  data, including fields and their types.

Example:
    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        published_date = models.DateField()
"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from treebeard.mp_tree import MP_Node
from django.contrib.auth.models import Group, AbstractUser, Permission
from core.middleware import get_current_user
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ImproperlyConfigured

try:
    USER_MODEL = get_user_model()
except ImproperlyConfigured:
    USER_MODEL = settings.AUTH_USER_MODEL


class Log(models.Model):
    """Class used to track log of changes made in the db, logging dates and users"""
    active = models.BooleanField(default=True)

    # Created
    user_created = models.ForeignKey(USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="user_created_logs")
    date_created = models.DateTimeField(auto_now_add=True)

    # Edited
    user_edited = models.ForeignKey(USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="user_edited_logs")
    date_edited = models.DateTimeField(auto_now=True, null=True, blank=True)

    # Deleted (Soft Delete)
    user_deleted = models.ForeignKey(USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="user_deleted_logs")
    date_deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Automatically track user-created and user-edited actions."""
        user = get_current_user()  # Retrieve user from middleware
        if not self.pk and user:  # If object is being created
            self.user_created = user
        elif user:  # If object is being updated
            self.user_edited = user
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Soft delete method that tracks the user who deleted the object."""
        user = get_current_user()  # Retrieve user from middleware
        self.user_deleted = user
        self.date_deleted = timezone.now()
        self.active = False
        self.save(update_fields=["user_deleted", "date_deleted", "active"])

    def force_delete(self, *args, **kwargs):
        """Permanently deletes the object from the database."""
        super().delete(*args, **kwargs)


class GroupHierarchy(MP_Node):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="hierarchy")
    is_supergroup = models.BooleanField(default=False)

    node_order_by = ["group"]

    def __str__(self):
        return self.group.name

    @property
    def permissions(self):
        return self.group.permissions

    def get_all_permissions(self, user_obj, obj=None):
        """Fetches all permissions from the group and its descendants."""
        perm_cache_name = "_group_hierarchy_perm_cache"
        permissions = self.permissions.values_list("content_type__app_label", "codename").order_by()  # Get direct permissions
        permissions = {f'{ct}.{name}' for ct, name in permissions}
        for descendant in self.get_descendants():  # Get all child nodes recursively
            # TODO: Probably wrong(not saving it in the user obj the information), but its working for now
            if not hasattr(user_obj, perm_cache_name):
                if user_obj.is_superuser:
                    perms = Permission.objects.values_list("content_type__app_label", "codename").order_by()
                else:
                    perms = descendant.permissions.values_list("content_type__app_label", "codename").order_by()
                perms = {f'{ct}.{name}' for ct, name in perms}
                permissions.update(perms)

        if not hasattr(user_obj, perm_cache_name):
            setattr(user_obj, perm_cache_name, permissions)

        return getattr(user_obj, perm_cache_name)

    def get_str_ancestors(self):
        ancestors = list(self.get_ancestors().filter(is_supergroup=False).values_list('group__name', flat=True))
        ancestors.append(self.group.name)
        return " ".join(ancestors)