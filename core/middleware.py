from contextvars import ContextVar

current_user: ContextVar = ContextVar("current_user", default=None)

class CurrentUserMiddleware:
    # not recomended, but Im going to try it anyway
    """Middleware to store the currently authenticated user in contextvar local storage."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = current_user.set(request.user if request.user.is_authenticated else None)
        try:
            response = self.get_response(request)
        finally:
            current_user.reset(token)
        return response

def get_current_user():
    return current_user.get() # not recomended, but Im going to try it anyway
