from django.db import models

# Create your models here.

# ________________________________________________________
# device _________________________________________________
# ________________________________________________________


class DeviceBanner(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.CharField(max_length=20)

    def __str__(self):
        return self.img


class DeviceProduct(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.CharField(max_length=70)
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    discount = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.img
