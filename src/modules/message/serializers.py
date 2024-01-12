from rest_framework import serializers
from .models import Message


# _______________________________________________________
# Message _______________________________________________
# _______________________________________________________
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

