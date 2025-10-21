import threading

_local = threading.local()


class CurrentUserMiddleware:
    """Middleware to store the currently authenticated user in thread-local storage."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _local.user = request.user if request.user.is_authenticated else None
        response = self.get_response(request)
        _local.user = None  # Cleanup after request
        return response


def get_current_user():
    """Retrieve the user from thread-local storage."""
    return getattr(_local, "user", None)
