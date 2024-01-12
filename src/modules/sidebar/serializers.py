from rest_framework import serializers
from .models import SideBarCategories


# _________________________________________________________
# sideBar _________________________________________________
# _________________________________________________________


class SideBarCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideBarCategories
        fields = "__all__"
