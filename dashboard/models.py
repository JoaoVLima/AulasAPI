"""
Models
- This file contains the definitions of the data models for the application.
- Each model corresponds to a database table and defines the structure of the
  data, including fields and their types.

Example:
    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        published_date = models.DateField()
"""
from django.contrib.auth.models import Group
from django.db import models
from core.models import Log


class Dashboard(Log):
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL, db_index=True)
    year = models.IntegerField(db_index=True)
    month = models.IntegerField(null=True, blank=True, db_index=True)
    day = models.IntegerField(null=True, blank=True, db_index=True)
    object_json = models.JSONField()

    def __str__(self):
        return f'{self.day:02d}/{self.month:02d}/{self.year} - {self.group}'
