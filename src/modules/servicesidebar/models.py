from django.db import models

# Create your models here.

# _________________________________________________________
# servicesSideBar _________________________________________
# _________________________________________________________


class ServiceNavbar(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.title
