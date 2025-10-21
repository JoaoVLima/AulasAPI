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
