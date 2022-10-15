from django.db import models

# Create your models here.

class Home(models.Model):
    heading = models.CharField(max_length=20000)
    description = models.CharField(max_length=20000)
    image = models.ImageField()

    def __str__(self):
        return self.heading

class About(models.Model):
    heading = models.CharField(max_length=20000)
    description = models.CharField(max_length=20000)
    image = models.ImageField()

    def __str__(self):
        return self.heading

class Whatwedo(models.Model):
    description = models.CharField(max_length=20000)
    image = models.ImageField()

    def __str__(self):
        return self.description

class Story(models.Model):
    heading = models.CharField(max_length=20000, default=None)
    description = models.CharField(max_length=20000)
    image = models.ImageField()

    def __str__(self):
        return self.heading

class Adopters(models.Model):
    image = models.ImageField()

    def __str__(self):
        return 'Adopter'+str(self.id)

class Adoption(models.Model):
    description = models.CharField(max_length=20000)
    image = models.ImageField()

    def __str__(self):
        return self.description

class Donation(models.Model):
    description = models.CharField(max_length=20000)
    image = models.ImageField()

    def __str__(self):
        return self.description[:30]+'...'

class BackgroundNav(models.Model):
    image = models.ImageField()

    def __str__(self):
        return 'NavBAckground'+str(self.id)