"""
Apps
- This file contains the configuration for the application.
- It defines the application name and any specific settings or behaviors
  related to the app.
- The configuration class is used by Django to manage the app's lifecycle
  and settings.

Example:
    from django.apps import AppConfig

    class MyAppConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'myapp'
"""
from django.apps import AppConfig


class IntegrationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'integrations'
