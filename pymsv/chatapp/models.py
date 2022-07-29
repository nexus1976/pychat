"""
Models module: collection of OR/M entity models
"""
from django.db import models

class Message(models.Model):
    """Model class represent the underlying Messages table in the RDBMS"""
    id = models.UUIDField(db_column='id', primary_key=True)
    userid = models.UUIDField(db_column='userid')
    messagedate = models.DateTimeField(db_column='messagedate')
    messagetext = models.TextField(db_column='messagetext')

    objects: models.Manager()
    def __str__(self):
        return str(self.id)

    class Meta:
        """Subclass that specifies additional metadata for the Message model class"""
        db_table = 'Messages'
        app_label = 'chatapp'
