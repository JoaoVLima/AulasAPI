"""
Decorators
- This file contains custom decorators used throughout the application.
- Decorators are functions that modify the behavior of other functions or classes.
- They help improve code reusability, readability, and maintainability.

Example:
    from functools import wraps

    def require_authentication(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied("User must be authenticated")
            return func(request, *args, **kwargs)

        return wrapper
"""
import inspect
import traceback
from itertools import zip_longest
from django.conf import settings
from rest_framework.exceptions import APIException
from .exceptions import ResponseError


class Response:
    def __init__(self,
                 error_message,
                 success_message = 'OK',
                 return_keys: list = None,
                 keep_return_value: bool = False,
                 ):
        self.error_message = error_message
        self.success_message = success_message
        self.return_keys = return_keys or []
        self.keep_return_value = keep_return_value

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            response = {
                'status': True,
                'status_code': 200,
                'message': self.success_message,
            }

            try:
                func_return = func(*args, **kwargs)
                return self._format_response(response, func_return)

            except ResponseError as error:
                return self._handle_response_error(response, error)

            except APIException as error:
                return self._handle_api_error(response, error)

            except Exception as error:
                return self._handle_generic_error(response, error)

        wrapper.__signature__ = inspect.signature(func)
        return wrapper

    def _format_response(self, response, func_return):
        if self.keep_return_value:
            return func_return

        if func_return is None:
            return self._set_default_return_values(response)

        try:
            if not self.return_keys:
                response['data'] = func_return

            elif isinstance(func_return, dict):
                response.update(func_return) if 'status' in func_return else response.update({self.return_keys[0]: func_return})

            elif isinstance(func_return, tuple):
                for index, (key, value) in enumerate(zip_longest(self.return_keys, func_return)):
                    response[key or f'data_{index + 1}'] = value

            elif len(self.return_keys) == 1:
                response[self.return_keys[0]] = func_return

        except Exception:
            response.update({'status': False,
                             'status_code': 500,
                             'message': 'Error in decorator'
                             })

        return response

    def _set_default_return_values(self, response: dict) -> dict:
        for key in self.return_keys:
            response[key] = None
        return response

    def _add_error_detail(self, response: dict, error: Exception) -> dict:
        if settings.DEBUG:
            response["error_detail"] = {
                "type": error.__class__.__name__,
                "description": str(error),
                "traceback": traceback.format_exc().split("\n")  # Converts traceback into a list for readability
            }
        return response

    def _handle_response_error(self, response: dict, error: ResponseError) -> dict:
        response.update({
            'status': False,
            'status_code': error.status_code,
            'message': error.message
        })
        return response

    def _handle_api_error(self, response: dict, error: APIException) -> dict:
        response.update({
            "status": False,
            "status_code": error.status_code,
            "message": error.detail
        })
        return self._add_error_detail(response, error)

    def _handle_generic_error(self, response: dict, error: Exception) -> dict:
        response.update({
            "status": False,
            "status_code": 500,
            "message": self.error_message
        })
        return self._add_error_detail(response, error)
