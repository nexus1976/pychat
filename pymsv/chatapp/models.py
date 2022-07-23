from django.db import models

class Message(models.Model):
    id = models.UUIDField(db_column='id', primary_key=True)
    userid = models.UUIDField(db_column='userid')
    messagedate = models.DateTimeField(db_column='messagedate')
    messagetext = models.TextField(db_column='messagetext')

    objects: models.Manager()
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Messages'
        app_label = 'chatapp'
