from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('modules.global.urls')),
    path('', include('modules.home.urls')),
    path('', include('modules.appointments.urls')),
    path('', include('modules.message.urls'))
]
