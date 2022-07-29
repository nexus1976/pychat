"""
Serializers module: collection of serializer classes
"""
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.Serializer):
    """Serializer class that allows the Message OR/M class to be mapped to a serializable object."""
    id = serializers.UUIDField(required=True)
    userid = serializers.UUIDField(required=True)
    messagedate = serializers.DateTimeField(required=True)
    messagetext = serializers.CharField()
    def create(self, validated_data):
        return Message.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.userid = validated_data.get('userid', instance.userid)
        instance.messagedate = validated_data.get('messagedate', instance.messagedate)
        instance.messagetext = validated_data.get('messagetext', instance.messagetext)
        instance.save()
        return instance
    class Meta:
        """Subclass that specifies additional metadata for the MessageSerializer"""
        model = Message
        fields = ['id', 'userid', 'messagedate', 'messagetext']
