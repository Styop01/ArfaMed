from rest_framework import serializers

from .models import *


# _______________________________________________________
# aboutUs _______________________________________________
# _______________________________________________________


class AccordionSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = AboutUsAccordion
        fields = "__all__"


class AccordionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsAccordion
        fields = ("img", "title", "body")
