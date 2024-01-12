from rest_framework import serializers
from .models import *


# ___________________________________________________________
# contactUs _________________________________________________
# ___________________________________________________________


class ContactUsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsForm
        fields = "__all__"


class ContactUsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsCard
        fields = "__all__"
