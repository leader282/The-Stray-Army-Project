from django.db import models

# Create your models here.

class Home(models.Model):
    heading = models.CharField(max_length=20000)
    description = models.CharField(max_length=20000)
    image = models.ImageField()

class About(models.Model):
    heading = models.CharField(max_length=20000)
    description = models.CharField(max_length=20000)
    image = models.ImageField()

class Whatwedo(models.Model):
    description = models.CharField(max_length=20000)
    image = models.ImageField()

class Story(models.Model):
    heading = models.CharField(max_length=20000, default=None)
    description = models.CharField(max_length=20000)
    image = models.ImageField()