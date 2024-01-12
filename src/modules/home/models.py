from django.db import models

# Create your models here.

# ________________________________________________________
# HOME ___________________________________________________
# ________________________________________________________


class IconBox(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    icon = models.CharField(unique=True, max_length=70)
    title = models.CharField(unique=True, max_length=70)
    subtitle = models.TextField(max_length=250)

    def __str__(self):
        return self.title


class ServiceBox(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    icon = models.CharField(unique=True, max_length=30)
    title = models.CharField(unique=True, max_length=30)
    subtitle = models.TextField(max_length=250)

    def __str__(self):
        return self.title

