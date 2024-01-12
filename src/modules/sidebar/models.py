from django.db import models

# Create your models here.

# _________________________________________________________
# sideBar _________________________________________________
# _________________________________________________________


class SideBarCategories(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    text = models.CharField(max_length=20)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.text
