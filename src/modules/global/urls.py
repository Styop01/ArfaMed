from django.urls import path
from .views import *

urlpatterns = [
    # For Home Global
    path('get/<str:slug>/', GlobalAll.as_view()),
    # For Global -------------------------------------------------------------
    path('get/global/<str:slug>/', GlobalView.as_view()),
    path('global/post', GlobalView.as_view()),
]
