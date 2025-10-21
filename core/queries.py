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
from abc import ABC


class BaseQuery(ABC):
    def __init__(self, model=None):
        self.model = model

    def active(self, active: bool = True):
        """Return all active (or not active) instances of the model."""
        return self.model.objects.filter(active=active)

    def all(self):
        """Return all instances of the model."""
        return self.model.objects.all()

    def by_id(self, id):
        """Return an instance by ID, or None if not found."""
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            return None

    def create(self, **kwargs):
        """Create a new instance with the given attributes."""
        return self.model.objects.create(**kwargs)

    def update(self, id, **kwargs):
        """Update an instance by ID and return the updated instance, or None if not found."""
        instance = self.by_id(id)
        if instance:
            for attr, value in kwargs.items():
                setattr(instance, attr, value)
            instance.save()
            return instance
        return None

    def force_delete(self, id):
        """Delete an instance by ID and return True if deleted, False if not found."""
        instance = self.by_id(id)
        if instance:
            instance.force_delete()
            return True
        return False

    def delete(self, id):
        """Deactivate(Soft Delete) an instance by ID (set active to False) and return the updated instance, or None if not found."""
        instance = self.by_id(id)
        if instance:
            instance.delete()
            return True
        return None
