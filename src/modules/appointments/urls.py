from django.urls import path
from .views import *

urlpatterns = [
    # For Appointments ------------------------------------------------------
    path('post/appointments/', AppointmentsAPIList.as_view())
    ]