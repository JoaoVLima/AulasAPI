from rest_framework_simplejwt.authentication import JWTAuthentication
from core.middleware import _local

class CurrentUserJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        result = super().authenticate(request)
        if result is not None:
            user, token = result
            _local.user = user  # store in thread local
        return result
