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

class AboutHero(models.Model):
    image = models.ImageField()

class Whatwedo(models.Model):
    description = models.CharField(max_length=20000)
    image = models.ImageField()

    def __str__(self):
        return self.description

class WhatwedoHero(models.Model):
    image = models.ImageField()

class Story(models.Model):
    heading = models.CharField(max_length=20000, default=None)
    description = models.CharField(max_length=20000)
    image = models.ImageField()

    def __str__(self):
        return self.heading

class StoryHero(models.Model):
    image = models.ImageField()

class Adopters(models.Model):
    image = models.ImageField()

    def __str__(self):
        return 'Adopter'+str(self.id)

class UpForAdoptionHero(models.Model):
    image = models.ImageField()

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

class ContactUsHero(models.Model):
    image = models.ImageField()

class DonateHero(models.Model):
    image = models.ImageField()