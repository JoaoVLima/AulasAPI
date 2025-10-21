"""
Views
- This file contains the view functions that handle incoming HTTP requests
  and return HTTP responses.
- Each view function processes user input, calls queries defined in queries.py
  to process the data, and renders the appropriate templates to display data
  to the user.

Example:
class BooksView(APIView):

    def get(self, request):
        book = BookQuery.by_id(request.get('book_id'))
        if book:
            return JsonResponse({'book': {'id': book.id, 'name': book.name}})
        return JsonResponse({'error': 'Book not found'}, status=404)
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _


class IndexView(APIView):

    def get(self, request):
        data = dict(
                title="AulasAPI",
                description=_("The AulasAPI is a backend project. "
                              "The API is the heart of the system, responsible "
                              "for collecting, processing, and providing data "
                              "to the frontend, enabling the generation of "
                              "reports, dashboards, and strategic analyses."),
                version="0.0.1",
                contact={
                    "name": "João Lima",
                    "url": "https://limadeveloper.com/",
                    "email": "joao@limadeveloper.com",
                },
        )
        return Response(data, status=status.HTTP_200_OK)
