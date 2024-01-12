from rest_framework import serializers

from .models import *


# ________________________________________________________
# device _________________________________________________
# ________________________________________________________


class DeviceBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceBanner
        fields = "__all__"


class DeviceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceProduct
        fields = "__all__"
