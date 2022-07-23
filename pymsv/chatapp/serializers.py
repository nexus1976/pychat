from .models import Message
from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
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
        model = Message
        fields = ['id', 'userid', 'messagedate', 'messagetext']
