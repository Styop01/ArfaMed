from rest_framework import serializers
from .models import *


# _________________________________________________________
# servicesSideBar _________________________________________
# _________________________________________________________


class ServiceNavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceNavbar
        fields = "__all__"
