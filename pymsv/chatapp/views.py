"""
Modules Views: Collection of viewsets that used as datasources for api endpoints
"""
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """Class definition for the Message model's viewset"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
