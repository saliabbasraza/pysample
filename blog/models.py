from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)
    image_url = models.CharField(max_length=2083)


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
