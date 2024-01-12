from rest_framework import serializers
from .models import *


# _________________________________________________________
# faq _____________________________________________________
# _________________________________________________________


class FaqQuestionsSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = FaqQuestions
        fields = "__all__"


class FaqQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqQuestions
        fields = ("title", "body")
