from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response

from modules.contactus.serializers import *
from modules.device.models import DeviceProduct
from modules.faq.serializers import *
from modules.home.serializers import *
from modules.servicesidebar.serializers import *
from modules.sidebar.models import SideBarCategories
from modules.sidebar.serializers import SideBarCategoriesSerializer
from .serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000


# __________________________ GLOBAL AND HOME _________________________________

class GlobalAll(APIView):
    def get(self, request, slug):
        side_categories = SideBarCategories.objects.all()
        global_team = GlobalTeam.objects.all()
        global_test = GlobalTestimonial.objects.all()
        global_clients = GlobalClients.objects.all()
        global_header = GlobalHeader.objects.all()
        for_blog = ForBlog.objects.all()
        icon_box = IconBox.objects.all()
        service_box = ServiceBox.objects.all()
        service_navbar = ServiceNavbar.objects.all()
        device_product = DeviceProduct.objects.all()
        contact_form = ContactUsForm.objects.all()
        contact_card = ContactUsCard.objects.all()
        faq = FaqQuestions.objects.all()
        paggination_class = StandardResultsSetPagination

        if slug == "global":
            return Response({"global": {"team": GlobalTeamSerializer(global_team, many=True).data,
                             "testimonial": GlobalTestimonialSerializer(global_test, many=True).data,
                             "clients": GlobalClientsSerializer(global_clients, many=True).data,
                             "header": GlobalHeaderSerializer(global_header, many=True).data,
                             "blog": ForBlogSerializer(for_blog, many=True).data},
                             "home": {"iconBox": IconBoxSerializer(icon_box, many=True).data,
                             "serviceIconBox": ServiceBoxSerializer(service_box, many=True).data},
                             "sideBar": {"categories": SideBarCategoriesSerializer(side_categories, many=True).data}
                             })

        if slug == "navbar":
            return Response({"serviceSideBar": {"navbar": ServiceNavbarSerializer(service_navbar, many=True).data}})

        if slug == "device_product":
            return Response({"device": {"product": DeviceProduct(device_product, many=True)}})

        if slug == "contactUs":
            return Response({"contactUs": {"form": ContactUsFormSerializer(contact_form, many=True).data,
                             "card": ContactUsCard(contact_card, many=True)}})

        if slug == "faq":
            return Response({"faq": {"questions": FaqQuestionsSerializer(faq, many=True).data}})

# ----------------------- VIEW FOR GLOBAL PAGE # ------------------------------


class GlobalView(APIView):
    def get(self, request, slug):
        global_team = GlobalTeam.objects.all()
        global_test = GlobalTestimonial.objects.all()
        global_clients = GlobalClients.objects.all()
        global_header = GlobalHeader.objects.all()
        for_blog = ForBlog.objects.all()

        if slug == "globalTeam":
            return Response({"team": GlobalTeamSerializer(global_team, many=True).data})

        if slug == "globalTestimonial":
            return Response({"test": GlobalTestimonialSerializer(global_test, many=True).data})

        if slug == "globalClients":
            return Response({"clients": GlobalClientsSerializer(global_clients, many=True).data})

        if slug == "globalHeader":
            return Response({"header": GlobalHeaderSerializer(global_header, many=True).data})

        if slug == "blog":
            return Response({"global": {"blog": ForBlogSerializer(for_blog, many=True).data}})

        if slug == "dataAll":
            return Response({"team": GlobalTeamSerializer(global_team, many=True).data,
                             "testimonial": GlobalTestimonialSerializer(global_test, many=True).data,
                             "clients": GlobalClientsSerializer(global_clients, many=True).data,
                             })


class ForBlogAPIList(generics.ListCreateAPIView):
    queryset = ForBlog.objects.all()
    serializer_class = ForBlogSerializer
