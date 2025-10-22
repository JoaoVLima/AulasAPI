# core/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.context import current_user

class CurrentUserJWTAuthentication(JWTAuthentication):
    """Custom JWT auth that sets the current user in contextvars."""

    def authenticate(self, request):
        result = super().authenticate(request)
        if result is not None:
            user, token = result
            current_user.set(user) # not recomended, but Im going to try it anyway
        return result
