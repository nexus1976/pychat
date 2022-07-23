import uuid
from django.db import models

class MessageManager(models.Manager):
    def create_message(self, messageid, userid, messagedate, messagetext):
        message = self.create(id=messageid)
        message.userid = userid
        message.messagedate = messagedate
        message.messagetext = messagetext
        return message

class Message(models.Model):
    id = models.UUIDField(db_column='id', primary_key=True, default=uuid.uuid4),
    userid = models.UUIDField(db_column='userid', default=uuid.uuid4),
    messagedate = models.DateTimeField(db_column='messagedate'),
    messagetext = models.TextField(db_column='messagetext')

    objects: MessageManager()
    class Meta:
        db_table = 'Messages'
        app_label = 'chatapp'
