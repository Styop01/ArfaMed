from django.shortcuts import render
from rest_framework import generics
from .serializers import *


# Create your views here.

# _____________________________________________________ MESSAGE ________________________________________________________


class MessageAPIList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

