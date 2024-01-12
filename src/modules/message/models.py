from django.db import models

# Create your models here.

# _______________________________________________________
# Message _______________________________________________
# _______________________________________________________


class Message(models.Model):
    # id = models.PositiveIntegerField
    your_name = models.CharField(max_length=50)
    your_phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    venue = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.venue
