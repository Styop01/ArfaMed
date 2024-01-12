from django.urls import path
from .views import *

urlpatterns = [
    # For Home ---------------------------------------------------------------
    path("get/home/<str:slug>/", HomeView.as_view()),
    path('home/icon/box/post/', HomeIconAPIList.as_view()),
    path('home/service/box/post/', HomeServiceAPIList.as_view()),
]



