from rest_framework import serializers
from .models import *


# _______________________________________________________
# Appointments __________________________________________
# _______________________________________________________
class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = "__all__"
