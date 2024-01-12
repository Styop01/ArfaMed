from rest_framework import serializers
from .models import *


# ________________________________________________________
# HOME ___________________________________________________
# ________________________________________________________

class IconBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconBox
        fields = "__all__"


class ServiceBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBox
        fields = "__all__"
