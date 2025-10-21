"""
Services
- This file contains service classes that implement business logic for the app.
- Services handle complex operations and validations that don't belong in views or models.
- They act as an intermediate layer between views and database queries.

Example:
    class BookService(BaseService):

        @Response(error_message='Failed to get instance by id')
        def by_id(self, id):
            instance = self.query.by_id(id)
            if instance is None:
                raise ResponseError('Instance not found', status_code=404)
            return instance
"""
from typing import Type
from abc import ABC
from core.queries import BaseQuery
from utils.decorators import Response
from rest_framework.exceptions import NotFound
from django.utils.translation import gettext_lazy as _


class BaseService(ABC):
    def __init__(self, query: Type[BaseQuery]):
        self.query = query()

    @Response(success_message=_('Successfully retrieved instance by id'),
              error_message=_('Failed to get instance by id'))
    def by_id(self, id):
        instance = self.query.by_id(id)
        if instance is None:
            raise NotFound(_('Instance not found'))
        return instance

    @Response(success_message=_('Successfully retrieved active instances'),
              error_message=_('Failed to get active instances'))
    def active(self, active=True):
        return self.query.active(active)

    @Response(success_message=_('Successfully retrieved all instances'),
              error_message=_('Failed to get all instances'))
    def all(self):
        return self.query.all()

    @Response(success_message=_('Successfully created instance'),
              error_message=_('Failed to create instance'))
    def create(self, **kwargs):
        return self.query.create(**kwargs)

    @Response(success_message=_('Successfully updated instance'),
              error_message=_('Failed to update instance'))
    def update(self, id, **kwargs):
        return self.query.update(id, **kwargs)

    @Response(success_message=_('Successfully deleted instance'),
              error_message=_('Failed to delete instance'))
    def delete(self, id):
        return self.query.delete(id)

    @Response(success_message=_('Successfully force deleted instance'),
              error_message=_('Failed to force delete instance'))
    def force_delete(self, id):
        return self.query.force_delete(id)
