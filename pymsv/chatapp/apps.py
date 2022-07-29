"""
Module AppConfig: Django application configuration module
"""
from django.apps import AppConfig

class ChatappConfig(AppConfig):
    """Class definition to specify certain application attributes to Django"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pymsv.chatapp'
