from django.shortcuts import render
from rest_framework import generics
from .serializers import *

# Create your views here.
# ____________________________________________________ APPOINTMENTS ____________________________________________________


class AppointmentsAPIList(generics.ListCreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer
