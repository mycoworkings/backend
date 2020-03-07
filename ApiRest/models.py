from django.db import models

# Create your models here.

class Contact(models.Model):

    WebUrl = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)


class Coworking(models.Model):
     Contact = models.ManyToManyField(Contact)