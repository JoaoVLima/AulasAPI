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
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services import DashboardService


class DashboardView(APIView):
    """Handle HTTP requests to manipulate dashboard data."""
    permission_classes = [IsAuthenticated]
    service = DashboardService()

    class GetParams(serializers.Serializer):
        group = serializers.IntegerField()
        year = serializers.IntegerField()
        month = serializers.IntegerField(required=False)
        day = serializers.IntegerField(required=False)

    def get(self, request):
        # Serializer for verifying params passed to the request
        serializer = self.GetParams(data=request.query_params)
        if not serializer.is_valid():
            return Response(dict(status=False, status_code=400, mensagem=serializer.errors), status=400)

        group = serializer.validated_data.get('group')
        year = serializer.validated_data.get('year')
        month = serializer.validated_data.get('month')
        day = serializer.validated_data.get('day')

        response = self.service.get_dashboard_data(group, year, month, day)
        return Response(response, status=response['status_code'])
