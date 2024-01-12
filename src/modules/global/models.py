from django.db import models


# ___________________________________________________________
# GLOBAL ____________________________________________________
# ___________________________________________________________


class GlobalTeam(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.TextField(max_length=100)
    content = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.content


class GlobalTestimonial(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    body = models.TextField()

    def __str__(self):
        return self.name


class GlobalClients(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.CharField(max_length=50)
    hover = models.CharField(max_length=20)

    def __str__(self):
        return self.hover


class GlobalHeader(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ForBlog(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    img = models.CharField(max_length=20)
    dateAttr = models.CharField(max_length=30)
    day = models.PositiveIntegerField()
    month = models.CharField(max_length=10)
    year = models.PositiveIntegerField()
    commCount = models.IntegerField()
    publisher = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    to = models.CharField(max_length=10)
    subtitle = models.TextField()
    single = models.TextField()

    def __str__(self):
        return self.title

