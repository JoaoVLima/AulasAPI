"""
URLs
- This file contains the URL routing configuration for the application.
- It maps URL patterns to corresponding view functions, allowing Django
  to direct incoming requests to the appropriate views.
- You can also include other URL configurations from different apps.

Example:
    from django.urls import path
    from .views import book_list

    urlpatterns = [
        path('books/', book_list, name='book_list'),
    ]
"""
from django.urls import path

from core.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
