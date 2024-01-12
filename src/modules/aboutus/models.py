from django.db import models

# Create your models here.

# _______________________________________________________
# aboutUs _______________________________________________
# _______________________________________________________


class AboutUsAccordion(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    toggle = models.CharField(max_length=20, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title
