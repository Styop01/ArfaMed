from django.urls import path
from .views import *

urlpatterns = [
    # For Message -----------------------------------------------------------
    path('post/message/', MessageAPIList.as_view())
    ]
