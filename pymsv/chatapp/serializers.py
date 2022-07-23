from .models import Message
from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = ['id', 'userid', 'messagedate', 'messagetext']
