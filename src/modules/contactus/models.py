from django.db import models

# Create your models here.

# ___________________________________________________________
# contactUs _________________________________________________
# ___________________________________________________________


class ContactUsForm(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    icon = models.TextField(max_length=70)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.icon


class ContactUsCard(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    icon = models.TextField(max_length=70)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)

    def __str__(self):
        return self.icon
