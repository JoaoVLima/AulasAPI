"""
Queries
- This file contains functions that encapsulate database queries for the
  application.
- Each function is responsible for retrieving or manipulating data from the
  database using the models defined in models.py.
- This separation of query logic helps keep the views clean and focused on
  handling HTTP requests and responses.

Example:
    class BookQuery(BaseQuery):
        def by_name(self, name):
            return self.model.objects.filter(name=name)
"""
from core.queries import BaseQuery
from .models import Dashboard


class DashboardQuery(BaseQuery):
    def __init__(self):
        super().__init__(model=Dashboard)

    def get_object_json(self, group, year: int, month: int = None, day: int = None):
        filters = {
            'group': group,
            'year': year,
            'month': month,
            'day': day,
        }

        return self.model.objects.filter(**filters).order_by('-date_created', '-date_edited').values_list('object_json', flat=True).first()

