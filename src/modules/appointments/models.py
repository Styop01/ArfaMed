from django.db import models

# Create your models here.

# _______________________________________________________
# Appointments __________________________________________
# _______________________________________________________


class Appointments(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    fullName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    eMail = models.EmailField(max_length=50)
    healthComplaints = models.CharField(max_length=50)

    def __str__(self):
        return self.fullName
