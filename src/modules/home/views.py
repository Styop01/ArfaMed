from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


# Create your views here.
# ------------------------------------------------------ VIEW FOR HOME -------------------------------------------------


class HomeView(APIView):
    def get(self, request, slug):
        service_box = ServiceBox.objects.all()
        icon_box = IconBox.objects.all()

        if slug == "iconBox":
            return Response({"iconBox": IconBoxSerializer(icon_box, many=True).data})

        if slug == "serviceIconBox":
            return Response({"serviceIconBox": ServiceBoxSerializer(service_box, many=True).data})

        if slug == "dataAll":
            return Response({"iconBox": IconBoxSerializer(icon_box, many=True).data,
                             "serviceIconBox": ServiceBoxSerializer(service_box, many=True).data})


class HomeIconAPIList(generics.ListCreateAPIView):
    queryset = IconBox.objects.all()
    serializer_class = IconBoxSerializer


class HomeServiceAPIList(generics.ListCreateAPIView):
    queryset = ServiceBox.objects.all()
    serializer_class = ServiceBoxSerializer

