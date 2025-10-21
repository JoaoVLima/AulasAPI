"""
Admin
- This file is used to register models with the Django admin site.
- It allows you to customize the admin interface for your models, including
  how they are displayed and what actions can be performed.
- By registering models, you enable easy management of your application's
  data through the admin interface.

Example:
    from django.contrib import admin
    from .models import Book

    @admin.register(Book)
    class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'published_date')
"""

from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from django.contrib.auth.admin import UserAdmin
from .models import GroupHierarchy


class GroupHierarchyAdmin(TreeAdmin):
    form = movenodeform_factory(GroupHierarchy)


admin.site.register(GroupHierarchy, GroupHierarchyAdmin)
